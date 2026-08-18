#!/usr/bin/env python3
"""Regenerate homepage 'Recently deepened' cards for Echopedia.

Curated Featured people/orgs stay in content/index.md.
This script only fills <!-- featured-start --> … <!-- featured-end -->.

Usage:
  python3 scripts/featured-regen.py --root /home/leedt/echo-system --dry-run
  python3 scripts/featured-regen.py --root /home/leedt/echo-system --inject
"""

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    lines = content.split("\n")
    in_fm = False
    fm = {}
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            break
        if in_fm and ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm


def _clean_summary(text: str) -> str:
    text = re.sub(
        r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
        lambda m: m.group(2) or m.group(1).split("/")[-1],
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]+", "", text)
    return " ".join(text.split())


def extract_summary(content: str, fm: dict) -> str:
    raw = (fm.get("featured_summary") or "").strip().strip('"').strip("'")
    if raw:
        return _clean_summary(raw)[:220]

    lines = content.split("\n")
    in_fm = False
    past_fm = False
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
            else:
                past_fm = True
            continue
        if not past_fm:
            continue
        if line.startswith("## "):
            break
        stripped = line.strip()
        if not stripped or stripped.startswith(("# ", "- ", ">", "<!--")):
            continue
        if stripped.startswith("**") and stripped.endswith("**") and len(stripped) < 80:
            continue
        cleaned = _clean_summary(stripped)
        if len(cleaned) < 40:
            continue
        return cleaned[:220]
    return ""


@dataclass
class Page:
    slug: str
    title: str
    page_type: str
    summary: str
    featured: bool
    last_reviewed: str
    path: str
    body_chars: int = 0


def scan_pages(root: Path) -> list:
    pages = []
    for folder in ("people", "organizations"):
        dir_path = root / "content" / folder
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            name = md_file.name
            if name in ("index.md",):
                continue
            if name.endswith("-review.md"):
                continue
            if "audiobook" in name or "consent" in name:
                continue

            content = md_file.read_text(errors="replace")
            fm = parse_frontmatter(content)

            slug = md_file.stem
            title = (fm.get("title") or slug).strip().strip('"').strip("'")
            raw_type = (fm.get("type") or "").strip().strip('"').lower()
            if folder == "organizations":
                page_type = "organization"
            elif raw_type in {"person", "organization"}:
                page_type = raw_type
            else:
                page_type = "person"
            featured = fm.get("featured", "false").lower() == "true"
            last_reviewed = (fm.get("last_reviewed") or "2000-01-01").strip().strip('"')
            summary = extract_summary(content, fm)
            pages.append(
                Page(
                    slug=slug,
                    title=title,
                    page_type=page_type,
                    summary=summary,
                    featured=featured,
                    last_reviewed=last_reviewed,
                    path=name,
                    body_chars=len(content),
                )
            )
    return pages


def select_recent(
    pages: list,
    recency_window: int = 14,
    max_people: int = 4,
    max_orgs: int = 2,
    min_body: int = 2500,
    max_body: int = 40000,
) -> list:
    """Quality recency — ignore featured:true overflow, thin stubs, and dump pages."""
    now = datetime.now()
    people, orgs = [], []
    for p in pages:
        if p.body_chars < min_body or p.body_chars > max_body or not p.summary:
            continue
        if any(x in p.path for x in ("review", "audiobook", "consent", "scratch")):
            continue
        try:
            review_date = datetime.strptime(p.last_reviewed, "%Y-%m-%d")
        except ValueError:
            continue
        if (now - review_date).days > recency_window:
            continue
        (people if p.page_type == "person" else orgs).append(p)
    # Prefer newest, then richer-but-not-dump pages
    people.sort(key=lambda p: (p.last_reviewed, p.body_chars), reverse=True)
    orgs.sort(key=lambda p: (p.last_reviewed, p.body_chars), reverse=True)
    return people[:max_people] + orgs[:max_orgs]


def select_featured(
    pages: list,
    recency_window: int = 30,
    max_people: int = 6,
    max_orgs: int = 3,
) -> list:
    now = datetime.now()
    pinned_people = [p for p in pages if p.page_type == "person" and p.featured]
    pinned_orgs = [p for p in pages if p.page_type == "organization" and p.featured]
    recency_people, recency_orgs = [], []
    for p in pages:
        if p.featured:
            continue
        try:
            review_date = datetime.strptime(p.last_reviewed, "%Y-%m-%d")
        except ValueError:
            continue
        if (now - review_date).days <= recency_window:
            (recency_people if p.page_type == "person" else recency_orgs).append(p)
    recency_people.sort(key=lambda p: p.last_reviewed, reverse=True)
    recency_orgs.sort(key=lambda p: p.last_reviewed, reverse=True)
    remaining_people = max(0, max_people - len(pinned_people))
    remaining_orgs = max(0, max_orgs - len(pinned_orgs))
    final_people = pinned_people[:max_people] + recency_people[:remaining_people]
    final_orgs = pinned_orgs[:max_orgs] + recency_orgs[:remaining_orgs]
    seen, result = set(), []
    for p in final_people + final_orgs:
        if p.slug not in seen:
            seen.add(p.slug)
            result.append(p)
    return result


def generate_html(pages: list) -> str:
    if not pages:
        return ""
    folder_for = {"person": "people", "organization": "organizations"}
    html = '<div class="echo-card-grid">\n'
    for p in pages:
        folder = folder_for.get(p.page_type, "people")
        summary = p.summary or "Recently updated Echopedia page."
        html += (
            f'<div class="echo-card">\n'
            f'  <h3 id="recent-{p.slug}">'
            f'<a href="./{folder}/{p.slug}">{p.title}</a></h3>\n'
            f"  <p>{summary}</p>\n"
            f"</div>\n"
        )
    html += "</div>\n"
    return html


def _replace_div_by_id(content: str, div_id: str, inner_html: str) -> str | None:
    needle = f'id="{div_id}"'
    i = content.find(needle)
    if i < 0:
        return None
    start = content.rfind("<div", 0, i)
    if start < 0:
        return None
    pos = start
    depth = 0
    end = None
    while pos < len(content):
        nxt_open = content.find("<div", pos)
        nxt_close = content.find("</div>", pos)
        if nxt_close < 0:
            return None
        if nxt_open >= 0 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + 4
        else:
            depth -= 1
            pos = nxt_close + 6
            if depth == 0:
                end = pos
                break
    if end is None:
        return None
    block = f'<div id="{div_id}" class="echo-recent">\n{inner_html}</div>'
    return content[:start] + block + content[end:]


def inject_into_index(html_cards: str, index_path: Path) -> bool:
    """Replace #echo-recent (preferred) or comment markers. Never dump before </body>."""
    if not index_path.exists():
        print(f"WARNING: {index_path} not found, skipping injection", file=sys.stderr)
        return False

    content = index_path.read_text()
    replaced = _replace_div_by_id(content, "echo-recent", html_cards)
    if replaced is not None:
        index_path.write_text(replaced)
        print(f"Injected featured cards into {index_path} (#echo-recent)")
        return True

    start_marker = "<!-- featured-start -->"
    end_marker = "<!-- featured-end -->"
    if start_marker in content and end_marker in content:
        start = content.find(start_marker)
        end = content.find(end_marker, start)
        block = start_marker + "\n" + html_cards + "\n" + end_marker
        tail = content[end + len(end_marker) :]
        tail = re.sub(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            "",
            tail,
            flags=re.DOTALL,
        )
        index_path.write_text(content[:start] + block + tail)
        print(f"Injected featured cards into {index_path} (comment markers)")
        return True

    print(
        f"WARNING: no #echo-recent or featured markers in {index_path}; skip (will not dump before </body>)",
        file=sys.stderr,
    )
    return False


def main():
    parser = argparse.ArgumentParser(description="Regenerate homepage recent cards")
    parser.add_argument("--root", default="/home/leedt/echo-system")
    parser.add_argument("--recency-window", type=int, default=14)
    parser.add_argument("--max-people", type=int, default=4)
    parser.add_argument("--max-orgs", type=int, default=2)
    parser.add_argument("--min-body", type=int, default=2500)
    parser.add_argument("--max-body", type=int, default=40000)
    parser.add_argument("--output", default=None)
    parser.add_argument("--inject", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--mode",
        choices=("recent", "pinned"),
        default="recent",
        help="recent = quality recency strip (default). pinned = old 6+3 hybrid.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    pages = scan_pages(root)
    print(
        f"Scanned {len(pages)} pages "
        f"({sum(1 for p in pages if p.page_type == 'person')} people, "
        f"{sum(1 for p in pages if p.page_type == 'organization')} orgs)"
    )

    if args.mode == "recent":
        selected = select_recent(
            pages,
            recency_window=args.recency_window,
            max_people=args.max_people,
            max_orgs=args.max_orgs,
            min_body=args.min_body,
            max_body=args.max_body,
        )
    else:
        selected = select_featured(
            pages,
            recency_window=args.recency_window,
            max_people=args.max_people,
            max_orgs=args.max_orgs,
        )

    if args.dry_run:
        print(f"\n=== SELECTED ({len(selected)} pages, mode={args.mode}) ===")
        for p in selected:
            tag = "PINNED" if p.featured else "RECENT"
            print(
                f"  [{tag}] {p.title} ({p.slug}) "
                f"reviewed={p.last_reviewed} chars={p.body_chars}"
            )
        return

    html_cards = generate_html(selected)
    if args.output:
        Path(args.output).write_text(html_cards)
        print(f"Wrote {len(html_cards)} chars to {args.output}")
    elif not args.inject:
        print(html_cards)

    if args.inject:
        targets = []
        for cand in (root / "index.html", root / "public" / "index.html"):
            if cand.exists() and cand not in targets:
                targets.append(cand)
        if not targets:
            print(f"WARNING: index.html not found under {root}", file=sys.stderr)
        for index_path in targets:
            inject_into_index(html_cards, index_path)


if __name__ == "__main__":
    main()

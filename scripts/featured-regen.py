#!/usr/bin/env python3
"""Regenerate Featured People/Orgs cards for the Echopedia homepage.

Hybrid model:
  1. Pinned: featured: true in frontmatter → always included (human-curated)
  2. Recency: last_reviewed within recency_window days → auto-included

Output: HTML cards injected between <!-- featured-start --> and <!-- featured-end -->
markers in root/index.html.

Usage:
  python3 scripts/featured-regen.py --root /home/leedt/echo-system
  python3 scripts/featured-regen.py --root /home/leedt/echo-system --output /tmp/featured.html
  python3 scripts/featured-regen.py --root /home/leedt/echo-system --dry-run
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as dict."""
    lines = content.split("\n")
    in_fm = False
    fm = {}
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm and ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm


def extract_summary(content: str, fm: dict) -> str:
    """Extract a summary string for the featured card.

    Priority:
    1. featured_summary frontmatter (if set)
    2. First paragraph after frontmatter (up to ## heading)
    3. Identity Snapshot first bullet
    """
    # 1. Check for explicit featured_summary
    if fm.get("featured_summary"):
        return fm["featured_summary"]

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
        if in_fm:
            continue
        if not past_fm:
            continue
        # Stop at second-level heading
        if line.startswith("## "):
            break
        # Skip Identity Snapshot bullets
        if line.strip().startswith("- **"):
            continue
        # Take first non-empty line
        stripped = line.strip()
        if stripped and not stripped.startswith("- "):
            return stripped[:250]
    return ""


@dataclass
class Page:
    slug: str
    title: str
    page_type: str  # "person" or "organization"
    summary: str
    featured: bool
    last_reviewed: str
    path: str


def scan_pages(root: Path) -> list:
    """Scan content/people and content/organizations for all pages."""
    pages = []
    for folder in ("people", "organizations"):
        dir_path = root / "content" / folder
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            name = md_file.name
            # Skip index files and non-content files
            if name in ("index.md",):
                continue
            if name.endswith("-review.md"):
                continue
            if "audiobook" in name or "consent" in name:
                continue

            content = md_file.read_text(errors="replace")
            fm = parse_frontmatter(content)

            slug = md_file.stem
            title = fm.get("title", slug)
            page_type = fm.get("type", "person")
            featured = fm.get("featured", "false").lower() == "true"
            last_reviewed = fm.get("last_reviewed", "2000-01-01")

            summary = extract_summary(content, fm)

            pages.append(Page(
                slug=slug, title=title, page_type=page_type,
                summary=summary, featured=featured,
                last_reviewed=last_reviewed, path=name
            ))
    return pages


def select_featured(
    pages: list,
    recency_window: int = 30,
    max_people: int = 6,
    max_orgs: int = 3,
) -> list:
    """Select which pages to feature.

    Priority:
    1. Pinned (featured: true) — always included
    2. Recency — last_reviewed within window
    3. Cap at max_people / max_orgs
    """
    now = datetime.now()

    pinned_people = [p for p in pages if p.page_type == "person" and p.featured]
    pinned_orgs = [p for p in pages if p.page_type == "organization" and p.featured]

    recency_people = []
    recency_orgs = []
    for p in pages:
        if p.featured:
            continue  # already pinned
        try:
            review_date = datetime.strptime(p.last_reviewed, "%Y-%m-%d")
            if (now - review_date).days <= recency_window:
                if p.page_type == "person":
                    recency_people.append(p)
                else:
                    recency_orgs.append(p)
        except ValueError:
            pass

    # Sort recency by last_reviewed descending (newest first)
    recency_people.sort(key=lambda p: p.last_reviewed, reverse=True)
    recency_orgs.sort(key=lambda p: p.last_reviewed, reverse=True)

    # Cap
    remaining_people = max_people - len(pinned_people)
    remaining_orgs = max_orgs - len(pinned_orgs)
    if remaining_people < 0:
        remaining_people = 0
    if remaining_orgs < 0:
        remaining_orgs = 0

    final_people = pinned_people[:max_people] + recency_people[:remaining_people]
    final_orgs = pinned_orgs[:max_orgs] + recency_orgs[:remaining_orgs]

    # Deduplicate by slug
    seen = set()
    result = []
    for p in final_people + final_orgs:
        if p.slug not in seen:
            seen.add(p.slug)
            result.append(p)

    return result


def generate_html(pages: list) -> str:
    """Generate HTML cards for the selected pages."""
    if not pages:
        return ""

    html = '<div class="echo-card-grid">\n'
    for p in pages:
        folder = p.page_type
        html += (
            f'<div class="echo-card">\n'
            f'  <h3 id="{p.slug}">'
            f'<a href="./{folder}/{p.slug}" class="internal alias" '
            f'data-slug="{folder}/{p.slug}">{p.title}</a></h3>\n'
            f'  <p>{p.summary}</p>\n'
            f'</div>\n'
        )
    html += "</div>\n"
    return html


def inject_into_index(html_cards: str, index_path: Path) -> bool:
    """Inject featured cards between markers in index.html.

    Returns True if markers were found and replaced.
    If markers don't exist, appends before </body>.
    """
    if not index_path.exists():
        print(f"WARNING: {index_path} not found, skipping injection", file=sys.stderr)
        return False

    content = index_path.read_text()

    start_marker = "<!-- featured-start -->"
    end_marker = "<!-- featured-end -->"

    if start_marker in content and end_marker in content:
        # Replace between markers
        start_idx = content.index(start_marker) + len(start_marker)
        end_idx = content.index(end_marker)
        new_content = content[:start_idx] + "\n" + html_cards + "\n" + content[end_idx:]
        index_path.write_text(new_content)
        print(f"Injected featured cards into {index_path.name} (between markers)")
        return True
    else:
        # Append before </body>
        if "</body>" in content:
            insert_point = content.index("</body>")
            new_content = (
                content[:insert_point]
                + "\n" + start_marker + "\n" + html_cards + "\n" + end_marker + "\n"
                + content[insert_point:]
            )
            index_path.write_text(new_content)
            print(f"Appended featured cards to {index_path.name} (before </body>)")
            return True
        else:
            print(f"WARNING: No </body> tag in {index_path.name}", file=sys.stderr)
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate Featured pages HTML for Echopedia homepage"
    )
    parser.add_argument(
        "--root", default="/home/leedt/echo-system", help="Vault root directory"
    )
    parser.add_argument(
        "--recency-window", type=int, default=30, help="Days for recency window"
    )
    parser.add_argument(
        "--max-people", type=int, default=6, help="Max people to feature"
    )
    parser.add_argument(
        "--max-orgs", type=int, default=3, help="Max orgs to feature"
    )
    parser.add_argument(
        "--output", default=None, help="Output HTML file (stdout if omitted)"
    )
    parser.add_argument(
        "--inject", action="store_true", help="Inject into index.html (default: false)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show selected pages without generating HTML"
    )
    args = parser.parse_args()

    root = Path(args.root)

    # Scan all pages
    pages = scan_pages(root)
    print(f"Scanned {len(pages)} pages ({sum(1 for p in pages if p.page_type == 'person')} people, {sum(1 for p in pages if p.page_type == 'organization')} orgs)")

    # Select featured
    selected = select_featured(
        pages,
        recency_window=args.recency_window,
        max_people=args.max_people,
        max_orgs=args.max_orgs,
    )

    if args.dry_run:
        print(f"\n=== SELECTED ({len(selected)} pages) ===")
        for p in selected:
            pin = "PINNED" if p.featured else "RECENCY"
            print(f"  [{pin}] {p.title} ({p.slug}) — last_reviewed: {p.last_reviewed}")
        print(f"\nPinned: {sum(1 for p in selected if p.featured)}, Recency: {sum(1 for p in selected if not p.featured)}")
        return

    # Generate HTML
    html_cards = generate_html(selected)

    if args.output:
        Path(args.output).write_text(html_cards)
        print(f"Wrote {len(html_cards)} chars to {args.output}")
    else:
        print(html_cards)

    # Inject into index.html
    if args.inject:
        index_path = root / "index.html"
        if not index_path.exists():
            index_path = root / "root" / "index.html"
        if index_path.exists():
            inject_into_index(html_cards, index_path)
        else:
            print(f"WARNING: index.html not found in {root} or {root}/root", file=sys.stderr)


if __name__ == "__main__":
    from dataclasses import dataclass
    main()
#!/usr/bin/env python3
"""Regenerate content/{people,organizations}/index.md.

Why: people/index.md used raw <h3> after an HTML A–Z div. CommonMark treats
everything until the next blank line as an HTML block, so Quartz never
resolves [[people/slug]] — live /people/ shows 2000+ literal wikilinks.

Rules (GitHub Pages project site + CONTROL names lock):
- Markdown ### A  (never raw <h3>)
- Sibling links [[kind/slug|Title]] full wikilinks — Quartz resolves these from
  any depth. Relative ./slug is rewritten to ../slug by Quartz pathToRoot, which
  escapes the /people/ folder and 404s at /wiki-public/slug. Same fix that healed
  works/index.md: full wikilinks, no relative ./slug.
- Labels from dest frontmatter title / name_zh — never %e5 URL encoding
- Skip index.md, type:index, echo:scratch, audiobook-review leaks
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
CONTENT = REPO / "content"

SKIP_SLUG_RE = re.compile(
    r"^(albert-chapter|albert-en-sku|albert-g-chang-review)"
)
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def fm_field(fm: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.MULTILINE)
    if not m:
        return ""
    return m.group(1).strip().strip("\"'")


def parse_page(path: Path) -> dict | None:
    if path.name == "index.md":
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    fm_m = FM_RE.match(text)
    fm = fm_m.group(1) if fm_m else ""
    typ = fm_field(fm, "type")
    if typ == "index":
        return None
    if fm_field(fm, "echo") == "scratch":
        return None
    slug = path.stem
    if SKIP_SLUG_RE.match(slug):
        return None
    tags = fm_field(fm, "tags")
    title = fm_field(fm, "title") or slug
    # reject leftover URL-encoded hub labels
    if "%e" in title.lower() or "%E" in title:
        zh = fm_field(fm, "name_zh")
        title = zh or slug
    name_zh = fm_field(fm, "name_zh")
    if name_zh and name_zh not in title and "(" not in title:
        title = f"{title} ({name_zh})"
    # drop review/audiobook bake-offs from the public A–Z
    blob = f"{title} {tags}".lower()
    if "audiobook" in blob and "review" in blob:
        return None
    return {"slug": slug, "title": title}


def letter_of(title: str) -> str:
    for ch in title:
        if ch.isascii() and ch.isalpha():
            return ch.upper()
    return "#"


def render(kind: str, heading: str, blurb: str, rows: list[dict]) -> str:
    by: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by[letter_of(r["title"])].append(r)
    letters = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c in by]
    if "#" in by:
        letters.append("#")
    az = " · ".join(
        f"[{('#' if c == '#' else c)}](#{'other' if c == '#' else c.lower()})"
        for c in letters
    )
    parts = [
        "---",
        f'title: "{heading}"',
        "type: index",
        "tags:",
        f"  - {kind}",
        "  - index",
        f"last_reviewed: 2026-08-18",
        "---",
        "",
        f"# {heading}",
        "",
        blurb,
        "",
        "On a phone, **use header search** (漢名 or English). This page is an A–Z list.",
        "",
        "## Directory",
        "",
        az,
        "",
    ]
    for c in letters:
        hid = "other" if c == "#" else c.lower()
        parts.append(f"### {c} {{#{hid}}}")
        parts.append("")
        for r in sorted(by[c], key=lambda x: x["title"].casefold()):
            # Full wikilink [[kind/slug|title]] — Quartz resolves from any depth
            # under /wiki-public/. Relative ./slug becomes ../slug (Quartz
            # pathToRoot) and 404s; full wikilink is the proven fix (works/).
            parts.append(f"[[{kind}/{r['slug']}|{r['title']}]]")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


BLURBS = {
    "people": (
        "Person records in **Echopedia**. Names keep Chinese characters "
        "and romanized forms where a source already has them "
        "(CONTROL invariant 11 — no converter-invented POJ/Tâi-lô)."
    ),
    "organizations": (
        "Organization records in **Echopedia** — churches, cultural centers, "
        "historical societies, and related institutions."
    ),
}


def regen_one(kind: str) -> tuple[int, Path]:
    d = CONTENT / kind
    rows = []
    for p in sorted(d.glob("*.md")):
        rec = parse_page(p)
        if rec:
            rows.append(rec)
    out = d / "index.md"
    heading = "People" if kind == "people" else "Organizations"
    out.write_text(render(kind, heading, BLURBS[kind], rows), encoding="utf-8")
    return len(rows), out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["people", "organizations", "both"], default="both")
    args = ap.parse_args()
    kinds = ["people", "organizations"] if args.only == "both" else [args.only]
    for k in kinds:
        n, path = regen_one(k)
        text = path.read_text(encoding="utf-8")
        leftover_raw_h3 = text.count("<h3")
        # Full wikilinks [[kind/slug|title]] are the intended output now — mirror
        # works/index.md. Only fail on a raw <h3> reappearing.
        print(f"REGEN_DIR: {k} n={n} raw_h3={leftover_raw_h3} -> {path}")
        if leftover_raw_h3:
            print(f"REGEN_DIR_FAIL: {k} still has raw h3 headings", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

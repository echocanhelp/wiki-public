#!/usr/bin/env python3
"""Reader catalog for content/works/index.md — titled A-band stories, not operator bands.

Wired into echopedia-publish.sh before Quartz. Do not hand-edit works/index.md
between markers; the rest of the homepage lives in content/index.md.

Usage:
  python3 ~/echo-system/scripts/echopedia-regen-works-index.py
"""
from __future__ import annotations

import html
import re
from collections import defaultdict
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
WORKS = REPO / "content" / "works"
OUT = WORKS / "index.md"
FEATURED_N = 12
PER_SOURCE_A = 40

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
DATE_RE = re.compile(r"\*\*Date:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2}|undated)")


def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def load_works() -> list[dict]:
    rows = []
    if not WORKS.is_dir():
        return rows
    for src_dir in sorted(p for p in WORKS.iterdir() if p.is_dir()):
        for md in src_dir.glob("*.md"):
            if md.name == "index.md":
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            meta = parse_fm(text)
            if meta.get("type") != "work":
                continue
            title = html.unescape(meta.get("title") or md.stem.replace("-", " "))
            band = (meta.get("value_band") or "").upper()
            dm = DATE_RE.search(text)
            date = dm.group(1) if dm else ""
            rows.append(
                {
                    "src": src_dir.name,
                    "slug": md.stem,
                    "title": title,
                    "band": band,
                    "date": date,
                    "href": f"works/{src_dir.name}/{md.stem}",
                }
            )
    rows.sort(key=lambda r: (r["date"] or "", r["title"]), reverse=True)
    return rows


def md_link(r: dict) -> str:
    t = r["title"].replace("|", "\\|").replace("]", "")
    # Full works/ wikilink — relative ./src/slug becomes ../src (404 at site root)
    return f"- [[{r['href']}|{t}]] — {r['date'] or 'undated'}"


def main() -> int:
    rows = load_works()
    a = [r for r in rows if r["band"] == "A"]
    by_src: dict[str, list] = defaultdict(list)
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in rows:
        by_src[r["src"]].append(r)
        counts[r["src"]][r["band"] or "?"] += 1
        counts[r["src"]]["all"] += 1

    featured = a[:FEATURED_N]
    feat_lines = "\n".join(
        f"- [[{r['href']}|{html.unescape(r['title']).replace(']', '')}]] — {r['date']} · {r['src']}"
        for r in featured
    )

    src_blocks = []
    for src, items in sorted(by_src.items()):
        aa = [r for r in items if r["band"] == "A"]
        c = counts[src]
        listed = aa[:PER_SOURCE_A]
        more = max(0, len(aa) - len(listed))
        lines = "\n".join(md_link(r) for r in listed) or "_No A-band stories yet._"
        extra = f"\n\n_{more} more A-band in this source — use header search._" if more else ""
        src_blocks.append(
            f"### {src}\n\n"
            f"A {c.get('A', 0)} · B {c.get('B', 0)} · C {c.get('C', 0)} · total {c.get('all', 0)}\n\n"
            f"{lines}{extra}"
        )

    body = f"""---
title: "Stories & historical works"
type: index
tags:
  - index
  - works
  - stories
verification_status: pending
last_reviewed: 2026-08-20
---
# Stories & historical works

Interviews, oral history, and named-subject features absorbed as Echopedia **work** pages. These are the stories — not a URL dump. Use header **search** for a title or 漢名.

<!-- works-index-start -->
## Featured stories

{feat_lines or '_No A-band stories yet._'}

[→ All sources below](#by-source)

## By source

{chr(10).join(src_blocks) if src_blocks else '_No work pages yet._'}
<!-- works-index-end -->

## Related Pages
- [[organizations/taiwanese-american-historical-society|TAHS]]
- [[organizations/taiwaneseamerican-org|TaiwaneseAmerican.org]]
- [[sources/taiwaneseamerican-org]]
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(body, encoding="utf-8")
    print(f"REGEN_WORKS: n={len(rows)} A={len(a)} featured={len(featured)} -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

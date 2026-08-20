#!/usr/bin/env python3
"""Create a Tier1 historical work page from a receive unit. No invented bio.

  python3 scripts/echopedia-work-stub.py --self-test
  python3 scripts/echopedia-work-stub.py --unit-json '{...}'
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REPO = Path("/home/leedt/echo-system")
WORKS = REPO / "content" / "works"

SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(url: str, unit_id: str = "") -> str:
    path = (urlparse(url).path or "").strip("/")
    last = path.split("/")[-1] if path else ""
    last = last.removesuffix(".html")
    s = SLUG_RE.sub("-", last.lower()).strip("-")
    if len(s) < 4:
        s = SLUG_RE.sub("-", str(unit_id).lower()).strip("-") or "unit"
    return s[:80]


def value_band(unit: dict) -> str:
    if unit.get("value_band") in ("A", "B", "C", "D"):
        return unit["value_band"]
    cats = [str(c).lower() for c in (unit.get("categories") or [])]
    genre = str(unit.get("genre") or "").lower()
    blob = " ".join(cats) + " " + genre + " " + str(unit.get("title") or "").lower() + " " + str(unit.get("url") or "").lower()
    if any(x in blob for x in ("gift-guide", "gift_guide", "old-events")) and "interview" not in blob:
        return "D"
    if genre in ("fiction", "poetry", "cnf", "creative-nonfiction") or "creative-writing" in blob:
        return "C"
    if any(
        x in blob
        for x in (
            "interview",
            "community",
            "social-issues",
            "perspectives",
            "oral",
        )
    ):
        return "A"
    return "B"


def default_absorb(band: str) -> str:
    return "skip" if band == "D" else "work-page"


def page_body(unit: dict, band: str, slug: str) -> str:
    title = unit.get("title") or slug
    url = unit["url"]
    src = unit.get("source_id") or "unknown"
    byline = unit.get("byline") or ""
    dt = unit.get("date") or ""
    year = (dt[:4] if dt else "") or "undated"
    lic = unit.get("license") or "all-rights"
    genre = unit.get("genre") or "story"
    excerpt = (unit.get("excerpt") or "").strip()
    if lic == "all-rights" or band == "C":
        excerpt_block = "_Bibliographic record only. Full text stays in the vault (copyright)._ \n"
    elif excerpt:
        excerpt_block = excerpt[:500] + ("…" if len(excerpt) > 500 else "")
    else:
        excerpt_block = "_Excerpt not captured yet._"
    subjects = unit.get("subjects") or []
    subj_lines = "\n".join(f"- {s}" for s in subjects) if subjects else "- (named subjects pending absorb)"
    today = date.today().isoformat()
    org = unit.get("primary_org") or ""
    hub = unit.get("source_hub") or f"sources/{src}"
    related = ["- [[organizations/taiwanese-american-historical-society|TAHS]]"]
    if org:
        related.append(f"- [[{org}]]")
    hub_link = hub if hub.startswith("sources/") or hub.startswith("organizations/") else f"sources/{hub}"
    related.append(f"- [[{hub_link}|Source hub]]")
    return f"""---
title: "{title.replace('"', "'")}"
type: work
source_id: {src}
value_band: {band}
license: {lic}
verification_status: pending
last_reviewed: {today}
---
# {title}

## Identity Snapshot
- Era: {year}
- Geography: Taiwanese America
- Core roles: historical work ({genre}; band {band})

## Record
- **Date:** {dt or "undated"}
- **Byline:** {byline or "—"}
- **Original:** [{url}]({url})
- **Value band:** {band} (A=oral/interview/community history · B=essay/feature · C=creative bib · D=chrome/skip)
- **License:** {lic}

## Excerpt
{excerpt_block}

## Subjects
{subj_lines}

## Related Pages
{chr(10).join(related)}
"""


def write_unit(unit: dict, *, force: bool = False) -> Path | None:
    band = value_band(unit)
    if default_absorb(band) == "skip":
        return None
    src = unit.get("source_id") or "unknown"
    slug = slugify(unit["url"], str(unit.get("unit_id") or ""))
    dest_dir = WORKS / src
    dest = dest_dir / f"{slug}.md"
    if dest.exists() and not force:
        return dest
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest.write_text(page_body(unit, band, slug), encoding="utf-8")
    return dest


def self_test() -> int:
    unit = {
        "class": "story-corpus",
        "source_id": "_selftest",
        "unit_id": "wp:1",
        "url": "https://example.org/2026/01/interview-example/",
        "title": "Interview example",
        "date": "2026-01-15",
        "byline": "Jane Doe",
        "categories": ["interviews"],
        "license": "fair-cite",
        "excerpt": "A short fair-cite.",
        "absorb": "work-page",
    }
    assert value_band(unit) == "A"
    p = write_unit(unit, force=True)
    assert p and p.is_file()
    text = p.read_text(encoding="utf-8")
    assert "## Identity Snapshot" in text and "type: work" in text
    p.unlink()
    try:
        p.parent.rmdir()
    except OSError:
        pass
    fic = {
        **unit,
        "url": "https://example.org/2026/01/a-story/",
        "genre": "fiction",
        "categories": ["creative-writing-prize-selections"],
        "license": "all-rights",
    }
    assert value_band(fic) == "C"
    print("SELF_TEST OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit-json")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.unit_json:
        print("usage: echopedia-work-stub.py --self-test | --unit-json JSON", file=sys.stderr)
        return 2
    unit = json.loads(args.unit_json)
    p = write_unit(unit, force=args.force)
    if p is None:
        print("SKIP D-band")
        return 0
    print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

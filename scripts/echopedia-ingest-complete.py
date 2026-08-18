#!/usr/bin/env python3
"""Machine Gate C: official About prose must be on the primary wiki page.

WEBSITE_INGEST COMPLETE is a planner checkbox today. This script fails
PARTIAL when an intro/about archive exists but the primary page has no
History/Mission narrative. No new cron. No AUTO rewrite.

  python3 scripts/echopedia-ingest-complete.py
  python3 scripts/echopedia-ingest-complete.py --only taiwancenter-org
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
REG = REPO / "knowledge/operational/source-watch-registry.json"

INTRO_NAME_RE = re.compile(r"(introduction|about|簡介|jianjie)", re.I)
NEEDLE_RE = re.compile(
    r"(設立過程|會館宗旨|founded|foundation was established|## History|## Mission)",
    re.I,
)
MIN_HISTORY_CHARS = 400


def load_registry() -> list[dict]:
    data = json.loads(REG.read_text(encoding="utf-8"))
    return [s for s in data.get("sources", []) if s.get("enabled") and not s.get("removed")]


def intro_archives(glob_pat: str) -> list[Path]:
    hits = []
    for p in REPO.glob(glob_pat):
        if INTRO_NAME_RE.search(p.name):
            hits.append(p)
    return hits


def history_blob(primary: Path) -> str:
    text = primary.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## History\b.*?(?=^## |\Z)", text, re.M | re.S)
    mission = re.search(r"^## Mission\b.*?(?=^## |\Z)", text, re.M | re.S)
    parts = []
    if m:
        parts.append(m.group(0))
    if mission:
        parts.append(mission.group(0))
    return "\n".join(parts)


def check_site(site: dict) -> list[str]:
    issues: list[str] = []
    sid = site.get("id", "?")
    primaries = [REPO / p for p in site.get("primary_pages") or []]
    sheet = site.get("entities_sheet")
    glob_pat = site.get("tier2_glob") or ""
    if sheet and not (REPO / sheet).is_file():
        print(f"INGEST_COMPLETE_WARN: {sid}: fact sheet missing {sheet}", file=sys.stderr)
    live_primary = [p for p in primaries if p.is_file()]
    if not live_primary:
        issues.append(f"{sid}: no primary page on disk")
        return issues
    intros = intro_archives(glob_pat) if glob_pat else []
    if not intros:
        return issues  # no intro corpus → skip narrative gate
    blob = "\n".join(history_blob(p) for p in live_primary)
    if len(blob) < MIN_HISTORY_CHARS:
        issues.append(
            f"{sid}: primary History+Mission is {len(blob)} chars "
            f"(need ≥{MIN_HISTORY_CHARS}); intro archives exist: "
            f"{', '.join(p.name for p in intros[:3])}"
        )
    if blob and not NEEDLE_RE.search(blob):
        issues.append(
            f"{sid}: History/Mission lacks 設立/founded/宗旨/Mission heading "
            f"while intro archive exists"
        )
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    args = ap.parse_args()
    sites = load_registry()
    if args.only:
        sites = [s for s in sites if s.get("id") == args.only]
        if not sites:
            print(f"INGEST_COMPLETE: unknown id {args.only}", file=sys.stderr)
            return 2
    issues: list[str] = []
    for s in sites:
        issues.extend(check_site(s))
    if issues:
        print("INGEST_COMPLETE: PARTIAL")
        for i in issues:
            print(f"- {i}")
        return 1
    print(f"INGEST_COMPLETE: OK sites={len(sites)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

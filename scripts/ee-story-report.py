#!/usr/bin/env python3
"""Print one EE sitting report (Telegram/CLI). Never includes U-ids."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ORAL = Path("/home/leedt/echo-system/knowledge/oral-stories")
INDEX = ORAL / "_index.csv"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="", help="displayName substring")
    ap.add_argument("--date", default="", help="YYYY-MM-DD")
    ap.add_argument("--days", type=int, default=0)
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if not INDEX.is_file():
        print("no _index.csv — run ee-import-sheet.py first", file=sys.stderr)
        return 2
    rows = list(csv.DictReader(INDEX.open(encoding="utf-8")))
    hits = rows
    if args.date:
        hits = [r for r in hits if r["date"] == args.date]
    if args.name:
        q = args.name.strip().lower()
        hits = [r for r in hits if q in r["displayName"].lower()]
    if args.list or (not args.name and not args.date):
        print(f"sittings {len(hits)}")
        for r in hits:
            print(f"{r['date']}  {r['displayName']}  {r['source']}  turns={r['turns']}  {r['gist'][:80]}")
        return 0
    if not hits:
        print("no sitting match")
        return 1
    # newest match
    r = hits[-1]
    path = Path(r["vault_path"])
    print(f"{r['date']} · {r['displayName']} · {r['source']} · consent={r['consent']}")
    print(f"turns={r['turns']} voice={r['voice']} photo={r['photo']}")
    print("---")
    if path.is_file():
        body = path.read_text(encoding="utf-8")
        # strip yaml front matter for the spoken report
        if body.startswith("---"):
            parts = body.split("---", 2)
            body = parts[2].lstrip() if len(parts) >= 3 else body
        if len(body) > 8000:
            body = body[:8000] + "\n…[truncated]"
        print(body.rstrip())
        print("---")
        print(path)
    else:
        print("missing vault file")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

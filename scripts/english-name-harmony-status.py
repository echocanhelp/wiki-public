#!/usr/bin/env python3
"""Append-only state for the English-name harmony sweep.

Does not edit wiki pages. Prints the open queue, then counts pages that
are not yet stamped. A mechanical pass is not a harmonized stamp.
"""
import json
import sys
from pathlib import Path

ROOT = Path("/home/leedt/echo-system")
STATE = ROOT / "knowledge/operational/english-name-harmony/state.jsonl"


def load():
    rows = []
    if not STATE.exists():
        return rows
    for line in STATE.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def main():
    rows = load()
    by = {}
    for r in rows:
        by.setdefault(r["status"], []).append(r)
    print(f"stamped={len(rows)}")
    for status, items in sorted(by.items()):
        print(f"  {status}: {len(items)}")
    print("--- queue ---")
    for r in by.get("queue", []):
        print(f"{r['kind']}\t{r['slug']}\t{r.get('note','')}")
    if "--count-unstamped" in sys.argv:
        stamped = {r["slug"] for r in rows}
        n = 0
        for folder in ("people", "organizations"):
            for p in (ROOT / "content" / folder).glob("*.md"):
                if p.name == "index.md":
                    continue
                if p.stem not in stamped:
                    n += 1
        print(f"unstamped={n}")


if __name__ == "__main__":
    main()

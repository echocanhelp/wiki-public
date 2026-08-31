#!/usr/bin/env python3
"""Append a LINE 歲月有聲 turn to knowledge/interactions/line-stories/."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path("/home/leedt/echo-system")
OUT_DIR = VAULT / "knowledge" / "interactions" / "line-stories"


def sanitize(s: str, max_len: int = 8000) -> str:
    s = s.replace("\x00", "")
    if len(s) > max_len:
        s = s[:max_len] + "…[truncated]"
    return s


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--display-name", required=True)
    p.add_argument("--text", default="")
    p.add_argument("--role", default="User", choices=["User", "Bot", "Voice (transcribed)"])
    p.add_argument("--source", default="dm", choices=["group", "dm", "room"])
    p.add_argument("--language", default="")
    p.add_argument("--media-path", default="")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    text = sanitize(args.text)
    text = re.sub(
        r"(?i)(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|sk-[A-Za-z0-9]{10,})",
        "[REDACTED]",
        text,
    )
    now = datetime.now(timezone.utc)
    day = now.strftime("%Y-%m-%d")
    record = {
        "ts": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "platform": "line",
        "source_oa": "suiyue",
        "source": args.source,
        "display_name": args.display_name,
        "role": args.role,
        "text": text,
        "language": args.language,
        "media_path": args.media_path,
    }
    out_path = OUT_DIR / f"{day}.jsonl"
    line = json.dumps(record, ensure_ascii=False) + "\n"
    if args.dry_run:
        print(out_path)
        print(line, end="")
        return 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with out_path.open("a", encoding="utf-8") as f:
        f.write(line)
    print(f"appended {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

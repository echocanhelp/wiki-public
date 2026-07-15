#!/usr/bin/env python3
"""Append a LINE community message to Tier 2 (knowledge/interactions/line/).

Usage:
  python3 line_tier2_append.py --chat-id Cxxx --user-id Uxxx --text "hello" \\
      [--display-name "Name"] [--message-id mid] [--source group|dm]

Designed for no_agent cron / adapter hooks. Does not publish to content/.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path("/home/leedt/echo-system")
OUT_DIR = VAULT / "knowledge" / "interactions" / "line"


def sanitize(s: str, max_len: int = 8000) -> str:
    s = s.replace("\x00", "")
    if len(s) > max_len:
        s = s[: max_len] + "…[truncated]"
    return s


def main() -> int:
    p = argparse.ArgumentParser(description="LINE → Tier 2 append")
    p.add_argument("--chat-id", required=True)
    p.add_argument("--user-id", required=True)
    p.add_argument("--text", required=True)
    p.add_argument("--display-name", default="")
    p.add_argument("--message-id", default="")
    p.add_argument("--source", default="group", choices=["group", "dm", "room"])
    p.add_argument("--mentioned", default="0", help="1 if bot was @mentioned")
    p.add_argument("--agent-invoked", default="0", help="1 if agent will/was run")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    # Basic secret redaction
    text = sanitize(args.text)
    text = re.sub(r"(?i)(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|sk-[A-Za-z0-9]{10,})", "[REDACTED]", text)

    now = datetime.now(timezone.utc)
    day = now.strftime("%Y-%m-%d")
    record = {
        "ts": now.isoformat(),
        "platform": "line",
        "source": args.source,
        "chat_id": args.chat_id,
        "user_id": args.user_id,
        "display_name": args.display_name,
        "message_id": args.message_id,
        "text": text,
        "mentioned": args.mentioned in ("1", "true", "yes"),
        "agent_invoked": args.agent_invoked in ("1", "true", "yes"),
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

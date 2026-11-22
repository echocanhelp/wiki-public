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


def append_turn(
    *,
    display_name: str,
    text: str,
    role: str = "User",
    source: str = "dm",
    language: str = "",
    media_path: str = "",
    out_dir: Path = OUT_DIR,
) -> dict:
    """Append one sitting line. No LINE user id. Returns the record."""
    clean = sanitize(text)
    clean = re.sub(
        r"(?i)(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|sk-[A-Za-z0-9]{10,})",
        "[REDACTED]",
        clean,
    )
    privacy = bool(
        re.search(
            r"(?i)(don'?t publish|do not publish|keep (this|it) private|"
            r"please don'?t share|不要公開|請不要公開|這段不要公開|別公開|不要刊)",
            clean,
        )
    )
    now = datetime.now(timezone.utc)
    record = {
        "ts": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "platform": "line",
        "source_oa": "suiyue",
        "source": source if source in ("group", "dm", "room") else "dm",
        "display_name": (display_name or "unknown")[:80],
        "role": role if role in ("User", "Bot", "Voice (transcribed)") else "User",
        "text": clean,
        "language": language,
        "media_path": media_path,
        "privacy_requested": privacy,
    }
    out_path = Path(out_dir) / f"{now.strftime('%Y-%m-%d')}.jsonl"
    line = json.dumps(record, ensure_ascii=False) + "\n"
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with out_path.open("a", encoding="utf-8") as f:
        f.write(line)
    return record


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
    if args.dry_run:
        import tempfile
        rec = append_turn(
            display_name=args.display_name,
            text=args.text,
            role=args.role,
            source=args.source,
            language=args.language,
            media_path=args.media_path,
            out_dir=Path(tempfile.mkdtemp(prefix="ee-tape-dry-")),
        )
        print(json.dumps(rec, ensure_ascii=False))
        return 0
    rec = append_turn(
        display_name=args.display_name,
        text=args.text,
        role=args.role,
        source=args.source,
        language=args.language,
        media_path=args.media_path,
    )
    print(f"appended {OUT_DIR}")
    print(json.dumps({"privacy_requested": rec["privacy_requested"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

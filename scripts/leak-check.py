#!/usr/bin/env python3
"""Report dated/numeric archive lines that never landed on a content page.

Scans knowledge/web-archives/*.md newer than the last run (state file under
~/.hermes/cache/). A line is a leak when it has a year or number and a proper
name, and it appears neither in content/ nor under some page's `## Skipped`.
First run with no state writes the baseline and scans nothing, so the
historical vault is not re-litigated. Report only: exit 0.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

YEAR_OR_NUM = re.compile(r"\b(?:1[89]\d{2}|20\d{2})\b|\b\d{2,}\b")
PROPER = re.compile(r"[\u4e00-\u9fff]{2,}|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+")
MAX_FILES = 200
MAX_LINES = 300


def interesting(line: str) -> bool:
    s = line.strip()
    if len(s) < 40 or s.startswith(("#", "!", "|", "<", ">")):
        return False
    if not YEAR_OR_NUM.search(s) or not PROPER.search(s):
        return False
    return True


def skipped_blobs(content: Path) -> list[str]:
    blobs = []
    if not content.is_dir():
        return blobs
    for dirpath, _dirs, files in os.walk(content):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            text = Path(dirpath, fn).read_text(encoding="utf-8", errors="replace")
            lines = text.splitlines()
            i = 0
            while i < len(lines):
                if re.match(r"^##\s+Skipped\s*$", lines[i], re.I):
                    i += 1
                    buf = []
                    while i < len(lines) and not re.match(r"^##\s+[^#]", lines[i]):
                        buf.append(lines[i])
                        i += 1
                    if buf:
                        blobs.append("\n".join(buf))
                    continue
                i += 1
    return blobs


def covered_by_skip(line: str, blobs: list[str]) -> bool:
    probe = line.strip()
    short = probe[:80]
    for blob in blobs:
        if probe in blob or (len(short) >= 40 and short in blob):
            return True
    return False


def new_archives(root: Path, since: float) -> list[Path]:
    found = []
    if not root.is_dir():
        return found
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath, fn)
            try:
                if p.stat().st_mtime > since:
                    found.append(p)
            except OSError:
                continue
    found.sort()
    return found


def content_has(content: Path, lines: list[str]) -> set[str]:
    """Return the subset of lines that occur as fixed strings under content/."""
    if not lines:
        return set()
    rg = shutil.which("rg")
    if rg:
        proc = subprocess.run(
            [rg, "-F", "-f", "-", "--glob", "*.md", "-N", str(content)],
            input="\n".join(lines) + "\n",
            text=True,
            capture_output=True,
        )
        blob = proc.stdout or ""
        return {ln for ln in lines if ln in blob}
    blob_parts = []
    for dirpath, _dirs, files in os.walk(content):
        for fn in files:
            if fn.endswith(".md"):
                blob_parts.append(
                    Path(dirpath, fn).read_text(encoding="utf-8", errors="replace")
                )
    blob = "\n".join(blob_parts)
    return {ln for ln in lines if ln in blob}


def load_since(state: Path, explicit: str | None) -> tuple[float, bool]:
    """Return (since_epoch, initialized_baseline)."""
    if explicit is not None:
        return float(explicit), False
    if not state.is_file():
        return time.time(), True
    try:
        data = json.loads(state.read_text())
        return float(data.get("last_run", 0)), False
    except (OSError, ValueError, json.JSONDecodeError):
        return time.time(), True


def write_state(state: Path, when: float) -> None:
    state.parent.mkdir(parents=True, exist_ok=True)
    state.write_text(json.dumps({"last_run": when}) + "\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archives", default=str(Path.home() / "echo-system/knowledge/web-archives"))
    ap.add_argument("--content", default=str(Path.home() / "echo-system/content"))
    ap.add_argument("--state", default=str(Path.home() / ".hermes/cache/leak-check-state.json"))
    ap.add_argument("--since", default=None, help="epoch override; does not mean 'no state'")
    ap.add_argument("--no-save", action="store_true")
    args = ap.parse_args(argv)
    state = Path(args.state)
    since, baseline = load_since(state, args.since)
    if baseline and args.since is None:
        if not args.no_save:
            write_state(state, since)
        print("LEAK_CHECK: initialized baseline scanned=0")
        return 0
    files = new_archives(Path(args.archives), since)
    truncated = len(files) > MAX_FILES
    files = files[:MAX_FILES]
    lines: list[tuple[str, str]] = []
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            if interesting(line):
                lines.append((f"{p}:{i}", line.strip()))
            if len(lines) >= MAX_LINES:
                break
        if len(lines) >= MAX_LINES:
            break
    content = Path(args.content)
    blobs = skipped_blobs(content)
    pending = [(loc, ln) for loc, ln in lines if not covered_by_skip(ln, blobs)]
    found = content_has(content, [ln for _, ln in pending])
    leaks = [(loc, ln) for loc, ln in pending if ln not in found]
    for loc, ln in leaks[:80]:
        print(f"LEAK: {loc}: {ln[:160]}")
    if len(leaks) > 80:
        print(f"LEAK_CHECK: {len(leaks) - 80} more not shown")
    print(
        f"LEAK_CHECK: files={len(files)} lines={len(lines)} leaks={len(leaks)} "
        f"truncated={int(truncated or len(lines) >= MAX_LINES)}"
    )
    if not args.no_save:
        write_state(state, time.time())
    return 0


if __name__ == "__main__":
    sys.exit(main())

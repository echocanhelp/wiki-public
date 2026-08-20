#!/usr/bin/env python3
"""Fail publish if Quartz rewrote works catalog links to site-root 404s.

Looks at quartz-v4/public/works/index.html after build.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PUBLIC = Path("/home/leedt/quartz-v4/public")
INDEX = PUBLIC / "works" / "index.html"
BAD = re.compile(r'href="(\.\./taiwaneseamerican-org/[^"]+)"')
GOOD_NEEDLE = "works/taiwaneseamerican-org/"


def main() -> int:
    if not INDEX.is_file():
        print("LINKCHECK: no works/index.html yet — skip")
        return 0
    html = INDEX.read_text(encoding="utf-8", errors="replace")
    bad = BAD.findall(html)
    if bad:
        print("LINKCHECK_FAIL: works/index hrefs escape /works/ (will 404 at site root)")
        for h in bad[:8]:
            print("  ", h)
        return 1
    n_good = html.count(GOOD_NEEDLE)
    print(f"LINKCHECK_OK: works/index good_hrefs≈{n_good} bad_root=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

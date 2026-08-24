#!/usr/bin/env python3
"""Fail publish if Quartz rewrote catalog/directory links to site-root 404s.

Runs AFTER `npx quartz build` on quartz-v4/public, BEFORE tree-copy.

Two failure modes this gate exists for:

1. works/index.html — `href="../taiwaneseamerican-org/..."` escapes /works/
   and 404s at the GitHub Pages project root.

2. people/index.html + organizations/index.html — markdown `./slug` is
   rewritten by Quartz pathToRoot to `href="../slug"` (no folder). Those
   resolve to /wiki-public/<slug> and 404. Canonical emit is
   [[kind/slug|title]] → href="../people/<slug>" / "../organizations/<slug>".

Do not hand-edit the A–Z hubs. Regen:
  python3 ~/echo-system/scripts/echopedia-regen-directory-index.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PUBLIC = Path("/home/leedt/quartz-v4/public")

# One-segment ../foo from a folder index — these are real root assets, not pages.
OK_ROOT_ASSETS = {
    "index.css",
    "index.html",
    "favicon.ico",
    "icon.png",
    "postscript.js",
    "prescript.js",
    "404.html",
    "robots.txt",
    "sitemap.xml",
}

BARE_HREF = re.compile(r'href="\.\./([^"/?#]+)"')
WORKS_BAD = re.compile(r'href="(\.\./taiwaneseamerican-org/[^"]+)"')
WORKS_GOOD = "works/taiwaneseamerican-org/"


def _bare_escapes(html: str) -> list[str]:
    out = []
    for slug in BARE_HREF.findall(html):
        if slug in OK_ROOT_ASSETS:
            continue
        if slug.endswith((".css", ".js", ".png", ".ico", ".svg", ".xml", ".json", ".txt", ".woff", ".woff2")):
            continue
        out.append(slug)
    return out


def check_works() -> int:
    index = PUBLIC / "works" / "index.html"
    if not index.is_file():
        print("LINKCHECK: no works/index.html yet — skip")
        return 0
    html = index.read_text(encoding="utf-8", errors="replace")
    bad = WORKS_BAD.findall(html)
    if bad:
        print("LINKCHECK_FAIL: works/index hrefs escape /works/ (will 404 at site root)")
        for h in bad[:8]:
            print("  ", h)
        return 1
    n_good = html.count(WORKS_GOOD)
    print(f"LINKCHECK_OK: works/index good_hrefs≈{n_good} bad_root=0")
    return 0


def check_directory(kind: str) -> int:
    index = PUBLIC / kind / "index.html"
    if not index.is_file():
        print(f"LINKCHECK_FAIL: missing {kind}/index.html")
        return 1
    html = index.read_text(encoding="utf-8", errors="replace")
    leftover = html.count(f"[[{kind}/")
    if leftover:
        print(f"LINKCHECK_FAIL: {kind}/index.html has {leftover} leftover [[{kind}/ wikilink strings (CommonMark HTML-block swallow)")
        return 1
    good_needle = f"../{kind}/"
    n_good = html.count(f'href="{good_needle}')
    if n_good < 10:
        print(f"LINKCHECK_FAIL: {kind}/index.html has only {n_good} href=\"../{kind}/…\" (catalog empty or emit broke)")
        return 1
    bare = _bare_escapes(html)
    if bare:
        uniq = sorted(set(bare))
        print(
            f"LINKCHECK_FAIL: {kind}/index.html has {len(bare)} href=\"../<slug>\" "
            f"escapes ({len(uniq)} unique) — Quartz pathToRoot of ./slug; "
            f"will 404 at /wiki-public/<slug>"
        )
        for s in uniq[:12]:
            print(f"  ../{s}")
        if len(uniq) > 12:
            print(f"  ... +{len(uniq) - 12} more")
        return 1
    print(f"LINKCHECK_OK: {kind}/index good_hrefs≈{n_good} leftover_wikilink=0 bare_escape=0")
    return 0


def main() -> int:
    if not PUBLIC.is_dir():
        print(f"LINKCHECK_FAIL: build tree not found: {PUBLIC}")
        return 1
    rc = 0
    rc |= check_works()
    rc |= check_directory("people")
    rc |= check_directory("organizations")
    if rc:
        print("LINKCHECK_FAIL: regenerate indexes then rebuild (do not hand-edit hubs)")
        return 1
    print("LINKCHECK_OK: works + people + organizations catalogs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

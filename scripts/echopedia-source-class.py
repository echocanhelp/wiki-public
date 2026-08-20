#!/usr/bin/env python3
"""Classify a source for WEBSITE_INGEST §0. No network in --self-test.

  python3 scripts/echopedia-source-class.py --self-test
  python3 scripts/echopedia-source-class.py --signals '{"posts_total":2421,"pages_total":13,"cms":"wordpress"}'
"""
from __future__ import annotations

import argparse
import json
import sys

CHURCH_NAV = (
    "ministries",
    "bulletin",
    "our pastor",
    "worship",
    "團契",
    "牧者",
    "執委",
    "事工",
)

SOCIAL_HOSTS = (
    "instagram.com",
    "facebook.com",
    "fb.com",
    "threads.com",
    "x.com",
    "twitter.com",
    "tiktok.com",
)


def classify(signals: dict) -> str:
    """Return source class. Default live-small (church/org bar)."""
    kind = (signals.get("kind") or "").lower()
    if kind in ("pdf", "publication", "yearbook"):
        return "publication"
    host = (signals.get("host") or "").lower()
    if any(h in host for h in SOCIAL_HOSTS):
        return "social-short"
    if kind in ("static-v1", "laijohn", "史料庫"):
        return "static-v1"
    posts = int(signals.get("posts_total") or 0)
    pages = int(signals.get("pages_total") or 0)
    cms = (signals.get("cms") or "").lower()
    if posts >= 200 and pages <= 50 and cms in ("wordpress", "wp", "wordpress.com"):
        return "story-corpus"
    nav = (signals.get("nav_text") or "").lower()
    church_hits = sum(1 for k in CHURCH_NAV if k in nav)
    if church_hits >= 2:
        return "live-small"
    return "live-small"


def self_test() -> int:
    cases = [
        (
            {"posts_total": 2421, "pages_total": 13, "cms": "wordpress", "host": "taiwaneseamerican.org"},
            "story-corpus",
        ),
        (
            {"nav_text": "Our Pastor Ministries Bulletin Worship", "host": "gstpc.org"},
            "live-small",
        ),
        ({"kind": "pdf"}, "publication"),
        ({"host": "instagram.com"}, "social-short"),
        ({"kind": "static-v1"}, "static-v1"),
        ({}, "live-small"),
    ]
    fail = 0
    for sig, expect in cases:
        got = classify(sig)
        if got != expect:
            print(f"FAIL {sig} → {got} want {expect}")
            fail += 1
    if fail:
        print(f"SELF_TEST FAIL n={fail}")
        return 1
    print("SELF_TEST OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--signals", help="JSON object of detector signals")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.signals:
        print("usage: echopedia-source-class.py --self-test | --signals JSON", file=sys.stderr)
        return 2
    sig = json.loads(args.signals)
    print(classify(sig))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

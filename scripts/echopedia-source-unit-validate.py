#!/usr/bin/env python3
"""Validate source-unit JSONL (receive envelope). Stdlib only.

  python3 scripts/echopedia-source-unit-validate.py --self-test
  python3 scripts/echopedia-source-unit-validate.py knowledge/research/<id>/units.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CLASSES = {"live-small", "static-v1", "story-corpus", "publication", "social-short"}
LICENSES = {"all-rights", "fair-cite", "cc"}
ABSORB = {"work-page", "cite-existing", "dossier-new", "hub-list-only", "skip"}
REQUIRED = ("class", "source_id", "unit_id", "url", "title", "date", "license", "absorb")


def validate_unit(obj: object, line_no: int) -> list[str]:
    errs: list[str] = []
    prefix = f"L{line_no}"
    if not isinstance(obj, dict):
        return [f"{prefix}: not an object"]
    for k in REQUIRED:
        if not obj.get(k) and obj.get(k) != 0:
            errs.append(f"{prefix}: missing {k}")
    cls = obj.get("class")
    if cls is not None and cls not in CLASSES:
        errs.append(f"{prefix}: bad class {cls!r}")
    lic = obj.get("license")
    if lic is not None and lic not in LICENSES:
        errs.append(f"{prefix}: bad license {lic!r}")
    ab = obj.get("absorb")
    if ab is not None and ab not in ABSORB:
        errs.append(f"{prefix}: bad absorb {ab!r}")
    url = obj.get("url") or ""
    if url and not str(url).startswith(("http://", "https://")):
        errs.append(f"{prefix}: url must be http(s)")
    if "subjects" in obj and not isinstance(obj["subjects"], list):
        errs.append(f"{prefix}: subjects must be a list")
    if cls == "story-corpus" and lic == "all-rights" and ab == "dossier-new":
        errs.append(f"{prefix}: all-rights story-corpus cannot absorb=dossier-new (no body dump; use work-page bib)")
    return errs


def validate_path(path: Path) -> list[str]:
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"{path}: empty"]
    for i, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"L{i}: json {e}")
            continue
        errs.extend(validate_unit(obj, i))
    return errs


FIXTURE_OK = {
    "class": "story-corpus",
    "source_id": "taiwaneseamerican-org",
    "unit_id": "wp:24856",
    "url": "https://www.taiwaneseamerican.org/2026/07/theyve-always-come-to-us-fiction-eddie-lo/",
    "title": "They’ve Always Come to Us…",
    "date": "2026-07-30",
    "byline": "Eddie Lo",
    "subjects": [],
    "genre": "fiction",
    "value_band": "C",
    "license": "all-rights",
    "absorb": "work-page",
}

FIXTURE_BAD = {
    "class": "story-corpus",
    "source_id": "taiwaneseamerican-org",
    "unit_id": "wp:1",
    "url": "not-a-url",
    "title": "x",
    "date": "2026-01-01",
    "license": "all-rights",
    "absorb": "dossier-new",
}


def self_test() -> int:
    e1 = validate_unit(FIXTURE_OK, 1)
    e2 = validate_unit(FIXTURE_BAD, 1)
    if e1:
        print("SELF_TEST FAIL ok-fixture", e1)
        return 1
    if not e2:
        print("SELF_TEST FAIL bad-fixture should error")
        return 1
    print("SELF_TEST OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.path:
        print("usage: echopedia-source-unit-validate.py --self-test | <units.jsonl>", file=sys.stderr)
        return 2
    p = Path(args.path)
    if not p.is_file():
        print(f"MISSING {p}", file=sys.stderr)
        return 2
    errs = validate_path(p)
    if errs:
        print("UNITS_INVALID")
        for e in errs[:50]:
            print(f"- {e}")
        return 1
    print(f"UNITS_OK {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

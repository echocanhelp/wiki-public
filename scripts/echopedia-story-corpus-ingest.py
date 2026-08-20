#!/usr/bin/env python3
"""Story-corpus harvest (parent Python). Not a Grok drip.

  python3 scripts/echopedia-story-corpus-ingest.py --source-id taiwaneseamerican-org \\
      --home https://www.taiwaneseamerican.org/ --limit 50
  # then: --apply-works   (A/B/C work pages)
  # --all  paginates REST (full corpus). Default is --limit only.

Vault = knowledge/web-archives/ (gitignored). Never git add bulk.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
UA = "EchopediaStoryCorpus/1.0"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


validate = _load("unitval", REPO / "scripts" / "echopedia-source-unit-validate.py")
workstub = _load("workstub", REPO / "scripts" / "echopedia-work-stub.py")


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8", "replace")), dict(r.headers)


def cat_slugs(row: dict) -> list[str]:
    slugs = []
    for group in (row.get("_embedded") or {}).get("wp:term") or []:
        if not isinstance(group, list):
            continue
        for t in group:
            if isinstance(t, dict) and t.get("taxonomy") in ("category", "post_tag"):
                slugs.append(str(t.get("slug") or ""))
    return slugs


def title_of(row: dict) -> str:
    t = row.get("title")
    if isinstance(t, dict):
        return str(t.get("rendered") or "")
    return str(t or "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--home", required=True)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply-works", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.25)
    args = ap.parse_args()
    home = args.home.rstrip("/")
    dest = REPO / "knowledge" / "research" / args.source_id / "units.jsonl"
    dest.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    page = 1
    per = min(args.limit, 20) if not args.all else 20
    cap = 10**9 if args.all else args.limit
    seen: set[str] = set()
    if dest.is_file():
        for line in dest.read_text(encoding="utf-8").splitlines():
            try:
                seen.add(str(json.loads(line).get("unit_id")))
            except json.JSONDecodeError:
                pass
    new_units = []
    while n < cap:
        url = f"{home}/wp-json/wp/v2/posts?per_page={per}&page={page}&_embed=1"
        try:
            data, hdr = fetch_json(url)
        except Exception as e:
            print(f"FETCH_FAIL page={page} {e}", file=sys.stderr)
            break
        if not isinstance(data, list) or not data:
            break
        for row in data:
            if n >= cap:
                break
            link = str(row.get("link") or "")
            uid = str(row.get("id") or link)
            if uid in seen:
                continue
            unit = {
                "class": "story-corpus",
                "source_id": args.source_id,
                "unit_id": uid,
                "url": link,
                "title": title_of(row),
                "date": str(row.get("date") or "")[:10],
                "categories": cat_slugs(row),
                "license": "all-rights",
                "absorb": "work-page",
            }
            band = workstub.value_band(unit)
            unit["value_band"] = band
            unit["absorb"] = workstub.default_absorb(band)
            errs = validate.validate_unit(unit, n + 1)
            if errs:
                print("SKIP", errs)
                continue
            with dest.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(unit, ensure_ascii=False) + "\n")
            seen.add(uid)
            new_units.append(unit)
            n += 1
            if args.apply_works:
                p = workstub.write_unit(unit)
                print("WORK", p or "SKIP")
        total_pages = int(hdr.get("X-WP-TotalPages") or 1)
        page += 1
        if page > total_pages or not args.all:
            break
        time.sleep(args.sleep)
    print(f"INDEXED n={n} file={dest} apply_works={args.apply_works}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

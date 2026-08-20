#!/usr/bin/env python3
"""Thicken A-band work pages (dossier-lite). Parent Python — not a Grok drip.

Pulls WP REST excerpt + byline + category names. Fair-cite teaser only (≤500 chars).
Never writes full post body to content/works/.

  python3 scripts/echopedia-thicken-work-a.py --source-id taiwaneseamerican-org \\
      --home https://www.taiwaneseamerican.org/ [--limit N]
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
UA = "EchopediaThickenA/1.0"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


stub = _load("wstub", REPO / "scripts" / "echopedia-work-stub.py")


def strip_html(s: str) -> str:
    t = re.sub(r"<[^>]+>", " ", s or "")
    t = html.unescape(re.sub(r"\s+", " ", t)).strip()
    return t


def get_json(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def rest_by_slug(home: str, slug: str) -> dict | None:
    api = f"{home.rstrip('/')}/wp-json/wp/v2/posts?slug={urllib.parse.quote(slug)}&_embed=1"
    rows = get_json(api)
    if isinstance(rows, list) and rows:
        return rows[0]
    return None


def cats_from_row(row: dict) -> list[str]:
    out: list[str] = []
    for group in (row.get("_embedded") or {}).get("wp:term") or []:
        if not isinstance(group, list):
            continue
        for t in group:
            if isinstance(t, dict) and t.get("taxonomy") == "category":
                name = t.get("name") or t.get("slug") or ""
                if name and str(name).lower() not in ("slider", "uncategorized"):
                    out.append(str(name))
    return out


def author_from_row(row: dict) -> str:
    auth = (row.get("_embedded") or {}).get("author") or []
    if auth and isinstance(auth[0], dict):
        return str(auth[0].get("name") or "")
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--home", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0.15)
    args = ap.parse_args()
    units_path = REPO / "knowledge/research" / args.source_id / "units.jsonl"
    if not units_path.is_file():
        print("NO_UNITS", units_path)
        return 1
    n = 0
    thickened = 0
    missing = 0
    for line in units_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        unit = json.loads(line)
        if (unit.get("value_band") or stub.value_band(unit)) != "A":
            continue
        n += 1
        if args.limit and thickened >= args.limit:
            break
        url = unit.get("url") or ""
        slug = url.rstrip("/").split("/")[-1]
        try:
            row = rest_by_slug(args.home, slug)
        except Exception as e:
            print("REST_FAIL", slug, e)
            missing += 1
            time.sleep(args.sleep)
            continue
        if not row:
            missing += 1
            time.sleep(args.sleep)
            continue
        excerpt = strip_html((row.get("excerpt") or {}).get("rendered") or "")
        if not excerpt:
            # first ~400 of content as last resort — still teaser, not full body
            excerpt = strip_html((row.get("content") or {}).get("rendered") or "")[:400]
        unit["excerpt"] = excerpt
        unit["byline"] = author_from_row(row) or unit.get("byline") or ""
        unit["subjects"] = cats_from_row(row) or unit.get("subjects") or []
        unit["primary_org"] = unit.get("primary_org") or f"organizations/{args.source_id}"
        unit["source_hub"] = f"sources/{args.source_id}"
        unit["source_id"] = args.source_id
        unit["license"] = unit.get("license") or "all-rights"
        p = stub.write_unit(unit, force=True)
        if p:
            thickened += 1
            print("A", p.name)
        time.sleep(args.sleep)
    print(f"THICKEN_A n_seen={n} wrote={thickened} rest_miss={missing}")
    return 0 if thickened else 1


if __name__ == "__main__":
    raise SystemExit(main())

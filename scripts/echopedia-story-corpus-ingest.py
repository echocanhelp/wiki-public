#!/usr/bin/env python3
"""Story-corpus harvest (parent Python). Not a Grok drip.

  python3 scripts/echopedia-story-corpus-ingest.py --source-id taiwaneseamerican-org \\
      --home https://www.taiwaneseamerican.org/ --limit 50
  # --all  paginates REST (full corpus). Default is --limit only.
  # --apply-works   A/B/C work pages (wiki)
  # --fill-vault    REST-page A/B/C **full text** into gitignored web-archives (default on --all)

Vault = knowledge/web-archives/<id>/ (gitignored). Never git add bulk.
TAHS: saving A/B/C bodies is the default. D chrome is index-only.
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
        body = json.loads(r.read().decode("utf-8", "replace"))
        hdr = {k.lower(): v for k, v in r.headers.items()}
        return body, hdr


def fetch_html(url: str) -> str:
    """Live HTML when REST content.rendered is empty. Never skip high-value text."""
    if not url:
        return ""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"HTML_FETCH_FAIL {url} {e}", file=sys.stderr)
        return ""


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


def html_to_md(raw: str) -> str:
    import html
    import re

    s = raw or ""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", s)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n\n", s, flags=re.I)
    s = re.sub(r"</div>", "\n", s, flags=re.I)
    s = re.sub(r"<h[1-6][^>]*>", "\n### ", s, flags=re.I)
    s = re.sub(r"</h[1-6]>", "\n\n", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "\n- ", s, flags=re.I)
    s = re.sub(r"<blockquote[^>]*>", "\n> ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def write_vault(source_id: str, url: str, title: str, body: str, subdir: str = "") -> Path | None:
    """Gitignored society copy. Never commit."""
    if not body:
        return None
    slug = url.rstrip("/").split("/")[-1] or "unit"
    vault = REPO / "knowledge/web-archives" / source_id
    if subdir:
        vault = vault / subdir
    vault.mkdir(parents=True, exist_ok=True)
    path = vault / f"{slug}.md"
    path.write_text(
        f"---\nsource_url: {url}\nfetched: auto\n---\n\n# {title}\n\n{body}\n",
        encoding="utf-8",
    )
    return path


REST_SUBDIR = {"posts": "posts", "pages": "pages", "tah_video": "videos"}


def fill_vault(
    source_id: str,
    home: str,
    sleep: float,
    rest_bases: list[str] | None = None,
) -> int:
    """Page WP REST and save A/B/C full text. Skip existing vault files >400 bytes. D chrome skipped."""
    units_path = REPO / "knowledge/research" / source_id / "units.jsonl"
    by_id: dict[str, dict] = {}
    if units_path.is_file():
        for line in units_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            u = json.loads(line)
            by_id[str(u.get("unit_id") or "")] = u
            by_id[str(u.get("url") or "")] = u
    wrote = skipped = dskip = missing_band = 0
    for rest in rest_bases or ["posts"]:
        subdir = REST_SUBDIR.get(rest, rest)
        vault_dir = REPO / "knowledge/web-archives" / source_id / subdir
        page = 1
        while True:
            url = f"{home}/wp-json/wp/v2/{rest}?per_page=20&page={page}&_embed=1"
            try:
                data, hdr = fetch_json(url)
            except Exception as e:
                print(f"VAULT_FETCH_FAIL rest={rest} page={page} {e}", file=sys.stderr)
                break
            if not isinstance(data, list) or not data:
                break
            for row in data:
                link = str(row.get("link") or "")
                uid = str(row.get("id") or link)
                unit = by_id.get(uid) or by_id.get(link) or {
                    "title": title_of(row),
                    "url": link,
                    "categories": cat_slugs(row),
                }
                band = workstub.value_band(unit)
                if band == "D":
                    dskip += 1
                    continue
                if band not in ("A", "B", "C"):
                    missing_band += 1
                    continue
                slug = link.rstrip("/").split("/")[-1] or uid
                dest = vault_dir / f"{slug}.md"
                if dest.is_file() and dest.stat().st_size > 400:
                    skipped += 1
                    continue
                body = html_to_md((row.get("content") or {}).get("rendered") or "")
                if len(body) < 80 and link:
                    body = html_to_md(fetch_html(link)) or body
                    time.sleep(sleep)
                if len(body) < 40:
                    continue
                p = write_vault(
                    source_id,
                    link,
                    title_of(row) or unit.get("title") or slug,
                    body,
                    subdir=subdir,
                )
                if p:
                    wrote += 1
                    if wrote <= 8 or wrote % 200 == 0:
                        print(f"VAULT {band} {rest} {p.name} {len(body)}")
            total_pages = int(hdr.get("x-wp-totalpages") or hdr.get("X-WP-TotalPages") or 1)
            page += 1
            if page > total_pages:
                break
            time.sleep(sleep)
    print(f"FILL_VAULT wrote={wrote} skipped_existing={skipped} d_chrome={dskip} other={missing_band}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--home", required=True)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply-works", action="store_true")
    ap.add_argument("--fill-vault", action="store_true", help="Save A/B/C full text to gitignored vault")
    ap.add_argument("--no-vault", action="store_true", help="Skip vault even on --all (not the TAHS default)")
    ap.add_argument("--sleep", type=float, default=0.25)
    ap.add_argument(
        "--rest-bases",
        default="posts",
        help="comma REST bases to vault (default posts). TAH: posts,pages,tah_video",
    )
    args = ap.parse_args()
    home = args.home.rstrip("/")
    dest = REPO / "knowledge" / "research" / args.source_id / "units.jsonl"
    dest.parent.mkdir(parents=True, exist_ok=True)
    rest_bases = [x.strip() for x in (args.rest_bases or "posts").split(",") if x.strip()]
    if args.fill_vault and not args.all and not args.apply_works:
        return fill_vault(args.source_id, home, args.sleep, rest_bases=rest_bases)
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
            if not args.no_vault and unit.get("value_band") in ("A", "B", "C"):
                body = html_to_md((row.get("content") or {}).get("rendered") or "")
                write_vault(args.source_id, link, unit.get("title") or "", body, subdir="posts")
        total_pages = int(hdr.get("x-wp-totalpages") or hdr.get("X-WP-TotalPages") or 1)
        page += 1
        if page > total_pages or not args.all:
            break
        time.sleep(args.sleep)
    print(f"INDEXED n={n} file={dest} apply_works={args.apply_works}")
    if args.all and not args.no_vault:
        fill_vault(args.source_id, home, args.sleep, rest_bases=rest_bases)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

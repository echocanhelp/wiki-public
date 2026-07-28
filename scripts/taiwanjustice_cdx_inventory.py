#!/usr/bin/env python3
"""Phase 1: Wayback CDX inventory for taiwanjustice.net (dead site recovery).

Writes research artifacts under knowledge/research/taiwanjustice-net/.
No HTML bulk download (that's Phase 2).
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

OUT = Path("/home/leedt/echo-system/knowledge/research/taiwanjustice-net")
CDX = "https://web.archive.org/cdx/search/cdx"
HOSTS = (
    "taiwanjustice.net/*",
    "www.taiwanjustice.net/*",
)
PAGE_SIZE = 5000
SLEEP_S = 0.35
USER_AGENT = "EchopediaTAHS-ArchiveRecovery/1.0 (+historical; contact via echocanhelp)"
PARKING_MARKERS = (
    "parked domain",
    "hostinger dns",
    "domain is parked",
    "buy this domain",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cdx_fetch(params: dict, retries: int = 5) -> list[str]:
    q = urllib.parse.urlencode(params, doseq=True)
    url = f"{CDX}?{q}"
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read().decode("utf-8", errors="replace")
            return [ln for ln in body.splitlines() if ln.strip()]
        except Exception as e:  # noqa: BLE001 — inventory must survive transient IA errors
            last_err = e
            wait = min(60, 2 ** attempt)
            print(f"CDX retry {attempt+1}/{retries} after error: {e}; sleep {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"CDX failed after retries: {last_err}")


def paginate_cdx(url_pat: str, collapse: str | None = "urlkey") -> list[list[str]]:
    """Return list of [timestamp, original, mimetype, statuscode, length, digest]."""
    rows: list[list[str]] = []
    page = 0
    while True:
        params = {
            "url": url_pat,
            "output": "json",
            "fl": "timestamp,original,mimetype,statuscode,length,digest",
            "pageSize": str(PAGE_SIZE),
            "page": str(page),
        }
        if collapse:
            params["collapse"] = collapse
        # Prefer HTTP 200 for primary inventory; still include other codes without filter
        # when collapse set — filter in post for stats.
        raw = cdx_fetch(params)
        time.sleep(SLEEP_S)
        if not raw:
            break
        try:
            data = json.loads("\n".join(raw) if raw[0].strip().startswith("[") else f"[{','.join(raw)}]")
        except json.JSONDecodeError:
            # line-oriented fallback
            data = []
            for ln in raw:
                try:
                    data.append(json.loads(ln))
                except json.JSONDecodeError:
                    parts = ln.split()
                    if len(parts) >= 6:
                        data.append(parts[:6])
        if not data:
            break
        # First page may include header row
        start = 0
        if page == 0 and data and data[0] and data[0][0] == "timestamp":
            start = 1
        chunk = data[start:]
        if not chunk:
            break
        rows.extend(chunk)
        print(f"  {url_pat} collapse={collapse} page={page} +{len(chunk)} total={len(rows)}", flush=True)
        # IA often returns the full collapse set on page=0 and 400s on page>0
        if page == 0 and len(chunk) >= PAGE_SIZE:
            # probe page 1 once; stop on 400/empty
            try:
                probe = dict(params)
                probe["page"] = "1"
                raw2 = cdx_fetch(probe, retries=2)
                time.sleep(SLEEP_S)
                if not raw2:
                    break
                data2 = json.loads("\n".join(raw2))
                start2 = 1 if data2 and data2[0] and data2[0][0] == "timestamp" else 0
                chunk2 = data2[start2:]
                if not chunk2:
                    break
                rows.extend(chunk2)
                print(f"  {url_pat} collapse={collapse} page=1 +{len(chunk2)} total={len(rows)}", flush=True)
                if len(chunk2) < PAGE_SIZE:
                    break
                page = 2
                continue
            except Exception as e:  # noqa: BLE001
                print(f"  page>0 not available ({e}); using page0 only", flush=True)
                break
        if len(chunk) < PAGE_SIZE:
            break
        page += 1
        if page > 500:  # safety
            print("WARN: page safety stop", file=sys.stderr)
            break
    return rows


def classify_path(url: str) -> str:
    try:
        p = urllib.parse.urlparse(url)
        path = urllib.parse.unquote(p.path or "/")
    except Exception:
        return "other"
    low = path.lower()
    q = (p.query or "").lower()
    if low in ("", "/"):
        return "home"
    if "newsletter" in low or "電子報" in path or "報導" in path and "newsletter" in low:
        return "newsletter"
    if "/feed" in low or low.endswith("/feed/") or "rss" in low:
        return "feed"
    if "/category/" in low or low.startswith("/category"):
        return "category"
    if "/tag/" in low:
        return "tag"
    if "/author/" in low:
        return "author"
    if "/wp-json" in low or "/wp-admin" in low or "/wp-content" in low or "/wp-includes" in low:
        return "wordpress_infra"
    if "comment" in low or "replytocom=" in q:
        return "comment_related"
    if "/page/" in low or re.search(r"/page/\d+", low):
        return "pagination"
    if path.count("/") <= 2 and not low.endswith((".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico")):
        # pretty permalink article candidate
        return "article_candidate"
    if any(low.endswith(ext) for ext in (".pdf", ".doc", ".docx", ".mp3", ".mp4", ".zip")):
        return "binary_asset"
    if any(low.endswith(ext) for ext in (".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".woff", ".woff2")):
        return "static_asset"
    return "other"


def year_of(ts: str) -> str:
    return ts[:4] if ts and len(ts) >= 4 else "????"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    print(f"TJ CDX inventory start {started}", flush=True)

    all_unique: dict[str, dict] = {}
    host_counts: Counter[str] = Counter()

    for host_pat in HOSTS:
        print(f"Inventory unique URLs: {host_pat}", flush=True)
        rows = paginate_cdx(host_pat, collapse="urlkey")
        for r in rows:
            if len(r) < 6:
                continue
            ts, original, mime, status, length, digest = r[:6]
            key = original
            # normalize scheme-ish key
            prev = all_unique.get(key)
            rec = {
                "timestamp": ts,
                "original": original,
                "mimetype": mime,
                "statuscode": status,
                "length": length,
                "digest": digest,
                "class": classify_path(original),
                "year": year_of(ts),
            }
            host_counts[host_pat] += 1
            if prev is None:
                all_unique[key] = rec
            else:
                # keep latest timestamp for this URL
                if ts > prev["timestamp"]:
                    all_unique[key] = rec

    # Also digest-collapsed pass for body uniqueness estimate (200 only via filter)
    print("Inventory unique digests (status 200)...", flush=True)
    digest_set: set[str] = set()
    digest_samples: list[dict] = []
    for host_pat in HOSTS:
        params_base_rows = []
        page = 0
        while True:
            params = {
                "url": host_pat,
                "output": "json",
                "fl": "timestamp,original,mimetype,statuscode,length,digest",
                "filter": "statuscode:200",
                "collapse": "digest",
                "pageSize": str(PAGE_SIZE),
                "page": str(page),
            }
            raw = cdx_fetch(params)
            time.sleep(SLEEP_S)
            if not raw:
                break
            data = json.loads("\n".join(raw))
            start = 1 if data and data[0] and data[0][0] == "timestamp" else 0
            chunk = data[start:]
            if not chunk:
                break
            for r in chunk:
                if len(r) < 6:
                    continue
                digest_set.add(r[5])
                if len(digest_samples) < 30:
                    digest_samples.append(
                        {
                            "timestamp": r[0],
                            "original": r[1],
                            "mimetype": r[2],
                            "length": r[4],
                            "digest": r[5],
                        }
                    )
            print(f"  digests {host_pat} page={page} unique_so_far={len(digest_set)}", flush=True)
            if page == 0 and len(chunk) >= PAGE_SIZE:
                try:
                    params_p1 = dict(params)
                    params_p1["page"] = "1"
                    raw2 = cdx_fetch(params_p1, retries=2)
                    time.sleep(SLEEP_S)
                    data2 = json.loads("\n".join(raw2)) if raw2 else []
                    start2 = 1 if data2 and data2[0] and data2[0][0] == "timestamp" else 0
                    for r in data2[start2:]:
                        if len(r) >= 6:
                            digest_set.add(r[5])
                    print(f"  digests {host_pat} page=1 unique_so_far={len(digest_set)}", flush=True)
                except Exception as e:  # noqa: BLE001
                    print(f"  digests page>0 skip ({e})", flush=True)
                break
            if len(chunk) < PAGE_SIZE:
                break
            page += 1
            if page > 500:
                break

    # Stats
    by_status = Counter(r["statuscode"] for r in all_unique.values())
    by_mime = Counter(r["mimetype"] for r in all_unique.values())
    by_class = Counter(r["class"] for r in all_unique.values())
    by_year = Counter(r["year"] for r in all_unique.values())
    status_200 = [r for r in all_unique.values() if r["statuscode"] == "200"]
    articles = [r for r in status_200 if r["class"] == "article_candidate"]
    newsletters = [r for r in all_unique.values() if r["class"] == "newsletter" or "newsletter" in r["original"].lower()]
    comments = [r for r in all_unique.values() if r["class"] == "comment_related"]

    # Write unique URL jsonl
    urls_path = OUT / "cdx-unique-urls.jsonl"
    with urls_path.open("w", encoding="utf-8") as f:
        for url in sorted(all_unique.keys()):
            f.write(json.dumps(all_unique[url], ensure_ascii=False) + "\n")

    # by year csv
    year_path = OUT / "cdx-by-year.csv"
    with year_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "unique_urls"])
        for y in sorted(by_year.keys()):
            w.writerow([y, by_year[y]])

    # class breakdown
    class_path = OUT / "cdx-by-class.csv"
    with class_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["class", "count"])
        for k, v in by_class.most_common():
            w.writerow([k, v])

    # Sample article URLs for pilot
    sample_articles = sorted(articles, key=lambda r: r["timestamp"], reverse=True)[:50]
    sample_path = OUT / "sample-article-urls.json"
    sample_path.write_text(json.dumps(sample_articles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Parking digests placeholder — Phase 2 will fingerprint; list empty + instructions
    parking_path = OUT / "PARKING_DIGESTS.txt"
    parking_path.write_text(
        "# Digests identified as Hostinger parking / non-content.\n"
        "# Phase 1 leaves empty until Phase 2 samples homepage parking hash.\n"
        "# Known live parking title: 'Parked Domain name on Hostinger DNS system'\n"
        f"# generated {utc_now()}\n",
        encoding="utf-8",
    )

    summary = {
        "generated_at": utc_now(),
        "started_at": started,
        "domain": "taiwanjustice.net",
        "cdx_hosts": list(HOSTS),
        "unique_url_count": len(all_unique),
        "unique_digest_count_status_200": len(digest_set),
        "status_200_unique_urls": len(status_200),
        "by_status": dict(by_status.most_common()),
        "by_mimetype_top": by_mime.most_common(15),
        "by_class": dict(by_class.most_common()),
        "by_year": dict(sorted(by_year.items())),
        "article_candidate_count": len(articles),
        "newsletter_class_count": len(newsletters),
        "comment_related_count": len(comments),
        "host_row_counts": dict(host_counts),
        "outputs": {
            "unique_urls_jsonl": str(urls_path),
            "by_year_csv": str(year_path),
            "by_class_csv": str(class_path),
            "sample_articles": str(sample_path),
            "parking_digests": str(parking_path),
        },
        "decisions": {
            "hard_end_date": None,
            "keep_comments": True,
            "keep_newsletters": True,
            "multi_day_download_ok": True,
            "high_value_keep_all": True,
        },
        "notes": [
            "Live site is Hostinger parked — not a content source.",
            "No hard end date: filter parking digests in P2, do not drop late real captures.",
            "Unique URL count uses collapse=urlkey latest timestamp per original URL.",
            "Digest count uses collapse=digest filter statuscode:200 across both hosts (may double-count same body under www/non-www).",
        ],
        "digest_samples": digest_samples[:10],
    }
    summary_path = OUT / "cdx-summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = OUT / "README.md"
    readme.write_text(
        f"""# taiwanjustice.net CDX inventory (Phase 1)

Generated: {summary['generated_at']}

## Counts
- Unique URLs (urlkey collapse, both hosts merged by original URL): **{summary['unique_url_count']}**
- Status 200 among those: **{summary['status_200_unique_urls']}**
- Unique digests (status 200, digest collapse): **{summary['unique_digest_count_status_200']}**
- Article-candidate paths: **{summary['article_candidate_count']}**
- Newsletter-class: **{summary['newsletter_class_count']}**
- Comment-related: **{summary['comment_related_count']}**

## Files
- `cdx-unique-urls.jsonl` — one JSON object per unique URL
- `cdx-summary.json` — machine summary
- `cdx-by-year.csv` / `cdx-by-class.csv`
- `sample-article-urls.json` — pilot list for Phase 2
- `PARKING_DIGESTS.txt` — parking fingerprints (filled in P2)

## Next
Phase 2 bulk download from chosen snapshots; keep comments + newsletters; skip parking digests only.
""",
        encoding="utf-8",
    )

    print(json.dumps({k: summary[k] for k in (
        "generated_at", "unique_url_count", "status_200_unique_urls",
        "unique_digest_count_status_200", "article_candidate_count",
        "newsletter_class_count", "comment_related_count", "by_year", "by_class",
    )}, ensure_ascii=False, indent=2))
    print(f"WROTE {summary_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

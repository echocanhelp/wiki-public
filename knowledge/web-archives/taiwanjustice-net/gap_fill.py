#!/usr/bin/env python3
"""
TJ-P4 gap-fill: residual Wayback fails → secondary archives.

Sources (priority):
  1. Arquivo.pt CDX (works from pinto 2026-07-28)
  2. Ghostarchive HTML search (domain + per-URL term)
  3. Internet Archive CDX recheck (often flaky; best-effort)
  4. Common Crawl index — often empty-reply from this host; recorded as unavailable

Inputs:
  download-state.json (authoritative residual fails)
  failed_urls_tjp2b.json (legacy bulk fail list; optional)

Outputs (same directory):
  gap_fill_results.json
  gap_fill_summary.json
  ../../research/taiwanjustice-net/GAP_REPORT.md
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent
STATE_FILE = BASE_DIR / "download-state.json"
LEGACY_FAILS = BASE_DIR / "failed_urls_tjp2b.json"
RESULTS_FILE = BASE_DIR / "gap_fill_results.json"
SUMMARY_FILE = BASE_DIR / "gap_fill_summary.json"
REPORT_FILE = BASE_DIR.parent.parent / "research" / "taiwanjustice-net" / "GAP_REPORT.md"

UA = "Echopedia-TJ-P4-gap-fill/1.1 (+https://echocanhelp.github.io/wiki-public/; archive recovery)"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA, "Accept": "*/*"})

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".ico", ".tiff", ".pdf"}
SKIP_RE = re.compile(
    r"(/wp-content/uploads/|/feed/?$|/sitemap|\.xml$|/robots\.txt$|/wp-json/|/wp-admin/|/wp-includes/|"
    r"\.(?:jpg|jpeg|png|gif|svg|webp|bmp|ico|tiff|pdf|css|js)(?:$|\?))",
    re.I,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_url(url: str) -> str:
    url = url.strip()
    if "#" in url:
        url = url.split("#", 1)[0]
    # strip :80 from netloc
    p = urllib.parse.urlparse(url)
    host = p.hostname or ""
    scheme = p.scheme or "https"
    path = p.path or "/"
    query = f"?{p.query}" if p.query else ""
    # prefer https bare host
    return f"{scheme}://{host}{path}{query}"


def is_content_url(url: str) -> bool:
    if SKIP_RE.search(url):
        return False
    path = urllib.parse.urlparse(url).path.lower()
    _, ext = os.path.splitext(path)
    if ext in IMAGE_EXT:
        return False
    return True


def load_residual_fails() -> list[str]:
    """Prefer download-state residual fails; fall back to legacy list."""
    urls: list[str] = []
    if STATE_FILE.exists():
        st = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        done = st.get("done_urls") or {}
        for u, v in done.items():
            if isinstance(v, dict) and v.get("status") in ("fail", "failed", "error"):
                urls.append(u)
    if not urls and LEGACY_FAILS.exists():
        raw = json.loads(LEGACY_FAILS.read_text(encoding="utf-8"))
        if isinstance(raw, list):
            urls = raw
    # de-dupe by normalized form, keep first
    seen = set()
    out = []
    for u in urls:
        n = normalize_url(u)
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def check_arquivo(url: str, timeout: float = 20.0) -> dict:
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "arquivo.pt",
        "error": None,
    }
    try:
        # strip scheme for broader match; arquivo CDX accepts full URL too
        q = urllib.parse.quote(url, safe="")
        api = f"https://arquivo.pt/wayback/cdx?url={q}&output=json&limit=5&filter=status:200"
        r = SESSION.get(api, timeout=timeout)
        if r.status_code != 200 or not r.text.strip():
            # try host+path wildcard-ish by bare host path
            p = urllib.parse.urlparse(url)
            alt = f"{p.netloc}{p.path}"
            api = f"https://arquivo.pt/wayback/cdx?url={urllib.parse.quote(alt, safe='')}&output=json&limit=5"
            r = SESSION.get(api, timeout=timeout)
        if r.status_code != 200:
            result["error"] = f"http {r.status_code}"
            return result
        # NDJSON or JSON lines
        lines = [ln for ln in r.text.strip().splitlines() if ln.strip()]
        best = None
        for ln in lines:
            try:
                obj = json.loads(ln)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, list):
                # unlikely array form
                continue
            if not isinstance(obj, dict):
                continue
            status = str(obj.get("status") or obj.get("statuscode") or "")
            ts = obj.get("timestamp")
            orig = obj.get("url") or url
            if status and status not in ("200", "226"):
                # keep 200 preferred; allow others as weak
                if best is None:
                    best = (ts, orig, status, True)
                continue
            best = (ts, orig, status, False)
            break
        if best:
            ts, orig, status, weak = best
            if ts:
                result["found"] = True
                result["timestamp"] = ts
                result["status_code"] = status
                result["snapshot_url"] = f"https://arquivo.pt/wayback/{ts}/{orig}"
                if weak:
                    result["weak"] = True
    except Exception as e:
        result["error"] = str(e)[:300]
    return result


def check_ghostarchive(url: str, timeout: float = 20.0) -> dict:
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "ghostarchive",
        "error": None,
    }
    try:
        # Ghostarchive search uses ?term=
        term = urllib.parse.urlparse(url).path or url
        # Prefer full URL without scheme for precision
        p = urllib.parse.urlparse(url)
        term = f"{p.netloc}{p.path}"
        api = f"https://ghostarchive.org/search?term={urllib.parse.quote(term)}"
        r = SESSION.get(api, timeout=timeout)
        if r.status_code != 200:
            result["error"] = f"http {r.status_code}"
            return result
        html = r.text
        # rows: <a href="/archive/XXXX">URL</a> ... Date
        for m in re.finditer(
            r'href="(/archive/[^"]+)"[^>]*>(https?://[^<]+)</a></td><td>([^<]+)',
            html,
        ):
            snap_path, found_url, date = m.group(1), m.group(2), m.group(3).strip()
            # loose path match
            if urllib.parse.urlparse(found_url).path.rstrip("/") == p.path.rstrip("/") or p.path in found_url:
                result["found"] = True
                result["snapshot_url"] = f"https://ghostarchive.org{snap_path}"
                result["timestamp"] = date
                break
        # domain-only fallback already handled in bulk domain probe
    except Exception as e:
        result["error"] = str(e)[:300]
    return result


def check_ia_cdx(url: str, timeout: float = 25.0) -> dict:
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "internet_archive_cdx",
        "error": None,
    }
    try:
        q = urllib.parse.quote(url, safe="")
        api = (
            "https://web.archive.org/cdx/search/cdx"
            f"?url={q}&output=json&filter=statuscode:200&limit=3&fl=timestamp,original,statuscode,digest"
        )
        r = SESSION.get(api, timeout=timeout)
        if r.status_code != 200:
            result["error"] = f"http {r.status_code}"
            return result
        data = r.json()
        if not isinstance(data, list) or len(data) < 2:
            return result
        # first row header
        for row in data[1:]:
            if len(row) < 3:
                continue
            ts, original, status = row[0], row[1], row[2]
            result["found"] = True
            result["timestamp"] = ts
            result["status_code"] = status
            result["snapshot_url"] = f"https://web.archive.org/web/{ts}id_/{original}"
            break
    except Exception as e:
        result["error"] = str(e)[:300]
    return result


def check_common_crawl_probe(timeout: float = 12.0) -> dict:
    """Single probe — CC index often empty-reply from this host."""
    out = {"available": False, "error": None, "endpoint": "https://index.commoncrawl.org/collinfo.json"}
    try:
        r = SESSION.get(out["endpoint"], timeout=timeout)
        out["available"] = r.status_code == 200 and bool(r.text.strip())
        if not out["available"]:
            out["error"] = f"http {r.status_code} empty={not bool(r.text.strip())}"
    except Exception as e:
        out["error"] = str(e)[:300]
    return out


def ghostarchive_domain_hits(timeout: float = 25.0) -> list[dict]:
    hits = []
    try:
        r = SESSION.get("https://ghostarchive.org/search?term=taiwanjustice.net", timeout=timeout)
        if r.status_code != 200:
            return hits
        for m in re.finditer(
            r'href="(/archive/[^"]+)"[^>]*>(https?://[^<]+)</a></td><td>([^<]+)',
            r.text,
        ):
            hits.append(
                {
                    "snapshot_url": f"https://ghostarchive.org{m.group(1)}",
                    "url": m.group(2),
                    "timestamp": m.group(3).strip(),
                }
            )
    except Exception:
        pass
    return hits


def check_all(url: str) -> dict:
    row = {
        "url": url,
        "arquivo": check_arquivo(url),
        "ghostarchive": check_ghostarchive(url),
        "internet_archive_cdx": check_ia_cdx(url),
    }
    sources = [k for k in ("arquivo", "ghostarchive", "internet_archive_cdx") if row[k].get("found")]
    row["sources_found"] = sources
    row["total_sources"] = len(sources)
    return row


def main() -> int:
    print(f"[{utc_now()}] TJ-P4 gap-fill start")
    residual = load_residual_fails()
    content = [u for u in residual if is_content_url(u)]
    non_content = [u for u in residual if not is_content_url(u)]
    print(f"Residual fails: {len(residual)} | content: {len(content)} | non-content: {len(non_content)}")

    cc_probe = check_common_crawl_probe()
    print(f"Common Crawl index available: {cc_probe}")

    ga_domain = ghostarchive_domain_hits()
    print(f"Ghostarchive domain hits: {len(ga_domain)}")

    results = []
    max_workers = 4
    t0 = time.time()
    if content:
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = {ex.submit(check_all, u): u for u in content}
            done_n = 0
            for fut in as_completed(futs):
                results.append(fut.result())
                done_n += 1
                if done_n % 25 == 0 or done_n == len(content):
                    rate = done_n / max(time.time() - t0, 0.1)
                    print(f"  Progress {done_n}/{len(content)} ({rate:.2f}/s)")

    # coverage
    def count_found(key):
        return sum(1 for r in results if r.get(key, {}).get("found"))

    any_found = sum(1 for r in results if r.get("total_sources", 0) > 0)
    none_found = [r["url"] for r in results if r.get("total_sources", 0) == 0]
    recoverable = [r for r in results if r.get("total_sources", 0) > 0]

    summary = {
        "generated_at": utc_now(),
        "script_version": "gap_fill.py 1.1",
        "residual_fails_total": len(residual),
        "content_urls_checked": len(content),
        "non_content_skipped": len(non_content),
        "common_crawl_probe": cc_probe,
        "ghostarchive_domain_hits": len(ga_domain),
        "ghostarchive_domain_samples": ga_domain[:20],
        "coverage": {
            "arquivo": count_found("arquivo"),
            "ghostarchive": count_found("ghostarchive"),
            "internet_archive_cdx": count_found("internet_archive_cdx"),
            "any_source": any_found,
            "no_source": len(none_found),
            "any_source_pct": round(100.0 * any_found / len(results), 1) if results else 0.0,
        },
        "prioritized_still_missing": none_found[:500],
        "recoverable_count": len(recoverable),
    }

    RESULTS_FILE.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    SUMMARY_FILE.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    # GAP_REPORT.md for Freeman / Leonard
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# GAP_REPORT — taiwanjustice.net residual archive gaps")
    lines.append("")
    lines.append(f"**Generated:** {summary['generated_at']}  ")
    lines.append(f"**Script:** `{summary['script_version']}`  ")
    lines.append(f"**Kanban:** `t_6b71e5a7` TJ-P4  ")
    lines.append("")
    lines.append("## Context")
    lines.append("")
    lines.append("After Wayback bulk download (P2) + fail-retry (P2b), residual download-state fails were checked against secondary archives.")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|------:|")
    lines.append(f"| Residual fails (download-state) | {len(residual)} |")
    lines.append(f"| Content URLs checked | {len(content)} |")
    lines.append(f"| Non-content skipped (media/feed/etc.) | {len(non_content)} |")
    lines.append(f"| Recoverable from ≥1 secondary source | {any_found} |")
    lines.append(f"| Still missing all secondaries | {len(none_found)} |")
    lines.append(f"| Arquivo.pt hits | {summary['coverage']['arquivo']} |")
    lines.append(f"| Ghostarchive per-URL hits | {summary['coverage']['ghostarchive']} |")
    lines.append(f"| IA CDX recheck hits | {summary['coverage']['internet_archive_cdx']} |")
    lines.append(f"| Ghostarchive domain-level hits | {len(ga_domain)} |")
    lines.append("")
    lines.append("## Source availability (from pinto, this run)")
    lines.append("")
    lines.append(f"- **Arquivo.pt CDX:** used as primary secondary index")
    lines.append(f"- **Ghostarchive:** HTML search `?term=` works; domain search returned {len(ga_domain)} hit(s)")
    lines.append(f"- **Internet Archive CDX:** best-effort recheck (timeouts/503 possible)")
    lines.append(f"- **Common Crawl index:** **unavailable** from this host — `{cc_probe.get('error')}`")
    lines.append(f"- **Memento TimeTravel (`timetravel.mementoweb.org`):** DNS resolve failed on pinto")
    lines.append("")
    lines.append("## Ghostarchive domain captures")
    lines.append("")
    if ga_domain:
        for h in ga_domain:
            lines.append(f"- [{h.get('timestamp','')}]({h.get('snapshot_url')}) — `{h.get('url')}`")
    else:
        lines.append("_None parsed._")
    lines.append("")
    lines.append("## Recoverable residual content URLs (sample)")
    lines.append("")
    if recoverable:
        for r in recoverable[:50]:
            srcs = ", ".join(r.get("sources_found") or [])
            snap = None
            for k in ("arquivo", "ghostarchive", "internet_archive_cdx"):
                if r.get(k, {}).get("found"):
                    snap = r[k].get("snapshot_url")
                    break
            lines.append(f"- `{r['url']}`")
            lines.append(f"  - sources: {srcs}")
            if snap:
                lines.append(f"  - snapshot: {snap}")
    else:
        lines.append("_No residual content URL matched secondary indexes in this pass._")
    lines.append("")
    lines.append("## Still missing (content) — for Freeman if unique copies exist")
    lines.append("")
    lines.append("These residual content URLs were not found in Arquivo.pt / Ghostarchive / IA CDX during this run.")
    lines.append("They may still exist only on private disks, email newsletters, or social shares.")
    lines.append("")
    if none_found:
        for u in none_found[:100]:
            lines.append(f"- {u}")
        if len(none_found) > 100:
            lines.append(f"- … and {len(none_found) - 100} more (see `gap_fill_summary.json`)")
    else:
        lines.append("_None — all residual content URLs had at least one secondary hit (or list empty)._")
    lines.append("")
    lines.append("## Artifacts")
    lines.append("")
    lines.append("- `knowledge/web-archives/taiwanjustice-net/gap_fill_results.json`")
    lines.append("- `knowledge/web-archives/taiwanjustice-net/gap_fill_summary.json`")
    lines.append("- `knowledge/research/taiwanjustice-net/GAP_REPORT.md` (this file)")
    lines.append("")
    lines.append("## Recommended next steps")
    lines.append("")
    lines.append("1. Optionally fetch Arquivo/Ghostarchive bodies for recoverable URLs into `raw-html/` + re-run Tier2 converter.")
    lines.append("2. Ask Freeman only for **still-missing content** titles if high-value.")
    lines.append("3. Proceed TJ-P5 Tier-1 absorb on healthy Tier2 corpus (29k md) — do not block P5 on residual media fails.")
    lines.append("")
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Wrote", RESULTS_FILE)
    print("Wrote", SUMMARY_FILE)
    print("Wrote", REPORT_FILE)
    print(
        f"DONE content={len(content)} any={any_found} none={len(none_found)} "
        f"arquivo={summary['coverage']['arquivo']} ga={summary['coverage']['ghostarchive']} ia={summary['coverage']['internet_archive_cdx']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

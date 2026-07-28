#!/usr/bin/env python3
"""Phase 2: Bulk Wayback download for taiwanjustice.net.

Resume-safe, rate-limited, parking-aware. Keeps full HTML (comments embedded).
Reads P1 inventory: knowledge/research/taiwanjustice-net/cdx-unique-urls.jsonl
Writes: knowledge/web-archives/taiwanjustice-net/
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/leedt/echo-system")
INV = ROOT / "knowledge/research/taiwanjustice-net/cdx-unique-urls.jsonl"
OUT = ROOT / "knowledge/web-archives/taiwanjustice-net"
RAW = OUT / "raw-html"
STATE = OUT / "download-state.json"
MANIFEST = OUT / "DOWNLOAD_MANIFEST.jsonl"
LOG = OUT / "download.log"
PARKING_FILE = ROOT / "knowledge/research/taiwanjustice-net/PARKING_DIGESTS.txt"
PROGRESS = OUT / "progress.json"

USER_AGENT = "EchopediaTAHS-ArchiveRecovery/1.0 (historical bulk; multi-day; +taiwanjustice)"
SLEEP_S = float(os.environ.get("TJ_SLEEP", "0.85"))
TIMEOUT = int(os.environ.get("TJ_TIMEOUT", "90"))
MAX_RETRIES = 4
# Optional cap for testing: TJ_MAX_DOWNLOADS=100
MAX_DOWNLOADS = int(os.environ.get("TJ_MAX_DOWNLOADS", "0"))  # 0 = unlimited

PARKING_MARKERS = (
    b"Parked Domain name on Hostinger",
    b"Parked Domain",
    b"Hostinger DNS system",
    b"domain is parked",
)

# Skip pure junk — not high-value content
SKIP_SUBSTR = (
    "/wp-login.php",
    "/xmlrpc.php",
    "/wp-cron.php",
    "/wp-admin/",
    "reauth=1",
    "/cgi-bin/",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg: str) -> None:
    line = f"{utc_now()} {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {
        "done_urls": {},  # original -> {path, status, sha256, ts, bytes}
        "parking_digests": [],
        "stats": {
            "ok": 0,
            "parking": 0,
            "fail": 0,
            "skip": 0,
            "bytes": 0,
        },
        "started_at": utc_now(),
        "updated_at": utc_now(),
    }


def save_state(state: dict) -> None:
    state["updated_at"] = utc_now()
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE)
    PROGRESS.write_text(
        json.dumps(
            {
                "updated_at": state["updated_at"],
                "stats": state["stats"],
                "done_count": len(state["done_urls"]),
                "started_at": state.get("started_at"),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def priority(rec: dict) -> int:
    c = rec.get("class") or "other"
    order = {
        "newsletter": 0,
        "article_candidate": 1,
        "comment_related": 2,
        "category": 3,
        "author": 4,
        "tag": 5,
        "home": 6,
        "feed": 7,
        "other": 8,
        "static_asset": 9,
        "binary_asset": 10,
        "wordpress_infra": 11,
        "pagination": 12,
    }
    return order.get(c, 50)


def should_skip_url(url: str) -> bool:
    low = url.lower()
    return any(s in low for s in SKIP_SUBSTR)


def safe_name(url: str, ts: str) -> str:
    # stable filename from url + ts
    h = hashlib.sha1(f"{ts}|{url}".encode()).hexdigest()[:16]
    path = urllib.parse.urlparse(url).path or "/"
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff\-]+", "_", urllib.parse.unquote(path))[:80].strip("_")
    if not slug:
        slug = "root"
    return f"{ts}_{slug}_{h}.html"


def wayback_id_url(ts: str, original: str) -> str:
    # Normalize :80 junk
    original = original.replace("http://www.taiwanjustice.net:80", "http://www.taiwanjustice.net")
    original = original.replace("https://www.taiwanjustice.net:80", "https://www.taiwanjustice.net")
    return f"https://web.archive.org/web/{ts}id_/{original}"


def is_parking(body: bytes) -> bool:
    head = body[:8000]
    return any(m in head for m in PARKING_MARKERS)


def fetch(url: str) -> tuple[int, bytes, str]:
    last_err = ""
    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                code = getattr(resp, "status", 200) or 200
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
                return code, data, ctype
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}"
            if e.code in (429, 503, 504):
                time.sleep(min(120, 5 * (2**attempt)))
                continue
            if e.code == 404:
                return 404, b"", ""
            time.sleep(2**attempt)
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
            time.sleep(min(60, 2**attempt))
    return 0, b"", last_err


def load_queue() -> list[dict]:
    rows: list[dict] = []
    with INV.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if str(rec.get("statuscode")) != "200":
                continue
            url = rec.get("original") or ""
            if should_skip_url(url):
                continue
            # Prefer HTML + known content; still keep images under newsletter/wp-content
            mime = (rec.get("mimetype") or "").lower()
            cls = rec.get("class") or ""
            if mime.startswith("text/") or mime in ("application/xhtml+xml", "application/xml", "application/rss+xml", ""):
                rows.append(rec)
            elif cls in ("newsletter", "binary_asset") or "wp-content/uploads" in url:
                rows.append(rec)
            elif mime.startswith("image/") and cls != "wordpress_infra":
                rows.append(rec)
    rows.sort(key=lambda r: (priority(r), r.get("timestamp") or ""))
    return rows


def append_manifest(entry: dict) -> None:
    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def process_one(
    rec: dict,
    state: dict,
    parking_set: set,
    *,
    is_retry: bool = False,
) -> str:
    """Fetch+store one inventory record. Returns outcome: ok|fail|parking|skip."""
    original = rec["original"]
    ts = rec["timestamp"]
    digest = rec.get("digest") or ""

    if digest in parking_set:
        state["stats"]["parking"] += 1
        state["done_urls"][original] = {
            "status": "parking_digest_skip",
            "digest": digest,
            "ts": ts,
        }
        state["stats"]["skip"] += 1
        return "skip"

    wb = wayback_id_url(ts, original)
    code, body, ctype = fetch(wb)
    time.sleep(SLEEP_S)

    if code != 200 or not body:
        # On retry, replace prior fail; don't double-count fail if already failed
        prev = state["done_urls"].get(original) or {}
        if not (is_retry and prev.get("status") == "fail"):
            state["stats"]["fail"] += 1
        entry = {
            "status": "fail",
            "http": code,
            "original": original,
            "archive_ts": ts,
            "wayback": wb,
            "error": ctype if code == 0 else f"http_{code}",
            "at": utc_now(),
            "retry": bool(is_retry),
        }
        state["done_urls"][original] = entry
        append_manifest(entry)
        return "fail"

    if is_parking(body):
        sha = hashlib.sha256(body).hexdigest()
        parking_set.add(digest)
        parking_set.add(sha)
        state["parking_digests"] = sorted(parking_set)
        prev = state["done_urls"].get(original) or {}
        if is_retry and prev.get("status") == "fail":
            state["stats"]["fail"] = max(0, int(state["stats"].get("fail") or 0) - 1)
        state["stats"]["parking"] += 1
        entry = {
            "status": "parking",
            "original": original,
            "archive_ts": ts,
            "sha256": sha,
            "digest_cdx": digest,
            "bytes": len(body),
            "at": utc_now(),
            "retry": bool(is_retry),
        }
        state["done_urls"][original] = entry
        append_manifest(entry)
        PARKING_FILE.write_text(
            "# Parking digests/hashes (Hostinger or empty park)\n"
            + "\n".join(sorted(parking_set))
            + f"\n# updated {utc_now()}\n",
            encoding="utf-8",
        )
        return "parking"

    ext = ".html"
    if "image/jpeg" in ctype or original.lower().endswith((".jpg", ".jpeg")):
        ext = ".jpg"
    elif "image/png" in ctype or original.lower().endswith(".png"):
        ext = ".png"
    elif "pdf" in ctype or original.lower().endswith(".pdf"):
        ext = ".pdf"
    elif "xml" in ctype or "rss" in ctype:
        ext = ".xml"

    fname = safe_name(original, ts).rsplit(".", 1)[0] + ext
    year = ts[:4] if ts else "unknown"
    dest_dir = RAW / year
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / fname
    dest.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()

    meta = {
        "source_url": original,
        "archive_ts": ts,
        "archive_url": f"https://web.archive.org/web/{ts}/{original}",
        "wayback_id_url": wb,
        "cdx_digest": digest,
        "cdx_mimetype": rec.get("mimetype"),
        "cdx_class": rec.get("class"),
        "content_type": ctype,
        "sha256": sha,
        "bytes": len(body),
        "fetched_at": utc_now(),
        "method": "wayback-id_",
        "keep_comments": True,
        "keep_newsletters": True,
        "retry": bool(is_retry),
    }
    dest.with_suffix(dest.suffix + ".json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    prev = state["done_urls"].get(original) or {}
    if is_retry and prev.get("status") == "fail":
        state["stats"]["fail"] = max(0, int(state["stats"].get("fail") or 0) - 1)

    entry = {
        "status": "ok",
        "original": original,
        "path": str(dest.relative_to(ROOT)),
        "archive_ts": ts,
        "sha256": sha,
        "bytes": len(body),
        "class": rec.get("class"),
        "at": utc_now(),
        "retry": bool(is_retry),
    }
    state["done_urls"][original] = entry
    state["stats"]["ok"] += 1
    state["stats"]["bytes"] += len(body)
    append_manifest(entry)
    return "ok"


def collect_fail_urls(state: dict) -> set[str]:
    """URLs currently marked fail in state (authoritative for retry)."""
    out: set[str] = set()
    for url, meta in (state.get("done_urls") or {}).items():
        if isinstance(meta, dict) and meta.get("status") == "fail":
            out.add(url)
    return out


def main() -> int:
    retry_fails = "--retry-fails" in sys.argv or os.environ.get("TJ_RETRY_FAILS") == "1"

    OUT.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)
    state = load_state()
    parking_set = set(state.get("parking_digests") or [])

    mode = "P2-retry-fails" if retry_fails else "P2"
    log(
        f"{mode} start sleep={SLEEP_S}s max={MAX_DOWNLOADS or 'unlimited'} "
        f"done_already={len(state['done_urls'])}"
    )
    queue = load_queue()
    log(f"queue size after filters: {len(queue)}")

    if not parking_set:
        parking_set.add("LIVE_HOSTINGER_TITLE")

    fail_urls: set[str] = set()
    if retry_fails:
        fail_urls = collect_fail_urls(state)
        log(f"retry queue: {len(fail_urls)} fail URLs from state")
        if not fail_urls:
            log("no fails to retry — exit")
            return 0

    processed_this_run = 0
    try:
        for rec in queue:
            original = rec["original"]

            if retry_fails:
                if original not in fail_urls:
                    continue
            else:
                if original in state["done_urls"]:
                    continue

            outcome = process_one(rec, state, parking_set, is_retry=retry_fails)
            processed_this_run += 1
            if processed_this_run % 5 == 0:
                save_state(state)
                log(
                    f"progress mode={mode} n={processed_this_run} "
                    f"last={outcome} done={len(state['done_urls'])} stats={state['stats']}"
                )
            if MAX_DOWNLOADS and processed_this_run >= MAX_DOWNLOADS:
                log(f"hit TJ_MAX_DOWNLOADS={MAX_DOWNLOADS}")
                break

    except KeyboardInterrupt:
        log("interrupted — saving state")
    finally:
        state["parking_digests"] = sorted(parking_set)
        save_state(state)
        log(f"{mode} checkpoint stats={state['stats']} done_urls={len(state['done_urls'])}")

    summary = {
        "updated_at": utc_now(),
        "mode": mode,
        "stats": state["stats"],
        "done_urls": len(state["done_urls"]),
        "queue_total": len(queue),
        "remaining_est": (
            len(collect_fail_urls(state))
            if retry_fails
            else max(0, len(queue) - len(state["done_urls"]))
        ),
        "retry_fails_remaining": len(collect_fail_urls(state)),
        "out": str(OUT),
        "raw": str(RAW),
    }
    (OUT / "download-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    log(f"summary {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fetch one taiwandaily.net month into knowledge/web-archives/.

Listing is /date/YYYY/MM/page/N/ . The ?m=YYYYMM front page is not an archive.
Writes tdm-YYYYMM.json and one markdown file per article. Never creates a
kanban card. Resume: an existing article file is not fetched again.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

# Imported lazily inside extract_body() rather than at module level. WHY:
# --verify is the manifest GATE every taiwandaily slice card runs first, and
# verify()/grade() touch neither the network nor trafilatura. A module-level
# import made the gate die with ModuleNotFoundError on any interpreter missing
# the scraper, and the card's rule is "believe the exit code" — so a crash
# (exit 1) was indistinguishable from a genuine REFETCH verdict and would
# wrongly close a healthy month as `manifest-incomplete`. Fetching still fails
# loudly here, at the first byte of extraction, exactly as before.
try:
    import trafilatura
except ModuleNotFoundError:  # pragma: no cover - gate path must stay importable
    trafilatura = None

REPO = Path.home() / "echo-system"
ARCH = REPO / "knowledge" / "web-archives"
UA = "Mozilla/5.0 (compatible; echopedia-archive/1.0)"
ART_RE = re.compile(
    r"https?://(?:www\.)?taiwandaily\.net/([^\"'\s<>]+)/(\d+)/", re.I
)
# The date archive itself matches ART_RE: /date/2024/11/page/1/ looks like
# category "date/2024/11" with article id "1". Without this the listing fills
# with pagination links and the month "completes" at ~8% coverage.
NAV_PREFIXES = ("date/", "page/", "paged/", "author/", "category/", "tag/",
                "comments/", "attachment/", "feed/", "wp-", "xmlrpc")
DATE_RE = re.compile(r'datetime="(\d{4}-\d{2}-\d{2})')
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)


def extract_body(html: str) -> str:
    """Article text, with a recall fallback.

    WHY (measured 2026-10-19): favor_precision=True discards short opinion posts down to
    ~9 chars — the title and nothing else. The caller's gate is len(body) < 40, so those
    pages were filed `empty-extract` and written to no file. Default extraction returns
    ~460 chars for the SAME 25 pages (政治評論 / uncategorized in 202411 + 202601). The
    precision pass is kept because it is cleaner on real news copy; it is simply not
    allowed to be the last word.
    """
    if trafilatura is None:
        raise RuntimeError(
            "trafilatura is not installed in this interpreter; fetching would "
            "extract every body as empty and mis-file real articles as "
            "empty-extract. Install trafilatura or run the fetcher from the "
            "interpreter that has it (--verify does not need it)."
        )
    body = trafilatura.extract(html, include_comments=False, favor_precision=True) or ""
    if len(body) < 40:
        body = trafilatura.extract(html, include_comments=False) or ""
    return body


def fetch(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def month_parts(ym: str) -> tuple[str, str, str]:
    if not re.fullmatch(r"20\d{4}", ym):
        raise SystemExit(f"bad month {ym}")
    return ym, ym[:4], ym[4:]


def listing_entries(html: str, ym: str) -> list[dict]:
    """Parse the post modules, not the whole page.

    A td-module block carries its own href and its own datetime. Matching
    hrefs against the nearest datetime anywhere on the page instead pairs
    every article with the sidebar's recent posts, which makes a working
    archive look empty.
    """
    want = f"{ym[:4]}-{ym[4:]}"
    out = []
    for block in re.split(r'class="td-module-', html)[1:]:
        m_href = re.search(r'href="(https?://[^"]+/(\d{4,})/)"', block)
        # Capture the FULL date (measured 2026-10-20): the old 7-char capture
        # stored date="2026-07" on listing-sourced records, and coverage()'s
        # startswith filter counted that string as one extra phantom day —
        # 202607 graded days=32/31 in a 31-day month.
        m_dt = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', block)
        if not m_href or not m_dt:
            continue
        if not m_dt.group(1).startswith(want):
            continue
        cat = m_href.group(1).split("taiwandaily.net/")[-1].rsplit("/", 2)[0]
        if cat.lower().startswith(NAV_PREFIXES):
            continue
        out.append({"id": m_href.group(2), "url": m_href.group(1), "date": m_dt.group(1)})
    return out


def list_articles(ym: str) -> tuple[list[dict], int]:
    _, year, month = month_parts(ym)
    seen: dict[str, dict] = {}
    pages = 0
    empty = 0
    # Identical-page detector (measured 2026-10-20): /date/2026/07/ and its
    # /page/N/ variants return the SAME current-posts page — same module ids
    # 163392…, October datetimes in the modules, with a handful of stale
    # July datetimes that the ym filter happily matched, so the dead archive
    # masqueraded as a working 10/page listing. A live archive never repeats
    # its module-id fingerprint; a dead one repeats it every page.
    fp_seen: dict[str, int] = {}
    for n in range(1, 401):
        url = f"https://www.taiwandaily.net/date/{year}/{month}/page/{n}/"
        if n == 1:
            url = f"https://www.taiwandaily.net/date/{year}/{month}/"
        try:
            html = fetch(url)
        except urllib.error.HTTPError as e:
            print(f"list page {n} http {e.code}", flush=True)
            break
        except Exception as e:
            print(f"list page {n} {type(e).__name__}: {e}", flush=True)
            break
        blocks = re.split(r'class="td-module-', html)[1:]
        fp = ",".join(sorted({
            m.group(1) for b in blocks
            for m in [re.search(r'href="https?://[^"]+/(\d{4,})/"', b)] if m}))
        if fp:
            fp_seen[fp] = fp_seen.get(fp, 0) + 1
            if fp_seen[fp] >= 3:
                print(f"list page {n}: identical page 3x — dead date archive, "
                      f"aborting listing", flush=True)
                return [], pages
        new = 0
        for item in listing_entries(html, ym):
            if item["id"] in seen:
                continue
            seen[item["id"]] = item
            new += 1
        pages = n
        print(f"list page {n} new={new} total={len(seen)}", flush=True)
        if new == 0:
            empty += 1
            if empty >= 3:
                break
        else:
            empty = 0
        time.sleep(0.2)
    if len(seen) < 50 or (pages >= 5 and len(seen) / pages < 4):
        print(f"ABORT {ym} listing looks wrong: {len(seen)} articles over {pages} pages", flush=True)
        return [], pages
    return list(seen.values()), pages


def article_file(art_id: str) -> Path:
    return ARCH / f"taiwandaily-net-{art_id}-{art_id}.md"


# ---- ID-scan listing: the replacement for the dead date archive ------------
# WHY (measured 2026-10-20): /date/YYYY/MM/ now serves the SAME current-posts
# page for every month (2026/07 and 2026/10 returned byte-length-identical
# pages full of October datetimes; /date/2024/11/ too). That is how tdm-202607
# ended up holding articles published 2026-10-04 and 2024-01-09. The WP REST
# API is 401, Wayback has no snapshots of the July listing, and the AIOSEO
# sitemap's lastmod is the MODIFIED date (article 161: published 2024-01-09,
# sitemap says 2024-01-24) — so the only complete per-article date source left
# is the article page itself: JSON-LD datePublished, reachable by sequential id
# at /?p=ID (404 = no post, soft-error pages carry no JSON-LD at all).
# Post ids are monotonic in publish date (verified 143000->2026-06-19 …
# 161000->2026-10-05, no inversions), so binary search bounds the month and a
# range scan enumerates it. Posts are discriminated from static pages by
# "@type":"BlogPosting" (pages are "WebPage"); video posts are BlogPosting too.

POSTING_RE = re.compile(r'"@type"\s*:\s*"BlogPosting"')
CANON_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')


PROBE_READ_BYTES = 131072  # 128 KB


def id_html_probe(art_id: int, timeout: int = 30) -> str | None:
    """PROBE-ONLY cheap read of /?p=ID (t_7766bcaf, measured 2026-10-20).

    The full page is ~520 KB and costs ~9 s; the first 128 KB arrives in
    ~2 s. All 15 sampled BlogPosting pages carry their JSON-LD block at
    bytes ~2.4-2.8 KB and the canonical <link> in <head>, so a 128 KB
    prefix is a superset of everything parse_post() reads. If the prefix
    has no BlogPosting AND the page is bigger than the prefix we fall back
    to the full fetch, so a probe can never be a false negative vs
    id_html(); 404/soft-error semantics are identical.
    NEVER use this where the body is archived — only for date probes.
    """
    return id_html(art_id, timeout=timeout, probe_bytes=PROBE_READ_BYTES)


def id_html(art_id: int, timeout: int = 30,
            probe_bytes: int | None = None) -> str | None:
    """HTML for /?p=ID, or None for 404 / soft-error / transient failure
    after retries. Soft-error pages (no title, no JSON-LD) are indistinguish-
    able from absent posts for our purpose."""
    url = f"https://www.taiwandaily.net/?p={art_id}"
    for attempt in range(3):
        try:
            if probe_bytes:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return resp.read(probe_bytes).decode("utf-8", "replace")
            return fetch(url, timeout=timeout)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            return None
        except Exception:
            if attempt < 2:
                time.sleep(1 + attempt)
                continue
            return None
    return None


def parse_post(html: str) -> dict | None:
    """{'date','url'} for a real BlogPosting article, else None."""
    if not POSTING_RE.search(html):
        return None
    m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    if not m:
        return None
    c = CANON_RE.search(html)
    return {"date": m.group(1), "url": c.group(1) if c else ""}


def max_post_id() -> int:
    html = fetch("https://www.taiwandaily.net/")
    ids = [int(x) for x in re.findall(r'taiwandaily\.net/(?:[^/"]+/)?(\d{4,})/', html)]
    return max(ids) if ids else 0


def _dates_for(ids: list[int], workers: int = 8) -> dict[int, str]:
    """Parallel {id: publish-date} for existing BlogPosting ids."""
    with ThreadPoolExecutor(max_workers=workers) as ex:
        pages = list(ex.map(lambda i: (i, id_html(i)), ids))
    out: dict[int, str] = {}
    for i, html in pages:
        if not html:
            continue
        p = parse_post(html)
        if p:
            out[i] = p["date"]
    return out


def _first_id_at_or_after(target: str, hi_probe: int, workers: int = 8) -> int:
    """First post id whose publish date >= target 'YYYY-MM-DD'.

    Grid refinement, not plain binary search: the id space has 2000-id
    sparse stretches (measured 151000..153000), so serial probing timed out
    a 300s budget. Each round probes ~64 ids in parallel and narrows to the
    bracketing interval. Unknown/missing probes bias the lower bound DOWN
    (a too-wide scan wastes fetches; a too-narrow one loses articles).
    """
    lo, hi = 100, hi_probe
    while hi - lo > 2:
        step = max(1, (hi - lo) // 64)
        ids = list(range(lo, hi + 1, step))
        dd = _dates_for(ids, workers)
        cands = [i for i, d in dd.items() if d >= target]
        if cands:
            hi = min(cands)
        else:
            jumped = max(dd.keys(), default=lo)
            lo = max(lo + 1, jumped + 1)  # always progress
    return hi


def find_id_bounds(ym: str) -> tuple[int, int]:
    """Inclusive id range that can contain posts published in ym."""
    y, mo = int(ym[:4]), int(ym[4:])
    ny, nmo = (y + 1, 1) if mo == 12 else (y, mo + 1)
    start = f"{ym[:4]}-{ym[4:]}-01"
    end = f"{ny:04d}-{nmo:02d}-01"
    hi_id = max_post_id() + 100
    newest = _dates_for([hi_id - 100, hi_id - 50, hi_id - 10, hi_id])
    if newest and max(newest.values()) < start:
        return 0, -1  # month is in the future / site has no such posts
    lo = _first_id_at_or_after(start, hi_id)
    hi = _first_id_at_or_after(end, hi_id) - 1
    return max(100, lo - 30), hi + 30


def set_published(path: Path, date: str) -> bool:
    """Write the published: key into an existing file's frontmatter.

    The pre-direct-trafilatura fetcher wrote no published: key, so months
    fetched with it grade days=0/N no matter how complete they are. This
    backfills the key from the authoritative article-page datePublished
    without touching the body. Returns True if the file changed.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    fm = text[:end]
    m = re.search(r"^published:\s*(\d{4}-\d{2}-\d{2})[^\n]*$", fm, re.M)
    if m:
        if m.group(1) == date:
            return False
        fm = fm[: m.start()] + f"published: {date}" + fm[m.end():]
    elif re.search(r"^published:\s*$", fm, re.M):
        fm = re.sub(r"^published:\s*$", f"published: {date}", fm, count=1, flags=re.M)
    else:
        fm = fm + f"\npublished: {date}"
    path.write_text(fm + text[end:], encoding="utf-8")
    return True


def write_from_html(art_id: str, url: str, html: str | None, ym: str,
                    published: str) -> dict:
    """Archive one already-fetched article page. Shared by the date-archive
    path (one_article) and the id-scan path, so both produce identical files
    and identical manifest records — including the per-article date.
    html=None means the file is already a valid archive: only the published:
    key is backfilled, no body parsing."""
    dest = article_file(art_id)
    if html is None or is_valid_archive(dest):
        set_published(dest, published)
        return {"url": url, "file": dest.name, "bytes": dest.stat().st_size,
                "status": "exists", "date": published, "id": art_id}
    if dest.exists() and not is_valid_archive(dest):
        try:
            dest.unlink()
        except OSError:
            pass
    title_m = TITLE_RE.search(html)
    title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else art_id
    body = extract_body(html)
    if len(body) < 40:
        # 熱門影音 posts are videos with no text body. The page is a correct,
        # complete fetch — it simply has no article container (verified: zero
        # td-post-content/entry-content/articleBody markers, distinct correct
        # titles). Calling that `empty-extract` scored it a failure and pinned
        # the month's archive rate at 0.32, so a complete month read PARTIAL.
        if is_video_post(html):
            text = (
                "---\n"
                f"source_url: {url}\n"
                f"fetched: {datetime.now().date().isoformat()}\n"
                "method: direct-trafilatura\n"
                f"title: {json.dumps(title, ensure_ascii=False)}\n"
                f"published: {published}\n"
                "domain: taiwandaily.net\n"
                "kind: video\n"
                "---\n\n"
                "（影音篇，無文字內文。Video post — title and date archived, no body.）\n"
            )
            dest.write_text(text, encoding="utf-8")
            return {"url": url, "file": dest.name, "bytes": dest.stat().st_size,
                    "status": "ok-video", "date": published, "id": art_id}
        return {"url": url, "file": None, "bytes": 0, "status": "empty-extract",
                "date": published, "id": art_id}
    text = (
        "---\n"
        f"source_url: {url}\n"
        f"fetched: {datetime.now().date().isoformat()}\n"
        "method: direct-trafilatura\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"published: {published}\n"
        "domain: taiwandaily.net\n"
        "---\n\n"
        f"{body}\n"
    )
    dest.write_text(text, encoding="utf-8")
    return {"url": url, "file": dest.name, "bytes": dest.stat().st_size,
            "status": "ok", "date": published, "id": art_id}


def scan_month(ym: str, workers: int = 5,
               bounds: tuple[int, int] | None = None) -> tuple[list[dict], int, tuple[int, int]]:
    """Enumerate + archive a month by scanning the post-id range.

    Returns (results, scanned_ids, (lo, hi)) in the shape main expects.
    Every settled record carries its per-article date, so coverage() has a
    real signal. This is the listing the dead /date/ archive can no longer
    give; it is also strictly better — the date archive silently leaked
    current-page content, the id range cannot lie about a publish date that
    the article page itself prints.
    """
    lo, hi = bounds if bounds else find_id_bounds(ym)
    want = f"{ym[:4]}-{ym[4:]}"
    print(f"id-scan {ym}: range {lo}..{hi} ({hi - lo + 1} ids)", flush=True)
    # Resume cache: an id-scan of an 18k-id range is an hour of fetches, and
    # the first 202607/202610 run lost everything when the worker iteration
    # budget cut it off. Cache every probe ("" = probed, not an article) and
    # reuse it across runs; delete the cache file to force a re-probe.
    cache_path = ARCH / f"tdm-{ym}.idscan-cache.json"
    cache: dict[str, str] = {}
    if cache_path.exists():
        try:
            cache = {str(k): str(v) for k, v in
                     json.loads(cache_path.read_text()).items()}
            print(f"id-scan {ym}: resume cache {len(cache)} ids", flush=True)
        except Exception:
            cache = {}

    def save_cache() -> None:
        tmp = cache_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(cache), encoding="utf-8")
        tmp.replace(cache_path)

    results: list[dict] = []
    found = 0
    chunk = 50
    for c0 in range(lo, hi + 1, chunk):
        ids = [i for i in range(c0, min(c0 + chunk, hi + 1))
               if str(i) not in cache]
        if ids:
            def _probe(i: int) -> str | None:
                # Cheap prefix read for the date probe (t_7766bcaf); full
                # fetch only when the prefix is too small to disprove a post.
                html = id_html_probe(i)
                if (html is not None and len(html) >= PROBE_READ_BYTES
                        and not POSTING_RE.search(html)):
                    html = id_html(i)
                return html
            with ThreadPoolExecutor(max_workers=workers) as ex:
                pages = list(ex.map(lambda i: (i, _probe(i)), ids))
            for i, html in pages:
                post = parse_post(html) if html else None
                cache[str(i)] = (post["date"] + "|" + post["url"]) if post else ""
            save_cache()
        for i in range(c0, min(c0 + chunk, hi + 1)):
            v = cache.get(str(i), "")
            if not v or not v.startswith(want):
                continue
            d, _, url = v.partition("|")
            if not d.startswith(want):
                continue
            found += 1
            dest = article_file(str(i))
            if not is_valid_archive(dest):  # refetch only hits we must write
                html = id_html(i)
                if html is None:
                    continue
            else:
                html = None
            results.append(write_from_html(
                str(i), url or f"https://www.taiwandaily.net/?p={i}",
                html, ym, d))
        if (c0 // chunk) % 10 == 0:
            # Persist partial progress so verify() sees a live picture and an
            # interrupted run never starts the index from zero.
            write_manifest(ym, hi - lo + 1, results, done=False,
                           listing=f"https://www.taiwandaily.net/?p={lo}..{hi} (post-id scan)")
        print(f"id-scan {ym}: {min(c0 + chunk, hi + 1) - lo}/{hi - lo + 1} ids, {found} in month", flush=True)
    save_cache()
    return results, hi - lo + 1, (lo, hi)


def published_date(html: str) -> str:
    """The first datetime=" on this site is the header's last-updated stamp,
    not the article date. Trusting it skipped every article fetched."""
    m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    m = re.search(r'class="[^"]*entry-date[^"]*"[^>]*datetime="(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    m = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', html)
    return m.group(1) if m else ""


ERROR_STUB_RE = re.compile(
    r'RateLimitTriggeredError|Per IP rate limit|"name"\s*:\s*"[A-Za-z]*Error"'
    # WP fatal DB page (measured 2026-10-20, t_7766bcaf): the curl-era fetcher
    # saved 448-byte "資料庫錯誤 / 建立資料庫連線時發生錯誤" upstream error
    # pages that the JSON-shape check missed, so 60 of them sat in
    # tdm-202410 as settled-valid and were never refetched. Strengthening
    # only: more files judged invalid -> refetched, never fewer.
    r'|建立資料庫連線時發生錯誤|Error establishing a database connection'
)


def is_valid_archive(path: Path) -> bool:
    """A >200-byte file is NOT proof of an archived article.

    The jina-era fetch wrote upstream error payloads to disk verbatim
    ({"data":null,...,"code":429,"name":"RateLimitTriggeredError"} with an
    empty `published:`), and the old `size > 200` gate froze 102 of them into
    tdm-202411.json as status=exists — permanently unrefetchable while
    grade() still reported days=30/30 PASS.

    Deliberately NOT a `published:`-date requirement: 16,996 of 34,491 real
    archived files carry no published date (4,655 of them >2KB), so a date
    gate would delete genuine articles. Validity is decided by upstream-error
    SHAPE only — a null-data JSON error body, or a jina rate-limit marker.
    """
    try:
        if not path.exists() or path.stat().st_size <= 200:
            return False
        head = path.read_text(errors="ignore")[:1200]
    except OSError:
        return False
    body = head.split("---", 2)[-1]  # skip YAML frontmatter, inspect the payload
    if '"data":null' in body.replace(" ", "") and re.search(r'"code"\s*:\s*\d{3}', body):
        return False
    if ERROR_STUB_RE.search(body):
        return False
    return True


def one_article(item: dict, ym: str) -> dict:
    art_id = item["id"]
    url = item["url"]
    dest = article_file(art_id)
    known_date = str(item.get("date") or "")
    if is_valid_archive(dest):
        if known_date:
            set_published(dest, known_date)
        return {
            "url": url,
            "file": dest.name,
            "bytes": dest.stat().st_size,
            "status": "exists",
            "date": known_date,
            "id": art_id,
        }
    if dest.exists() and not is_valid_archive(dest):
        # Invalid on content (upstream error payload): remove it so the fetch
        # below actually runs, instead of a stale file short-circuiting forever.
        try:
            dest.unlink()
        except OSError:
            pass
    try:
        html = fetch(url, timeout=30)
    except Exception as e:
        return {"url": url, "file": None, "bytes": 0, "status": f"fetch-fail:{type(e).__name__}", "id": art_id}
    published = published_date(html) or known_date
    want = f"{ym[:4]}-{ym[4:]}"
    if published and not published.startswith(want):
        return {
            "url": url,
            "file": None,
            "bytes": 0,
            "status": f"skipped-not-{ym}:{published}",
            "date": published,
            "id": art_id,
        }
    return write_from_html(art_id, url, html, ym, published)


def expected_days(ym: str) -> int:
    import calendar
    return calendar.monthrange(int(ym[:4]), int(ym[4:]))[1]


def file_published(path: Path) -> str:
    """Legacy manifests carry no per-article date. The article file's own
    frontmatter does, so read it rather than calling a covered day missing.

    WHY the body fallback (measured 2026-10-19): the pre-direct-trafilatura
    fetcher (`method: curl+trafilatura`) wrote no `published:` key at all — its
    date survives only as the body's `Published Time: YYYY-MM-DD` line.
    tdm-202510 graded days=0/31 -> REFETCH while holding 1529/1529 files on
    disk with all 31 days present: a complete month locked out by a schema the
    grader could not read. This fallback only ADDS a date source, so it cannot
    turn a real fragment into a PASS — re-graded with it, the other legacy
    months still fail (202512 0/31, 202601 7/31, 202603 1/31, 202604 5/30,
    202605 2/31, 202606 2/30).

    WHY the date_published key (measured 2026-10-20): a third frontmatter key
    exists — the fetcher that wrote tdm-202506 emitted
    `date_published: YYYY-MM-DDTHH:MM:SS-07:00` and neither pattern above
    reads it. tdm-202506 graded days=0/30 -> REFETCH while holding 1376/1376
    ok files on disk with all 30 days present (census: date_published
    1376/1376, published: 0, Published Time: 0): the same lockout as 202510,
    a different key. With this pattern the month re-grades days=0/30 ->
    30/30 PASS. Additive only, same class as the body fallback — it can add
    a date source, never turn a real fragment into a PASS.
    """
    try:
        head = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    m = re.search(r"^published:\s*(\d{4}-\d{2}-\d{2})", head[:1200], re.M)
    if m:
        return m.group(1)
    m = re.search(r"^Published Time:\s*(\d{4}-\d{2}-\d{2})", head[:3000], re.M)
    if m:
        return m.group(1)
    m = re.search(r"^date_published:\s*(\d{4}-\d{2}-\d{2})", head[:1200], re.M)
    return m.group(1) if m else ""


def is_video_post(html: str) -> bool:
    """A post with no text container at all but an embedded player. The absence
    of every article container is the signal; a mere youtube mention in the
    nav/footer is not (those appear on every page of this site)."""
    has_container = any(m in html for m in ("td-post-content", "tdb-single-content", "entry-content", "articleBody"))
    if has_container:
        return False
    low = html.lower()
    return any(m in low for m in ("youtube", "vimeo", "<video", "player"))


SETTLED = ("ok", "exists")


def is_settled(status: str) -> bool:
    # A page that genuinely belongs to another month is a correct answer,
    # not a failed fetch. It must not drag the archive rate down. Neither is a
    # video post: it was archived as completely as it can be.
    return status.startswith(SETTLED) or status.startswith(("skipped-not-", "ok-video"))


def coverage(ym: str, results: list[dict]) -> dict:
    # Any settled record proves the day was reached — a video post is a
    # complete archive of a video post.
    #
    # WHY the month filter (measured 2026-10-20): tdm-202607 graded days=17/31
    # while only TWO July days were present — the other 15 "days" came from
    # wrong-month articles (2024-01, 2026-10 …) that the dead /date/ listing
    # had leaked into the manifest. A day only counts if its date is in the
    # graded month. This can only lower days_present: a strengthening, never a
    # weakening of the gate.
    ok = [r for r in results if is_settled(str(r.get("status", "")))]
    want = f"{ym[:4]}-{ym[4:]}"
    days = set()
    for r in ok:
        d = r.get("date") or ""
        if not d and r.get("file"):
            d = file_published(ARCH / r["file"])
        # A day counts only if it is a REAL calendar day (exact 10-char ISO).
        # "2026-07" (listing truncation) and "2026-07-32" both startswith the
        # month but are not days; counting them inflated days_present. This
        # can only lower the count — a strengthening, never a weakening.
        if d.startswith(want) and len(d) == 10:
            try:
                datetime.strptime(d, "%Y-%m-%d").date()
            except ValueError:
                continue
            days.add(d)
    exp = expected_days(ym)
    return {
        "expected_days": exp,
        "days_present": len(days),
        "days_missing": sorted(
            f"{ym[:4]}-{ym[4:]}-{d:02d}"
            for d in range(1, exp + 1)
            if f"{ym[:4]}-{ym[4:]}-{d:02d}" not in days
        ),
    }


def grade(ym: str, listed: int, results: list[dict]) -> tuple[bool, dict]:
    """A month is complete only if it is finished AND covers the calendar.
    A worker that died mid-month leaves a manifest that passes a count check
    and fails this one."""
    ok = sum(1 for r in results if str(r.get("status", "")).startswith(SETTLED))
    settled = sum(1 for r in results if is_settled(str(r.get("status", ""))))
    cov = coverage(ym, results)
    if not listed:
        return False, cov
    rate = settled / listed
    if ym == datetime.now().strftime("%Y%m"):
        floor_days = max(1, cov["expected_days"] - 2)
    else:
        floor_days = max(1, cov["expected_days"] - 5)
    done = ok >= 200 and rate >= 0.85 and cov["days_present"] >= floor_days
    cov["archive_rate"] = round(rate, 3)
    return done, cov


def write_manifest(ym: str, pages: int, results: list[dict], done: bool,
                   listing: str | None = None) -> Path:
    ARCH.mkdir(parents=True, exist_ok=True)
    ok = sum(1 for r in results if r.get("status") in ("ok", "exists"))
    cov = coverage(ym, results)
    payload = {
        "domain": "taiwandaily.net",
        "month": ym,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "listing": listing or f"https://www.taiwandaily.net/date/{ym[:4]}/{ym[4:]}/",
        "listing_pages": pages,
        "article_count": ok,
        "listed": len(results),
        "complete": done,
        "coverage": cov,
        "results": results,
    }
    dest = ARCH / f"tdm-{ym}.json"
    tmp = dest.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(dest)
    return dest


def verify(ym: str) -> int:
    """Audit an existing manifest against disk. No network, no writes."""
    dest = ARCH / f"tdm-{ym}.json"
    if not dest.exists():
        print(f"VERIFY {ym} NO_MANIFEST -> refetch")
        return 1
    try:
        d = json.loads(dest.read_text())
    except Exception as e:
        print(f"VERIFY {ym} UNPARSEABLE {type(e).__name__} -> refetch")
        return 1
    results = d.get("results") or []
    missing_files = [
        r.get("file") for r in results
        if r.get("file") and not (ARCH / r["file"]).exists()
    ]
    listed = d.get("listed") or len(results)
    # Never trust the flag. A listing bug can produce a "complete" manifest
    # with 8% coverage. The grade is recomputed from disk every time.
    done, cov = grade(ym, listed, results)
    ok_n = sum(1 for r in results if str(r.get("status", "")).startswith(("ok", "exists")))
    print(
        f"VERIFY {ym} complete_flag={d.get('complete')} listed={listed} "
        f"ok={ok_n} "
        f"days={cov['days_present']}/{cov['expected_days']} "
        f"rate={cov.get('archive_rate')} ghost_files={len(missing_files)} "
        f"-> {'PASS' if done else 'REFETCH'}"
    )
    if cov["days_missing"]:
        print(f"  missing days: {', '.join(cov['days_missing'][:31])}")
    if missing_files:
        print(f"  ghost files: {', '.join(m for m in missing_files[:5] if m)}")
    return 0 if done else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("month", help="YYYYMM")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--verify", action="store_true",
                        help="audit an existing manifest, no network, no writes")
    args = parser.parse_args()
    ym = args.month
    month_parts(ym)
    if args.verify:
        return verify(ym)
    articles, pages = list_articles(ym)
    listing = None
    if not articles:
        # The /date/ archive is dead upstream (serves the current page for
        # every month, verified 2026-10-20) — the post-id scan is the
        # enumeration of record. It is slower but cannot lie: every date
        # comes from the article page's own JSON-LD.
        print(f"{ym}: date archive empty, falling back to id-scan", flush=True)
        articles, pages, (lo, hi) = scan_month(ym, workers=args.workers)
        listing = f"https://www.taiwandaily.net/?p={lo}..{hi} (post-id scan)"
        if len(articles) < 20:
            print(f"FAIL {ym} id-scan returned only {len(articles)} articles "
                  f"(network trouble? bounds wrong?) — manifest untouched", flush=True)
            return 1
    if not articles:
        print(f"FAIL {ym} listing returned 0 articles", flush=True)
        return 1
    # A listing that truncates early (rate limit, transient HTTP error) used to
    # overwrite a good manifest with the short one: 202601 went 1483 -> 290
    # listed, days 31/31 -> 7/31, complete True -> False, while the 1,478
    # article files sat untouched on disk. The manifest is the archive's index;
    # never let a partial enumeration replace a fuller one.
    #
    # WHY the modern-schema condition (2026-10-20): the legacy manifests
    # (tdm-202607: 1205 entries, tdm-202610: 780) were built by the dead
    # /date/ listing and are INFLATED with wrong-month content — 202607 held
    # articles published 2024-01-09 and 2026-10-04. Letting a known-broken
    # count veto the id-scan would pin the month at garbage forever. Only a
    # manifest written by this script's own schema (listed+coverage keys)
    # earns the truncation veto.
    prev = ARCH / f"tdm-{ym}.json"
    if prev.exists():
        try:
            old = json.loads(prev.read_text())
            modern = "listed" in old and "coverage" in old
            old_listed = old.get("listed") or len(old.get("results") or [])
            if modern and old_listed >= 50 and len(articles) < 0.6 * old_listed:
                print(
                    f"ABORT {ym} listing truncated: {len(articles)} articles vs "
                    f"{old_listed} in existing manifest ({pages} pages) — keeping "
                    f"the existing manifest, no files written. Re-run later.",
                    flush=True,
                )
                return 1
        except Exception:
            pass
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = [pool.submit(one_article, item, ym) for item in articles]
        for i, fut in enumerate(as_completed(futs), 1):
            results.append(fut.result())
            if i % 100 == 0:
                write_manifest(ym, pages, results, done=False, listing=listing)
                print(f"progress {i}/{len(articles)}", flush=True)
    dest = write_manifest(ym, pages, results, done=False, listing=listing)
    done, cov = grade(ym, len(articles), results)
    dest = write_manifest(ym, pages, results, done=done, listing=listing)
    ok = sum(1 for r in results if str(r.get("status", "")).startswith(("ok", "exists")))
    print(
        f"{'OK' if done else 'PARTIAL'} month={ym} listing_pages={pages} "
        f"listed={len(results)} archived={ok} rate={cov.get('archive_rate')} "
        f"days={cov['days_present']}/{cov['expected_days']} manifest={dest}", flush=True)
    if cov["days_missing"]:
        print(f"missing days: {', '.join(cov['days_missing'][:31])}", flush=True)
    return 0 if done else 1


if __name__ == "__main__":
    sys.exit(main())

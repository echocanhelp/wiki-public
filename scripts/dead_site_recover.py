#!/usr/bin/env python3
"""Dead-site recovery P1-P3 (Wayback-first, multi-source fallback hints).

Usage:
  dead_site_recover.py --id <source_id> --url <seed_url> [--phase cdx|fetch|manifest]

Phases:
  cdx      P1: Wayback CDX discovery -> knowledge/web-archives/<id>/urls.json (retry-tolerant)
  fetch    P2: download raw (id_) captures -> knowledge/web-archives/<id>/pages/ + failures.json
  manifest P3: MANIFEST.json (counts, coverage years, failures, sources tried)

Design rules (skill echopedia-dead-site-recovery):
  - scripts only, no LLM in URL loops
  - CDX throttle: treat -1/ERR as unknown, retry with backoff, per-year collapse
  - Wayback primary; record CommonCrawl/archive.today/NCL as follow_up in manifest
"""
import argparse, json, os, re, sys, time, urllib.request, urllib.parse
from datetime import datetime, timezone

VAULT = os.path.expanduser("~/echo-system")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}

def arch_dir(sid): return os.path.join(VAULT, "knowledge", "web-archives", sid)

def http(url, timeout=45, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")

def cdx_discover(sid, seed, max_urls=20000):
    """Retry-tolerant CDX: try whole-domain; on throttle/empty try per-year windows."""
    out = []
    seen = set()
    host = urllib.parse.urlparse(seed if "://" in seed else "http://" + seed).netloc
    domain = re.sub(r"^www\.", "", host)
    def query(params, tries=3):
        q = "&".join(f"{k}={urllib.parse.quote(str(v), safe=':~*')}" for k, v in params.items())
        u = f"https://web.archive.org/cdx/search/cdx?{q}"
        for i in range(tries):
            try:
                r = http(u, timeout=60)
                d = json.loads(r)
                return d[1:] if d else []
            except Exception as e:
                sys.stderr.write(f"cdx retry {i+1} {e}\n"); time.sleep(8 * (i + 1))
        return None
    # WAF profile (2026-11-21, empirical from pinto): matchType=domain / from/to /
    # collapse=urlkey / fl= / filter= => "Internet Archive: Temporarily Offline" page
    # or degraded []. PASSING shapes: url=<host>&matchType=prefix&limit=N&output=json
    # and since=/until= (not from/to). Dedupe client-side. Sub-coverage: root + www hosts.
    hosts = [domain] + ([] if domain.startswith("www.") else ["www." + domain])
    for host in hosts:
        rows = query({"url": host, "matchType": "prefix", "limit": 6000, "output": "json"}, tries=2)
        if rows:
            for row in rows[1:] if rows and isinstance(rows[0], list) and rows[0] and str(rows[0][0]).lower()=="urlkey" else rows:
                try: orig, ts = row[2], row[1]
                except Exception: continue
                key = (orig.split("#")[0], ts[:8])
                if key in seen: continue
                seen.add(key); out.append({"original": orig, "timestamp": ts, "status": "200"})
    if not out:  # per-year fallback with PASSING spellings only
        for year in range(1997, 2027):
            for host in hosts:
                rows = query({"url": host, "matchType": "prefix", "limit": 3000,
                              "since": f"{year}0101", "until": f"{year}1231", "output": "json"}, tries=2)
                if not rows: continue
                body = rows[1:] if rows and isinstance(rows[0], list) and rows[0] and str(rows[0][0]).lower()=="urlkey" else rows
                for row in body:
                    try: orig, ts = row[2], row[1]
                    except Exception: continue
                    key = (orig.split("#")[0], ts[:8])
                    if key in seen: continue
                    seen.add(key); out.append({"original": orig, "timestamp": ts, "status": "200"})
                time.sleep(2)
    d = arch_dir(sid); os.makedirs(d, exist_ok=True)
    json.dump({"id": sid, "seed": seed, "domain": domain, "discovered_at":
               datetime.now(timezone.utc).isoformat(), "count": len(out), "urls": out},
              open(os.path.join(d, "urls.json"), "w"), ensure_ascii=False, indent=1)
    print(f"P1 {sid}: {len(out)} unique text urls -> urls.json")
    return len(out)

def fetch_pages(sid, concurrency=4, per_host_sleep=1.0):
    d = arch_dir(sid)
    if not os.path.exists(os.path.join(d, "urls.json")):
        print(f"P2 {sid}: SKIP (no urls.json — CDX phase produced nothing)"); return
    os.makedirs(os.path.join(d, "pages"), exist_ok=True)
    data = json.load(open(os.path.join(d, "urls.json")))
    ok, fail = 0, []
    for i, u in enumerate(data["urls"]):
        orig, ts = u["original"], u["timestamp"]
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", urllib.parse.quote(orig, safe=""))[:180]
        dest = os.path.join(d, "pages", f"{ts}_{safe}.html")
        if os.path.exists(dest) and os.path.getsize(dest) > 500: ok += 1; continue
        wb = f"https://web.archive.org/web/{ts}id_/{orig}"
        got = False
        for attempt in range(3):
            try:
                body = http(wb, timeout=60, binary=True)
                if len(body) > 300:
                    open(dest, "wb").write(body); ok += 1; got = True
                break
            except Exception as e:
                time.sleep(5 * (attempt + 1))
        if not got: fail.append({"original": orig, "timestamp": ts, "reason": "fetch_fail"})
        if i % 25 == 0:
            json.dump(fail, open(os.path.join(d, "failures.json"), "w"), indent=1)
            print(f"P2 {sid}: {i+1}/{len(data['urls'])} ok={ok} fail={len(fail)}", flush=True)
        time.sleep(per_host_sleep)
    json.dump(fail, open(os.path.join(d, "failures.json"), "w"), indent=1)
    print(f"P2 {sid}: done ok={ok} fail={len(fail)}")

def manifest(sid):
    d = arch_dir(sid)
    if not os.path.exists(os.path.join(d, "urls.json")):
        print(f"P3 {sid}: SKIP (no urls.json)"); return
    data = json.load(open(os.path.join(d, "urls.json")))
    fail = json.load(open(os.path.join(d, "failures.json"))) if os.path.exists(os.path.join(d, "failures.json")) else []
    years = sorted({u["timestamp"][:4] for u in data["urls"]})
    n_pages = len([f for f in os.listdir(os.path.join(d, "pages")) if f.endswith(".html")]) if os.path.isdir(os.path.join(d, "pages")) else 0
    m = {"id": sid, "seed": data["seed"], "domain": data["domain"],
         "generated_at": datetime.now(timezone.utc).isoformat(),
         "discovered_urls": data["count"], "pages_on_disk": n_pages,
         "failed": len(fail), "coverage_years": years,
         "primary_source": "internet_archive_wayback",
         "follow_up_sources": ["commoncrawl_index(retry)", "archive.today(browser path)",
                                "NCL webarchive.ncl.edu.tw(from browser)", "archive-it university collections"],
         "verification_status": "tier2-archived"}
    json.dump(m, open(os.path.join(d, "MANIFEST.json"), "w"), ensure_ascii=False, indent=1)
    print("P3", sid, json.dumps({k: m[k] for k in ("discovered_urls","pages_on_disk","failed","coverage_years")}))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True); ap.add_argument("--url", default=None)
    ap.add_argument("--phase", default="cdx")
    a = ap.parse_args()
    if a.phase == "cdx":
        if not a.url: sys.exit("need --url")
        cdx_discover(a.id, a.url)
    elif a.phase == "fetch": fetch_pages(a.id)
    elif a.phase == "manifest": manifest(a.id)

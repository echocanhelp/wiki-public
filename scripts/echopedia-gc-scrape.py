#!/usr/bin/env python3
"""Scrape GoatCounter private dashboard (server-rendered widgets) to a JSON cache.

Feeds deepen-x-build.py traffic ranking (and any audit that wants reader signal).
Login = email+password (no CSRF token). Static HTML only — no AJAX detail.

Output schema:
{
 "scraped": "YYYY-MM-DD",
 "window": "7d",
 "total_visits": int | null,          # dashboard total (widget 'total' counter)
 "pages_shown": int | null,          # "out of N visits" denominator when present
 "per_day": {"YYYY-MM-DD": n, ...},  # site-wide daily series if scrapeable
 "counts": {"/wiki-public/path": visits, ...}
}

Env for manual run:
  GC_BASE=https://echocanhelp.goatcounter.com GC_EMAIL=x GC_PASS=y \
    python3 scripts/echopedia-gc-scrape.py --cache knowledge/research/gc-path-counts.json
Env for cron (reuses shared secret file, never printed):
  source ~/echo-system/secrets/goatcounter.env first, or rely on the wrapper.
"""
import argparse, json, os, re, sys, time, datetime, urllib.parse, urllib.request, http.cookiejar

def login_and_fetch(base, email, pw):
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    data = urllib.parse.urlencode({"email": email, "password": pw}).encode()
    op.open(urllib.request.Request(base + "/user/requestlogin", data=data), timeout=30)
    return op  # session kept; fetch pages via op.open()

def fetch_page(op, path):
    return op.open(path, timeout=30).read().decode("utf-8", errors="replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="knowledge/research/gc-path-counts.json")
    ap.add_argument("--base", default=os.environ.get("GC_BASE", "https://echocanhelp.goatcounter.com"))
    args = ap.parse_args()
    email = os.environ.get("GC_EMAIL") or os.environ.get("GOATCOUNTER_EMAIL")
    pw = os.environ.get("GC_PASS") or os.environ.get("GOATCOUNTER_PASSWORD")
    if not (email and pw):
        print("GC_SCRAPE: NO_CREDS")
        sys.exit(2)

    import html as h
    op = login_and_fetch(args.base, email, pw)
    # ?period=7d renders the true 7-day window (verified live 2026-09-27);
    # root without param = default 30d view. Scrape the tightest honest window.
    try:
        page = fetch_page(op, args.base + "/?period=7d")
    except Exception:
        page = fetch_page(op, args.base + "/")

    tot = re.search(r'class="total">\(?(\d+)\)?<', page)
    shown = re.search(r'class="total-display">\(?(\d+)\)?<', page)
    counts = {p: int(c) for p, c in re.findall(r'<tr id="(/wiki-public[^"]*?)"[^>]*data-count="(\d+)"', page)}

    # per-row 7-day daily series: rows carry <tr id="/wiki-public/path" ... data-count="N">
    # then a data-stats="[{"day":..,"hourly":[24],"daily":n,...}]" (keys: day/hourly/daily;
    # HTML-escaped JSON). Per-page series only — GoatCounter renders no site-wide daily map.
    per_day = {}
    for m in re.finditer(r'<tr id="(/wiki-public[^"]*?)"[^>]*data-count="\d+"(.*?)</tr>', page, re.S):
        sm = re.search(r'data-stats="(.*?)"', m.group(2), re.S)
        if not sm:
            continue
        try:
            series = json.loads(h.unescape(sm.group(1)))
        except Exception:
            continue
        for item in series:
            day = item.get("day")
            val = item.get("daily")
            if day and val:
                per_day[day] = per_day.get(day, 0) + int(val)

    out = {
        "scraped": time.strftime("%Y-%m-%d"),
        "window": "7d",
        "total_visits": int(tot.group(1)) if tot else None,
        "pages_shown": int(shown.group(1)) if shown else None,
        "per_day": per_day,
        "counts": counts,
    }
    path = os.path.abspath(args.cache)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    old = None
    if os.path.exists(path):
        try:
            old = json.load(open(path)).get("counts")
        except Exception:
            pass
    json.dump(out, open(path, "w"), ensure_ascii=False)
    if old == counts and old is not None:
        print("GC_SCRAPE: NOCHANGE paths=%d total=%s" % (len(counts), out["total_visits"]))
    else:
        print("GC_SCRAPE: UPDATED paths=%d total=%s" % (len(counts), out["total_visits"]))

if __name__ == "__main__":
    main()

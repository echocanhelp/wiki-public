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
    html_txt = op.open(base + "/", timeout=30).read().decode("utf-8", errors="replace")
    return html_txt

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
    page = login_and_fetch(args.base, email, pw)

    tot = re.search(r'class="total">\((\d+)\)<', page)
    shown = re.search(r'class="total-display">\((\d+)\)<', page)
    counts = {p: int(c) for p, c in re.findall(r'<tr id="(/wiki-public[^"]*?)"[^>]*data-count="(\d+)"', page)}

    # site-wide daily series: chart widgets named e.g. 'totalpages'/'pages' with data-stats
    per_day = {}
    wm = re.search(r'data-widget="total"[^>]*data-stats="(.*?)"', page)
    if not wm:
        wm = re.search(r'data-stats="(\[\{&quot;d&quot;[^\"]*?)&quot;"', page)
    if wm:
        try:
            series = json.loads(h.unescape(wm.group(1)))
            for item in series:
                day = item.get("d") or item.get("label")
                val = item.get("v") if "v" in item else item.get("value")
                if day and val:
                    per_day[day] = per_day.get(day, 0) + int(val)
        except Exception:
            pass

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

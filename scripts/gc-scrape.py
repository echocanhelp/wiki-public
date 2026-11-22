#!/usr/bin/env python3
"""GoatCounter path-count scraper -> knowledge/research/gc-path-counts.json.

Deterministic (no_agent-safe): login via cookie jar, scrape the period-limited
dashboard page-rows, write the same JSON shape deepen-x-build.py consumes.
Parse recipes verified in skills/echopedia/echopedia-analytics/references/
goatcounter-widget-parse.md. Credentials: secrets/goatcounter.env, never printed.

Freshness contract: run at least weekly (cron); the builder ignores the file
when mtime > 7d, so a dead scraper silently degrades ranking to count-only —
by design, never trusts stale traffic.
"""
import html
import json
import os
import re
import sys
import urllib.request
import urllib.parse
import http.cookiejar
from datetime import date, timedelta
from pathlib import Path

REPO = Path(os.environ.get("ECHO_REPO", Path.home() / "echo-system")).resolve()
OUT = REPO / "knowledge" / "research" / "gc-path-counts.json"
ENV = REPO / "secrets" / "goatcounter.env"
BASE = "https://echocanhelp.goatcounter.com"
DAYS = 30


def load_creds():
    creds = {}
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip().strip('"').strip("'")
    return creds["GOATCOUNTER_EMAIL"], creds["GOATCOUNTER_PASSWORD"]


def main():
    email, password = load_creds()
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

    def get(url, data=None):
        req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode() if data else None,
                                     headers={"User-Agent": "echopedia-gc-scrape/1.0"})
        with opener.open(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")

    get(BASE + "/user/new")
    get(BASE + "/user/requestlogin", {"email": email, "password": password})

    end = date.today()
    start = end - timedelta(days=DAYS)
    dash = get(f"{BASE}/?period-start={start}&period-end={end}&hl-period=day")
    # page rows: <tr id="<path>" ... data-count="N" ...>
    rows = re.findall(r'<tr id="([^"]+)"[^>]*data-count="(\d+)"', dash)
    counts = {}
    for path, n in rows:
        path = html.unescape(path)
        if path.startswith("/"):
            counts[path] = counts.get(path, 0) + int(n)

    per_day = {}
    for d, n in re.findall(r'<tr id="(\d{4}-\d{2}-\d{2})"[^>]*data-count="(\d+)"', dash):
        per_day[d] = per_day.get(d, 0) + int(n)

    # Widen path set: the dashboard table lists only its first ~10 rows.
    # Widget 0 takes max/total (skill: without them it can 400). Merge by MAX
    # per path so dashboard+widget overlap does not double-count.
    total = sum(per_day.values()) or sum(counts.values())
    try:
        wdoc = json.loads(get(f"{BASE}/load-widget?widget=0&group=hour"
                              f"&period-start={start}&period-end={end}"
                              f"&max=200&total={total}"))
        wrows = (re.findall(r'data-key="([^"]+)"[^>]*data-count="(\d+)"', wdoc.get("html", ""))
                 + re.findall(r'<tr id="([^"]+)"[^>]*data-count="(\d+)"', wdoc.get("html", "")))
        for path, n in wrows:
            path = html.unescape(path)
            if path.startswith("/"):
                counts[path] = max(counts.get(path, 0), int(n))
    except Exception as e:  # widening is best-effort; dashboard rows remain valid
        print(f"gc-scrape: widget-0 widen skipped ({e})", file=sys.stderr)

    doc = {
        "scraped": date.today().isoformat(),
        "window": f"{DAYS}d",
        "total_visits": sum(counts.values()),
        "pages_shown": len(counts),
        "per_day": per_day,
        "counts": dict(sorted(counts.items(), key=lambda kv: -kv[1])),
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1))
    print(f"gc-scrape: {len(counts)} paths, {doc['total_visits']} visits -> {OUT.name}")


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""echopedia-quality-census.py — weekly quality trend line (2026-10-15).

Answers "is Echopedia better than last month?" with a number, not a story.
Deterministic, stdlib-only, runs inside echopedia-weekly-improvement.sh.

Metrics (person + organization pages, body >= 300 chars):
  story_pct  % pages with ## Story            (voice layer)
  quotes_pct % pages with ## Quotes           (voice layer)
  labeled_pct % pages whose record facts carry >=1 label marker
  dated_pct  % pages with >=6 year refs anywhere (density floor)
  zh_pct     % pages carrying a Chinese name
Each run appends one row to knowledge/research/quality-census.json (history)
and prints a CENSUS line for the digest. First run = baseline; deltas come
from row 2 onward.
"""
import glob
import json
import re
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "knowledge" / "research" / "quality-census.json"

DATE_RE = re.compile(r"\b(19[4-9]\d|20[0-2]\d)\b")
LABEL_RE = re.compile(r"sourced|inferred|alleged|unknown", re.I)


def measure() -> dict:
    rows = {"n": 0, "story": 0, "quotes": 0, "rec": 0, "labeled": 0,
            "dated": 0, "zh": 0}
    for pat in ("content/people/*.md", "content/organizations/*.md"):
        for f in glob.glob(str(REPO / pat)):
            t = Path(f).read_text(errors="ignore")
            if len(t) < 300:
                continue
            rows["n"] += 1
            if re.search(r"^## Story\s*$", t, re.M):
                rows["story"] += 1
            if re.search(r"^## Quotes", t, re.M):
                rows["quotes"] += 1
            rec = re.search(r"^## From the record\s*$(.*?)(?=^## |\Z)", t, re.M | re.S)
            if rec:
                facts = [l for l in rec.group(1).splitlines()
                         if re.match(r"\s*(\||- \*\*|\*\*)", l)
                         and re.search(r"\d{4}|n\.d\.", l)]
                if facts:
                    rows["rec"] += 1
                    if any(LABEL_RE.search(l) for l in facts):
                        rows["labeled"] += 1
            if len(DATE_RE.findall(t)) >= 6:
                rows["dated"] += 1
            if re.search(r"name_zh|## 中文名|\*\*中文", t):
                rows["zh"] += 1
    n = max(rows["n"], 1)
    return {
        "date": date.today().isoformat(),
        "pages": rows["n"],
        "story_pct": round(rows["story"] * 100 / n, 1),
        "quotes_pct": round(rows["quotes"] * 100 / n, 1),
        "labeled_pct": round(rows["labeled"] * 100 / max(rows["rec"], 1), 1),
        "dated_pct": round(rows["dated"] * 100 / n, 1),
        "zh_pct": round(rows["zh"] * 100 / n, 1),
    }


def main():
    cur = measure()
    hist = []
    if OUT.exists():
        try:
            hist = json.loads(OUT.read_text()).get("history", [])
        except (json.JSONDecodeError, OSError):
            hist = []
    hist.append(cur)
    OUT.write_text(json.dumps({"history": hist}, indent=1, ensure_ascii=False))
    prev = hist[-2] if len(hist) > 1 else None
    d = (f"CENSUS: pages={cur['pages']} story={cur['story_pct']}% "
         f"quotes={cur['quotes_pct']}% labeled={cur['labeled_pct']}% "
         f"dated={cur['dated_pct']}% zh={cur['zh_pct']}%")
    if prev:
        d += ("  delta: " + " ".join(
            f"{k}{'+' if cur[k] >= prev[k] else ''}{round(cur[k] - prev[k], 1)}"
            for k in ("story_pct", "quotes_pct", "labeled_pct", "dated_pct", "zh_pct")))
    else:
        d += "  (baseline — deltas start next week)"
    print(d)


if __name__ == "__main__":
    main()

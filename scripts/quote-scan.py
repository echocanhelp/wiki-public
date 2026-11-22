#!/usr/bin/env python3
"""quote-scan.py — corpus-wide attributed-speech extractor (2026-10-15).

The old quote extractor covered 75 hardcoded slugs and its "quotes" were
±context around a name, not speech. This is the real lane: ONE pass over all
articles, extract quoted-speech spans (CJK 「」 / English "...") that sit next
to an attribution verb AND a known person's name, write candidates with
confidence. It does NOT write to pages — misattributed quotes are worse than
no quotes. Candidates feed deepen cards (which already paste quotes) and the
review lane.

Output: knowledge/research/quote-candidates.jsonl (one JSON per candidate)
Usage: python3 scripts/quote-scan.py [--limit N] [--full]
Default: articles changed since last run (state file), or first 500 on --full
first run without state.
"""
import argparse
import glob
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ARTICLES = REPO / "content" / "articles"
OUT = REPO / "knowledge" / "research" / "quote-candidates.jsonl"
STATE = REPO / "knowledge" / "research" / "quote-scan-state.json"

CJK_VERBS = r"說|表示|指出|回憶|回憶說|強調|認為|談|批評|呼籲|補充|說明|回應|感謝|期待|期許|指出"
EN_VERBS = r"said|says|stated|noted|recalls|emphasized|argued|wrote|remarks?"

NAME_SPAN = 150  # chars around the quote to look for a name


def load_names():
    names = {}  # exact string -> slug
    for f in glob.glob(str(REPO / "content" / "people" / "*.md")):
        t = Path(f).read_text(errors="ignore")
        m = re.search(r"^name_zh:\s*[\"']?(.+?)[\"']?\s*$", t, re.M)
        if m:
            v = m.group(1).strip()
            if len(v) >= 2:
                names[v] = Path(f).stem
            # parenthetical variants: 黃慶三(農工)
            for part in re.findall(r"[（(](.+?)[)）]", v):
                if len(part) >= 2:
                    names[part] = Path(f).stem
        m = re.search(r"^name_en:\s*[\"']?(.+?)[\"']?\s*$", t, re.M)
        if m:
            v = m.group(1).strip()
            if len(v) >= 6:
                names[v] = Path(f).stem
    return names


def spans(body):
    """Yield (start, end, text) for quoted-speech candidates."""
    for pat in (r"「([^」\n]{10,300})」", r'"([^"\n]{20,300})"'):
        for m in re.finditer(pat, body):
            yield m.start(), m.end(), m.group(1)


def attribute(body, qstart, qend, names):
    """Return (slug, confidence) for the quote span, or None."""
    lo, hi = max(0, qstart - NAME_SPAN), min(len(body), qend + NAME_SPAN)
    zone = body[lo:hi]
    if not re.search(CJK_VERBS, zone) and not re.search(EN_VERBS, zone, re.I):
        return None
    best = None
    for name, slug in names.items():
        pos = zone.find(name)
        if pos < 0:
            continue
        # high confidence: name + verb adjacent to the quote (within 60 chars of span edge)
        edge = min(abs(pos - (qstart - lo)), abs(pos - (qend - lo)))
        conf = "high" if edge <= 60 else "medium"
        if best is None or conf == "high":
            best = (slug, conf)
            if conf == "high":
                break
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--full", action="store_true", help="scan ALL articles")
    args = ap.parse_args()

    names = load_names()
    print(f"names loaded: {len(names)}")

    state = {}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text()).get("scanned", {})
        except (json.JSONDecodeError, OSError):
            state = {}

    files = sorted(glob.glob(str(ARTICLES / "**" / "*.md"), recursive=True))
    todo = [f for f in files if args.full or f not in state]
    if args.limit:
        todo = todo[: args.limit]
    print(f"articles: {len(files)} total, {len(todo)} to scan")

    made = 0
    with OUT.open("a", encoding="utf-8") as out:
        for f in todo:
            try:
                content = Path(f).read_text(errors="ignore")
            except OSError:
                continue
            b0 = content.find("---", content.find("---") + 3)
            body = content[b0 + 3:] if b0 > 0 else content
            hits = {}
            for qs, qe, qtext in spans(body):
                att = attribute(body, qs, qe, names)
                if not att:
                    continue
                slug, conf = att
                key = slug + qtext[:60]
                if key in hits:
                    continue
                hits[key] = True
                out.write(json.dumps({
                    "slug": slug, "quote": qtext.strip(), "conf": conf,
                    "source": Path(f).stem, "path": str(Path(f).relative_to(REPO)),
                    "date": (re.search(r"/(\d{4})/", f) or re.search(r"date:\s*\"?(\d{4})", content) or [None, "unknown"])[1],
                }, ensure_ascii=False) + "\n")
                made += 1
            state[f] = 1
    if STATE.exists() or True:
        STATE.write_text(json.dumps({"scanned": state, "last_run": str(__import__("datetime").date.today())}))
    print(f"quote-scan: {made} new candidates -> {OUT.name}")


if __name__ == "__main__":
    main()

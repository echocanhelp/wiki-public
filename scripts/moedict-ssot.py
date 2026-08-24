#!/usr/bin/env python3
"""Taigi spelling SSOT: live 萌典 /t/ = Tâi-lô.

POJ is never invented here. Church/historical POJ stays on the named source.
Person names are HOLD unless --hold is omitted *and* the operator passed a
dictionary headword that is not a personal name.

Usage:
  python3 moedict-ssot.py lookup --words '家庭,手,陳善哲' --hold '陳善哲'
  python3 moedict-ssot.py trs --q tshiú
  python3 moedict-ssot.py audit-lyrics --file ~/media-outputs/jobs/<slug>-lyrics.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Echopedia-moedict-ssot/1.0 (TAHS; +https://echocanhelp.github.io/wiki-public/)"
API_T = "https://www.moedict.tw/t/{word}.json"
API_TRS = "https://www.moedict.tw/lookup/trs/{q}"

# Church-POJ letter shapes that are *not* Tâi-lô (萌典 /lookup/trs misses these).
POJ_MARKERS = re.compile(
    r"(chh|ch[aeiou]|o͘|o·|[aeiou]ⁿ|oa[ein]|oe[nh]?|eng\b)",
    re.IGNORECASE,
)


def fetch(url: str, timeout: int = 20) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def fetch_json(url: str) -> dict | None:
    try:
        _, raw = fetch(url)
        return json.loads(raw.decode("utf-8"))
    except Exception as e:
        print(f"JSON_FAIL {url} {type(e).__name__}: {e}", file=sys.stderr)
        return None


def lookup_word(word: str) -> dict:
    rec = {
        "word": word,
        "scheme": "tailo",
        "ok": False,
        "tailo": None,
        "tailo_all": [],
        "audio_id": None,
        "url": API_T.format(word=urllib.parse.quote(word)),
        "note": None,
    }
    d = fetch_json(rec["url"])
    if not d:
        rec["note"] = "no moedict /t/ entry"
        return rec
    seen: list[str] = []
    for h in d.get("h") or []:
        if not isinstance(h, dict):
            continue
        t = h.get("T")
        if t and t not in seen:
            seen.append(t)
        aid = h.get("_") or h.get("=")
        if rec["audio_id"] is None and aid is not None:
            rec["audio_id"] = str(aid)
    if not seen:
        rec["note"] = "entry but no h[].T"
        return rec
    rec.update(ok=True, tailo=seen[0], tailo_all=seen)
    return rec


def trs(q: str) -> dict:
    url = API_TRS.format(q=urllib.parse.quote(q))
    rec = {
        "q": q,
        "url": url,
        "ok": False,
        "hanzi": [],
        "looks_poj": bool(POJ_MARKERS.search(q)),
        "note": None,
    }
    try:
        _, raw = fetch(url)
        text = raw.decode("utf-8").strip()
    except Exception as e:
        rec["note"] = f"trs fail {type(e).__name__}"
        return rec
    if not text:
        rec["note"] = "empty — not Tâi-lô (church POJ often misses)"
        return rec
    rec["hanzi"] = [p for p in text.split("|") if p]
    rec["ok"] = bool(rec["hanzi"])
    return rec


def tokenize_lyrics(text: str) -> list[str]:
    toks: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s or (s.startswith("[") and s.endswith("]")):
            continue
        for t in re.split(r"[\s,.;:!?/]+", s):
            t = t.strip("\"'()（）")
            if t:
                toks.append(t)
    return toks


def cmd_lookup(args: argparse.Namespace) -> int:
    holds = {w.strip() for w in (args.hold or "").split(",") if w.strip()}
    words = [w.strip() for w in args.words.split(",") if w.strip()]
    rows = []
    for w in words:
        if w in holds:
            rows.append(
                {
                    "word": w,
                    "ok": False,
                    "hold": True,
                    "scheme": None,
                    "tailo": None,
                    "note": "HOLD — person/TAH/family is authority, not 萌典",
                }
            )
            continue
        rec = lookup_word(w)
        rec["hold"] = False
        rows.append(rec)
    out = {
        "authority": "https://www.moedict.tw/t/<詞>.json",
        "scheme": "tailo",
        "poj_scope": "church/historical-religious named source only",
        "n": len(rows),
        "n_ok": sum(1 for r in rows if r.get("ok")),
        "n_hold": sum(1 for r in rows if r.get("hold")),
        "rows": rows,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_trs(args: argparse.Namespace) -> int:
    print(json.dumps(trs(args.q), ensure_ascii=False, indent=2))
    return 0


def cmd_audit_lyrics(args: argparse.Namespace) -> int:
    text = Path(args.file).read_text(encoding="utf-8")
    toks = tokenize_lyrics(text)
    rows = []
    for t in toks:
        rec = trs(t)
        rec["token"] = t
        if rec.get("looks_poj") and not rec.get("ok"):
            rec["verdict"] = "POJ_OR_UNKNOWN"
        elif rec.get("ok"):
            rec["verdict"] = "TAILO_HIT"
        else:
            rec["verdict"] = "MISS"
        hz = rec.get("hanzi") or []
        if len(hz) > 8:
            rec["hanzi_n"] = len(hz)
            rec["hanzi"] = hz[:8]
        rows.append(rec)
    n = len(rows)
    hits = sum(1 for r in rows if r["verdict"] == "TAILO_HIT")
    poj = sum(1 for r in rows if r["verdict"] == "POJ_OR_UNKNOWN")
    out = {
        "file": str(args.file),
        "authority": "https://www.moedict.tw/lookup/trs/<tailo>",
        "default_scheme": "tailo",
        "n_tokens": n,
        "n_tailo_hit": hits,
        "n_poj_or_unknown": poj,
        "n_miss": n - hits - poj,
        "ship_as_taigi": hits >= max(1, int(0.5 * n)) and poj == 0,
        "rows": rows,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["ship_as_taigi"] else 2


def main() -> int:
    ap = argparse.ArgumentParser(description="萌典 Tâi-lô SSOT for Taigi spelling")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lookup", help="漢字 → Tâi-lô via /t/")
    p.add_argument("--words", required=True)
    p.add_argument("--hold", default="")
    p.set_defaults(fn=cmd_lookup)

    p = sub.add_parser("trs", help="Tâi-lô → 漢字 via /lookup/trs/")
    p.add_argument("--q", required=True)
    p.set_defaults(fn=cmd_trs)

    p = sub.add_parser("audit-lyrics", help="score a lyrics sidecar against /lookup/trs/")
    p.add_argument("--file", required=True)
    p.set_defaults(fn=cmd_audit_lyrics)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())

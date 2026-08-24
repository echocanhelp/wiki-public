#!/usr/bin/env python3
"""Gold 朗讀 from 萌典 official clips + coverage report.

Teacher = moedict.tw (教育部 via g0v), never HeartMuLa / Whisper / TTS.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Echopedia-listen/1.0 (TAHS; +https://echocanhelp.github.io/wiki-public/)"
ASSET = "https://r2-assets.moedict.tw/audio/{lang}/{aid}.mp3"
API = "https://www.moedict.tw/{lang}/{word}.json"


def fetch_json(url: str) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read()
        return json.loads(raw.decode("utf-8"))
    except Exception as e:
        print(f"JSON_FAIL {url} {e}", file=sys.stderr)
        return None


def fetch_mp3(url: str, dest: Path) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 500 or data[:4] == b"<htm" or data[:1] == b"<":
            return False
        dest.write_bytes(data)
        return True
    except Exception:
        return False


def audio_ids(entry: dict) -> list[str]:
    ids: list[str] = []
    for h in entry.get("h") or []:
        if not isinstance(h, dict):
            continue
        for key in ("=", "_"):
            v = h.get(key)
            if v is None:
                continue
            s = str(v).strip()
            if s.isdigit():
                ids.append(s)
                if len(s) < 5:
                    ids.append(s.zfill(5))
    # unique preserve order
    out, seen = [], set()
    for i in ids:
        if i not in seen:
            seen.add(i)
            out.append(i)
    return out


def lookup(word: str, lang: str) -> dict:
    q = urllib.parse.quote(word)
    url = API.format(lang=lang, word=q)
    d = fetch_json(url)
    rec = {
        "word": word,
        "lang": lang,
        "ok": False,
        "reading": None,
        "audio_id": None,
        "audio_path": None,
        "hold": False,
    }
    if not d:
        return rec
    hs = d.get("h") or []
    if hs and isinstance(hs[0], dict):
        rec["reading"] = hs[0].get("T") or hs[0].get("p")
    return rec | {"_entry": d}


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--lang", choices=["t", "a"], default="t", help="t=台語 a=國語")
    ap.add_argument("--words", required=True, help="comma-separated 漢字")
    ap.add_argument("--hold", default="", help="comma-separated names not in dict")
    ap.add_argument("--jobs", default=str(Path.home() / "media-outputs/jobs"))
    args = ap.parse_args()

    jobs = Path(args.jobs)
    work = jobs / f"{args.slug}-listen-clips"
    work.mkdir(parents=True, exist_ok=True)
    words = [w.strip() for w in args.words.split(",") if w.strip()]
    holds = {w.strip() for w in args.hold.split(",") if w.strip()}

    rows = []
    clips = []
    for w in words:
        rec = {"word": w, "lang": args.lang, "ok": False, "reading": None, "audio_id": None, "hold": w in holds}
        if w in holds:
            rec["note"] = "name/HOLD — person or TAH is authority, not 萌典"
            rows.append(rec)
            continue
        got = lookup(w, args.lang)
        rec["reading"] = got.get("reading")
        entry = got.get("_entry")
        if not entry:
            rec["note"] = "no moedict entry"
            rows.append(rec)
            continue
        ok = False
        for aid in audio_ids(entry):
            dest = work / f"{args.lang}-{aid}-{re.sub(r'[^0-9A-Za-z一-龥]+', '', w) or 'x'}.mp3"
            url = ASSET.format(lang=args.lang, aid=aid)
            if fetch_mp3(url, dest):
                rec.update(ok=True, audio_id=aid, audio_path=str(dest))
                clips.append(dest)
                ok = True
                break
        if not ok:
            rec["note"] = "entry but no playable official mp3"
        rows.append(rec)

    content = [r for r in rows if not r.get("hold")]
    n_ok = sum(1 for r in content if r.get("ok"))
    coverage = (100.0 * n_ok / len(content)) if content else 0.0

    gold = jobs / f"{args.slug}-gold-langdu.wav"
    gold_ok = False
    if clips:
        lst = work / "concat.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in clips), encoding="utf-8")
        r = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(gold)],
            capture_output=True,
            text=True,
        )
        gold_ok = r.returncode == 0 and gold.exists()
        if not gold_ok:
            print(r.stderr[-400:], file=sys.stderr)

    report = {
        "slug": args.slug,
        "authority": "moedict.tw (教育部 via g0v 萌典 official clips)",
        "lang": "taigi" if args.lang == "t" else "zh-TW",
        "coverage_pct": round(coverage, 1),
        "n_words": len(words),
        "n_content": len(content),
        "n_gold_clips": n_ok,
        "n_hold": len(holds),
        "gold_langdu": str(gold) if gold_ok else None,
        "tone_claim": coverage >= 40.0 and gold_ok,
        "junk": None,
        "rows": [{k: v for k, v in r.items() if k != "_entry"} for r in rows],
    }
    out = jobs / f"{args.slug}-listen.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in report if k != "rows"}, ensure_ascii=False, indent=2))
    print(f"LISTEN_JSON {out}")
    return 0 if gold_ok or coverage >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

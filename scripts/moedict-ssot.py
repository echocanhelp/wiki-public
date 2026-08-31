#!/usr/bin/env python3
"""Taigi spelling SSOT: live 萌典 /t/ = Tâi-lô.

Accuracy layers (2026-08-25):
  1. Spelling — word-level longest-match on /t/index.json + spoken 文白 picker
  2. Listen   — same picker’s audio_id (白/替, not 文)
  3. Sung     — NOT solved here. HeartMuLa has no Taigi G2P.

POJ is never invented here. Church/historical POJ stays on the named source.
Person names are HOLD.

Echo Resonance Taigi pack (locked 2026-08-25):
  <slug>-lyrics-hanzi.txt  → HeartMuLa (漢字 only — do not sing Tâi-lô)
  <slug>-lyrics-tailo.txt  → audit-lyrics (space-separated Tâi-lô)
  <slug>-lyrics.txt        → wiki interlinear (漢字 + Tâi-lô)
Never translate an English lyric line-by-line. Design a native 台語歌.

Usage:
  python3 moedict-ssot.py lookup --words '人,手,陳善哲' --hold '陳善哲'
  python3 moedict-ssot.py segment --hanzi ~/media-outputs/jobs/<slug>-lyrics-hanzi.txt --hold '陳善哲'
  python3 moedict-ssot.py trs --q tshiú
  python3 moedict-ssot.py audit-lyrics --file ~/media-outputs/jobs/<slug>-lyrics-tailo.txt
  python3 moedict-ssot.py audit-pack --hanzi …-hanzi.txt --tailo …-tailo.txt --wiki …-lyrics.txt --hold '陳善哲'
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Echopedia-moedict-ssot/1.1 (TAHS; +https://echocanhelp.github.io/wiki-public/)"
API_T = "https://www.moedict.tw/t/{word}.json"
API_TRS = "https://www.moedict.tw/lookup/trs/{q}"
API_INDEX = "https://www.moedict.tw/t/index.json"
INDEX_CACHE = Path.home() / ".cache/echopedia/moedict-t-index.json"
INDEX_TTL_S = 7 * 24 * 3600
OVERRIDE_PATH = Path(__file__).resolve().parents[1] / "echopedia" / "taigi-sense-overrides.json"
# Fallback if the JSON is missing. Values are NFC-normalized at load.
_OVERRIDE_FALLBACK = {"長": "tn̂g", "到": "kàu"}

# Church-POJ letter shapes that are *not* Tâi-lô (萌典 /lookup/trs misses these).
POJ_MARKERS = re.compile(
    r"(chh|ch[aeiou]|o͘|o·|[aeiou]ⁿ|oa[ein]|oe[nh]?|eng\b)",
    re.IGNORECASE,
)
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
SECTION_LABELS = {
    "Intro",
    "Verse",
    "Chorus",
    "Bridge",
    "Outro",
    "Pre-Chorus",
    "Hook",
    "Lyrics",
    "Taigi",
}
EN_PROPER = re.compile(r"\b[A-Z][A-Za-z]{2,}\b")
CJK = CJK_RE

def load_sense_overrides() -> dict[str, str]:
    """漢字 → forced Tâi-lô (NFC). Missing/bad JSON falls back to the two seeds."""
    out: dict[str, str] = {}
    raw = None
    if OVERRIDE_PATH.is_file():
        try:
            raw = json.loads(OVERRIDE_PATH.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"OVERRIDE_JSON_FAIL {OVERRIDE_PATH} {e}", file=sys.stderr)
    words = (raw or {}).get("words") if isinstance(raw, dict) else None
    src = words if isinstance(words, dict) else _OVERRIDE_FALLBACK
    for k, v in src.items():
        tailo = v.get("tailo") if isinstance(v, dict) else v
        if k and tailo:
            out[nfc(str(k))] = nfc(str(tailo))
    return out


def _same_tailo(a: str, b: str) -> bool:
    """萌典 /t/ stores NFD; files often NFC. Compare both + NFD."""
    if not a or not b:
        return False
    aa, bb = nfc(a), nfc(b)
    if aa == bb:
        return True
    return unicodedata.normalize("NFD", aa) == unicodedata.normalize("NFD", bb)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


def strip_marks(s: str | None) -> str:
    return re.sub(r"[`~]", "", s or "").strip()


def fetch(url: str, timeout: int = 20) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def fetch_json(url: str):
    try:
        _, raw = fetch(url)
        return json.loads(raw.decode("utf-8"))
    except Exception as e:
        print(f"JSON_FAIL {url} {type(e).__name__}: {e}", file=sys.stderr)
        return None


def load_index(force: bool = False) -> set[str]:
    INDEX_CACHE.parent.mkdir(parents=True, exist_ok=True)
    if (
        not force
        and INDEX_CACHE.is_file()
        and (time.time() - INDEX_CACHE.stat().st_mtime) < INDEX_TTL_S
    ):
        try:
            data = json.loads(INDEX_CACHE.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                return {str(x) for x in data}
        except Exception:
            pass
    data = fetch_json(API_INDEX)
    if not isinstance(data, list) or not data:
        if INDEX_CACHE.is_file():
            try:
                stale = json.loads(INDEX_CACHE.read_text(encoding="utf-8"))
                if isinstance(stale, list) and stale:
                    print("INDEX_STALE using cache", file=sys.stderr)
                    return {str(x) for x in stale}
            except Exception:
                pass
        return set()
    INDEX_CACHE.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
    return {str(x) for x in data}


def reading_rank(label: str | None, has_audio: bool) -> tuple[int, int]:
    """Lower is better for sung / spoken Taigi.

    白 (colloquial) > 替 (訓讀/口語) > unlabeled-with-audio > unlabeled > 文.
    """
    s = strip_marks(label)
    if "白" in s:
        tier = 0
    elif "替" in s:
        tier = 1
    elif "文" in s:
        tier = 5
    elif has_audio:
        tier = 3
    else:
        tier = 4
    return (tier, 0 if has_audio else 1)


def pick_spoken(heteronyms: list) -> dict | None:
    cands = []
    for h in heteronyms:
        if not isinstance(h, dict):
            continue
        t = h.get("T")
        if not t:
            continue
        aid = h.get("_") or h.get("=")
        cands.append((reading_rank(h.get("reading"), aid is not None), h))
    if not cands:
        return None
    cands.sort(key=lambda x: x[0])
    return cands[0][1]


def split_tailo(raw: str) -> list[str]:
    parts = []
    for p in re.split(r"[/／]", raw or ""):
        p = nfc(p.strip())
        if p and p not in parts:
            parts.append(p)
    return parts


def lookup_word(word: str) -> dict:
    rec = {
        "word": word,
        "scheme": "tailo",
        "ok": False,
        "tailo": None,
        "tailo_all": [],
        "reading": None,
        "spoken": True,
        "audio_id": None,
        "url": API_T.format(word=urllib.parse.quote(word)),
        "note": None,
        "sense_override": False,
        "picker_would": None,
    }
    d = fetch_json(rec["url"])
    if not d:
        rec["note"] = "no moedict /t/ entry"
        return rec
    hs = [h for h in (d.get("h") or []) if isinstance(h, dict) and h.get("T")]
    if not hs:
        rec["note"] = "entry but no h[].T"
        return rec
    picked = pick_spoken(hs)
    assert picked is not None
    all_t: list[str] = []
    for h in hs:
        for p in split_tailo(str(h.get("T"))):
            if p not in all_t:
                all_t.append(p)
    picker_primary = split_tailo(str(picked.get("T")))
    primary = list(picker_primary)
    aid = picked.get("_") or picked.get("=")
    label = strip_marks(picked.get("reading")) or None
    override_note = None
    forced = None

    override = load_sense_overrides().get(nfc(word))
    if override and any(_same_tailo(p, override) for p in all_t):
        for h in hs:
            parts = split_tailo(str(h.get("T")))
            if any(_same_tailo(p, override) for p in parts):
                picked = h
                forced = next(p for p in parts if _same_tailo(p, override))
                primary = [forced] + [p for p in parts if not _same_tailo(p, override)]
                aid = picked.get("_") or picked.get("=")
                label = strip_marks(picked.get("reading")) or None
                would = picker_primary[0] if picker_primary else "?"
                override_note = f"sense override {word}->{forced} (picker would give {would})"
                break

    rec.update(
        ok=True,
        tailo=forced or (primary[0] if primary else nfc(str(picked.get("T")))),
        tailo_all=all_t,
        reading=label,
        spoken="文" not in (label or ""),
        audio_id=str(aid) if aid is not None else None,
        sense_override=bool(forced),
        picker_would=(picker_primary[0] if picker_primary else None),
    )
    if label == "文" and len(hs) > 1 and not forced:
        rec["note"] = "only 文 reading available"
    if override_note:
        rec["note"] = override_note
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
    if not text or text.lstrip().startswith("<!"):
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


def hanzi_lines(text: str) -> list[str]:
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or (s.startswith("[") and s.endswith("]")):
            continue
        out.append(s)
    return out


def segment_text(text: str, lexicon: set[str], holds: set[str] | None = None) -> list[str]:
    """Longest-match CJK words against 萌典 /t/index.json. HOLD spans stay whole."""
    holds = holds or set()
    hold_list = sorted((h for h in holds if h), key=len, reverse=True)
    max_lex = max((len(w) for w in lexicon), default=8)
    max_lex = min(max(max_lex, 4), 12)
    toks: list[str] = []
    for line in hanzi_lines(text):
        i = 0
        n = len(line)
        while i < n:
            ch = line[i]
            if not CJK_RE.match(ch):
                i += 1
                continue
            held = None
            for h in hold_list:
                if line.startswith(h, i):
                    held = h
                    break
            if held:
                toks.append(held)
                i += len(held)
                continue
            matched = None
            upper = min(max_lex, n - i)
            for L in range(upper, 0, -1):
                cand = line[i : i + L]
                if not all(CJK_RE.match(c) for c in cand):
                    continue
                if cand in lexicon:
                    matched = cand
                    break
            if matched:
                toks.append(matched)
                i += len(matched)
            else:
                toks.append(ch)
                i += 1
    return toks


def english_proper_nouns(text: str) -> list[str]:
    found = []
    for m in EN_PROPER.findall(text):
        if m not in SECTION_LABELS:
            found.append(m)
    return found


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
                    "spoken": False,
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
        "picker": "白>替>audio>unlabeled>文",
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


def cmd_segment(args: argparse.Namespace) -> int:
    holds = {w.strip() for w in (args.hold or "").split(",") if w.strip()}
    text = Path(args.hanzi).read_text(encoding="utf-8")
    lex = load_index()
    toks = segment_text(text, lex, holds)
    uniq = list(dict.fromkeys(toks))
    out = {
        "authority": API_INDEX,
        "n_index": len(lex),
        "n_tokens": len(toks),
        "n_unique": len(uniq),
        "tokens": toks,
        "unique": uniq,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if lex else 2


def audit_lyrics_file(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
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
    return {
        "file": str(path),
        "authority": "https://www.moedict.tw/lookup/trs/<tailo>",
        "default_scheme": "tailo",
        "n_tokens": n,
        "n_tailo_hit": hits,
        "n_poj_or_unknown": poj,
        "n_miss": n - hits - poj,
        "ship_as_taigi": hits >= max(1, int(0.5 * n)) and poj == 0,
        "rows": rows,
    }


def cmd_audit_lyrics(args: argparse.Namespace) -> int:
    out = audit_lyrics_file(args.file)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["ship_as_taigi"] else 2


def cmd_audit_pack(args: argparse.Namespace) -> int:
    hanzi_text = Path(args.hanzi).read_text(encoding="utf-8")
    tailo_text = Path(args.tailo).read_text(encoding="utf-8")
    wiki_text = Path(args.wiki).read_text(encoding="utf-8") if args.wiki else ""
    n_cjk = len(CJK.findall(hanzi_text))
    n_lat = len(re.findall(r"[A-Za-z]", hanzi_text))
    en_hanzi = english_proper_nouns(hanzi_text)
    en_wiki = english_proper_nouns(wiki_text) if wiki_text else []
    holds = {w.strip() for w in (args.hold or "").split(",") if w.strip()}
    lex = load_index()
    auto_toks = segment_text(hanzi_text, lex, holds) if lex else []
    auto_uniq = [t for t in dict.fromkeys(auto_toks) if t not in holds]
    manual = [w.strip() for w in (args.words or "").split(",") if w.strip()]
    words = manual or auto_uniq
    lookup_rows = []
    for w in words:
        if w in holds:
            lookup_rows.append({"word": w, "ok": False, "hold": True, "spoken": False})
            continue
        rec = lookup_word(w)
        rec["hold"] = False
        lookup_rows.append(rec)
    n_lookup = len(lookup_rows)
    n_ok = sum(1 for r in lookup_rows if r.get("ok"))
    n_hold = sum(1 for r in lookup_rows if r.get("hold"))
    n_miss = n_lookup - n_ok - n_hold
    n_spoken = sum(1 for r in lookup_rows if r.get("ok") and r.get("spoken"))
    spoken_cov = (100.0 * n_spoken / n_ok) if n_ok else 0.0
    tailo = audit_lyrics_file(args.tailo)
    hz_lines = hanzi_lines(hanzi_text)
    missing_lines = [ln for ln in hz_lines if wiki_text and ln not in wiki_text]
    singer_is_hanzi = n_cjk >= 8 and n_cjk > n_lat
    wiki_ok = (not args.wiki) or (not missing_lines and n_cjk > 0)
    ship = (
        singer_is_hanzi
        and not en_hanzi
        and not en_wiki
        and n_miss == 0
        and n_ok >= 1
        and tailo["ship_as_taigi"]
        and wiki_ok
    )
    out = {
        "authority": "https://www.moedict.tw/t/<詞>.json",
        "picker": "白>替>audio>unlabeled>文",
        "design": "native-taigi-hanzi",
        "translate_from_english": False,
        "singer": "hanzi",
        "spelling": "tailo",
        "hanzi_file": str(args.hanzi),
        "tailo_file": str(args.tailo),
        "wiki_file": str(args.wiki) if args.wiki else None,
        "n_cjk": n_cjk,
        "n_latin": n_lat,
        "singer_is_hanzi": singer_is_hanzi,
        "english_proper_hanzi": en_hanzi,
        "english_proper_wiki": en_wiki,
        "n_index": len(lex),
        "segmented": auto_uniq,
        "words_source": "manual" if manual else "auto-segment",
        "n_lookup": n_lookup,
        "n_ok": n_ok,
        "n_hold": n_hold,
        "n_miss": n_miss,
        "n_spoken": n_spoken,
        "spoken_coverage_pct": round(spoken_cov, 1),
        "wiki_missing_hanzi_lines": missing_lines,
        "tailo": {k: tailo[k] for k in tailo if k != "rows"},
        "lookup_rows": [
            {k: r.get(k) for k in ("word", "ok", "hold", "tailo", "reading", "spoken", "audio_id", "sense_override", "picker_would", "note")}
            for r in lookup_rows
        ],
        "ship_as_taigi": ship,
        "sung_phonology": False,
        "sung_note": "HeartMuLa has no Taigi G2P; this gate is spelling+listen gold only",
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if ship else 2


def main() -> int:
    ap = argparse.ArgumentParser(description="萌典 Tâi-lô SSOT for Taigi spelling")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lookup", help="漢字 → spoken Tâi-lô via /t/ (白/替, not 文)")
    p.add_argument("--words", required=True)
    p.add_argument("--hold", default="")
    p.set_defaults(fn=cmd_lookup)

    p = sub.add_parser("segment", help="longest-match 漢字 against /t/index.json")
    p.add_argument("--hanzi", required=True)
    p.add_argument("--hold", default="")
    p.set_defaults(fn=cmd_segment)

    p = sub.add_parser("trs", help="Tâi-lô → 漢字 via /lookup/trs/")
    p.add_argument("--q", required=True)
    p.set_defaults(fn=cmd_trs)

    p = sub.add_parser("audit-lyrics", help="score a Tâi-lô sidecar against /lookup/trs/")
    p.add_argument("--file", required=True)
    p.set_defaults(fn=cmd_audit_lyrics)

    p = sub.add_parser(
        "audit-pack",
        help="native Taigi pack: 漢字 singer + Tâi-lô audit + wiki interlinear",
    )
    p.add_argument("--hanzi", required=True, help="<slug>-lyrics-hanzi.txt")
    p.add_argument("--tailo", required=True, help="<slug>-lyrics-tailo.txt")
    p.add_argument("--wiki", default="", help="<slug>-lyrics.txt interlinear")
    p.add_argument("--words", default="", help="optional comma 漢字 list; default = auto-segment")
    p.add_argument("--hold", default="")
    p.set_defaults(fn=cmd_audit_pack)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())

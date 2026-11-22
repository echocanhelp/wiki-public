#!/usr/bin/env python3
"""Nightly absorb: vault-first classify captures → private stubs.

Sources: Echo許 captures (line-echo) and 歲月有聲 sittings (line-stories).
Does NOT write wiki. Does NOT enqueue gaps / NEED YOU. Caps 8 stubs/night
shared across both sources. Skip already-on-page and duplicate text_sha.
A miss is eligible unless privacy was explicitly requested and acknowledged.
Absence of consent is not a skip.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CAPTURE = Path("/home/leedt/echo-system/knowledge/interactions/line-echo/captures.jsonl")
STORIES = Path("/home/leedt/echo-system/knowledge/interactions/line-stories")
STUBS = Path("/home/leedt/echo-system/knowledge/operational/intelligence/interaction-absorb.jsonl")
CURSOR = Path("/home/leedt/.hermes/cache/interaction-absorb.cursor")
CURSOR_STORIES = Path("/home/leedt/.hermes/cache/interaction-absorb-stories.cursor")
FA = Path("/home/leedt/.hermes/scripts/echopedia-first-answer.py")
CAP = 8
FREEZE = Path("/tmp/pinto-cpu-freeze")

_YEAR = re.compile(r"(?:19|20)\d{2}")
_HAN = re.compile(r"[\u4e00-\u9fff]{2,}")


def _load_answer():
    spec = importlib.util.spec_from_file_location("echopedia_first_answer", FA)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load echopedia-first-answer.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.answer


def _tokens(text: str) -> set[str]:
    years = _YEAR.findall(text or "")
    han = _HAN.findall(text or "")
    return {t for t in years + han if t}


def _already_on_page(body: str, text: str) -> bool:
    toks = _tokens(text)
    if not toks:
        return False
    return all(t in body for t in toks)


def _seen_shas(limit: int = 400) -> set[str]:
    if not STUBS.is_file():
        return set()
    out = set()
    for line in STUBS.read_text(encoding="utf-8").splitlines()[-limit:]:
        try:
            n = json.loads(line)
        except Exception:
            continue
        if n.get("text_sha"):
            out.add(n["text_sha"])
    return out


def classify(answer_fn, n: dict, query: str | None = None) -> dict | None:
    """Return stub dict or None to skip (tape kept, no NEED YOU).

    query overrides the lookup text. line-stories turns pass the teller's
    display name: an utterance like "Afternoon" misses the vault, the name hits.
    """
    text = (n.get("text") or "").strip()
    if not text:
        return None
    sha = n.get("text_sha") or ""
    q = (query or text)[:160]
    try:
        res = answer_fn(q, source="cron", no_gap=True)
    except Exception:
        res = {"status": "miss"}
    status = res.get("status") or "miss"
    slug = res.get("slug")
    path = res.get("source_path")
    consent = bool(n.get("consent"))

    if status == "skip":
        return None
    if status == "hit" and path:
        try:
            body = Path(path).read_text(encoding="utf-8", errors="replace")
        except Exception:
            body = ""
        if _already_on_page(body, text):
            return None
        return {
            "action": "deepen",
            "slug": slug,
            "path": path,
            "consent": consent,
            "playbook": "echopedia-capture-manicure",
            "wiki": False,
        }
    privacy_hold = _privacy_hold(n)
    if privacy_hold:
        return None
    if status == "miss":
        return {
            "action": "new_hold",
            "slug": None,
            "path": None,
            "consent": consent,
            "playbook": "echopedia-capture-manicure",
            "wiki": False,
        }
    return None


def _story_files(cursor: dict) -> list[Path]:
    """Dated jsonl sittings at or after the cursor date, oldest first."""
    if not STORIES.is_dir():
        return []
    since = cursor.get("date") or ""
    files = sorted(
        p for p in STORIES.glob("*.jsonl") if p.stem >= since and len(p.stem) == 10
    )
    return files


_SITTING_ROLES = frozenset({"User", "Voice (transcribed)"})


def _story_record(n: dict) -> dict | None:
    """Normalize a line-stories turn into classify()'s capture shape.

    Bot replies and empty turns are not sittings. Voice transcripts are:
    the appender stores them under role "Voice (transcribed)", and 33 of the
    imported sittings are only there. text_sha is derived here because the
    appender stores no hash. user_id is never copied out.
    """
    if n.get("role") not in _SITTING_ROLES:
        return None
    text = (n.get("text") or "").strip()
    if not text:
        return None
    return {
        "text": text,
        "text_sha": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
        "src": "line-stories",
        "consent": False,
        "privacy_requested": bool(n.get("privacy_requested")),
        "privacy_acknowledged": bool(n.get("privacy_acknowledged")),
        "display_name": (n.get("display_name") or "").strip(),
    }


def _privacy_hold(n: dict) -> bool:
    """Explicit request AND acknowledged. A request alone is not a hold."""
    return bool(n.get("privacy_requested")) and bool(n.get("privacy_acknowledged"))


def absorb_stories(answer_fn, seen: set[str], room: int) -> tuple[list[dict], int]:
    """Classify new 歲月有聲 turns. Returns (stubs, lines_scanned).

    Lookup key is the teller's display name, not the utterance. A turn with no
    display name blocks the cursor: skipping it would hide a later appender
    fix. Shares the nightly cap.
    """
    if room <= 0 or not STORIES.is_dir():
        return [], 0
    cursor = {}
    if CURSOR_STORIES.is_file():
        try:
            cursor = json.loads(CURSOR_STORIES.read_text())
        except Exception:
            cursor = {}
    stubs: list[dict] = []
    scanned = 0
    blocked = False
    new_cursor = dict(cursor)
    for f in _story_files(cursor):
        start = cursor.get("line", 0) if f.stem == cursor.get("date") else 0
        lines = f.read_text(encoding="utf-8").splitlines()
        i = start
        while i < len(lines):
            if len(stubs) >= room:
                blocked = True
                break
            raw = lines[i]
            try:
                n = json.loads(raw)
            except Exception:
                i += 1
                scanned += 1
                continue
            rec = _story_record(n)
            if rec is None:
                i += 1
                scanned += 1
                continue
            if not rec["display_name"]:
                blocked = True
                break
            i += 1
            scanned += 1
            # Hold wins over a vault hit. classify() only checks privacy on the
            # miss path, so a teller with a page would otherwise leak into a
            # deepen stub after an acknowledged privacy request.
            if _privacy_hold(rec):
                continue
            sha = rec["text_sha"]
            if sha in seen:
                continue
            stub = classify(answer_fn, rec, query=rec["display_name"])
            if not stub:
                continue
            stub.update(
                {
                    "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "src": "line-stories",
                    "teller": rec["display_name"],
                    "text": rec["text"][:300],
                    "text_sha": sha,
                }
            )
            stubs.append(stub)
            seen.add(sha)
        new_cursor = {"date": f.stem, "line": i}
        if blocked:
            break
    if new_cursor != cursor:
        CURSOR_STORIES.parent.mkdir(parents=True, exist_ok=True)
        CURSOR_STORIES.write_text(json.dumps(new_cursor) + "\n")
    return stubs, scanned


def main() -> int:
    if FREEZE.exists():
        return 0
    if not CAPTURE.is_file() or not FA.is_file():
        return 0
    answer_fn = _load_answer()
    lines = CAPTURE.read_text(encoding="utf-8").splitlines()
    last = int(CURSOR.read_text().strip()) if CURSOR.is_file() else 0
    last = max(0, min(last, len(lines)))
    seen = _seen_shas()
    stubs = []
    i = last
    while i < len(lines) and len(stubs) < CAP:
        raw = lines[i]
        i += 1
        try:
            n = json.loads(raw)
        except Exception:
            continue
        sha = n.get("text_sha") or ""
        if sha and sha in seen:
            continue
        stub = classify(answer_fn, n)
        if not stub:
            continue
        stub.update(
            {
                "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "src": n.get("src"),
                "text": (n.get("text") or "")[:300],
                "text_sha": sha,
            }
        )
        stubs.append(stub)
        if sha:
            seen.add(sha)
    CURSOR.parent.mkdir(parents=True, exist_ok=True)
    CURSOR.write_text(str(i) + "\n")
    story_stubs, story_scanned = absorb_stories(answer_fn, seen, CAP - len(stubs))
    stubs.extend(story_stubs)
    if not stubs:
        return 0
    STUBS.parent.mkdir(parents=True, exist_ok=True)
    with STUBS.open("a", encoding="utf-8") as f:
        for s in stubs:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    kinds = {}
    for s in stubs:
        kinds[s["action"]] = kinds.get(s["action"], 0) + 1
    print(
        f"AUTO absorb n={len(stubs)} {kinds} cursor={i} "
        f"stories_scanned={story_scanned} (no wiki)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

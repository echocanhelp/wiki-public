#!/usr/bin/env python3
"""Nightly absorb: vault-first classify Echo許 captures → private stubs.

Does NOT write wiki. Does NOT enqueue gaps / NEED YOU. Caps 8 stubs/night.
Skip already-on-page and duplicate text_sha. MISS without consent stays tape.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CAPTURE = Path("/home/leedt/echo-system/knowledge/interactions/line-echo/captures.jsonl")
STUBS = Path("/home/leedt/echo-system/knowledge/operational/intelligence/interaction-absorb.jsonl")
CURSOR = Path("/home/leedt/.hermes/cache/interaction-absorb.cursor")
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


def classify(answer_fn, n: dict) -> dict | None:
    """Return stub dict or None to skip (tape kept, no NEED YOU)."""
    text = (n.get("text") or "").strip()
    if not text:
        return None
    sha = n.get("text_sha") or ""
    q = text[:160]
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
    if status == "miss" and consent:
        return {
            "action": "new_hold",
            "slug": None,
            "path": None,
            "consent": True,
            "playbook": "echopedia-capture-manicure",
            "wiki": False,
        }
    return None  # miss, no consent: tape only


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
    if not stubs:
        return 0
    STUBS.parent.mkdir(parents=True, exist_ok=True)
    with STUBS.open("a", encoding="utf-8") as f:
        for s in stubs:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    kinds = {}
    for s in stubs:
        kinds[s["action"]] = kinds.get(s["action"], 0) + 1
    print(f"AUTO absorb n={len(stubs)} {kinds} cursor={i} (no wiki)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

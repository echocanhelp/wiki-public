#!/usr/bin/env python3
"""Voice-memo STT interpretation. Unclear transcripts get a read-back, never a guess."""
from __future__ import annotations

import re
import unicodedata

MEDIA = re.compile(r"^\[(audio|image|video|file|sticker)[^\]]*\]$", re.I)

_HALLU = (
    "thank you for watching",
    "thanks for watching",
    "please subscribe",
    "subscribe to",
    "like and subscribe",
    "thanks for listening",
    "please like",
    "字幕",
    "[music]",
    "[applause]",
    "www.youtube",
    "as an ai",
)

_MARKERS = re.compile(
    r"\[(inaudible|unintelligible|unclear|blank_audio|silence|music)\]|\?\?\?|…{2,}|\.{3,}",
    re.I,
)


def _fold(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = s.strip().strip('"').strip("'").strip()
    return re.sub(r"\s+", " ", s)


def interpret(*, text: str, voice: bool = False) -> dict:
    raw = (text or "").strip()
    heard = _fold(raw)
    if not voice or not heard or MEDIA.match(heard):
        return {"voice": bool(voice), "unclear": False, "reasons": [], "heard": heard}

    reasons: list[str] = []
    low = heard.lower()

    if _MARKERS.search(heard):
        reasons.append("inaudible_marker")
    if any(h in low for h in _HALLU):
        reasons.append("stt_hallucination")
    letters = re.sub(r"[^\w\u4e00-\u9fff]+", "", heard, flags=re.UNICODE)
    if len(letters) < 8 and not re.search(r"[\u4e00-\u9fff]{2,}", heard):
        # short roman with no 漢字 — often a clipped memo
        if len(letters) <= 2:
            reasons.append("too_short")
        elif not re.search(r"[A-Za-z]{2,}\s+[A-Za-z]{2,}", heard):
            reasons.append("too_short")
    toks = re.findall(r"[A-Za-z\u4e00-\u9fff]+", heard)
    if toks:
        longest_run = 1
        run = 1
        for a, b in zip(toks, toks[1:]):
            if a.lower() == b.lower():
                run += 1
                longest_run = max(longest_run, run)
            else:
                run = 1
        if longest_run >= 4:
            reasons.append("repeat_loop")
        if len(toks) >= 8 and len({t.lower() for t in toks}) <= 2:
            reasons.append("repeat_loop")
    latin = re.findall(r"[A-Za-z]{3,}", heard)
    if latin:
        vowelless = sum(1 for w in latin if not re.search(r"[aeiouyAEIOUY]", w))
        if vowelless / max(len(latin), 1) >= 0.5 and len(latin) >= 3:
            reasons.append("garbled")
    if re.fullmatch(r"[\W_]+", heard):
        reasons.append("no_words")
    if "\ufffd" in raw:
        reasons.append("garbled")

    unclear = bool(reasons)
    return {
        "voice": True,
        "unclear": unclear,
        "reasons": reasons,
        "heard": heard[:400],
    }


def render(payload: dict) -> str:
    if not payload.get("voice"):
        return ""
    if not payload.get("unclear"):
        return (
            "VOICE STT: this is a speech transcript, often slightly off. "
            "If any clause is odd, read it back in one short line and ask once. "
            "Do not invent missing words."
        )
    heard = payload.get("heard") or ""
    why = ", ".join(payload.get("reasons") or []) or "unclear"
    bits = [
        "VOICE INTERPRET: the transcript is not clear. Do not guess or invent words.",
        f'Heard (verbatim): "{heard}"',
        f"Why unclear: {why}",
        "Read back what you think they said in one short line, then ask 是這樣嗎 / is that right?",
        "If you cannot tell, ask them to type it or send the voice memo again.",
    ]
    return "\n".join(bits)

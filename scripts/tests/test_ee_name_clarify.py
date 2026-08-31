#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
from ee_name_clarify import clarify, phonetic_candidates, render
from ee_turn_context import route


def test_ken_woo_phonetic_hits_ken_wu():
    slugs = {c["slug"] for c in phonetic_candidates("Ken Woo")}
    assert "ken-wu" in slugs


def test_albert_lie_phonetic_hits_lai():
    slugs = {c["slug"] for c in phonetic_candidates("Albert Lie")}
    assert "albert-s-lai" in slugs


def test_typed_exact_person_stays_card():
    r = route(text="Ken Wu", display_name="Leonard Hsu Junior")
    assert r["action"] == "card"
    assert "ken-wu" in (r.get("text") or "").lower() or "吳" in (r.get("text") or "")


def test_voice_exact_person_asks_once():
    r = route(text="Ken Wu", display_name="Leonard Hsu Junior", voice=True)
    p = r["preamble"]
    assert r["action"] == "llm"
    assert "NAME CLARIFY" in p
    assert "ken-wu" in p
    assert "Ask once" in p or "ask once" in p.lower()
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None


def test_voice_stt_misspelling_offers_near_match():
    r = route(text="I met Ken Woo yesterday", display_name="Leonard Hsu Junior", voice=True)
    p = r["preamble"]
    assert r["action"] == "llm"
    assert "NAME CLARIFY" in p
    assert "Heard:" in p
    assert "ken-wu" in p
    assert "Do not invent" in p or "do not invent" in p.lower()
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None
    assert "626" not in p


def test_lowercase_stt_bigrams():
    cl = clarify(text="i met ken woo at church", voice=True)
    blob = render(cl)
    assert cl["ask"] is True
    assert "ken-wu" in blob
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None

#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
from ee_identity_hint import hint
from ee_turn_context import bind_ephemeral, route


def test_junior_matches_jr():
    h = hint(display_name="Leonard Hsu Junior")
    assert h["match"] == "proposed"
    assert h["slug"] == "leonard-hsu-jr"
    assert h["confirm"] is True


def test_good_morning_is_greet_not_llm():
    r = route(text="Good Morning!", display_name="Leonard Hsu Junior")
    assert r["action"] == "greet"
    assert "Historical Society" in r["text"]
    assert "historiographer" in r["text"].lower()
    assert "second brain" in r["text"].lower()
    assert "Story History" not in r["text"]
    assert "許景鴻" in r["text"] or "Leonard" in r["text"]


def test_zh_greet_is_historiographer():
    r = route(text="早安", display_name="Leonard Hsu Junior")
    assert r["action"] == "greet"
    assert "史家" in r["text"]
    assert "第二大腦" in r["text"]
    assert "Story History" not in r["text"]


def test_who_is_mugu_is_card():
    r = route(text="誰是牧谷", display_name="Leonard Hsu Junior")
    assert r["action"] == "card"
    assert "牧谷" in r["text"]
    assert "GSTPC" in r["text"] or "好牧者" in r["text"]


def test_greet_cites_teller_page_url():
    r = route(text="Good Morning!", display_name="Leonard Hsu Junior")
    assert r["action"] == "greet"
    assert "wiki-public/people/leonard-hsu-jr" in r["text"]
    assert "626" not in r["text"]
    assert "@" not in r["text"] or "echo" in r["text"].lower()


def test_audio_llm_preamble_has_teller_card():
    r = route(text="[audio]", display_name="Leonard Hsu Junior")
    assert r["action"] == "llm"
    p = r["preamble"]
    assert "wiki-public/people/leonard-hsu-jr" in p
    assert "TELLER PAGE" in p
    assert "historiographer" in p.lower()
    assert "2nd brain" in p.lower()
    assert "許景鴻" in p
    assert "terminal" in p.lower()
    assert "626" not in p
    assert "lhsu@" not in p
    assert "people," in p and "orgs" in p


def test_story_mentions_gstpc_injects_card():
    r = route(text="那天我在 GSTPC 幫忙", display_name="Leonard Hsu Junior")
    assert r["action"] == "llm"
    assert "good-shepherd-taiwanese-presbyterian-church" in r["preamble"]


def test_topical_monterey_park_hits_gstpc():
    r = route(text="Tell me about the church in Monterey Park", display_name="Leonard Hsu Junior")
    p = r["preamble"]
    assert r["action"] == "llm"
    assert "good-shepherd-taiwanese-presbyterian-church" in p
    assert "VAULT ORG DIRECTORY" in p
    assert "Monterey" in p or "好牧者" in p
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None


def test_verified_members_in_preamble_no_uids():
    r = route(text="[audio]", display_name="Leonard Hsu Junior")
    p = r["preamble"]
    assert "VERIFIED LINE MEMBER PAGES" in p
    assert "albert-s-lai" in p or "Albert" in p
    assert "賴信雄" in p or "Lai" in p
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None
    assert "626" not in p
    assert "lhsu@" not in p
    assert "TAHS-LINKED PEOPLE" in p
    assert "leonard-hsu-jr" in p
    assert "VAULT EVENTS" in p
    assert "228" in p or "台灣會館" in p or "tc-event" in p
    assert "VAULT PUBLICATIONS" in p
    assert "2017-tahs-publication" in p or "菁英錄" in p or "TAHS Publication" in p
    assert len(p) < 16000


def test_named_verified_keeps_dossier():
    r = route(text="Tell me about Albert Lai", display_name="Leonard Hsu Junior")
    p = r["preamble"]
    assert r["action"] == "llm"
    assert "VERIFIED LINE MEMBER PAGES" in p
    assert "albert-s-lai" in p
    assert "賴信雄" in p
    assert "Community of Hope" in p or "FPCLA" in p or "1971" in p
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None
    assert "NETWORK FROM VERIFIED MEMBERS" in p
    assert "formosan-presbyterian-church-in-los-angeles" in p or "taiwanese-american-historical-society" in p


def test_bind_ephemeral_does_not_persist_pack():
    spoken = "Tell me about Albert Lai"
    r = route(text=spoken, display_name="Leonard Hsu Junior")
    b = bind_ephemeral(r, spoken)
    assert b["action"] == "llm"
    assert b["persist_text"] == spoken
    assert "[EE]" not in b["persist_text"]
    assert "TELLER PAGE" not in b["persist_text"]
    assert "albert-s-lai" in b["channel_prompt"]
    assert "Community of Hope" in b["channel_prompt"] or "FPCLA" in b["channel_prompt"]
    assert re.search(r"\bU[0-9a-f]{20,}\b", b["channel_prompt"]) is None
    greet = route(text="Good Morning!", display_name="Leonard Hsu Junior")
    g = bind_ephemeral(greet, "Good Morning!")
    assert g["action"] == "greet"
    assert g["reply"]
    assert not g["channel_prompt"]

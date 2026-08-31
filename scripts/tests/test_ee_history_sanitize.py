#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
from ee_history_sanitize import strip_ee_history, strip_ee_pack

PACK = (
    "[EE] You are Echo 歲月有聲, historiographer for Taiwanese American Historical Society. "
    "Echopedia is your 2nd brain — the vault pack below is that library.\n"
    "TELLER PAGE: leonard-hsu-jr\n\n"
    "VAULT ORG DIRECTORY\nGSTPC\n\n"
    "VERIFIED LINE MEMBER PAGES\nAlbert Lai"
)


def test_plain_utterance_unchanged():
    assert strip_ee_pack("Wifey made me a delicious shake") == "Wifey made me a delicious shake"


def test_echopedia_brain_not_stripped():
    t = "[ECHOPEDIA BRAIN] albert-s-lai — pastor\n\nwho is Albert Lai"
    assert strip_ee_pack(t) == t


def test_utterance_then_pack_keeps_speech():
    spoken = "It's been a long time since I thought about grandma."
    assert strip_ee_pack(f'"{spoken}"  {PACK}') == spoken


def test_pack_only_is_empty():
    assert strip_ee_pack(PACK) == ""


def test_pack_then_utterance_keeps_tail():
    assert strip_ee_pack(PACK + "\n\n誰是牧谷") == "誰是牧谷"


def test_history_drops_pack_only_user_keeps_speech():
    rows = [
        {"role": "user", "content": PACK},
        {"role": "assistant", "content": "Hi."},
        {"role": "user", "content": f'"車上聊得很開心"  {PACK}'},
        {"role": "assistant", "content": "Go on."},
        {"role": "user", "content": "Wifey made me a delicious shake"},
    ]
    out = strip_ee_history(rows)
    users = [m["content"] for m in out if m["role"] == "user"]
    assert users == ["車上聊得很開心", "Wifey made me a delicious shake"]
    assert all("[EE]" not in (m.get("content") or "") for m in out)
    assert all("TELLER PAGE" not in (m.get("content") or "") for m in out)

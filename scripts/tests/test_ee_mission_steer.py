#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
from ee_mission_steer import steer
from ee_turn_context import route


def test_off_mission_bitcoin_asks_ta_question():
    r = route(text="Bitcoin is pumping and the Lakers won", display_name="Leonard Hsu Junior")
    p = r["preamble"]
    assert r["action"] == "llm"
    assert r["steer"]["off_mission"] is True
    assert "looks off-mission" in p
    assert "enthusiastic curious" in p or "curious 台美" in p
    assert "do not scold" in p.lower() or "Do not scold" in p
    assert re.search(r"\bU[0-9a-f]{20,}\b", p) is None


def test_on_mission_gstpc_no_pull():
    r = route(text="那天我在 GSTPC 幫忙", display_name="Leonard Hsu Junior")
    p = r["preamble"]
    assert r["steer"]["on_theme"] is True
    assert r["steer"]["off_mission"] is False
    assert "looks off-mission" not in p
    assert "MISSION STEER" in p
    assert "charm one detail" in p.lower() or "Charm one detail" in p


def test_mixed_church_and_nba_stays_on_theme():
    s = steer(text="After the NBA game we still went to GSTPC choir practice")
    assert s["on_theme"] is True
    assert s["off_mission"] is False
    assert "looks off-mission" not in s["block"]

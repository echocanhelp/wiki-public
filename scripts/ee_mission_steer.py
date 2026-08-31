#!/usr/bin/env python3
"""Subtle TAHS-mission steer. Honor the aside; one curious 台美 question. No lecture."""
from __future__ import annotations

import re
import unicodedata

# Family / church / language / migration / community memory — stay with the thread.
_ON = (
    "taiwan",
    "taiwanese",
    "formosa",
    "formosan",
    "tahs",
    "gstpc",
    "tpc",
    "pct",
    "ntpc",
    "itpc",
    "taiwanese american",
    "taiwanese-american",
    "immigra",
    "emigra",
    "hometown",
    "ancestr",
    "presbyterian",
    "church",
    "congregation",
    "taigi",
    "hokkien",
    "hakka",
    "bilingual",
    "228",
    "white terror",
    "martial law",
    "台灣",
    "臺灣",
    "台美",
    "台語",
    "閩南",
    "客家",
    "教會",
    "長老",
    "團契",
    "鄉親",
    "僑",
    "故鄉",
    "家鄉",
    "移民",
    "留學",
    "出國",
    "阿公",
    "阿媽",
    "阿祖",
    "祖先",
    "眷村",
    "戒嚴",
    "二二八",
    "見證",
    "聚會",
)

# Strong off-mission — sports-as-news, markets, gadgets, generic US chatter.
_OFF = (
    "bitcoin",
    "crypto",
    "nft",
    "nba",
    "nfl",
    "mlb",
    "lakers",
    "dodgers",
    "super bowl",
    "world cup",
    "tesla stock",
    "nasdaq",
    "chatgpt",
    "python code",
    "netflix binge",
    "marvel movie",
    "weather forecast",
    "traffic jam",
    "iphone",
    "加密貨幣",
    "股市",
    "籃球比賽",
    "美股",
)

_ALWAYS = (
    "MISSION STEER (always): you collect Taiwanese American memory for TAHS. "
    "If they wander off (sports scores, markets, gadgets, generic US news), "
    "do not scold and do not ignore what they said. Charm one detail, then one "
    "enthusiastic curious question that invites a 台美 thread — family, hometown, "
    "church, language, arrival, foodways, names, a person in the vault pack. "
    "Never force. Never lecture. One question only."
)

_PULL = (
    "This turn looks off-mission. Honor the aside in one clause, then ask one "
    "warm curious 台美 question (family / 故鄉 / church / language / how they "
    "arrived / who was there). Do not fact-dump. Do not invent a bio."
)


def _fold(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    return s.casefold()


def steer(*, text: str) -> dict:
    t = _fold(text)
    if not t or re.fullmatch(r"\[(audio|image|video|file|sticker)[^\]]*\]", t):
        return {"off_mission": False, "on_theme": False, "ask": False, "block": _ALWAYS}

    on = any(k in t for k in _ON)
    off = any(k in t for k in _OFF)
    off_mission = off and not on
    bits = [_ALWAYS]
    if off_mission:
        bits.append(_PULL)
    return {
        "off_mission": off_mission,
        "on_theme": on,
        "ask": off_mission,
        "block": " ".join(bits),
    }

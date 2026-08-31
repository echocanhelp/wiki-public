#!/usr/bin/env python3
"""TDD: ee-card-pack closed corpus."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path("/home/leedt/echo-system/scripts")
sys.path.insert(0, str(SCRIPTS))

from ee_card_pack import pack  # noqa: E402


def test_known_org_slug_has_wiki_public_url_only():
    card = pack(slug="good-shepherd-taiwanese-presbyterian-church")
    assert card["hit"] is True
    assert card["slug"] == "good-shepherd-taiwanese-presbyterian-church"
    assert card["kind"] == "org"
    assert card["url"].startswith("https://echocanhelp.github.io/wiki-public/")
    assert "wikipedia.org" not in card["url"]
    assert "http" not in card.get("one_liner", "") or "echocanhelp.github.io" in card.get("one_liner", "")


def test_unknown_is_miss_not_invented():
    card = pack(name="DefinitelyNotInVaultXYZ")
    assert card["hit"] is False
    assert card.get("query")
    assert "url" not in card or not card["url"]


def test_gstpc_alias_is_good_shepherd_not_mugu():
    card = pack(name="GSTPC")
    assert card["hit"] is True
    assert card["slug"] == "good-shepherd-taiwanese-presbyterian-church"


def test_mugu_is_not_gstpc():
    card = pack(name="牧谷")
    assert card["hit"] is True
    assert card.get("disambiguation") is True
    assert "好牧者" in card["one_liner"] or "GSTPC" in card["one_liner"]
    assert card["slug"] != "good-shepherd-taiwanese-presbyterian-church"


def test_who_is_mugu_wrapper():
    card = pack(name="誰是牧谷")
    assert card["hit"] is True
    assert card.get("disambiguation") is True


def test_gstpc_summary_not_phone():
    card = pack(slug="leonard-hsu-jr")
    assert card["hit"] is True
    assert "President" in card["one_liner"] or "許景鴻" in card["one_liner"]
    assert "626" not in card["one_liner"]
    assert "lhsu@" not in card["one_liner"]

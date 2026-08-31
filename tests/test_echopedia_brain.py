"""Echopedia 2nd-brain retrieve — GSTPC is the church, not Brother Ku."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path("/home/leedt/echo-system/scripts")
sys.path.insert(0, str(SCRIPTS))

from echopedia_brain import format_plain, retrieve  # noqa: E402


def test_gstpc_is_church_not_brother_ku():
    pack = retrieve("GSTPC")
    assert pack["hit"] is True
    slugs = [h["slug"] for h in pack["hits"]]
    assert "good-shepherd-taiwanese-presbyterian-church" in slugs
    assert slugs[0] == "good-shepherd-taiwanese-presbyterian-church"
    joined = " ".join(slugs)
    assert "ku-gstpc" not in joined or slugs[0] != "ku-gstpc"


def test_phoenix_ko():
    pack = retrieve("Phoenix Ko")
    assert pack["hit"] is True
    assert pack["hits"][0]["slug"] == "phoenix-ko"


def test_ops_skipped():
    pack = retrieve("go check logs")
    assert pack.get("skip") is True
    assert pack["hit"] is False
    assert format_plain(pack) == ""


def test_plain_has_no_pii():
    pack = retrieve("Leonard Hsu Jr")
    body = format_plain(pack)
    assert "lhsu@" not in body
    assert "626" not in body
    assert "46-4005384" not in body


def test_cli_plain_gstpc():
    p = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "echopedia_brain.py"),
            "--plain",
            "--text",
            "GSTPC",
        ],
        capture_output=True,
        text=True,
        timeout=20,
    )
    assert p.returncode == 0
    assert "good-shepherd-taiwanese-presbyterian-church" in p.stdout
    assert "Brother Ku" not in p.stdout.split("\n")[1] if p.stdout else True


def test_monterey_park_church_kernel():
    import vault_search as vs

    vs._PLACE_CACHE = None
    rows = vs._keyword_search("the church in Monterey Park", top_k=5)
    paths = [r["path"] for r in rows]
    assert any(
        p == "organizations/good-shepherd-taiwanese-presbyterian-church.md" for p in paths
    )
    pack = retrieve("Tell me about the church in Monterey Park")
    slugs = [h["slug"] for h in pack["hits"]]
    assert "good-shepherd-taiwanese-presbyterian-church" in slugs


def test_verified_line_names_retrieve():
    import vault_search as vs

    vs._REG_ALIAS = None
    aliases = vs.registry_slug_aliases()
    assert "ken wu" in aliases or "Ken Wu" in aliases
    assert aliases.get("ken wu") == "ken-wu" or aliases.get("Ken Wu") == "ken-wu"
    assert "陳乃光" in aliases
    blob = json.dumps(aliases)
    assert not re.search(r"U[0-9a-f]{20,}", blob)
    pack = retrieve("陳乃光")
    assert pack["hit"] is True
    slugs = [h["slug"] for h in pack["hits"]]
    assert slugs[0] == "rex-chen"
    pack2 = retrieve("吳兆峯")
    assert pack2["hits"][0]["slug"] == "ken-wu"

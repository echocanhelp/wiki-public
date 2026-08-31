#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
from ee_vault_retrieve import dossier, pack_context, search


def test_teller_dossier_no_phone():
    d = dossier(slug="leonard-hsu-jr")
    assert d["hit"] is True
    body = d["dossier"]
    assert "許景鴻" in body
    assert "President" in body or "會長" in body
    assert "Phoenix" in body
    assert "626" not in body
    assert "lhsu@" not in body
    assert "46-4005384" not in body
    assert "279 S" not in body
    assert "wiki-public/people/leonard-hsu-jr" in d["url"]


def test_search_gstpc():
    hits = search("那天我在 GSTPC 幫忙", skip_slugs=["leonard-hsu-jr"])
    slugs = {h.get("slug") for h in hits}
    assert "good-shepherd-taiwanese-presbyterian-church" in slugs


def test_audio_context_has_full_teller_and_hop():
    ctx = pack_context(text="[audio]", teller_slug="leonard-hsu-jr")
    assert ctx["teller"]["hit"] is True
    assert "許景鴻" in (ctx["teller"].get("dossier") or "")
    assert ctx["vault"]["people"] > 2000
    assert ctx["vault"]["orgs"] > 100
    slugs = {h.get("slug") for h in ctx["hits"]} | {h.get("slug") for h in ctx.get("hops") or []}
    assert "taiwanese-american-historical-society" in slugs
    known_slugs = {k.get("slug") for k in ctx.get("known") or []}
    assert "albert-s-lai" in known_slugs
    assert "ken-wu" in known_slugs
    # unnamed verified stay compact titles, not 900-char snapshots
    ken = next(k for k in ctx["known"] if k.get("slug") == "ken-wu")
    assert not (ken.get("dossier") or "")


def test_this_turn_hit_keeps_dossier():
    ctx = pack_context(text="Tell me about the church in Monterey Park", teller_slug="leonard-hsu-jr")
    hits = ctx["hits"]
    gstpc = next(h for h in hits if h.get("slug") == "good-shepherd-taiwanese-presbyterian-church")
    body = gstpc.get("dossier") or ""
    assert "Monterey" in body or "好牧者" in body or "Good Shepherd" in (gstpc.get("title") or "")
    assert "626" not in body
    assert ctx.get("orgs_dir")
    assert any("good-shepherd" in x for x in ctx["orgs_dir"])


def test_verified_network_hops():
    ctx = pack_context(text="Tell me about Albert Lai", teller_slug="leonard-hsu-jr")
    hop_slugs = {h.get("slug") for h in ctx.get("hops") or []}
    assert "formosan-presbyterian-church-in-los-angeles" in hop_slugs or "taiwanese-american-historical-society" in hop_slugs
    known = {h.get("slug") for h in ctx.get("known") or []}
    assert "albert-s-lai" in known
    blob = " ".join((h.get("dossier") or "") + (h.get("url") or "") for h in (ctx.get("hops") or []))
    assert "626" not in blob
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None


def test_tahs_people_directory():
    ctx = pack_context(text="[audio]", teller_slug="leonard-hsu-jr")
    rows = ctx.get("people_dir") or []
    blob = "\n".join(rows)
    assert rows
    assert "leonard-hsu-jr" in blob
    assert "david-lee" in blob or "ken-wu" in blob
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None
    assert "626" not in blob


def test_tahs_query_retrieves_affiliates():
    hits = search("Who is in TAHS?", skip_slugs=["leonard-hsu-jr"])
    slugs = {h.get("slug") for h in hits}
    assert "taiwanese-american-historical-society" in slugs
    people = [h for h in hits if h.get("kind") == "person"]
    assert people
    ctx = pack_context(text="Who is in TAHS?", teller_slug="leonard-hsu-jr")
    hit_slugs = {h.get("slug") for h in ctx["hits"]}
    known = {h.get("slug") for h in ctx["known"]}
    assert "david-lee" in known
    assert "david-lee" not in hit_slugs
    assert "taiwanese-american-historical-society" in hit_slugs
    assert any(s in hit_slugs for s in ("alan-thian", "anne-shih", "freeman-huang", "john-yang"))
    blob = " ".join(hit_slugs | known)
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None


def test_events_directory_and_228():
    ctx = pack_context(text="We went to the 228 memorial", teller_slug="leonard-hsu-jr")
    rows = ctx.get("events_dir") or []
    blob = "\n".join(rows)
    assert rows
    assert "228" in blob or "tc-event-228" in blob
    assert (ctx.get("vault") or {}).get("events", 0) >= 10
    slugs = {h.get("slug") for h in ctx.get("hits") or []}
    assert any("228" in (s or "") for s in slugs) or "228" in blob
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None


def test_tahs_yearbooks_and_lai_book():
    ctx = pack_context(text="菁英錄 yearbook", teller_slug="leonard-hsu-jr")
    rows = ctx.get("sources_dir") or []
    blob = "\n".join(rows)
    assert (ctx.get("vault") or {}).get("sources", 0) >= 3
    assert "2017-tahs-publication" in blob
    assert "2023-tahs-publication" in blob
    assert "toward-a-community-of-hope" in blob
    assert "good-shepherd-taiwanese-presbyterian-church" not in blob
    slugs = {h.get("slug") for h in ctx.get("hits") or []}
    assert "2017-tahs-publication" in slugs or "2023-tahs-publication" in slugs
    gstpc = search("GSTPC 好牧者", skip_slugs=["leonard-hsu-jr"])
    assert any(
        h.get("kind") == "org" and "good-shepherd" in (h.get("slug") or "") for h in gstpc
    )
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None


def test_vault_search_works_concert_not_private_index():
    """Reuse Echo許 SQLite — 2413 works/ pages, no v6 EE cache."""
    hits = search("228 Memorial Concert in NorCal", skip_slugs=["leonard-hsu-jr"])
    slugs = [h.get("slug") for h in hits]
    kinds = {h.get("slug"): h.get("kind") for h in hits}
    assert "228-memorial-concert-in-norcal" in slugs
    assert kinds.get("228-memorial-concert-in-norcal") == "work"
    concert = next(h for h in hits if h.get("slug") == "228-memorial-concert-in-norcal")
    assert "works/taiwaneseamerican-org/228-memorial-concert-in-norcal" in (concert.get("url") or "")
    blob = "\n".join((h.get("dossier") or "") + (h.get("url") or "") for h in hits)
    assert re.search(r"\bU[0-9a-f]{20,}\b", blob) is None
    gstpc = search("church in Monterey Park", skip_slugs=["leonard-hsu-jr"])
    assert any(
        h.get("kind") == "org" and "good-shepherd" in (h.get("slug") or "") for h in gstpc
    )


def test_brain_retrieve_shares_search_kernel():
    from echopedia_brain import retrieve

    pack = retrieve("228 Memorial Concert in NorCal", top=8)
    slugs = {h.get("slug") for h in pack.get("hits") or []}
    assert "228-memorial-concert-in-norcal" in slugs


def test_named_verified_gets_page_details():
    ctx = pack_context(text="Tell me about Albert Lai", teller_slug="leonard-hsu-jr")
    albert = next(k for k in ctx["known"] if k.get("slug") == "albert-s-lai")
    body = albert.get("dossier") or ""
    assert "Community of Hope" in body or "FPCLA" in body or "1971" in body
    assert "626" not in body
    assert re.search(r"\bU[0-9a-f]{20,}\b", body) is None
    ken = next(k for k in ctx["known"] if k.get("slug") == "ken-wu")
    assert not (ken.get("dossier") or "")
    teller = ctx["teller"].get("dossier") or ""
    assert "許景鴻" in teller
    assert "TAHS" in teller or "會長" in teller or "Leadership" in teller


def test_preamble_fits_context():
    from ee_turn_context import route

    audio = route(text="[audio]", display_name="Leonard Hsu Junior")["preamble"]
    named = route(text="Tell me about Albert Lai", display_name="Leonard Hsu Junior")["preamble"]
    assert len(audio) < 14000
    assert len(named) < 18000
    assert "albert-s-lai" in named
    assert re.search(r"\bU[0-9a-f]{20,}\b", named) is None

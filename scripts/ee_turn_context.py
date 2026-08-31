#!/usr/bin/env python3
"""EE turn router: greet / card / llm preamble. No U-ids in stdout."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ee_card_pack import pack
from ee_identity_hint import hint
from ee_mission_steer import steer
from ee_name_clarify import clarify, render as render_clarify
from ee_vault_retrieve import pack_context

GREET = re.compile(
    r"^(good\s*)?(morning|afternoon|evening|hi+|hello|hey|yo|嗨|早安|早上好|早|你好|哈囉)[\s!.。！?？]*$",
    re.I,
)
MEDIA = re.compile(r"^\[(audio|image|video|file|sticker)[^\]]*\]$", re.I)
TAHS = "Taiwanese American Historical Society (TAHS / 台美人歷史協會)"
CHARM = 220
PACK_ONE = 420


def _cite_lines(card: dict, *, max_one: int = CHARM) -> list[str]:
    if not card.get("hit"):
        return []
    bits = []
    title = (card.get("title") or "").strip()
    one = (card.get("one_liner") or "").strip()
    url = (card.get("url") or "").strip()
    if title:
        bits.append(title)
    if one:
        bits.append(one[:max_one] + ("…" if len(one) > max_one else ""))
    if url:
        bits.append(url)
    return bits


def _vault_block(ctx: dict) -> str:
    bits: list[str] = []
    vault = ctx.get("vault") or {}
    bits.append(
        f"Closed Echopedia vault: {vault.get('people', 0)} people, "
        f"{vault.get('orgs', 0)} orgs, {vault.get('events', 0)} events, "
        f"{vault.get('sources', 0)} sources. Cite only pages below. "
        "Do not use terminal, web, news, memory, or file tools."
    )
    teller = ctx.get("teller") or {}
    if teller.get("hit"):
        bits.append("TELLER PAGE (full, scrubbed):")
        bits.append(teller.get("title") or "")
        if teller.get("url"):
            bits.append(teller["url"])
        dossier = (teller.get("dossier") or "").strip()
        if dossier:
            bits.append(dossier)
        else:
            bits.extend(_cite_lines(teller, max_one=PACK_ONE)[1:])
    for hit in ctx.get("hits") or []:
        bits.append("ALSO IN VAULT THIS TURN:")
        bits.extend(_cite_lines(hit, max_one=PACK_ONE))
        dos = (hit.get("dossier") or "").strip()
        if dos:
            bits.append(dos)
    known = ctx.get("known") or []
    if known:
        bits.append("VERIFIED LINE MEMBER PAGES (cite when relevant; no U-ids):")
        for hit in known:
            bits.extend(_cite_lines(hit, max_one=280))
            dos = (hit.get("dossier") or "").strip()
            if dos:
                bits.append(dos)
    hops = ctx.get("hops") or []
    if hops:
        bits.append("NETWORK FROM VERIFIED MEMBERS (scrubbed pages):")
        for hit in hops:
            bits.extend(_cite_lines(hit, max_one=PACK_ONE))
            dos = (hit.get("dossier") or "").strip()
            if dos:
                bits.append(dos)
    orgs_dir = ctx.get("orgs_dir") or []
    if orgs_dir:
        bits.append("VAULT ORG DIRECTORY (titles; churches first; cite a slug only if packed above):")
        bits.extend(orgs_dir)
    people_dir = ctx.get("people_dir") or []
    if people_dir:
        bits.append("TAHS-LINKED PEOPLE (titles only; no bio unless packed above):")
        bits.extend(people_dir)
    events_dir = ctx.get("events_dir") or []
    if events_dir:
        bits.append("VAULT EVENTS (titles; cite a slug only if packed above):")
        bits.extend(events_dir)
    sources_dir = ctx.get("sources_dir") or []
    if sources_dir:
        bits.append("VAULT PUBLICATIONS (titles; cite a slug only if packed above):")
        bits.extend(sources_dir)
    return "\n".join(b for b in bits if b)


def route(*, text: str, display_name: str = "", line_user_id: str = "", voice: bool = False) -> dict:
    ident = hint(display_name=display_name, line_user_id=line_user_id)
    who = (display_name or "").strip()
    match = ident.get("match")
    title = ident.get("title") or ""
    slug = ident.get("slug") or ""
    ctx = pack_context(text=text, teller_slug=slug)
    teller = ctx.get("teller") or {}
    if not title and teller.get("title"):
        title = teller["title"]

    t = (text or "").strip()
    zh = bool(re.search(r"[\u4e00-\u9fff]", t))
    voice = bool(voice) or bool(MEDIA.match(t))

    if GREET.match(t):
        self_card = teller if teller.get("hit") else pack(slug=slug, max_one=PACK_ONE) if slug else {"hit": False}
        if zh:
            bits = ["早。我是 Echo 歲月有聲，台美人歷史協會的史家。Echopedia 是我的第二大腦。"]
            if match == "proposed":
                bits.append(f"Echopedia 有「{title}」這頁，是你嗎？")
            elif match == "linked":
                bits.append(f"Echopedia 有你這頁「{title}」。")
            else:
                bits.append("想從哪一段說起？")
            bits.extend(_cite_lines(self_card)[1:])
            if match in ("linked", "proposed"):
                bits.append("想補這頁，還是從別的故事說起？")
        else:
            bits = [f"Hello — Echo 歲月有聲, historiographer for {TAHS}. Echopedia is my second brain."]
            if match == "linked":
                bits.append(f"Echopedia already has you as {title}.")
            elif match == "proposed":
                bits.append(f"LINE shows {who or 'your name'}. Echopedia has {title}. Is that you?")
            else:
                bits.append("I listen and keep Taiwanese American memory here. What would you like to tell?")
            bits.extend(_cite_lines(self_card)[1:])
            if match in ("linked", "proposed"):
                bits.append("Want to add to that page, or start somewhere else?")
        return {"action": "greet", "text": " ".join(b for b in bits if b), "identity": ident}

    card = pack(name=t)
    # Voice/STT: never auto-state a person name even on exact card hit.
    if card.get("hit") and not (voice and card.get("kind") == "person"):
        bits = _cite_lines(card, max_one=PACK_ONE)
        if ident.get("confirm") and title:
            bits.append(f"LINE shows {who or 'your name'}. Echopedia has {title}. Is that you?")
        return {
            "action": "card",
            "text": "\n".join(b for b in bits if b),
            "identity": ident,
        }

    cl = clarify(text=t, voice=voice)
    ms = steer(text=t)
    preamble = (
        f"[EE] You are Echo 歲月有聲, historiographer for {TAHS}. "
        "Echopedia is your 2nd brain — the vault pack below is that library. "
        "Never say Story History. "
        f"LINE display name: {who or 'unknown'}. "
        "You already have the vault pack below — it is the whole library you may use. "
        "Closed corpus only. Do not use terminal, web, news, memory, or file tools. "
        "Cite the teller page when it fits. Teller beats the page "
        "(tag page_conflict, do not lecture). One short reply. Charm one detail. "
        "Never recite phone, email, address, EIN, or LINE ids. "
        "No profile-build, no /help. "
    )
    if match != "none":
        preamble += f"Identity {match}: {title}. "
        if ident.get("confirm"):
            preamble += "Ask once if that is them. "
    if cl.get("ask"):
        preamble += "STT names are usually wrong. Ask once. Do not invent a bio. "
    if ms.get("block"):
        preamble += ms["block"] + " "
    preamble += "\n" + _vault_block(ctx)
    clar_block = render_clarify(cl)
    if clar_block:
        preamble += "\n" + clar_block
    return {
        "action": "llm",
        "preamble": preamble,
        "identity": ident,
        "vault": ctx.get("vault"),
        "clarify": cl,
        "steer": ms,
    }


def bind_ephemeral(ctx: dict, utterance: str) -> dict:
    """Split vault pack off the stored user line.

    LINE history stacked every [EE] preamble (~95k tokens, 5-min compress).
    channel_prompt is applied at API call time and never persisted.
    """
    utter = (utterance or "").strip()
    act = (ctx or {}).get("action") or "llm"
    if act in ("greet", "card"):
        return {
            "action": act,
            "persist_text": utter,
            "channel_prompt": "",
            "reply": ((ctx or {}).get("text") or "").strip(),
        }
    pack = ((ctx or {}).get("preamble") or "").strip()
    return {
        "action": act,
        "persist_text": utter,
        "channel_prompt": pack,
        "reply": "",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--display-name", default="")
    ap.add_argument("--line-user-id", default="")
    ap.add_argument("--voice", action="store_true")
    args = ap.parse_args()
    print(
        json.dumps(
            route(
                text=args.text,
                display_name=args.display_name,
                line_user_id=args.line_user_id,
                voice=args.voice,
            ),
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Closed-corpus Echopedia card for EE. No HTTP. No gap queue."""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

VAULT = Path("/home/leedt/echo-system")
PEOPLE = VAULT / "content" / "people"
ORGS = VAULT / "content" / "organizations"
PUBLIC = "https://echocanhelp.github.io/wiki-public"
MAX_ONE = 900
ALIAS_PATH = Path(__file__).with_name("ee_card_aliases.json")


def _aliases() -> dict:
    if not ALIAS_PATH.is_file():
        return {"slug_aliases": {}, "disambiguations": {}}
    return json.loads(ALIAS_PATH.read_text(encoding="utf-8"))


def _norm_alias(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def pack(*, name: str = "", slug: str = "", max_one: int = MAX_ONE) -> dict:
    query = (slug or name or "").strip()
    if not query:
        return {"hit": False, "query": ""}
    raw = query
    # strip who-is wrappers
    q = re.sub(
        r"^(who\s+is|who'?s|what\s+is|tell\s+me\s+about|info\s+on|誰是|介紹)\s*",
        "",
        query,
        flags=re.I,
    ).strip(" ??.。！!")
    if slug:
        for kind, root in (("person", PEOPLE), ("org", ORGS)):
            p = root / f"{slug}.md"
            if p.is_file():
                return _card(p, kind, max_one)
        return {"hit": False, "query": slug}

    data = _aliases()
    nq = _norm_alias(q)
    for key, spec in (data.get("disambiguations") or {}).items():
        names = {_norm_alias(key), *(_norm_alias(a) for a in spec.get("also") or [])}
        if nq in names:
            return {
                "hit": True,
                "disambiguation": True,
                "slug": spec.get("slug") or "",
                "title": spec.get("title") or key,
                "kind": spec.get("kind") or "org",
                "url": spec.get("url") or "",
                "hanzi": spec.get("hanzi") or "",
                "one_liner": spec.get("one_liner") or "",
                "years": "",
                "affiliations": [],
                "related": [],
                "gaps": ["no standalone page"],
                "collision": True,
                "query": raw,
            }
    slug_map = data.get("slug_aliases") or {}
    mapped = slug_map.get(nq) or slug_map.get(slugify(q))
    if mapped:
        for kind, root in (("person", PEOPLE), ("org", ORGS)):
            p = root / f"{mapped}.md"
            if p.is_file():
                return _card(p, kind, max_one)

    s = slugify(q)
    hits: list[tuple[Path, str]] = []
    for kind, root in (("person", PEOPLE), ("org", ORGS)):
        p = root / f"{s}.md"
        if p.is_file():
            hits.append((p, kind))
    if len(hits) == 1:
        return _card(hits[0][0], hits[0][1], max_one)
    if len(hits) > 1:
        card = _card(hits[0][0], hits[0][1], max_one)
        card["collision"] = True
        return card
    return {"hit": False, "query": raw}


def slugify(name: str) -> str:
    s = (name or "").strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _scrub_pii(text: str) -> str:
    text = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "", text)
    text = re.sub(r"\b[\w.+-]+@[\w.-]+\.\w+\b", "", text)
    text = re.sub(r"\b\d{2}-\d{7}\b", "", text)  # EIN
    text = re.sub(r"\b\d{1,5}\s+[A-Z][A-Za-z.\s]+\s(?:St|Ave|Blvd|Rd|Dr)\b[^\n]*", "", text)
    return re.sub(r"\s+", " ", text).strip(" ,;")


def _one_liner(body: str, max_one: int = MAX_ONE) -> str:
    # drop yaml
    if body.startswith("---"):
        parts = body.split("---", 2)
        body = parts[2] if len(parts) >= 3 else body
    summary = re.search(r"^## Summary\s*\n+(.+?)(?:\n## |\Z)", body, re.S | re.M)
    chunk = summary.group(1) if summary else body
    chunk = re.sub(r"^#.*$", "", chunk, flags=re.M)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", chunk) if p.strip()]
    text = paras[0] if paras else ""
    text = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = _scrub_pii(text)
    if len(text) > max_one:
        text = text[: max_one - 1] + "…"
    return text


def _related(body: str) -> list[dict]:
    out = []
    for m in re.finditer(r"\[\[(people|organizations)/([^\]|]+)(?:\|([^\]]+))?\]\]", body):
        kind, slug, title = m.group(1), m.group(2), m.group(3) or m.group(2)
        out.append({"slug": slug, "title": title, "kind": "person" if kind == "people" else "org"})
        if len(out) >= 6:
            break
    return out


def _hanzi(body: str) -> str:
    m = re.search(r"\*\*Chinese name:\*\*\s*(.+)", body)
    if m:
        return m.group(1).strip()
    m = re.search(r"（([^）]*[\u4e00-\u9fff][^）]*)）", body)
    return m.group(1).strip() if m else ""


def _card(path: Path, kind: str, max_one: int = MAX_ONE) -> dict:
    slug = path.stem
    body = _read(path)
    title_m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', body, re.M)
    title = title_m.group(1) if title_m else slug
    folder = "people" if kind == "person" else "organizations"
    return {
        "hit": True,
        "slug": slug,
        "title": title,
        "kind": kind,
        "url": f"{PUBLIC}/{folder}/{slug}",
        "hanzi": _hanzi(body),
        "one_liner": _one_liner(body, max_one),
        "years": "",
        "affiliations": [],
        "related": _related(body),
        "gaps": [],
        "collision": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="EE Echopedia card (local vault only)")
    ap.add_argument("--name", default="")
    ap.add_argument("--slug", default="")
    ap.add_argument("--max-chars", type=int, default=MAX_ONE)
    ap.add_argument("--plain", action="store_true")
    args = ap.parse_args()
    card = pack(name=args.name, slug=args.slug, max_one=args.max_chars)
    if args.plain:
        if not card.get("hit"):
            return 2
        bits = [card.get("title") or "", card.get("one_liner") or ""]
        if card.get("url"):
            bits.append(card["url"])
        print("\n".join(b for b in bits if b))
        return 0
    print(json.dumps(card, ensure_ascii=False))
    return 0 if card.get("hit") else 2


if __name__ == "__main__":
    raise SystemExit(main())

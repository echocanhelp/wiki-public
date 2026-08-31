#!/usr/bin/env python3
"""Propose an Echopedia person from LINE displayName / linked id.

Never prints LINE U-ids. Confirm-with-user when match is name-only.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

REG = Path("/home/leedt/echo-system/echopedia/identity/identity_registry.json")
PUBLIC = "https://echocanhelp.github.io/wiki-public/people"


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", (s or "").strip().lower())
    s = s.replace(".", " ")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\bjr\b", "junior", s)
    s = re.sub(r"\bsr\b", "senior", s)
    return s


def hint(*, display_name: str = "", line_user_id: str = "", registry: Path = REG) -> dict:
    if not registry.is_file():
        return {"match": "none"}
    data = json.loads(registry.read_text(encoding="utf-8"))
    links = data.get("links") or []
    uid = (line_user_id or "").strip()
    if uid:
        for link in links:
            ids = [str(x) for x in (link.get("line_user_ids") or [])]
            if uid in ids and link.get("state") in ("verified", "owner_verified"):
                slug = link.get("person_slug") or ""
                en = link.get("display_name_en") or slug
                zh = link.get("display_name_zh") or ""
                return {
                    "match": "linked",
                    "slug": slug,
                    "title": f"{en} {zh}".strip(),
                    "confirm": False,
                    "url": f"{PUBLIC}/{slug}" if slug else "",
                }
    dn = _norm(display_name)
    if not dn or dn.startswith("u") and len(dn) > 20:
        return {"match": "none"}
    hits = []
    for link in links:
        if link.get("state") not in ("verified", "owner_verified", "proposed"):
            continue
        en = _norm(link.get("display_name_en") or "")
        zh = (link.get("display_name_zh") or "").strip()
        slug = link.get("person_slug") or ""
        names = {en, _norm(zh), _norm(slug.replace("-", " "))}
        names.discard("")
        if dn in names or (en and (dn in en or en in dn)):
            hits.append(link)
    if len(hits) == 1:
        link = hits[0]
        slug = link.get("person_slug") or ""
        en = link.get("display_name_en") or slug
        zh = link.get("display_name_zh") or ""
        return {
            "match": "proposed",
            "slug": slug,
            "title": f"{en} {zh}".strip(),
            "confirm": True,
            "url": f"{PUBLIC}/{slug}" if slug else "",
        }
    return {"match": "none"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--display-name", default="")
    ap.add_argument("--line-user-id", default="")
    args = ap.parse_args()
    print(json.dumps(hint(display_name=args.display_name, line_user_id=args.line_user_id), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

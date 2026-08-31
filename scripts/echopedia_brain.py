#!/usr/bin/env python3
"""Echopedia 2nd-brain retrieve — one door.

Order: first-answer card → vault title/alias → SQLite keyword (no rglob).
Cite the page. No HTTP. No U-ids. Web is the caller's last resort.

  python3 echopedia_brain.py --text "who is GSTPC"
  python3 echopedia_brain.py --plain --text "Phoenix Ko"
  python3 echopedia_brain.py --json --text "Albert Lai"
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
HERMES_SCRIPTS = Path.home() / ".hermes" / "scripts"
PUBLIC = "https://echocanhelp.github.io/wiki-public"

_OPS = re.compile(
    r"(?i)^\s*go\b|"
    r"\b(check\s+logs?|status|oauth|gateway|restart|config\.ya?ml|"
    r"vllm|laguna|system docs|review system|kanban|cron|llm model|"
    r"firmware|delegate_task)\b|"
    r"https?://|grokipedia\.com"
)
_PII = [
    re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"),
    re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    re.compile(r"\b\d{2}-\d{7}\b"),
    re.compile(r"\b\d{1,5}\s+[A-Z][A-Za-z]+\s+(St|Ave|Blvd|Rd|Dr|Ln|Way)\b", re.I),
]


def _scrub(text: str) -> str:
    out = text or ""
    try:
        sys.path.insert(0, str(SCRIPTS))
        from ee_card_pack import _scrub_pii  # type: ignore

        out = _scrub_pii(out)
    except Exception:
        pass
    for rx in _PII:
        out = rx.sub("[redacted]", out)
    return out


_FA_MOD = None
_FA_TRIED = False


def _load_first_answer():
    """Load first-answer once per process. Re-exec on every retrieve was ~21k parse."""
    global _FA_MOD, _FA_TRIED
    if _FA_TRIED:
        return _FA_MOD
    _FA_TRIED = True
    path = HERMES_SCRIPTS / "echopedia-first-answer.py"
    if not path.is_file():
        path = Path.home() / ".hermes" / "profiles" / "pinto" / "scripts" / "echopedia-first-answer.py"
    if not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("echopedia_first_answer", path)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _FA_MOD = mod
    return _FA_MOD


def _should_skip(query: str) -> bool:
    q = (query or "").strip()
    if not q:
        return True
    if re.fullmatch(r"\[(audio|image|video|file|sticker)[^\]]*\]", q, re.I):
        return True
    if "ECHOPEDIA BRAIN" in q or q.startswith("[EE]"):
        return True
    if _OPS.search(q):
        return True
    return False


# Scratch / audiobook review pages swamp "who is Albert" with extra hits.
# Keep them when the query itself is about those pages.
_NOISE_SLUG = re.compile(r"(?i)(?:scratch|audiobook|sku-a|chapter\d)")
_NOISE_QUERY = re.compile(r"(?i)(?:audiobook|scratch|sku[- ]?a|chapter\s*\d)")


def _noise_slug(slug: str, query: str = "") -> bool:
    if not slug or not _NOISE_SLUG.search(slug):
        return False
    if _NOISE_QUERY.search(query or ""):
        return False
    return True


def retrieve(query: str, *, top: int = 5, semantic: bool = False) -> dict:
    """Return {hit, card, hits, miss} from the vault only."""
    q = (query or "").strip()
    if _should_skip(q):
        return {"hit": False, "skip": True, "card": None, "hits": [], "query": q}

    card = None
    fa = _load_first_answer()
    if fa is not None:
        try:
            card = fa.answer(q, source="brain", no_gap=True)
            if card and card.get("status") != "hit":
                card = None
        except Exception:
            card = None

    if card and card.get("slug"):
        if _noise_slug(card["slug"], q):
            card = None
    hits: list[dict] = []
    seen: set[str] = set()
    if card and card.get("slug"):
        seen.add(card["slug"])
        hits.append(
            {
                "slug": card.get("slug"),
                "title": card.get("name_en") or card.get("name_zh") or card.get("slug") or "",
                "kind": card.get("kind") or card.get("type") or "",
                "url": card.get("url") or "",
                "one_liner": (card.get("role") or (card.get("facts") or [""])[0] or "")[:240],
                "source": "first-answer",
            }
        )

    try:
        sys.path.insert(0, str(SCRIPTS))
        import ee_vault_retrieve as ev  # type: ignore

        skip = [card["slug"]] if card and card.get("slug") else []
        for h in ev.search(q, skip_slugs=skip, limit=max(top * 3, top)):
            slug = h.get("slug") or ""
            if not slug or slug in seen:
                continue
            if _noise_slug(slug, q):
                continue
            seen.add(slug)
            hits.append(
                {
                    "slug": slug,
                    "title": h.get("title") or "",
                    "kind": h.get("kind") or "",
                    "url": h.get("url") or "",
                    "one_liner": (h.get("one_liner") or "")[:240],
                    "source": "vault-search",
                }
            )
    except Exception:
        pass

    # Optional semantic rerank only — keyword/place already live in ev.search.
    if semantic:
        try:
            import vault_search as vs  # type: ignore

            extra = vs.hybrid_search(q, top_k=top + 3)
            for r in extra:
                path = r.get("path") or ""
                slug = Path(path).stem
                if not slug or slug in seen:
                    continue
                if _noise_slug(slug, q):
                    continue
                if not path.startswith(("people/", "organizations/", "events/", "works/")):
                    continue
                seen.add(slug)
                kind = "org" if path.startswith("organizations/") else (
                    "person" if path.startswith("people/") else r.get("type") or ""
                )
                hits.append(
                    {
                        "slug": slug,
                        "title": r.get("title") or slug,
                        "kind": kind,
                        "url": f"{PUBLIC}/{path.replace('.md', '')}",
                        "one_liner": "",
                        "source": "vault-semantic",
                    }
                )
                if len(hits) >= top:
                    break
        except Exception:
            pass

    return {
        "hit": bool(hits),
        "skip": False,
        "card": card,
        "hits": hits[:top],
        "query": q,
    }


def format_plain(pack: dict) -> str:
    if pack.get("skip") or not pack.get("hits"):
        return ""
    lines = ["[ECHOPEDIA BRAIN — vault first, cite these pages, no web unless miss]"]
    for h in pack["hits"]:
        kind = h.get("kind") or ""
        title = h.get("title") or h.get("slug")
        url = h.get("url") or ""
        one = (h.get("one_liner") or "").replace("\n", " ").strip()
        bit = f"- {title}"
        if kind:
            bit += f" ({kind})"
        if url:
            bit += f" {url}"
        if one:
            bit += f" — {one[:180]}"
        lines.append(bit)
    return _scrub("\n".join(lines))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("query", nargs="*", help="query text")
    p.add_argument("--text", default="")
    p.add_argument("--plain", action="store_true")
    p.add_argument("--json", dest="as_json", action="store_true")
    p.add_argument("--semantic", action="store_true")
    p.add_argument("--top", type=int, default=5)
    args = p.parse_args()
    q = args.text or " ".join(args.query)
    pack = retrieve(q, top=args.top, semantic=args.semantic)
    if args.as_json:
        print(json.dumps(pack, ensure_ascii=False, indent=2)[:8000])
    else:
        text = format_plain(pack)
        if text:
            print(text)
        elif not pack.get("skip"):
            print("MISS")
            return 2
    return 0 if pack.get("hit") or pack.get("skip") else 2


if __name__ == "__main__":
    sys.exit(main())

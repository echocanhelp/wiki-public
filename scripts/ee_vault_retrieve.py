#!/usr/bin/env python3
"""Closed-corpus Echopedia retrieve for EE. No HTTP. No U-ids."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from ee_card_pack import ORGS, PEOPLE, PUBLIC, _aliases, _hanzi, _one_liner, _related, _scrub_pii

CACHE = Path("/home/leedt/echo-system/knowledge/operational/ee-vault-index.v5.json")
CONTENT = Path("/home/leedt/echo-system/content")
EVENTS = CONTENT / "events"
SOURCES = CONTENT / "sources"
WORKS = CONTENT / "works"
_WORKS_STEM: dict[str, Path] | None = None
# Website mirrors collide with org slugs. Only memory-works / yearbooks.
_SOURCE_KEEP = (
    "tahs-publication",
    "toward-a-community-of-hope",
    "laijohn-com",
)


def _keep_source(stem: str) -> bool:
    s = (stem or "").lower()
    return any(k in s for k in _SOURCE_KEEP)


def _works_stem() -> dict[str, Path]:
    """Nested works/ pages. Echo許 vault_search already indexes these."""
    global _WORKS_STEM
    if _WORKS_STEM is None:
        found: dict[str, Path] = {}
        if WORKS.is_dir():
            for path in WORKS.rglob("*.md"):
                if path.name in SKIP_NAMES or path.name.endswith(".wiki-index.md"):
                    continue
                found[path.stem] = path
        _WORKS_STEM = found
    return _WORKS_STEM


SKIP_NAMES = {"index.md", ".wiki-index.md"}
STOP_KEYS = {
    "taiwan",
    "taiwanese",
    "american",
    "church",
    "presbyterian",
    "history",
    "historical",
    "society",
    "index",
    "people",
    "organization",
    "organizations",
    "台灣",
    "台美",
    "教會",
    "長老",
    "協會",
    "歷史",
}
KEEP_HEADINGS = {
    "identity snapshot",
    "identity",
    "family",
    "summary",
    "overview",
    "role",
    "tahs leadership",
    "tahs membership assignment",
    "tahs founding",
    "areas of work",
    "echopedia role",
    "network",
    "affiliations",
    "related pages",
    "timeline",
    "historical context",
    "introduction context",
    "professional context",
    "professional / career context",
    "early life and education",
    "career and community leadership",
    "community / volunteer leadership",
    "contributions and legacy",
    "contributions / responsibilities",
    "known public footprint",
    "legacy",
    "name variants / disambiguation",
    "disambiguation",
}
DROP_HEADINGS = {
    "personal information",
    "contact",
    "quotes",
    "revision history",
    "works",
    "taiwan justice",
    "citations",
    "consent",
    "verification",
}
REG = Path("/home/leedt/echo-system/echopedia/identity/identity_registry.json")
MAX_DOSSIER = 3200
MAX_HIT = 520
MAX_HITS = 4
MAX_KNOWN = 8
HIT_DOSSIER = 900
ORG_DIR_LIMIT = 24
MAX_HOPS = 4
PIN_ORGS = (
    "taiwanese-american-historical-society",
    "good-shepherd-taiwanese-presbyterian-church",
    "formosan-presbyterian-church-in-los-angeles",
)


def _page_card(slug: str, kind: str = "", max_chars: int = HIT_DOSSIER) -> dict:
    """Page card with scrubbed dossier. Never carries U-ids."""
    card = dossier(slug=slug, kind=kind, max_chars=max_chars)
    if not card.get("hit"):
        return {"hit": False, "slug": slug}
    return {
        "hit": True,
        "slug": card["slug"],
        "kind": card.get("kind") or kind,
        "title": card.get("title") or slug,
        "url": card.get("url") or "",
        "one_liner": (card.get("one_liner") or "")[:MAX_HIT],
        "dossier": (card.get("dossier") or "")[:max_chars],
        "related": card.get("related") or [],
    }


def org_directory(idx: dict, *, limit: int = ORG_DIR_LIMIT) -> list[str]:
    """Compact org titles (churches first). Titles/hanzi/slug only."""
    churches: list[str] = []
    rest: list[str] = []
    for d in idx.get("docs") or []:
        if d.get("kind") != "org":
            continue
        slug = (d.get("slug") or "").strip()
        title = (d.get("title") or slug).strip()
        hanzi = (d.get("hanzi") or "").strip()
        if not slug or slug == "index":
            continue
        blob = f"{title} {hanzi} {slug}".lower()
        line = title
        if hanzi and hanzi not in title:
            line = f"{title} / {hanzi}"
        line = f"{line} ({slug})"
        if slug in PIN_ORGS or any(
            k in blob for k in ("church", "presbyterian", "教會", "tpc", "pct", "congregation")
        ):
            churches.append(line)
        else:
            rest.append(line)
    pinned = [ln for ln in churches if any(s in ln for s in PIN_ORGS)]
    other_ch = [ln for ln in churches if ln not in pinned]
    return (pinned + other_ch + rest)[:limit]


def people_directory(idx: dict, *, limit: int = 24) -> list[str]:
    """TAHS-linked people titles only. Verified LINE members first. No U-ids, no bios."""
    mark = "taiwanese-american-historical-society"
    verified = set(verified_slugs())
    first: list[str] = []
    rest: list[str] = []
    for d in idx.get("docs") or []:
        if d.get("kind") != "person":
            continue
        slug = (d.get("slug") or "").strip()
        if not slug or slug == "index":
            continue
        keys = " ".join(str(k).lower() for k in (d.get("keys") or []))
        if slug not in verified and mark not in keys and mark not in slug:
            continue
        title = (d.get("title") or slug).strip()
        hanzi = (d.get("hanzi") or "").strip()
        line = f"{title} / {hanzi} ({slug})" if hanzi and hanzi not in title else f"{title} ({slug})"
        if slug in verified:
            first.append(line)
        else:
            rest.append(line)
        if len(first) + len(rest) >= 400:
            break
    return (first + rest)[:limit]


def events_directory(idx: dict, *, limit: int = 20) -> list[str]:
    """Event titles only. No U-ids."""
    rows: list[str] = []
    for d in idx.get("docs") or []:
        if d.get("kind") != "event":
            continue
        slug = (d.get("slug") or "").strip()
        if not slug or slug == "index":
            continue
        title = (d.get("title") or slug).strip()
        rows.append(f"{title} ({slug})")
        if len(rows) >= limit:
            break
    return rows


def sources_directory(idx: dict, *, limit: int = 12) -> list[str]:
    """Yearbooks / memory-works titles only. No U-ids."""
    rows: list[str] = []
    for d in idx.get("docs") or []:
        if d.get("kind") != "source":
            continue
        slug = (d.get("slug") or "").strip()
        if not slug or slug == "index":
            continue
        title = (d.get("title") or slug).strip()
        rows.append(f"{title} ({slug})")
        if len(rows) >= limit:
            break
    return rows


def _collect_hops(sources: list[dict], skip: set[str], limit: int = MAX_HOPS) -> list[dict]:
    """1-hop pages from teller + verified members. No U-ids."""
    hops: list[dict] = []
    seen = set(skip)
    for src in sources:
        for rel in src.get("related") or []:
            slug = (rel.get("slug") or "").strip()
            if not slug or slug in seen or slug == "index":
                continue
            seen.add(slug)
            hop = _page_card(
                slug,
                kind="org" if rel.get("kind") == "org" else "person",
                max_chars=0,
            )
            if hop.get("hit"):
                hop["dossier"] = ""
                hops.append(hop)
            if len(hops) >= limit:
                return hops
    return hops


def _mtime_stamp() -> float:
    stamps = []
    for root in (PEOPLE, ORGS, EVENTS, SOURCES):
        try:
            stamps.append(root.stat().st_mtime)
        except OSError:
            pass
    return max(stamps) if stamps else 0.0


def _extract_title(raw: str, slug: str) -> str:
    m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', raw, re.M)
    return (m.group(1) if m else slug).strip()


def _keys_for(title: str, hanzi: str, slug: str, extra: list[str] | None = None) -> list[str]:
    keys: set[str] = set()
    blob = f"{title} {hanzi}"
    for tok in re.findall(r"[\u4e00-\u9fff]{2,8}", blob):
        keys.add(tok)
    for tok in re.findall(r"[A-Za-z][A-Za-z.'-]{2,}", title):
        low = tok.lower().strip(".")
        if low not in STOP_KEYS and len(low) >= 3:
            keys.add(low)
    slug_words = [w for w in slug.replace("_", "-").split("-") if len(w) >= 3]
    keys.update(slug_words)
    for tok in re.findall(r"\b\d{3,4}\b", title + " " + slug):
        keys.add(tok)
    if hanzi:
        keys.add(hanzi)
    for item in extra or []:
        item = (item or "").strip()
        if item:
            keys.add(item.lower() if re.fullmatch(r"[A-Za-z0-9 .'-]+", item) else item)
    return [k for k in keys if k and k.lower() not in STOP_KEYS]


def build_index() -> dict:
    docs: list[dict] = []
    for kind, root in (("person", PEOPLE), ("org", ORGS), ("event", EVENTS)):
        if not root.is_dir():
            continue
        for path in root.glob("*.md"):
            if path.name in SKIP_NAMES or path.name.endswith(".wiki-index.md"):
                continue
            try:
                raw = path.read_text(encoding="utf-8", errors="replace")[:5000]
            except OSError:
                continue
            title = _extract_title(raw, path.stem)
            hanzi = _hanzi(raw)
            extra = re.findall(r"\[\[organizations/([^\]|]+)", raw)
            extra += re.findall(r"\[\[people/([^\]|]+)", raw)
            if "菁英錄" in raw:
                extra.append("菁英錄")
            if re.search(r"(?i)yearbook", raw):
                extra.append("yearbook")
            docs.append(
                {
                    "slug": path.stem,
                    "kind": kind,
                    "title": title,
                    "hanzi": hanzi,
                    "keys": _keys_for(title, hanzi, path.stem, extra=extra),
                }
            )
    occupied = {d["slug"] for d in docs}
    if SOURCES.is_dir():
        for path in SOURCES.glob("*.md"):
            if path.name in SKIP_NAMES or path.name.endswith(".wiki-index.md"):
                continue
            if path.stem in occupied or not _keep_source(path.stem):
                continue
            try:
                raw = path.read_text(encoding="utf-8", errors="replace")[:5000]
            except OSError:
                continue
            title = _extract_title(raw, path.stem)
            hanzi = _hanzi(raw)
            extra = re.findall(r"\[\[organizations/([^\]|]+)", raw)
            extra += re.findall(r"\[\[people/([^\]|]+)", raw)
            if "菁英錄" in raw:
                extra.append("菁英錄")
            if re.search(r"(?i)yearbook", raw):
                extra.append("yearbook")
            docs.append(
                {
                    "slug": path.stem,
                    "kind": "source",
                    "title": title,
                    "hanzi": hanzi,
                    "keys": _keys_for(title, hanzi, path.stem, extra=extra),
                }
            )
    data = {
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "content_mtime": _mtime_stamp(),
        "people": sum(1 for d in docs if d["kind"] == "person"),
        "orgs": sum(1 for d in docs if d["kind"] == "org"),
        "events": sum(1 for d in docs if d["kind"] == "event"),
        "sources": sum(1 for d in docs if d["kind"] == "source"),
        "docs": docs,
    }
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


def load_index() -> dict:
    try:
        if CACHE.is_file():
            data = json.loads(CACHE.read_text(encoding="utf-8"))
            n_events = int(data.get("events") or 0)
            n_src = int(data.get("sources") or 0)
            mtime_ok = abs(float(data.get("content_mtime") or 0) - _mtime_stamp()) < 0.01
            if mtime_ok and (n_events > 0 or not EVENTS.is_dir()) and (n_src > 0 or not SOURCES.is_dir()):
                return data
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        pass
    return build_index()


def _sections(body: str) -> list[tuple[str, str]]:
    if body.startswith("---"):
        parts = body.split("---", 2)
        body = parts[2] if len(parts) >= 3 else body
    chunks = re.split(r"(?m)^##\s+", body)
    out: list[tuple[str, str]] = []
    lead = chunks[0].strip() if chunks else ""
    if lead:
        out.append(("", lead))
    for chunk in chunks[1:]:
        lines = chunk.splitlines()
        heading = (lines[0] if lines else "").strip()
        text = "\n".join(lines[1:]).strip()
        out.append((heading, text))
    return out


def dossier(*, slug: str = "", kind: str = "", max_chars: int = MAX_DOSSIER) -> dict:
    if not slug:
        return {"hit": False}
    roots = []
    if kind == "org":
        roots = [("org", ORGS), ("person", PEOPLE), ("event", EVENTS), ("source", SOURCES)]
    elif kind == "person":
        roots = [("person", PEOPLE), ("org", ORGS), ("event", EVENTS), ("source", SOURCES)]
    elif kind == "event":
        roots = [("event", EVENTS), ("org", ORGS), ("person", PEOPLE), ("source", SOURCES)]
    elif kind == "source":
        roots = [("source", SOURCES), ("org", ORGS), ("person", PEOPLE), ("event", EVENTS)]
    elif kind == "work":
        roots = []
    else:
        roots = [("person", PEOPLE), ("org", ORGS), ("event", EVENTS), ("source", SOURCES)]
    path = None
    used_kind = ""
    for k, root in roots:
        p = root / f"{slug}.md"
        if p.is_file():
            path, used_kind = p, k
            break
    if not path:
        wp = _works_stem().get(slug)
        if wp is not None and wp.is_file():
            path, used_kind = wp, "work"
    if not path:
        return {"hit": False, "slug": slug}

    raw = path.read_text(encoding="utf-8", errors="replace")
    title = _extract_title(raw, slug)
    if used_kind == "work":
        folder = str(path.relative_to(CONTENT).with_suffix(""))
        page_url = f"{PUBLIC}/{folder}"
    else:
        folder = {"person": "people", "org": "organizations", "event": "events", "source": "sources"}.get(used_kind, "people")
        page_url = f"{PUBLIC}/{folder}/{slug}"
    kept: list[str] = []
    for heading, text in _sections(raw):
        h = heading.lower().strip()
        if any(h.startswith(d) or d in h for d in DROP_HEADINGS):
            continue
        if heading and h not in KEEP_HEADINGS and not h.startswith("related"):
            if not any(k in h or h.startswith(k) for k in KEEP_HEADINGS):
                # keep unknown short factual sections except dumps
                if len(text) > 1200:
                    continue
        text = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"(?im)^\s*[-*]\s*\*\*Contact:\*\*.*$", "", text)
        text = _scrub_pii(text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if not text:
            continue
        block = f"## {heading}\n{text}" if heading else text
        kept.append(block)
    body = "\n\n".join(kept)
    if len(body) > max_chars:
        body = body[: max_chars - 1] + "…"
    return {
        "hit": True,
        "slug": slug,
        "kind": used_kind,
        "title": title,
        "hanzi": _hanzi(raw),
        "url": page_url,
        "one_liner": _one_liner(raw, 420),
        "related": _related(raw),
        "dossier": body,
    }


def _alias_hits(text: str, skip: set[str]) -> list[dict]:
    found: list[dict] = []
    aliases = _aliases()
    keys = list((aliases.get("slug_aliases") or {}).keys())
    keys += list((aliases.get("disambiguations") or {}).keys())
    for also in (aliases.get("disambiguations") or {}).values():
        keys += list(also.get("also") or [])
    try:
        from vault_search import registry_slug_aliases

        keys += list(registry_slug_aliases().keys())
    except Exception:
        pass
    keys = sorted({k for k in keys if k and len(k) >= 2}, key=len, reverse=True)
    hay = text
    hay_l = text.lower()
    seen = set(skip)
    from ee_card_pack import pack

    for key in keys:
        if re.search(r"[\u4e00-\u9fff]", key):
            matched = key in hay
        else:
            matched = bool(re.search(rf"\b{re.escape(key)}\b", hay_l, re.I))
        if matched:
            mapped_slug = ""
            try:
                from vault_search import registry_slug_aliases

                mapped_slug = registry_slug_aliases().get(key) or registry_slug_aliases().get(key.lower()) or ""
            except Exception:
                mapped_slug = ""
            card = pack(name=key, max_one=MAX_HIT)
            slug = (card.get("slug") if card.get("hit") else "") or mapped_slug or key
            packed = _page_card(str(slug))
            if packed.get("hit") and packed["slug"] not in seen:
                found.append(packed)
                seen.add(packed["slug"])
            if len(found) >= MAX_HITS:
                break
    return found


def verified_slugs() -> list[str]:
    """owner_verified / verified person slugs only. Never returns U-ids."""
    if not REG.is_file():
        return []
    try:
        data = json.loads(REG.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[str] = []
    seen: set[str] = set()
    for link in data.get("links") or []:
        if link.get("state") not in ("verified", "owner_verified"):
            continue
        slug = (link.get("person_slug") or "").strip()
        if not slug or slug in seen:
            continue
        seen.add(slug)
        out.append(slug)
        if len(out) >= MAX_KNOWN:
            break
    return out


def topical_hits(text: str, *, skip_slugs: list[str] | None = None, limit: int = MAX_HITS) -> list[dict]:
    """Whole-vault retrieve when the turn has no exact name (Monterey Park → GSTPC)."""
    t = (text or "").strip()
    if not t or re.fullmatch(r"\[(audio|image|video|file|sticker)[^\]]*\]", t, re.I):
        return []
    skip = set(skip_slugs or [])
    hits: list[dict] = []

    def _add(card: dict) -> bool:
        slug = card.get("slug") or ""
        if not card.get("hit") or not slug or slug in skip:
            return False
        packed = _page_card(slug, kind=card.get("kind") or "")
        if not packed.get("hit"):
            return False
        skip.add(slug)
        hits.append(packed)
        return len(hits) >= limit

    try:
        from ee_card_pack import _aliases, _norm_alias, pack

        hay = _norm_alias(t)
        for key, slug in (_aliases().get("slug_aliases") or {}).items():
            k = _norm_alias(str(key))
            if len(k) < 8 or k not in hay:
                continue
            if _add(pack(slug=str(slug), max_one=MAX_HIT)):
                return hits
    except Exception:
        pass
    try:
        from echopedia_brain import retrieve

        pack = retrieve(t, top=limit)
        for h in pack.get("hits") or []:
            if _add(h):
                break
    except Exception:
        pass
    return hits


def search(text: str, *, skip_slugs: list[str] | None = None, limit: int = MAX_HITS) -> list[dict]:
    t = (text or "").strip()
    if not t or re.fullmatch(r"\[(audio|image|video|file|sticker)[^\]]*\]", t, re.I):
        return []
    skip = set(skip_slugs or [])
    hits = _alias_hits(t, skip)
    seen = set(skip)
    for h in hits:
        if h.get("slug"):
            seen.add(h["slug"])
    idx = load_index()
    scored: list[tuple[int, dict]] = []
    hay = t
    hay_l = t.lower()
    org_marks: set[str] = set()
    try:
        for k, slug in (_aliases().get("slug_aliases") or {}).items():
            if not k or not slug:
                continue
            if str(k).lower() in hay_l or str(k) in hay:
                org_marks.add(str(slug).lower())
    except Exception:
        pass
    for doc in idx.get("docs") or []:
        slug = doc.get("slug") or ""
        if slug in seen:
            continue
        best = 0
        keys = doc.get("keys") or []
        keyset = {str(k).lower() for k in keys if k}
        if org_marks and (org_marks & keyset):
            best = 24
        for key in keys:
            if not key:
                continue
            if re.search(r"[\u4e00-\u9fff]", key):
                if key in hay:
                    best = max(best, len(key) * 3)
            else:
                if re.search(rf"\b{re.escape(key)}\b", hay_l, re.I):
                    best = max(best, len(key))
        if best:
            scored.append((best, doc))
    scored.sort(key=lambda x: (-x[0], x[1].get("title") or ""))
    idx_hits: list[dict] = []
    for _score, doc in scored:
        packed = _page_card(doc["slug"], kind=doc.get("kind") or "")
        if not packed.get("hit"):
            continue
        idx_hits.append(packed)
        seen.add(packed["slug"])
        if len(idx_hits) >= limit:
            break
    # Echo許 rank (works/place) before weak title-key matches.
    sqlite = _sqlite_hits(t, set(skip) | {h.get("slug") or "" for h in hits}, limit)
    merged: list[dict] = []
    seen_m = set(skip)
    for card in hits + sqlite + idx_hits:
        slug = card.get("slug") or ""
        if not slug or slug in seen_m:
            continue
        merged.append(card)
        seen_m.add(slug)
        if len(merged) >= limit:
            break
    return merged[:limit]


def _sqlite_hits(text: str, seen: set[str], limit: int) -> list[dict]:
    """Same SQLite title/path/place index Echo許 uses. No new EE cache."""
    if limit <= 0:
        return []
    try:
        from vault_search import _keyword_search
    except Exception:
        return []
    allow = ("people/", "organizations/", "events/", "works/", "sources/")
    try:
        rows = _keyword_search(text, top_k=limit + 8)
    except Exception:
        return []
    out: list[dict] = []
    for row in rows:
        path = row.get("path") or ""
        if not path.startswith(allow):
            continue
        slug = Path(path).stem
        if not slug or slug in seen:
            continue
        if path.startswith("sources/") and not _keep_source(slug):
            continue
        if path.startswith("organizations/"):
            kind = "org"
        elif path.startswith("people/"):
            kind = "person"
        elif path.startswith("events/"):
            kind = "event"
        elif path.startswith("works/"):
            kind = "work"
        else:
            kind = "source"
        packed = _page_card(slug, kind=kind)
        if not packed.get("hit"):
            continue
        out.append(packed)
        seen.add(slug)
        if len(out) >= limit:
            break
    return out


def pack_context(*, text: str, teller_slug: str = "") -> dict:
    idx = load_index()
    teller = dossier(slug=teller_slug, kind="person") if teller_slug else {"hit": False, "related": []}
    verified = set(verified_slugs())
    skip = [s for s in [teller_slug] if s]
    named = search(text, skip_slugs=skip, limit=MAX_HITS)
    extra_skip = skip + [h.get("slug") or "" for h in named if h.get("slug")]
    topical = topical_hits(text, skip_slugs=extra_skip, limit=MAX_HITS)
    mentioned = {
        (h.get("slug") or "")
        for h in (named + topical)
        if (h.get("slug") or "") in verified
    }
    known: list[dict] = []
    # Teller has the full page. Named verified this turn get a deep
    # dossier; other verified stay compact titles so the pack fits.
    known_skip = set(skip)
    for slug in verified_slugs():
        if slug in known_skip:
            continue
        deep = slug in mentioned
        maxc = MAX_DOSSIER if deep else 420
        card = dossier(slug=slug, kind="person", max_chars=maxc)
        if not card.get("hit"):
            continue
        known.append(
            {
                "hit": True,
                "slug": card["slug"],
                "kind": "person",
                "title": card.get("title") or slug,
                "url": card.get("url") or "",
                "one_liner": (card.get("one_liner") or "")[:MAX_HIT],
                "dossier": (card.get("dossier") or "")[:maxc] if deep else "",
                "related": card.get("related") or [],
            }
        )
        known_skip.add(slug)
    hit_list = [
        h
        for h in (named + topical)
        if (h.get("slug") or "") not in verified
    ][:MAX_HITS]
    for i, h in enumerate(hit_list):
        if i >= 2 and h.get("dossier"):
            h = dict(h)
            h["dossier"] = ""
            hit_list[i] = h
    hop_skip = set(known_skip)
    for h in hit_list:
        if h.get("slug"):
            hop_skip.add(h["slug"])
    sources = []
    if teller.get("hit"):
        sources.append(teller)
    sources.extend(known)
    hops = _collect_hops(sources, hop_skip)
    return {
        "vault": {
            "people": idx.get("people") or 0,
            "orgs": idx.get("orgs") or 0,
            "events": idx.get("events") or 0,
            "sources": idx.get("sources") or 0,
        },
        "teller": teller,
        "hits": hit_list[:MAX_HITS],
        "known": known[:MAX_KNOWN],
        "hops": hops[:MAX_HOPS],
        "orgs_dir": org_directory(idx),
        "people_dir": people_directory(idx),
        "events_dir": events_directory(idx),
        "sources_dir": sources_directory(idx),
    }

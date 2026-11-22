#!/usr/bin/env python3
"""Echopedia-first answer path + gap queue.

Primary use: agent / LINE fact questions about TAHS people & orgs.
  1) Look up vault content/people|organizations (no invention)
  2) On HIT → emit short grounded answer JSON
  3) On MISS → append gap-queue entry + emit capture message

Usage:
  python3 echopedia-first-answer.py "who is Phoenix Ko"
  python3 echopedia-first-answer.py --name "Sunu Tsai"
  python3 echopedia-first-answer.py --slug phoenix-ko
  python3 echopedia-first-answer.py --text "tell me about 柯貝昀" --source line
  python3 echopedia-first-answer.py --list-gaps
  python3 echopedia-first-answer.py --resolve GAP_ID
  python3 echopedia-first-answer.py --plain   # human text only (LINE-friendly)

Exit codes: 0=hit, 2=miss (gap enqueued), 1=error
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import uuid
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path("/home/leedt/echo-system")
PEOPLE = VAULT / "content" / "people"
ORGS = VAULT / "content" / "organizations"
OPS = VAULT / "knowledge" / "operational"
GAP_QUEUE = OPS / "echopedia-gap-queue.jsonl"
GAP_STATE = OPS / "echopedia-gap-queue-state.json"
METRICS = OPS / "intelligence" / "first-answer-metrics.jsonl"
PUBLIC_BASE = "https://echopedia.tah-society.org"
_COMPACT = False  # set by main --compact

STOP = {
    "who", "what", "is", "are", "the", "a", "an", "about", "tell", "me", "info",
    "on", "of", "for", "please", "誰", "是", "什麼", "介紹", "一下", "嗎", "呢",
    "do", "you", "know", "anything", "someone", "person", "named", "called",
}

# Ops / infra questions must never become vault HITs or gap-queue NEED YOU.
_OPS_QUERY = re.compile(
    r"(?i)^\s*go\b|"
    r"\b(check\s+logs?|status|oauth|gateway|restart|config\.ya?ml|"
    r"vllm|laguna|system docs|review system|kanban|cron|llm model)\b|"
    r"https?://|grokipedia\.com"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s


def extract_query_name(text: str) -> str:
    t = text.strip()
    # strip common question wrappers
    t = re.sub(
        r"^(who\s+is|who'?s|what\s+is|tell\s+me\s+about|info\s+on|about)\s+",
        "",
        t,
        flags=re.I,
    )
    t = t.strip(" ??.。！!")
    return t.strip() or text.strip()


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict = {}
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip().strip('"').strip("'")
        meta[k] = v
    return meta, parts[2]


def page_role_line(body: str, meta: dict) -> str:
    # Prefer explicit role bullets
    for pat in [
        r"\*\*Core role[^*]*\*\*:\s*(.+)",
        r"-\s*\*\*Title:\*\*\s*(.+)",
        r"-\s*\*\*Core role[^*]*\*\*:\s*(.+)",
        r"serves as \*\*([^*]+)\*\*",
    ]:
        m = re.search(pat, body, re.I)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()[:200]
    if meta.get("source_note"):
        return meta["source_note"][:200]
    # first non-empty paragraph after H1
    lines = []
    after_h1 = False
    for line in body.splitlines():
        if line.startswith("# "):
            after_h1 = True
            continue
        if after_h1:
            if line.startswith("#"):
                break
            if line.strip():
                lines.append(line.strip())
            elif lines:
                break
    if lines:
        return re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", " ".join(lines))[:240]
    return ""


def load_name_index() -> list[dict]:
    """Build lightweight index of people + orgs."""
    idx = []
    for folder, kind in ((PEOPLE, "person"), (ORGS, "organization")):
        if not folder.is_dir():
            continue
        for path in folder.glob("*.md"):
            if path.name in {"index.md"}:
                continue
            try:
                raw = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta, body = parse_frontmatter(raw)
            if meta.get("verification_status") == "redirect" or meta.get("redirect_to"):
                # still index redirect target name lightly
                pass
            title = meta.get("title") or path.stem
            en = meta.get("name_en") or ""
            zh = meta.get("name_zh_hanzi") or meta.get("name_zh") or ""
            # pull 2–4 Hanzi from title if name_zh missing (e.g. "Hsu Ling-yun (許凌雲)")
            if not zh:
                mzh = re.search(r"[\u4e00-\u9fff]{2,4}", title)
                if mzh:
                    zh = mzh.group(0)
            aliases = {path.stem, slugify(path.stem)}
            for a in (title, en, zh):
                if a:
                    aliases.add(a.strip())
                    aliases.add(slugify(a))
            # aka:/aliases: frontmatter LISTS are dropped by the simple key:value
            # parser — index their items (2026-10-24: 沈伯洋's "Puma Shen /
            # Shen Pao-yang" aka list was invisible, so romanized queries lost
            # to same-surname pages).
            if raw.startswith("---"):
                fm = raw.split("---", 2)[1]
                for key in ("aka", "aliases", "alias"):
                    blk = re.search(
                        rf"^{key}:\s*\n((?:[ \t]+-[ \t]+.+\n?)+)", fm, re.M
                    )
                    if blk:
                        for line in blk.group(1).splitlines():
                            item = line.strip().lstrip("-").strip().strip("\"'")
                            if item:
                                aliases.add(item)
                                aliases.add(slugify(item))
            # pull LINE display if present
            for m in re.finditer(r"displayName:\s*`([^`]+)`", body):
                aliases.add(m.group(1).strip())
                aliases.add(slugify(m.group(1)))
            for m in re.finditer(r"LINE display[^:]*:\s*[\"'`]([^\"'`]+)[\"'`]", body, re.I):
                aliases.add(m.group(1).strip())
            idx.append(
                {
                    "kind": kind,
                    "slug": path.stem,
                    "path": str(path),
                    "title": title,
                    "name_en": en or title,
                    "name_zh": zh,
                    "aliases": {a for a in aliases if a and a != "-"},
                    "meta": meta,
                    "body": body,
                    "raw": raw,
                }
            )
    return idx


def _word_in(needle: str, hay: str) -> bool:
    """Word-aligned containment (2026-10-24: raw substring let 'ian chen'
    match inside 'brian cheng')."""
    if not needle:
        return False
    return (
        re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", hay)
        is not None
    )


def _lev(a: str, b: str) -> int:
    """Bounded Levenshtein (early-exit when length gap already exceeds cap)."""
    if abs(len(a) - len(b)) > 4:
        return 99
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def score_match(query: str, entry: dict) -> int:
    q = query.strip()
    ql = q.lower()
    qs = slugify(q)
    score = 0
    slug = entry["slug"]
    if qs == slug or ql == slug:
        score = max(score, 100)
    if ql == (entry.get("name_en") or "").lower():
        score = max(score, 95)
    if q == entry.get("name_zh"):
        score = max(score, 95)
    for a in entry["aliases"]:
        al = a.lower()
        if ql == al or qs == slugify(a):
            score = max(score, 90)
        elif (
            (len(ql) >= 4 or bool(re.search(r"[\u4e00-\u9fff]", ql)))
            and len(al) >= 2
            and len(ql) <= 48
            and (_word_in(ql, al) or _word_in(al, ql))
        ):
            score = max(score, 60)
        elif (
            qs
            and (len(qs) >= 4 or bool(re.search(r"[\u4e00-\u9fff]", qs)))
            and qs in slugify(a)
            and len(qs) >= len(slugify(a)) - 2
        ):
            score = max(score, 50)
    # token overlap for multi-word (word-boundary, not substring — 2026-10-24:
    # substring hits let "shen bo yang" score on "bo" inside unrelated aliases)
    q_tokens = {t for t in re.split(r"[\s\-]+", ql) if len(t) > 1 and t not in STOP}
    if q_tokens:
        blob = " " + " ".join(entry["aliases"]).lower() + " "
        hit = sum(
            1
            for t in q_tokens
            if re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", blob)
        )
        if hit:
            score = max(score, 40 + 10 * hit)
        # pinyin-syllable fuzzy (2026-10-24, Grok-tightened): strip hyphens on
        # BOTH sides; cap 2 only for names >=10 chars (else 1); require one
        # shared word token — kills surname-swaps like sam hung → sam huang.
        if len(qs) >= 6 and not re.search(r"[\u4e00-\u9fff]", qs):
            qn = re.sub(r"[^a-z0-9]", "", ql)
            q_words = {w for w in re.split(r"[^a-z0-9]+", ql) if len(w) >= 3}
            for a in entry["aliases"]:
                if re.search(r"[\u4e00-\u9fff]", a):
                    continue
                an = re.sub(r"[^a-z0-9]", "", a.lower())
                if not an or abs(len(an) - len(qn)) > 4:
                    continue
                a_words = {w for w in re.split(r"[^a-z0-9]+", a.lower()) if len(w) >= 3}
                if not (q_words & a_words):
                    continue
                cap = 2 if min(len(qn), len(an)) >= 10 else 1
                if _lev(qn, an) <= cap:
                    score = max(score, 70)
                    break
    return score


def extract_facts(body: str, limit: int = 2) -> list[str]:
    """Up to N short grounded facts from snapshot/timeline/overview."""
    facts: list[str] = []
    for m in re.finditer(r"^[-*]\s+\*\*[^*]+\*\*:\s*(.+)$", body, re.M):
        fact = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(1))
        fact = re.sub(r"[`*_]", "", fact).strip()
        if 8 <= len(fact) <= 160 and fact not in facts:
            facts.append(fact)
        if len(facts) >= limit:
            return facts
    for m in re.finditer(
        r"^[-*]\s+\*\*(\d{4}[^*]*)\*\*\s*[—\-–]\s*(.+)$", body, re.M
    ):
        fact = f"{m.group(1).strip()}: " + re.sub(
            r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(2)
        )
        fact = re.sub(r"\s+", " ", fact).strip()[:160]
        # skip citation dump lines
        if any(x in fact.lower() for x in ("score ", "article:", "source article", "archive path", "publisher:")):
            continue
        if fact not in facts:
            facts.append(fact)
        if len(facts) >= limit:
            return facts
    m = re.search(r"## Overview\s*\n+(.+?)(?:\n## |\Z)", body, re.S)
    if m:
        para = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(1))
        para = re.sub(r"\s+", " ", para).strip()
        for sent in re.split(r"(?<=[。\.!?])\s+", para):
            sent = sent.strip()
            if 20 <= len(sent) <= 180 and sent not in facts:
                facts.append(sent)
            if len(facts) >= limit:
                break
    return facts[:limit]


def extract_related(body: str, limit: int = 3) -> list[str]:
    rels: list[str] = []
    section = ""
    m = re.search(r"## Related(?: Pages)?\s*\n(.*?)(?:\n## |\Z)", body, re.S | re.I)
    if m:
        section = m.group(1)
    else:
        m = re.search(r"## Network\s*\n(.*?)(?:\n## |\Z)", body, re.S | re.I)
        if m:
            section = m.group(1)
    for wm in re.finditer(r"\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]", section):
        target, label = wm.group(1).strip(), (wm.group(2) or "").strip()
        label = label or target.split("/")[-1]
        if label not in rels:
            rels.append(label)
        if len(rels) >= limit:
            break
    return rels


def public_url(kind: str, slug: str) -> str:
    folder = "people" if kind == "person" else "organizations"
    return f"{PUBLIC_BASE}/{folder}/{slug}"


def record_metric(res: dict, source: str) -> None:
    """Silent append-only metrics (no Telegram)."""
    try:
        METRICS.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "ts": utc_now(),
            "status": res.get("status"),
            "query": res.get("query"),
            "slug": res.get("slug"),
            "source": source,
            "kind": res.get("kind"),
        }
        with METRICS.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    except OSError:
        pass


def format_answer(entry: dict, compact: bool = False) -> str:
    """Card: EN/ZH · role · ≤2 facts · source URL · related."""
    meta = entry["meta"]
    body = entry["body"]
    en = entry.get("name_en") or entry["slug"]
    zh = entry.get("name_zh") or ""
    name = f"{en}" + (f" ({zh})" if zh else "")
    role = page_role_line(body, meta)
    if compact:
        bits = [name]
        if role:
            bits.append(role.rstrip("."))
        bits.append(
            "Echopedia person page." if entry["kind"] == "person" else "Echopedia org page."
        )
        text = " — ".join(bits)
        return text[:500]
    facts = extract_facts(body, 2)
    related = extract_related(body, 3)
    url = public_url(entry["kind"], entry["slug"])
    status = meta.get("verification_status") or ""
    lines = [name]
    if role:
        lines.append(role.rstrip("."))
    for fct in facts:
        fct = re.sub(r"[*_`]+", "", fct).strip()
        lines.append(f"· {fct}")
    lines.append(f"Source: {url}")
    if related:
        lines.append("Related: " + "; ".join(related))
    if status and status not in {"published", "owner_verified", "pending", ""}:
        lines.append(f"({status})")
    text = "\n".join(lines)
    if len(text) > 900:
        text = text[:897] + "..."
    return text


def append_gap(query: str, source: str, extra: dict | None = None) -> dict:
    OPS.mkdir(parents=True, exist_ok=True)
    gap = {
        "id": f"gap_{uuid.uuid4().hex[:10]}",
        "ts": utc_now(),
        "status": "open",
        "query": query,
        "source": source or "unknown",
        "kind": "echopedia_miss",
        "priority": "need_you" if source in {"line", "owner", "telegram"} else "backfill",
        "notes": "",
    }
    if extra:
        gap.update(extra)
    with GAP_QUEUE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(gap, ensure_ascii=False) + "\n")
    return gap


def list_gaps(status: str = "open") -> list[dict]:
    if not GAP_QUEUE.exists():
        return []
    out = []
    for line in GAP_QUEUE.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if status == "all" or o.get("status") == status:
            out.append(o)
    return out


def resolve_gap(gap_id: str, note: str = "") -> bool:
    if not GAP_QUEUE.exists():
        return False
    rows = []
    found = False
    for line in GAP_QUEUE.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            rows.append(line)
            continue
        if o.get("id") == gap_id and o.get("status") == "open":
            o["status"] = "resolved"
            o["resolved_at"] = utc_now()
            if note:
                o["resolve_note"] = note
            found = True
        rows.append(json.dumps(o, ensure_ascii=False))
    if found:
        GAP_QUEUE.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return found


def _brain_retrieve(name: str, query: str, source: str) -> dict | None:
    """Whole-vault title/alias retrieve. First place to look after exact miss."""
    scripts = Path("/home/leedt/echo-system/scripts")
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    try:
        from ee_vault_retrieve import search
    except Exception:
        return None
    hits = search(name) or search(query)
    if not hits:
        return None
    slug = hits[0].get("slug") or ""
    kind = hits[0].get("kind") or "person"
    folder = PEOPLE if kind == "person" else ORGS
    path = folder / f"{slug}.md"
    if not path.is_file():
        other = ORGS if folder == PEOPLE else PEOPLE
        path = other / f"{slug}.md"
    if not path.is_file():
        return None
    # Strength gate (2026-10-24, Grok-audited): only curated registry-alias
    # hits pass free. INDEX-key and SQLITE works/place hits are token evidence
    # — they must not be beaten by the scorer's best candidate, and a weak (<=60)
    # tie among many equal pages must not win (bare-surname guessing).
    if (hits[0].get("src") or "alias") in ("index", "sqlite"):
        idx = load_name_index()
        entry = next((e for e in idx if e["slug"] == path.stem), None)
        if entry is not None:
            brain_score = score_match(name, entry)
            scores = [score_match(name, e) for e in idx]
            best = max(scores, default=0)
            ties = sum(1 for s in scores if s == best)
            if best > brain_score or (brain_score <= 60 and ties > 1):
                return None
    return answer_from_path(path, query, source)


def answer(query: str, source: str = "cli", no_gap: bool = False) -> dict:
    raw_q = (query or "").strip()
    if _OPS_QUERY.search(raw_q) or len(raw_q) > 160:
        msg = "SKIP: not a person/org fact query"
        res = {
            "status": "skip",
            "query": raw_q,
            "raw_query": raw_q,
            "answer": msg,
            "source_path": None,
            "slug": None,
            "gap": None,
            "alternates": [],
        }
        return res
    name = extract_query_name(query)
    # direct slug attempt
    candidates = []
    idx = load_name_index()
    # exact path fast path
    for folder in (PEOPLE, ORGS):
        p = folder / f"{slugify(name)}.md"
        if p.exists():
            raw = p.read_text(encoding="utf-8", errors="replace")
            meta, body = parse_frontmatter(raw)
            entry = {
                "kind": "person" if folder == PEOPLE else "organization",
                "slug": p.stem,
                "path": str(p),
                "title": meta.get("title") or p.stem,
                "name_en": meta.get("name_en") or p.stem,
                "name_zh": meta.get("name_zh_hanzi") or "",
                "aliases": set(),
                "meta": meta,
                "body": body,
                "raw": raw,
            }
            # follow redirect
            if meta.get("redirect_to"):
                tgt = PEOPLE / f"{meta['redirect_to']}.md"
                if not tgt.exists():
                    tgt = ORGS / f"{meta['redirect_to']}.md"
                if tgt.exists():
                    return answer_from_path(tgt, query, source)
            return hit_result(entry, query, source)

    # 2nd brain: alias/title retrieve beats fuzzy name-index
    # (GSTPC must hit the church, not Brother Ku).
    brain = _brain_retrieve(name, query, source)
    if brain is not None:
        return brain

    for e in idx:
        sc = score_match(name, e)
        if sc >= 50:
            candidates.append((sc, e))
    candidates.sort(key=lambda x: -x[0])
    if candidates and candidates[0][0] >= 60:
        top = candidates[0][0]
        q_tok_count = len([t for t in re.split(r"[\s\-]+", name.lower()) if len(t) > 1])
        ambiguous = q_tok_count == 1 and sum(1 for sc, _ in candidates if sc == top) > 1
        if not ambiguous:
            entry = candidates[0][1]
            # follow redirect pages
            if entry["meta"].get("redirect_to"):
                tgt = PEOPLE / f"{entry['meta']['redirect_to']}.md"
                if not tgt.exists():
                    tgt = ORGS / f"{entry['meta']['redirect_to']}.md"
                if tgt.exists():
                    return answer_from_path(tgt, query, source)
            return hit_result(entry, query, source)
        # bare surname with many equal pages — miss+gap, never guess one

    # MISS
    gap = None if no_gap else append_gap(query=name, source=source, extra={"raw_query": query})
    msg = (
        f"I don’t have a solid Echopedia page for “{name}” yet — noted for the archive."
        if source in {"line", "telegram"}
        else f"MISS: no Echopedia hit for “{name}” (gap enqueued)."
    )
    res = {
        "status": "miss",
        "query": name,
        "raw_query": query,
        "answer": msg,
        "source_path": None,
        "slug": None,
        "gap": gap,
        "alternates": [
            {"slug": e["slug"], "score": sc, "title": e["title"]}
            for sc, e in candidates[:5]
        ],
    }
    record_metric(res, source)
    return res


def answer_from_path(path: Path, query: str, source: str) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(raw)
    # Brain hits land here and used to stop on the stub. Follow one hop.
    redir = (meta.get("redirect_to") or "").strip().strip("\"'")
    redir = redir.removeprefix("people/").removeprefix("organizations/")
    if redir:
        tgt = PEOPLE / f"{redir}.md"
        if not tgt.is_file():
            tgt = ORGS / f"{redir}.md"
        if tgt.is_file() and tgt.resolve() != path.resolve():
            return answer_from_path(tgt, query, source)
    entry = {
        "kind": "person" if "/people/" in str(path) else "organization",
        "slug": path.stem,
        "path": str(path),
        "title": meta.get("title") or path.stem,
        "name_en": meta.get("name_en") or path.stem,
        "name_zh": meta.get("name_zh_hanzi") or "",
        "aliases": set(),
        "meta": meta,
        "body": body,
        "raw": raw,
    }
    return hit_result(entry, query, source)


def hit_result(entry: dict, query: str, source: str, compact: bool | None = None) -> dict:
    body = entry["body"]
    res = {
        "status": "hit",
        "query": extract_query_name(query),
        "raw_query": query,
        "answer": format_answer(entry, compact=_COMPACT if compact is None else compact),
        "source_path": entry["path"],
        "slug": entry["slug"],
        "kind": entry["kind"],
        "name_en": entry.get("name_en"),
        "name_zh": entry.get("name_zh"),
        "role": page_role_line(body, entry["meta"]),
        "facts": extract_facts(body, 2),
        "related": extract_related(body, 3),
        "url": public_url(entry["kind"], entry["slug"]),
        "gap": None,
    }
    record_metric(res, source)
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Echopedia-first answer + gap queue")
    ap.add_argument("query", nargs="?", help="Natural language or name")
    ap.add_argument("--name", help="Explicit name")
    ap.add_argument("--slug", help="Explicit slug")
    ap.add_argument("--text", help="Alias of query")
    ap.add_argument("--source", default="cli", help="line|telegram|cli|owner|cron")
    ap.add_argument("--plain", action="store_true", help="Print answer card text only")
    ap.add_argument("--compact", action="store_true", help="One-line answer (legacy)")
    ap.add_argument("--no-gap", action="store_true", help="Do not enqueue on miss")
    ap.add_argument("--list-gaps", action="store_true")
    ap.add_argument("--resolve", metavar="GAP_ID")
    ap.add_argument("--resolve-note", default="")
    args = ap.parse_args(argv)
    global _COMPACT
    _COMPACT = bool(getattr(args, "compact", False))

    if args.list_gaps:
        gaps = list_gaps("open")
        if args.plain:
            if not gaps:
                print("No open gaps.")
            for g in gaps[-50:]:
                print(f"{g.get('id')}\t{g.get('ts')}\t{g.get('query')}\t{g.get('source')}")
        else:
            print(json.dumps({"open": len(gaps), "gaps": gaps[-50:]}, ensure_ascii=False, indent=2))
        return 0

    if args.resolve:
        ok = resolve_gap(args.resolve, args.resolve_note)
        print(json.dumps({"resolved": ok, "id": args.resolve}))
        return 0 if ok else 1

    if args.slug:
        for folder in (PEOPLE, ORGS):
            p = folder / f"{args.slug}.md"
            if p.exists():
                res = answer_from_path(p, args.slug, args.source)
                if args.plain:
                    print(res["answer"])
                else:
                    print(json.dumps(res, ensure_ascii=False, indent=2))
                return 0
        res = answer(args.slug, source=args.source, no_gap=args.no_gap)
    else:
        q = args.name or args.text or args.query
        if not q:
            ap.error("query/name/text/slug required")
        res = answer(q, source=args.source, no_gap=args.no_gap)

    if args.plain:
        print(res["answer"])
    else:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    if res["status"] == "hit":
        return 0
    if res["status"] == "skip":
        return 3
    return 2


if __name__ == "__main__":
    sys.exit(main())

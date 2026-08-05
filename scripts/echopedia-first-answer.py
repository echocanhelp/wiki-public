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

STOP = {
    "who", "what", "is", "are", "the", "a", "an", "about", "tell", "me", "info",
    "on", "of", "for", "please", "誰", "是", "什麼", "介紹", "一下", "嗎", "呢",
    "do", "you", "know", "anything", "someone", "person", "named", "called",
}


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
            aliases = {path.stem, slugify(path.stem)}
            for a in (title, en, zh):
                if a:
                    aliases.add(a.strip())
                    aliases.add(slugify(a))
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
        elif len(ql) >= 2 and (ql in al or al in ql):
            score = max(score, 60)
        elif qs and qs in slugify(a):
            score = max(score, 50)
    # token overlap for multi-word
    q_tokens = {t for t in re.split(r"[\s\-]+", ql) if len(t) > 1 and t not in STOP}
    if q_tokens:
        blob = " ".join(entry["aliases"]).lower()
        hit = sum(1 for t in q_tokens if t in blob)
        if hit:
            score = max(score, 40 + 10 * hit)
    return score


def format_answer(entry: dict) -> str:
    meta = entry["meta"]
    body = entry["body"]
    en = entry.get("name_en") or entry["slug"]
    zh = entry.get("name_zh") or ""
    name = f"{en}" + (f" / {zh}" if zh else "")
    role = page_role_line(body, meta)
    kind = entry["kind"]
    status = meta.get("verification_status") or ""
    bits = [name]
    if role:
        bits.append(role.rstrip("."))
    if kind == "organization":
        bits.append("Echopedia org page.")
    else:
        bits.append("Echopedia person page.")
    if status and status not in {"published", "owner_verified", ""}:
        bits.append(f"(status: {status})")
    # LINE soft length
    text = " — ".join(bits)
    if len(text) > 500:
        text = text[:497] + "..."
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


def answer(query: str, source: str = "cli", no_gap: bool = False) -> dict:
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

    for e in idx:
        sc = score_match(name, e)
        if sc >= 50:
            candidates.append((sc, e))
    candidates.sort(key=lambda x: -x[0])
    if candidates and candidates[0][0] >= 60:
        entry = candidates[0][1]
        # follow redirect pages
        if entry["meta"].get("redirect_to"):
            tgt = PEOPLE / f"{entry['meta']['redirect_to']}.md"
            if not tgt.exists():
                tgt = ORGS / f"{entry['meta']['redirect_to']}.md"
            if tgt.exists():
                return answer_from_path(tgt, query, source)
        return hit_result(entry, query, source)

    # MISS
    gap = None if no_gap else append_gap(query=name, source=source, extra={"raw_query": query})
    msg = (
        f"I don’t have a solid Echopedia page for “{name}” yet — noted for the archive."
        if source in {"line", "telegram"}
        else f"MISS: no Echopedia hit for “{name}” (gap enqueued)."
    )
    return {
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


def answer_from_path(path: Path, query: str, source: str) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(raw)
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


def hit_result(entry: dict, query: str, source: str) -> dict:
    return {
        "status": "hit",
        "query": extract_query_name(query),
        "raw_query": query,
        "answer": format_answer(entry),
        "source_path": entry["path"],
        "slug": entry["slug"],
        "kind": entry["kind"],
        "name_en": entry.get("name_en"),
        "name_zh": entry.get("name_zh"),
        "gap": None,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Echopedia-first answer + gap queue")
    ap.add_argument("query", nargs="?", help="Natural language or name")
    ap.add_argument("--name", help="Explicit name")
    ap.add_argument("--slug", help="Explicit slug")
    ap.add_argument("--text", help="Alias of query")
    ap.add_argument("--source", default="cli", help="line|telegram|cli|owner|cron")
    ap.add_argument("--plain", action="store_true", help="Print answer text only")
    ap.add_argument("--no-gap", action="store_true", help="Do not enqueue on miss")
    ap.add_argument("--list-gaps", action="store_true")
    ap.add_argument("--resolve", metavar="GAP_ID")
    ap.add_argument("--resolve-note", default="")
    args = ap.parse_args(argv)

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
    return 0 if res["status"] == "hit" else 2


if __name__ == "__main__":
    sys.exit(main())

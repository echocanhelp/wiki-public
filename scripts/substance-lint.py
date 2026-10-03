#!/usr/bin/env python3
"""Tier floors for content/people and content/organizations.

Missing `tier:` is treated as M and listed as BACKFILL (not itself a failure).
An anchored fact is a line with a date, number, or quote AND a source marker
(URL, archive path, wikilink, or `per <source>` — filler-check anchor style).
A sourced Source Notes section also anchors dated lines elsewhere on the page,
because these dossiers keep provenance there. hits-hash stamps do not count.

Floors (echopedia-ingestion-protocol, Tiered Expansion):
  M  >=3 anchored facts and >=1 internal wikilink
  1  >=2 anchored facts, >=1 internal wikilink, and a why-linked line
  2  must set publish: false

Online arms: if the page has `## Online arms`, or an open kanban card baked
that section for this path, Tier M needs all 4 arms accounted and Tier 1
needs one. Accounted = absorb, HOLD, or `searched <query>, <date>`.

Exit 1 on a floor / arms / tier-2 publish violation. --publish-gate always
exits 0 and writes an rsync exclude list. Nightly publish must not drop a legacy corpus that never got `tier:` keys.
When floor failures exceed 50, the exclude list keeps only `publish: false`
unless --enforce-floor is set. --dry-run prints every would-skip either way.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

FACT = re.compile(
    r"\b(?:1[89]\d{2}|20\d{2})\b"
    r"|\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{1,2}\b"
    r"|\$\s?\d"
    r"|\b\d{1,3}(?:,\d{3})+\b"
    r"|\b\d+(?:\.\d+)?\s?(?:%|acres?|年)\b"
    r"|[\"“”「」『』]",
    re.I,
)
SOURCE = re.compile(
    r"https?://|\[\[(?!https?://)|works/|knowledge/|web-archives/"
    r"|\.md:\d+|#\d{1,4}\b|[Ss]ource[: ]|TAH #|Our Journeys|公報|記載於|記載:"
    r"|\bper\s+\S"
    r"|\b(?:LA Times|World Journal|China Times|Epoch Times|Daily News|"
    r"Orange County Business Journal|OCBJ|世界日報|世界新闻网|大紀元|台灣日報|華人今日)\b"
    r"|\b(?:own words|bylined|documented|official site|self-sourced|according to)\b",
    re.I,
)
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
WHY = re.compile(r"why[- ]linked", re.I)
ARM_PATTERNS = (
    re.compile(r"wikipedia|維基|zh-wp|zh\.wikipedia", re.I),
    re.compile(r"wikidata", re.I),
    re.compile(r"official site|官網", re.I),
    re.compile(r"world journal|大紀元|台灣日報|epoch times|zh press|華文", re.I),
)
ACCOUNT = re.compile(r"\babsorb\b|\bHOLD\b|searched\s+.+?,\s*\d{4}", re.I)
HOLD_FLOOR_ABS = 50

DOSSIER = ("people", "organizations")


def parse_frontmatter(text: str) -> tuple[str, bool | None, bool, str]:
    """Return tier, publish (None if unset), tier_explicit, body."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "M", None, False, text
    fm, body = m.group(1), text[m.end():]
    mt = re.search(r"^tier:\s*[\"']?([Mm12])[\"']?\s*$", fm, re.M)
    mp = re.search(r"^publish:\s*[\"']?(true|false)[\"']?\s*$", fm, re.M | re.I)
    tier = mt.group(1).upper() if mt else "M"
    publish = None if not mp else mp.group(1).lower() == "true"
    return tier, publish, bool(mt), body


def internal_links(body: str) -> int:
    n = 0
    for m in WIKILINK.finditer(body):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://")):
            continue
        n += 1
    return n


def anchored_facts(body: str) -> int:
    """Date/number/quote line plus a source marker on that line, or a dated
    line whose page carries a sourced Source Notes section (these dossiers
    put provenance in that section, not on every bullet)."""
    section = ""
    sourced_notes = False
    fact_lines: list[tuple[str, bool]] = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*)", line)
        if m:
            section = m.group(1).strip().lower()
            continue
        s = line.strip()
        if not s or s.startswith("#") or "hits-hash=" in s:
            continue
        has_src = bool(SOURCE.search(s))
        if "source note" in section and has_src:
            sourced_notes = True
        if FACT.search(s):
            fact_lines.append((section, has_src))
    n = 0
    for sec, has_src in fact_lines:
        if sec in ("related pages", "online arms", "skipped"):
            continue
        if has_src or sourced_notes:
            n += 1
    return n


def online_arms_section(body: str) -> str | None:
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+Online arms\s*$", line, re.I):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^##\s+[^#]", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def arms_accounted(section: str) -> int:
    if not section:
        return 0
    n = 0
    for pat in ARM_PATTERNS:
        m = pat.search(section)
        if not m:
            continue
        window = section[m.start(): m.start() + 400]
        if ACCOUNT.search(window):
            n += 1
    return n


def lint_text(rel: str, text: str, *, armed: bool = False) -> list[str]:
    tier, publish, explicit, body = parse_frontmatter(text)
    out: list[str] = []
    if not explicit:
        out.append(f"BACKFILL: {rel} missing tier (treated as M)")
    facts = anchored_facts(body)
    links = internal_links(body)
    if tier == "2":
        if publish is not False:
            out.append(f"TIER2_PUBLISH: {rel} tier 2 without publish: false")
        return out
    need = 3 if tier == "M" else 2
    if facts < need or links < 1:
        out.append(
            f"FLOOR: {rel} tier={tier} anchored={facts} need={need} links={links}"
        )
    if tier == "1" and not WHY.search(body):
        out.append(f"WHY: {rel} tier=1 missing why-linked line")
    section = online_arms_section(body)
    if section is not None or armed:
        got = arms_accounted(section or "")
        need_arms = 4 if tier == "M" else 1
        if got < need_arms:
            out.append(
                f"ONLINE_ARMS_UNACCOUNTED: {rel} tier={tier} accounted={got}/{need_arms}"
            )
    return out


def is_violation(line: str) -> bool:
    return not line.startswith("BACKFILL:")


def iter_pages(root: Path):
    for kind in DOSSIER:
        d = root / kind
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            if p.name == "index.md":
                continue
            yield p


def armed_paths(db: Path | None) -> set[str]:
    path = db if db is not None else Path.home() / ".hermes" / "kanban.db"
    if not path.is_file():
        return set()
    try:
        con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        rows = con.execute(
            "select body from tasks where status not in ('done','archived') "
            "and body like '%## Online arms%'"
        ).fetchall()
        con.close()
    except sqlite3.Error:
        return set()
    found: set[str] = set()
    for (body,) in rows:
        for m in re.findall(
            r"(?:people|organizations)/[A-Za-z0-9][A-Za-z0-9._-]*", body or ""
        ):
            found.add(m)
            found.add(m + ".md")
    return found


def page_armed(rel: str, armed: set[str]) -> bool:
    stem = rel[:-3] if rel.endswith(".md") else rel
    return rel in armed or stem in armed


def collect(root: Path, files: list[Path] | None, db: Path | None):
    armed = armed_paths(db)
    pages = files if files is not None else list(iter_pages(root))
    rows: list[tuple[str, list[str]]] = []
    for p in pages:
        try:
            rel = str(p.relative_to(root)) if root in p.parents or p.parent == root else p.name
        except ValueError:
            rel = str(p)
        # Prefer content-relative when the file lives under root.
        try:
            rel = str(p.resolve().relative_to(root.resolve()))
        except ValueError:
            pass
        text = p.read_text(encoding="utf-8", errors="replace")
        rows.append((rel, lint_text(rel, text, armed=page_armed(rel, armed))))
    return rows


def gate_decision(rows, enforce: bool) -> tuple[list[str], str]:
    """Return rsync exclude paths and a one-line PUBLISH_GATE summary."""
    publish_false: list[str] = []
    floor_fail: list[str] = []
    dossier = 0
    for rel, lines in rows:
        if rel.startswith(DOSSIER):
            dossier += 1
        bad = [ln for ln in lines if is_violation(ln)]
        tier2 = any(ln.startswith("TIER2_PUBLISH:") for ln in bad)
        # publish:false is not a lint violation; detect from the absence of
        # TIER2 when tier is 2, and from a marker we add in scan_gate.
        if any(ln.startswith("SKIP_PUBLISH_FALSE:") for ln in lines):
            publish_false.append(rel)
        elif bad or tier2:
            floor_fail.append(rel)
    hold = not enforce and len(floor_fail) > HOLD_FLOOR_ABS
    exclude = list(publish_false)
    if not hold:
        exclude.extend(floor_fail)
    mode = "HOLD" if hold else "yes"
    summary = (
        f"PUBLISH_GATE: would-skip={len(publish_false) + len(floor_fail)} "
        f"publish_false={len(publish_false)} floor_fail={len(floor_fail)} "
        f"dossier={dossier} enforced={mode}"
    )
    return exclude, summary


def annotate_publish_false(root: Path, rows):
    """Tag pages whose frontmatter sets publish: false (gate skips them)."""
    out = []
    for rel, lines in rows:
        p = root / rel
        publish = None
        if p.is_file():
            text = p.read_text(encoding="utf-8", errors="replace")
            _, publish, _, _ = parse_frontmatter(text)
        if publish is False:
            lines = list(lines) + [f"SKIP_PUBLISH_FALSE: {rel}"]
        out.append((rel, lines))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content-dir", default=str(Path.home() / "echo-system" / "content"))
    ap.add_argument("--file", action="append", default=[], help="per-file mode; repeatable")
    ap.add_argument("--alert", action="store_true", help="summary + cache report for cron")
    ap.add_argument("--publish-gate", action="store_true")
    ap.add_argument("--enforce-floor", action="store_true")
    ap.add_argument("--exclude-file", default="")
    ap.add_argument("--kanban-db", default="")
    ap.add_argument("--report", default=str(Path.home() / ".hermes/cache/substance-lint-last.txt"))
    args = ap.parse_args(argv)
    root = Path(args.content_dir)
    files = [Path(f) if Path(f).is_absolute() else root / f for f in args.file] or None
    db = Path(args.kanban_db) if args.kanban_db else None
    rows = collect(root, files, db)
    if args.publish_gate:
        rows = annotate_publish_false(root, rows)
        exclude, summary = gate_decision(rows, args.enforce_floor)
        for rel, lines in rows:
            if any(ln.startswith("SKIP_PUBLISH_FALSE:") for ln in lines):
                print(f"would-skip: {rel} publish:false")
            elif any(is_violation(ln) for ln in lines):
                print(f"would-skip: {rel} floor")
        print(summary)
        if "enforced=HOLD" in summary:
            print(
                "PUBLISH_GATE: HOLD floor skips (legacy pages have no tier:). "
                "Pass --enforce-floor to drop them. publish:false still skipped."
            )
        if args.exclude_file:
            dest = Path(args.exclude_file)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text("".join(f"{rel}\n" for rel in exclude))
        return 0
    violations = [(rel, ln) for rel, lines in rows for ln in lines if is_violation(ln)]
    backfill = [ln for _, lines in rows for ln in lines if ln.startswith("BACKFILL:")]
    if args.alert:
        report = Path(args.report)
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(
            "".join(f"{ln}\n" for _, lines in rows for ln in lines if is_violation(ln))
        )
        from collections import Counter
        codes = Counter(ln.split(":", 1)[0] for _, ln in violations)
        print(
            f"substance-lint: violations={len(violations)} backfill={len(backfill)} "
            f"pages={len(rows)} codes={dict(codes)}"
        )
        for _, ln in violations[:40]:
            print(ln)
        if len(violations) > 40:
            print(f"... {len(violations) - 40} more in {report}")
        return 1 if violations else 0
    for _, lines in rows:
        for ln in lines:
            print(ln)
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""story-pass-build.py — mint STORY-PASS cards (2026-10-15).

Eligible: person pages WITHOUT ## Story that have enough sourced material to
write 3-8 sentences without inventing (>=5 dated lines, or >=3 dates + a
quote candidate). Ranked by material count x traffic weight. The worker
writes the Story from the page's own record only and MUST pass
scripts/story-verify.py before committing — the gate is the contract.
The card body calls the verifier by absolute path: the worker cwd is its
scratch workspace, so a repo-relative `scripts/story-verify.py` dies on the
first call and burns the iteration budget.

Usage: STORY_DRY=1 python3 scripts/story-pass-build.py   (plan only)
       python3 scripts/story-pass-build.py               (mint cards)
"""
import glob
import json
import os
import re
import sqlite3
import subprocess
from datetime import date
from pathlib import Path

# SWARM-GUARD-1 (t_0cb42501): fail-closed backlog gate before every create.
import sys
sys.path.insert(0, os.path.expanduser("~/.hermes/scripts"))
from mint_guard import gated_once, budget_args  # noqa: E402
from mint_gate import ensure_close_contract  # noqa: E402  OPS-FIX t_a802c5f8

REPO = Path(__file__).resolve().parents[1]
DATE_RE = re.compile(r"\b(19[4-9]\d|20[0-2]\d)\b")
NCARDS = int(os.environ.get("STORY_NCARDS", "3"))


def traffic_weights():
    p = REPO / "knowledge" / "research" / "gc-path-counts.json"
    if not p.exists():
        return {}
    try:
        d = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    from datetime import timedelta
    if (date.today() - date.fromisoformat(d.get("scraped", "2000-01-01"))
            > timedelta(days=7)):
        return {}
    per = {}
    for path, n in d.get("counts", {}).items():
        seg = path.strip("/").split("/")
        if len(seg) >= 2 and seg[0] == "wiki-public":
            per[seg[-1].removesuffix(".html")] = per.get(seg[-1].removesuffix(".html"), 0) + n
    if not per:
        return {}
    mx = max(per.values())
    return {k: v / mx for k, v in per.items()}


def material(text):
    """(dated_lines, quote_candidates) available to the writer."""
    dated = len(set(DATE_RE.findall(text)))
    rec = re.search(r"^## From the record\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    lines = len([l for l in (rec.group(1).splitlines() if rec else [])
                 if re.match(r"\s*-?\s*\|?\s*\*{0,2}(19|20)\d\d", l)]) if rec else 0
    return dated, lines


def quote_candidates(slug):
    p = REPO / "knowledge" / "research" / "quote-candidates.jsonl"
    n = 0
    if p.exists():
        for line in p.read_text(errors="ignore").splitlines():
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("slug") == slug:
                n += 1
    return n


def open_story_slugs():
    con = sqlite3.connect(str(Path.home() / ".hermes" / "kanban.db"))
    try:
        rows = con.execute(
            "select body from tasks where status not in ('done','archived') "
            "and title like 'STORY-PASS%'").fetchall()
        out = set()
        for (b,) in rows:
            m = re.search(r"content/people/([\w.-]+)\.md", b)
            if m:
                out.add(m.group(1))
        return out
    finally:
        con.close()


def main():
    dry = os.environ.get("STORY_DRY") == "1"
    weights = traffic_weights()
    claimed = open_story_slugs()
    rows = []
    for f in glob.glob(str(REPO / "content" / "people" / "*.md")):
        text = Path(f).read_text(errors="ignore")
        if len(text) < 300 or re.search(r"^## Story\s*$", text, re.M):
            continue
        slug = Path(f).stem
        if slug in claimed:
            continue
        dated, lines = material(text)
        qc = quote_candidates(slug)
        if not (dated >= 5 or (dated >= 3 and qc > 0)):
            continue
        score = (dated + lines + qc) * (1 + 3 * weights.get(slug, 0.0))
        rows.append((-score, rel := os.path.relpath(f, REPO), dated, lines, qc))
    rows.sort()
    top = rows[:NCARDS]
    if dry:
        print(f"dry: eligible={len(rows)} planned={len(top)}")
        for i, (_s, rel, d, l, q) in enumerate(top, 1):
            print(f"  card {i}: {rel} dates={d} record_lines={l} quote_cands={q}")
        return
    stamp = subprocess.run(["date", "+%m%d%H%M"], capture_output=True, text=True).stdout.strip()
    made = 0
    for i, (_s, rel, d, l, q) in enumerate(top, 1):
        slug = Path(rel).stem
        body = f"""STORY-PASS {i} — write ## Story for {rel}

Material on this page: {d} distinct years, {l} dated record lines, {q} quote candidates
(knowledge/research/quote-candidates.jsonl, grep the slug).

Rules:
1. Write 3-8 sentences of life-arc narrative. Facts ONLY from this page's own
   record / Identity / Education / Employment / Family / Quotes sections.
2. No new facts, no web search, no invented biography. A sentence you cannot
   trace to a line on the page does not go in.
3. Before committing, run: python3 {REPO / "scripts" / "story-verify.py"} {REPO / rel}
   It must print "passed": true. Fix or cut sentences until it does.
   Do not use a repo-relative path — your cwd is not the repo.
4. git -C {REPO} add -- {rel} && git -C {REPO} commit; kanban_complete.
"""
        body, _cc = ensure_close_contract(body)  # OPS-FIX t_a802c5f8: born-with-contract
        bodyfile = f"/tmp/story-pass-body-{slug}.md"
        Path(bodyfile).write_text(body)
        if not gated_once("story-pass-build", key=f"story-pass:{slug}"):  # SWARM-GUARD-1
            print("BACKLOG|SKIP", slug)
            continue
        r = subprocess.run(["hermes", "kanban", "create",
                            f"STORY-PASS {stamp}-{i} {slug}",
                            "--body-file", bodyfile,
                            "--assignee", "pinto",
                            "--max-runtime", "2400",
                            *budget_args("STORY-PASS")],  # SWARM-GUARD-3 t_418565a8: was NULL -> silent 30/30 deaths
                           capture_output=True, text=True)
        if r.returncode == 0:
            made += 1
            print(f"created: STORY-PASS {stamp}-{i} {slug}")
        else:
            print(f"card-failed: {slug}: {r.stderr[:100]}")
    print(f"story-pass: {made} cards")


if __name__ == "__main__":
    main()

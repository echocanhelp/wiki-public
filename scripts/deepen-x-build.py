#!/usr/bin/env python3
"""Build DEEPEN-X cards for thin pages that still have real reader demand.

Ranking is INBOUND WIKILINK DEMAND, not file size (2026-10-05 rewrite). The old
builder ranked `size * (1 + 3*visits)` off a GoatCounter cache that only ever
held ~10 paths / 29 visits, so the score collapsed to `size` and the same top-N
pages got re-sliced every tick — one page was sliced 846 times. Inbound links
survive that dead cache and are a real demand signal.

Dedupe keys on the PAGE PATHS a card would touch, never on the card title: a
title stamped with `date +%m%d%H%M` cannot dedupe against itself across ticks.

Already-saturated pages (they carry a hits-hash / verified-saturation stamp) are
excluded — re-grepping an unchanged corpus is SKIP work, not progress.

Env overrides:
  DEEPEN_SLICE   pages per card      (default 1)
  DEEPEN_NCARDS  max cards per run   (default 32)
  DEEPEN_DRY     set to 1 to print the plan without writing anything
"""
import glob
import json
import os
import re
import sqlite3
import subprocess
from collections import Counter
from pathlib import Path

REPO = Path('/home/leedt/echo-system')
OUT = REPO / 'knowledge/operational'
# 1 page per card -- same rationale as tjj-card-build.py: 4-item cards land in the
# p90 run-duration tail and exhaust agent.max_turns=30. Override with DEEPEN_SLICE=2
# if per-claim dispatch overhead ever shows up.
SLICE = int(os.environ.get('DEEPEN_SLICE', '1'))
NCARDS = int(os.environ.get('DEEPEN_NCARDS', '32'))
DRY = os.environ.get('DEEPEN_DRY') == '1'

# A page is "thin" by the historical rule; keep it so the queue stays comparable.
THIN_BYTES = 5000

# --- 1. demand vs material ---------------------------------------------------
# Two signals, from ONE pass. Value audit (2026-10-05) found 89% of queued pages
# had ZERO absorbable corpus material: "thin by byte count" is not work, it's a
# SKIP waiting to happen. So rank on BOTH:
#   MENTIONS = corpus pages (works/articles/sources/events/topics) that reference
#            the entity -> proof there is something to absorb. This is the GATE.
#   INLINKS  = every page that links to it -> reader demand, the tie-break.
# A page with high inlinks and no mentions is a well-known name we simply have
# no primary material on; deepening it invents biography, which the mission forbids.
CORPUS_DIRS = ('works', 'articles', 'sources', 'events', 'topics')


def demand_counts():
    """Returns (corpus_mentions, site_inlinks) Counters keyed by entity slug."""
    mentions = Counter()
    inlinks = Counter()
    content_root = REPO / 'content'
    for f in glob.glob(str(content_root / '**/*.md'), recursive=True):
        try:
            text = Path(f).read_text(errors='replace')
        except OSError:
            continue
        rel_parts = Path(f).relative_to(content_root).parts
        # corpus = the primary material, not the entity pages being deepened
        is_corpus = bool(rel_parts) and rel_parts[0] in CORPUS_DIRS
        for kind in ('people', 'organizations'):
            for m in re.finditer(r'\[\[' + kind + r'/([^|#]+)', text):
                slug = m.group(1).strip().removesuffix('.md')
                if Path(f).stem == slug:
                    continue
                inlinks[slug] += 1
                if is_corpus:
                    mentions[slug] += 1
    return mentions, inlinks


SATURATED_RE = re.compile(r'(hits.?hash|verified.?saturation|SATURATION)', re.I)


def thin_pages(mentions, inlinks):
    """Returns (value-ranked thin pages, saturated_skipped, no_material_skipped)."""
    rows = []
    saturated = 0
    no_material = 0
    for pat in ('content/people/*.md', 'content/organizations/*.md'):
        for f in glob.glob(str(REPO / pat)):
            size = os.path.getsize(f)
            if size >= THIN_BYTES:
                continue
            rel = os.path.relpath(f, REPO / 'content')
            slug = Path(f).stem
            text = Path(f).read_text(errors='replace')
            if SATURATED_RE.search(text):
                saturated += 1  # verified-saturated: re-grep is SKIP work, not progress
                continue
            mat = mentions.get(slug, 0)
            if mat == 0:
                no_material += 1  # thin by byte count only; deepening = invented bio
                continue
            # material first (can we do the work?), demand next, size as tie-break
            rows.append((-mat, -inlinks.get(slug, 0), -size, rel))
    rows.sort()
    return [rel for _m, _d, _s, rel in rows], saturated, no_material


# --- 2. dedupe on PAGE PATHS held by open cards ------------------------------
def open_card_paths():
    con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
    try:
        bodies = con.execute(
            "select body from tasks "
            "where status not in ('done','archived') and title like 'DEEPEN%'"
        ).fetchall()
    finally:
        con.close()
    paths = set()
    for (body,) in bodies:
        for m in re.finditer(r'deepen-x-slice(-\d+)?-(\d+)\.txt', body or ''):
            sp = OUT / m.group(0)
            if sp.is_file():
                paths.update(sp.read_text().split())
    return paths


BODY_TPL = (
    "Deepen {n} Tier1 pages. Slice file: knowledge/operational/"
    "deepen-x-slice-{stamp}-{i}.txt (paths relative to content/). "
    "MISSION: this is the Taiwanese American movement record — community/corpus "
    "facts outrank press-kit bios. Every page in your slice was PRE-GATED: it is "
    "under 5k bytes AND at least one corpus document references it, so material "
    "exists. If a grep finds nothing, your names were wrong, not absent — try "
    "name_zh / name_en / aliases / surname-only before concluding SKIP. "
    "PER PAGE, EXACTLY 3 STEPS: (1) read the page; (2) ONE shell call, grep ALL "
    "corpus dirs: `grep -rl 'NAME_ZH\\|NAME_EN\\|SURNAME' content/works content/articles content/sources content/events content/topics 2>/dev/null | head -6` "
    "then `grep -h -m2 -A2 'NAME_ZH\\|NAME_EN\\|SURNAME' $(hits) | head -40` — our "
    "memoirs are the primary material; (3) edit: absorb into '## Role in the "
    "Community' (or Timeline), wikilink each work touched ([[works/...|label]]), "
    "reconcile with existing text, HOLD conflicts ('HOLD: conflict A vs B', never "
    "auto-merge dates/ages), set last_reviewed: today. "
    "No web, no new pages, no invented biography, wikilinks to EXISTING slugs only. "
    "FRONTMATTER RULE: append notes BELOW the closing '---' fence only — an HTML "
    "comment inside YAML frontmatter breaks the ENTIRE Quartz build (fixed 6 files "
    "2026-09-26). "
    "COMMIT SAFETY — THIS IS WHERE WORKERS LOSE THEIR TURNS: six other workers run "
    "concurrently in the SAME repo. NEVER run `git add -A`, `git add .`, or "
    "`git commit -a`; that commits other workers' half-finished edits and fails the "
    "card. Stage ONLY your own files, by path. "
    "HARD RULES: (1) max 3 tool calls per page; (2) finish with this ONE command as "
    "your LAST action, substituting your touched paths and counts: "
    "`cd ~/echo-system && git add -- <your page paths> && git commit -m 'deepen-x "
    "slice {stamp}-{i}: N deepened, M skipped' ; hermes kanban complete __TASKID__ "
    "--result 'N deepened, M skipped, K corpus-linked'` — if git says 'index.lock "
    "exists', wait 5s and retry once, do not give up; (3) ending your turn without "
    "calling kanban_complete counts as a crash EVEN IF THE EDITS ARE DONE. "
    "Do NOT publish."
)


def main():
    mentions, inlinks = demand_counts()
    universe, saturated, no_material = thin_pages(mentions, inlinks)
    claimed = open_card_paths()
    top = [r for r in universe if r not in claimed][:SLICE * NCARDS]

    if DRY:
        print(f"dry: universe={len(universe)} saturated_excluded={saturated} "
              f"no_material_excluded={no_material} "
              f"claimed_by_open={len(claimed)} planned={len(top)}")
        for i in range(0, len(top), SLICE):
            print(f"  card {i // SLICE + 1}: {', '.join(top[i:i + SLICE])}")
        return

    OUT.mkdir(parents=True, exist_ok=True)
    stamp = subprocess.run(['date', '+%m%d%H%M'], capture_output=True, text=True).stdout.strip()
    made = 0
    for i in range(0, len(top), SLICE):
        chunk = top[i:i + SLICE]
        card_no = i // SLICE + 1
        slice_path = OUT / f'deepen-x-slice-{stamp}-{card_no}.txt'
        slice_path.write_text('\n'.join(chunk) + '\n')
        title = f'DEEPEN-X{stamp}-{card_no}: deepen {len(chunk)} thin pages (demand-ranked)'
        r = subprocess.run(['hermes', 'kanban', 'create', title,
                            '--assignee', 'pinto', '--body', 'pending',
                            '--max-runtime', '2400'],
                           capture_output=True, text=True)
        tid = re.search(r't_[0-9a-f]+', r.stdout)
        if not tid:
            print('create failed:', r.stdout.strip() or r.stderr.strip())
            continue
        con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
        con.execute("update tasks set body=? where id=?",
                    (BODY_TPL.replace('__TASKID__', tid.group(0))
                     .replace('{n}', str(len(chunk))).replace('{stamp}', stamp).replace('{i}', str(card_no)),
                     tid.group(0)))
        con.commit()
        con.close()
        subprocess.run(['hermes', 'kanban', 'promote', tid.group(0)], capture_output=True)
        made += 1
        print('created', tid.group(0), slice_path.name)
    print(f'cards: {made}  universe: {len(universe)}  excluded(claimed): {len(claimed)}')


if __name__ == '__main__':
    main()

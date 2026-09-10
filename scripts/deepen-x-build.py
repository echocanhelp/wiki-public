#!/usr/bin/env python3
"""Re-slice top thin pages into 6-page cards (iteration-budget-safe) and emit
protocol-fixed kanban cards. Rank: size desc (closest to good first).
Skips paths already claimed by an existing open DEEPEN-* card."""
import glob, json, os, re, subprocess
from pathlib import Path

REPO = Path('/home/leedt/echo-system')
OUT = REPO / 'knowledge/operational'
# 2026-09-08 audit: at conc-10 agg ~110 tok/s => ~7-10 tok/s/worker. 6-page
# cards needed ~20 min; 900s wall killed 9/10 mid-page. 4 pages fits 1500s
# with 60% margin; iteration budget (30) still comfortable at <=2 calls/page.
SLICE = 4
NCARDS = 32

rows = []
for pat in ('content/people/*.md', 'content/organizations/*.md'):
    for f in glob.glob(str(REPO / pat)):
        s = os.path.getsize(f)
        if s < 5000:
            rows.append((s, os.path.relpath(f, REPO / 'content')))
rows.sort(reverse=True)

# Dedupe against OPEN cards (any non-done/archived status) — two keys:
# (a) same card title already open, (b) slice path-set overlaps an open card.
# Read bodies straight from the DB: `kanban list --json` omits body, which
# made the old check a silent no-op and double-booked every slice (2026-09-08).
import sqlite3
con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
open_rows = con.execute(
    "select id, title, body from tasks "
    "where status not in ('done','archived') and title like 'DEEPEN%'"
).fetchall()
con.close()
open_titles = {r[1] for r in open_rows}
open_paths = set()
for _id, _title, body in open_rows:
    m = re.search(r'deepen-x-slice(-\d+)?-\d+\.txt', body or '')
    if m:
        sp = OUT / m.group(0)
        if sp.is_file():
            open_paths.update(sp.read_text().split())

top = [r for r in rows if r[1] not in open_paths][:SLICE * NCARDS]
made = 0
STAMP = subprocess.run(['date', '+%m%d%H%M'], capture_output=True, text=True).stdout.strip()
for i in range(NCARDS):
    chunk = top[i*SLICE:(i+1)*SLICE]
    if not chunk:
        break
    title = f'DEEPEN-X{STAMP}-{i+1}: deepen {len(chunk)} thin pages (protocol-fixed)'
    if title in open_titles or any(r[1] in open_paths for r in chunk):
        print('skip (open twin):', title)
        continue
    # unique filename per run — never clobber a slice file an open card points at
    p = OUT / f'deepen-x-slice-{STAMP}-{i+1}.txt'
    p.write_text('\n'.join(r[1] for r in chunk) + '\n')
    body_tpl = (
        f"Deepen {len(chunk)} thin Tier1 pages. Slice file: knowledge/operational/deepen-x-slice-{STAMP}-{i+1}.txt "
        "(paths relative to content/). Per page: read it; absorb facts ALREADY PRESENT in its cited sources/"
        "vault pages (no web); add wikilinks to EXISTING slugs only (no new pages, no invented biography); "
        "set last_reviewed: today. Pages needing more than 3 tool steps: note SKIP-with-reason and move on. "
        "HARD RULES: (1) max 2 tool calls per page; (2) when ALL pages are processed, you MUST run "
        "`git add -A content/ && git commit -m 'deepen-x slice' ; hermes kanban complete __TASKID__ "
        "--result 'N deepened, M skipped'` as your LAST action; (3) ending your turn without calling "
        "kanban_complete counts as a crash. Do NOT publish."
    )
    r = subprocess.run(['hermes', 'kanban', 'create',
                        title,
                        '--assignee', 'pinto', '--body', 'pending',
                        '--max-runtime', '2400'],
                       capture_output=True, text=True)
    tid = re.search(r't_[0-9a-f]+', r.stdout)
    if tid:
        # bake the real task id into the mandated complete command.
        # NOTE: sqlite3 CLI does not bind `?` args — the old call silently
        # left bodies at 'pending' (un-baked twins, 2026-09-08). Use Python.
        kc = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
        kc.execute("update tasks set body=? where id=?",
                   (body_tpl.replace('__TASKID__', tid.group(0)), tid.group(0)))
        kc.commit()
        kc.close()
        subprocess.run(['hermes', 'kanban', 'promote', tid.group(0)],
                       capture_output=True)
        made += 1
        print('created', tid.group(0), p.name)
print('cards:', made, 'skipped_open_paths:', len(open_paths))

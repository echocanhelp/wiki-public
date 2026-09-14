#!/usr/bin/env python3
"""DEEPEN-R revisit cards: force the 31 gwhyneth-class flagged pages into the
new vault-first protocol, priority-ordered by corpus-mention count."""
import json, os, re, sqlite3, subprocess
from datetime import datetime
from pathlib import Path

REPO = Path('/home/leedt/echo-system')
OUT = REPO / 'knowledge/operational'
SLICE = 4
flagged = json.load(open('knowledge/operational/revisit-flagged.json'))  # already sorted desc by mentions

# rebuild sorted list (json lost sizes; re-sort by mention count stored implicitly — order preserved)
con = sqlite3.connect(str(Path.home() / '.hermes/kanban.db'))
# dedupe against any open DEEPEN card touching the same path
open_rows = con.execute(
    "select title, body from tasks where status not in ('done','archived') and title like 'DEEPEN%'"
).fetchall()
open_titles = {t for t, _ in open_rows}
open_paths = set()
for _title, body in open_rows:
    m = re.search(r'deepen-[xr]-slice(-\d+)?-\d+\.txt', body or '')
    if m:
        sp = OUT / m.group(0)
        if sp.is_file():
            open_paths.update(sp.read_text().split())
STAMP = datetime.now().strftime('%m%d%H%M')
made = 0
# canonical vault-first protocol text, kept byte-compatible with the DEEPEN-X
# builder's body_tpl (SSOT drift is fixed by the WORKER.md pointer; this copy
# is literal because the builder template is an f-string).
BODY = (
    "[REVISIT — page was swarm-deepened but has corpus mentions and zero corpus wikilinks; "
    "the corpus grep is the whole point of this card. ]\n"
    "Deepen {N} revisited Tier1 pages. Slice file: knowledge/operational/{SLICEFILE} "
    "(paths relative to content/). MISSION: this is the Taiwanese American movement record — "
    "community/corpus facts outrank press-kit bios. Per page, exactly 3 steps: "
    "(1) read the page; (2) ONE shell call that greps the corpus for the person/org: "
    "`grep -rl 'NAME_ZH\\|NAME_EN' content/works content/articles 2>/dev/null | head -6` then "
    "`grep -h -m2 -A2 'NAME_ZH\\|NAME_EN' <hits> | head -40` — our memoirs are the primary material; "
    "(3) edit the page: absorb corpus facts into a '## Role in the Community' (or Timeline) section, "
    "wikilink each work page touched ([[works/...|label]]), reconcile with existing text, HOLD conflicts "
    "(write 'HOLD: conflict A vs B', never auto-merge dates/ages), set last_reviewed: today. "
    "No web, no new pages, no invented biography; wikilinks to EXISTING slugs only. "
    "Pages with no corpus hits and nothing absorbable: note SKIP-with-reason. "
    "HARD RULES: (1) max 3 tool calls per page; (2) when ALL pages are processed, you MUST run "
    "`git add -A content/ && git commit -m 'deepen-r revisit' ; hermes kanban complete __TASKID__ "
    "--result 'N deepened, M skipped, K corpus-linked'` as your LAST action; (3) ending your turn without calling "
    "kanban_complete counts as a crash. Do NOT publish."
)

for i in range((len(flagged) + SLICE - 1) // SLICE):
    chunk = flagged[i*SLICE:(i+1)*SLICE]
    paths = [p for p in chunk if p not in open_paths]
    if not paths:
        continue
    title = f'DEEPEN-R{STAMP}-{i+1}: revisit {len(paths)} corpus-link-missed pages'
    if title in open_titles:
        continue
    sp = OUT / f'deepen-r-slice-{STAMP}-{i+1}.txt'
    sp.write_text('\n'.join(paths) + '\n')
    body = BODY.replace('{N}', str(len(paths))).replace('{SLICEFILE}', sp.name)
    r = subprocess.run(['hermes', 'kanban', 'create', title,
                        '--assignee', 'pinto', '--body', 'pending',
                        '--max-runtime', '2400'], capture_output=True, text=True)
    tid = re.search(r't_[0-9a-f]+', r.stdout)
    if tid:
        con.execute("update tasks set body=? where id=?",
                    (body.replace('__TASKID__', tid.group(0)), tid.group(0)))
        con.commit()
        subprocess.run(['hermes', 'kanban', 'promote', tid.group(0)], capture_output=True)
        made += 1
        print('created', tid.group(0), sp.name)
con.close()
print('cards:', made, 'flagged:', len(flagged))

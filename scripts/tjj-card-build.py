#!/usr/bin/env python3
"""tjj-card-build.py — wave-2 fuel builder.

Deterministic first: run work-entity-linker.py over articles/ (pure CPU),
then build TJJ-A cards for articles that carry >=2 subject links. One article
per card. Skips paths already claimed by open cards, articles already stamped
verified-saturation, and articles whose latest TJJ commit in 7 days was a
zero-yield close (workers say "saturated" in the subject and do not stamp the
file, so the same large articles otherwise win the size sort every hour).

Env: TJJ_DRY=1 prints the plan and writes nothing (also skips the linker).
"""
import glob
import os
import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from feeder_recent_closes import recent_zero_yield_paths, still_closed

# SWARM-GUARD-1 (t_0cb42501): fail-closed backlog gate before every create.
sys.path.insert(0, os.path.expanduser("~/.hermes/scripts"))
from mint_guard import gated_once, budget_args  # noqa: E402

REPO = Path("/home/leedt/echo-system")
OUT = REPO / "knowledge/operational"
# 1 article per card. 4-item cards exhausted agent.max_turns=30 (8 timed_out +
# 64 reclaimed on 2026-10-07). Override is a code change, not an env, on purpose:
# the death was the slice size, and a quiet env default would reintroduce it.
SLICE = 1
NCARDS = 32
DRY = os.environ.get("TJJ_DRY") == "1"
STAMP = subprocess.run(["date", "+%m%d%H%M"], capture_output=True, text=True).stdout.strip()
TODAY = date.today().isoformat()
SATURATED_RE = re.compile(r'(hits.?hash|verified.?saturat|SATURATION)', re.I)

# 1) deterministic link pass. CPU lane stands down on the freeze pin.
# Dry-run must not apply: the linker writes.
if DRY:
    print("linker: skipped (TJJ_DRY)")
elif Path("/tmp/pinto-cpu-freeze").exists():
    print("linker: skipped (cpu-freeze pin up)")
else:
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts/work-entity-linker.py"), "--apply", "--stamp-saturated"],
        capture_output=True, text=True, cwd=REPO)
    print("linker:", r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:])

# 2) queue: article pages with >=2 subject links, not already stamped.
rows = []
stamped = 0
for f in glob.glob(str(REPO / "content/articles/**/*.md"), recursive=True):
    t = open(f, encoding="utf-8", errors="ignore").read(12000)
    if SATURATED_RE.search(t):
        stamped += 1
        continue
    n = 0
    if "## Subjects" in t:
        n = len(re.findall(r"\n- \[\[(?:people|organizations)/", t[t.find("## Subjects"):]))
    if n >= 2:
        rows.append((os.path.getsize(f), os.path.relpath(f, REPO / "content")))
rows.sort(reverse=True)

closed = recent_zero_yield_paths("tjj")
cooled = [p for _, p in rows if p in closed and still_closed(p, closed[p])]
cooled_set = set(cooled)

con = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
open_paths = set()
for (_id, body) in con.execute(
        "select id, body from tasks where status not in ('done','archived') "
        "and (title like 'TJJ%' or title like 'DEEPEN%')"):
    m = re.search(r"(?:deepen|tjj)-[xrab]?-slice(?:-\d+)?-\d+\.txt", body or "")
    if m:
        sp = OUT / m.group(0)
        if sp.is_file():
            open_paths.update(sp.read_text().split())
con.close()

top = [p for _, p in rows if p not in open_paths and p not in cooled_set][: SLICE * NCARDS]
print(f"plan: queue={len(rows)} stamped={stamped} cooled={len(cooled)} "
      f"open-covered={len(open_paths)} planned={len(top)}")
if DRY:
    for i, p in enumerate(top, 1):
        print(f"  card {i}: {p}")
    sys.exit(0)

made = 0
for i in range(0, len(top), SLICE):
    chunk = top[i:i + SLICE]
    if not chunk:
        break
    slice_file = OUT / f"tjj-a-slice-{STAMP}-{i // SLICE + 1}.txt"
    slice_file.write_text("\n".join(chunk) + "\n")
    title = f"TJJ-A{STAMP}-{i // SLICE + 1}: link+deepen {len(chunk)} TJJ articles"
    if not gated_once("tjj-card-build", key=title):  # SWARM-GUARD-1
        print("BACKLOG|SKIP", title)
        break
    # --goal-max-turns on a non-goal card = per-card iteration budget
    # (session_kanban pinto-local maps it to agent.max_turns; profile default
    # is 30). SWARM-GUARD-3 (t_418565a8): the budget comes from the ONE
    # registry (mint_guard.budget_args), fail closed — no literal here.
    r = subprocess.run(
        ["hermes", "kanban", "create", title, "--assignee", "pinto",
         "--created-by", "mint-wave",
         "--body", "pending", "--max-runtime", "2400",
         *budget_args("TJJ-A"), "--json"],
        capture_output=True, text=True)
    tid = re.search(r"t_[0-9a-f]+", r.stdout)
    if not tid:
        print("create failed:", r.stdout.strip() or r.stderr.strip())
        continue
    body = (
        f"Wave-2 TJJ absorb. Slice file: knowledge/operational/{slice_file.name} "
        f"(path under content/). Article: {chunk[0]}. "
        # 2026-11-03: the 45/45-death subclass burned turns on glyph-drift/gate
        # rework loops. The clean-first-try shape (581 runs, p50 183s) is baked
        # into EVERY body so workers stop rediscovering it. Do not trim.
        "MANDATORY RECIPE (clean-first-try shape, skill echopedia-tjj-wave2-worker): "
        "(1) NEVER type CJK literals anywhere in your scripts — build every CJK span and every "
        "search/replace anchor by harvesting verbatim fragments from 'git show HEAD:' lines "
        "(corpus-harvest) or chr() from hex STRING literals; a typed literal that drifts on disk "
        "burns the whole budget. "
        "(2) Article EOF comment must be PURE ASCII: assert all(ord(c)<0x80 for c in COMMENT) "
        "before writing; cite hash, post_date, Wayback, carriers==1 non-comment, fast-path used; "
        "must end with -->. "
        "(3) Fact lines: harvest the donor prefix from a saturated sibling line on the SAME people "
        "page (cut at the hex-built anchor built via chr(int(x,16)) from 'ff0c 8a72 9801 70ba'); "
        "novel prose only from corpus-resident fragments; gate unknown()==[] by CHAR membership "
        "(c not in ALLOWED) vs the hot-page charset. "
        "(4) Post-commit re-gate in a SEPARATE terminal call ~45s later: per touched page "
        "git show HEAD -> hash carrier==1 non-comment; own comment startswith '<!-- '+SLICE and "
        "endswith '-->'; codepoint scan of fact lines, comment AND git log -1 --pretty=%s via "
        "shell grep with hex parsed from string literals (never typed CJK, never trust printed "
        "stdout rendering — trust hex(ord())). "
        "(5) TURN DISCIPLINE: if the SAME gate fails twice on the same line, STOP — call "
        "kanban_block on your card with the defect string + line excerpt. A blocked card "
        "preserves strikes; looping to 45/45 wastes two full runs. "
        "Read ## Subjects. Confirm each person/org link is real; fix wrong links, "
        "remove spurious ones. For each confirmed subject, if that page does not "
        "already wikilink this article, add one dated fact with the article wikilink "
        "under '## From the record'. If it already links this article, do not add a "
        "duplicate line. "
        "If you changed nothing, add one line BELOW the article's closing --- fence, "
        f"never inside YAML: verified-saturation: {TODAY}. "
        "An HTML comment inside frontmatter breaks the whole site build. "
        "Commit subject must contain verified-saturated when nothing changed, or name "
        "the fact you added when it did — the feeder reads the subject. "
        "Stage only files you touched. Never git add -A. "
        f"Then call the kanban_complete tool on {tid.group(0)}. "
        "The hermes kanban CLI complete is rejected inside a worker and does not close "
        "the card. Do NOT publish."
    )
    db = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
    db.execute("update tasks set body=? where id=?", (body, tid.group(0)))
    db.commit()
    db.close()
    subprocess.run(["hermes", "kanban", "promote", tid.group(0)], capture_output=True)
    made += 1
    print("created", tid.group(0), slice_file.name)
print("cards:", made, "| queue:", len(rows), "| cooled:", len(cooled),
      "| open-covered:", len(open_paths))

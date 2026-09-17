#!/usr/bin/env python3
"""tjj-card-build.py — wave-2 fuel builder (2026-09-16 idle-backlog plan).

Deterministic first: run work-entity-linker.py over articles/ (pure CPU),
then build TJJ-A cards for the 2000+ taiwanjustice-net articles that received
entity links — each card = 4 linked articles whose subject pages the worker
verifies/deepens bidirectionally (article<->person). Skips paths already
claimed by open cards. LLM lane: respects the 01:00-07:29 window freeze via
the caller (rate-gate resume), same as DEEPEN-X.
"""
import glob, json, os, re, subprocess, sys
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
OUT = REPO / "knowledge/operational"
SLICE = 4
NCARDS = 32
STAMP = subprocess.run(["date", "+%m%d%H%M"], capture_output=True, text=True).stdout.strip()

# 1) deterministic link pass over articles (idempotent, resumable). CPU lane:
# stand down while the window-freeze pin is up (01:00-07:29 batch window).
if Path("/tmp/pinto-cpu-freeze").exists():
    print("linker: skipped (cpu-freeze pin up)")
else:
    r = subprocess.run([sys.executable, str(REPO / "scripts/work-entity-linker.py"), "--apply"],
                       capture_output=True, text=True, cwd=REPO)
    print("linker:", r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:])

# 2) queue: article pages that now carry >=2 subject links
rows = []
for f in glob.glob(str(REPO / "content/articles/**/*.md"), recursive=True):
    t = open(f, encoding="utf-8", errors="ignore").read(12000)
    n = len(re.findall(r"^## Subjects\n(?:.*\n)*?(?:- \[\[[^\]]+\]\|)", t))
    n = len(re.findall(r"\n- \[\[(?:people|organizations)/", t[t.find("## Subjects"):])) if "## Subjects" in t else 0
    if n >= 2:
        rows.append((os.path.getsize(f), os.path.relpath(f, REPO / "content")))
rows.sort(reverse=True)

# dedupe vs open TJJ/DEEPEN cards (dual-key like deepen-x builder)
import sqlite3
con = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
open_paths = set()
for (_id, body) in con.execute(
        "select id, body from tasks where status not in ('done','archived') and (title like 'TJJ%' or title like 'DEEPEN%')"):
    m = re.search(r"(?:deepen|tjj)-[xrab]?-slice(-\d+)?-\d+\.txt", body or "")
    if m:
        sp = OUT / m.group(0)
        if sp.is_file():
            open_paths.update(sp.read_text().split())
con.close()
top = [p for _, p in rows if p not in open_paths][: SLICE * NCARDS]

made = 0
for i in range(0, len(top), SLICE):
    chunk = top[i:i + SLICE]
    if not chunk:
        break
    slice_file = OUT / f"tjj-a-slice-{STAMP}-{i // SLICE + 1}.txt"
    slice_file.write_text("\n".join(chunk))
    title = f"TJJ-A{STAMP}-{i // SLICE + 1}: link+deepen {len(chunk)} TJJ articles"
    body = (
        f"Wave-2 TJJ absorb. Slice file: knowledge/operational/{slice_file.name} (paths under content/). "
        "For each article: read its ## Subjects links, (1) confirm each person/org mention is real "
        "(fix wrong links, remove spurious ones), (2) add a one-line dated fact with article wikilink "
        "to each confirmed person page under '## From the record', (3) commit. "
        "Call kanban_complete with task id and touched-page list at the end. "
        "No web search needed unless a link is doubtful."
    )
    subprocess.run(["hermes", "kanban", "create", title, "--body", body,
                    "--assignee", "pinto", "--json"], capture_output=True, text=True)
    made += 1
print("cards:", made, "| queue:", len(rows), "| open-covered:", len(open_paths))

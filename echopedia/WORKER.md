# Echopedia Worker Playbooks

**For local worker models.** Do **not** invent process. Do **not** plan creatively.  
Pick **one** playbook → run steps **in order** → emit **Report** template → **STOP**.

Human/smart model does thinking. You execute.

**Paths (always absolute or as written):**
- Vault: `/home/leedt/echo-system`
- Manual: `/home/leedt/echo-system/echopedia/USER_MANUAL.md`
- This file: `/home/leedt/echo-system/echopedia/WORKER.md`
- Scripts: `/home/leedt/.hermes/scripts/`

---

## GLOBAL RULES (every playbook)

1. Run **only one** playbook per request unless user lists IDs in order.
2. Use **exact commands** below. Do not substitute.
3. **Never** invent biographical facts.
4. **Never** copy all HTML to repo root (no flatten). Publish only via `echopedia-publish.sh`.
5. **Never** edit MEMORY with procedures.
6. **Never** create a new skill that duplicates an existing one.
7. If a command prints `FAIL` or exit code ≠ 0 on a critical step → go to **Report FAIL** and STOP (unless playbook says continue).
8. After file edits: run the verify command in that playbook before commit/push.
9. Default: **no git push** unless playbook is P5 full heal or user said `push` / playbook says push.
10. Max scope: touch only files the playbook names.

### Report template (always end with this)

```text
PLAYBOOK: <id>
STATUS: OK | FAIL | PARTIAL
COMMANDS_RUN:
- ...
KEY_OUTPUT:
- (paste lines with _STATUS: or SUMMARY or error)
FILES_CHANGED:
- (paths or none)
NEXT: STOP | human decision needed: <one line>
```

---

## ROUTING TABLE (pick playbook)

| User intent (keywords) | Playbook |
|------------------------|----------|
| orient, status, health, where are we, what's running | **P0** |
| broken site, drift, stale html, smoke, heal, ci | **P5** |
| publish, quartz, deploy, rebuild html | **P2** |
| **echopedia &lt;url/site&gt;** (no override) | **Planner full pipeline** then P2 **push** (see USER_MANUAL command language) — not archive-only |
| fix links, link hygiene, first-mention, one page | **P3** |
| drain queue, janitor queue, fix queue | **P4** |
| turn off push, disable auto, autonomy flag, standards | **P6** |
| improve pack, weekly, intake, freshness | **P7** |
| cron check, cron broken, jobs.json | **P11** |
| featured homepage cards | **P12** |
| site design, layout, mobile, homepage look, spelling sample | **P13** |
| edit person/org page content (not just links) | **P8** |
|| new work/source page for book/dissertation | **P9** |
|| multi-entity publication (yearbook, 菁英錄-style) | **PUBLICATION_INGEST.md** (standalone playbook) |
|| plan only / don't execute | **P0** then STOP (no other playbook) |

If unclear → **P0** only, then ask human one question in NEXT.

---

## P0 — ORIENT (read-only)

**GOAL:** Know health and mission. No edits.

**STEPS:**
1. `bash /home/leedt/.hermes/scripts/echopedia-system-status.sh`
2. `head -80 /home/leedt/echo-system/echopedia/WHERE_WE_ARE.md`
3. `python3 -c "import json;d=json.load(open('/home/leedt/echo-system/echopedia/standards.json'));print('version',d.get('version'));print(json.dumps(d.get('autonomy',{}),indent=2))"`
4. `head -40 /home/leedt/echo-system/echopedia/ci-heal-brief.md 2>/dev/null || true`
5. `head -30 /home/leedt/echo-system/echopedia/janitor-brief.md 2>/dev/null || true`

**SUCCESS:** All readable; you can state standards version + autonomy level + queue depth.  
**DO NOT:** edit files, commit, push.

**Report KEY_OUTPUT:** standards version, L2/L3 flags, last good deploy, queue depth, any FAIL in briefs.

---

## P1 — HEALTH CHECK (read-only)

**GOAL:** Pass/fail health.

**STEPS:**
1. `bash /home/leedt/.hermes/scripts/echopedia-ops-check.sh`
2. `bash /home/leedt/.hermes/scripts/echopedia-deploy-drift.sh`
3. `bash /home/leedt/.hermes/scripts/echopedia-smoke-test.sh`

**SUCCESS:** Note each `*_STATUS:` line.  
**FAIL hard:** `OPS_STATUS: FAIL`  
**DO NOT:** auto-fix (use P5 for heal).

---

## P2 — PUBLISH (build HTML trees)

**GOAL:** content → quartz → tree copy.  

**INPUT:** User may say `commit` and/or `push`. Default neither.

**STEPS:**
1. `bash /home/leedt/.hermes/scripts/echopedia-ops-check.sh`  
   - If `OPS_STATUS: FAIL` → Report FAIL, STOP.
2. If user said check only:  
   `bash /home/leedt/.hermes/scripts/echopedia-publish.sh --check`  
   Else:  
   `bash /home/leedt/.hermes/scripts/echopedia-publish.sh`
3. If user said `commit` (not push):  
   `bash /home/leedt/.hermes/scripts/echopedia-publish.sh --commit -m "echopedia publish"`
4. If user said `push`:  
   `bash /home/leedt/.hermes/scripts/echopedia-publish.sh --push -m "echopedia publish"`
5. `bash /home/leedt/.hermes/scripts/echopedia-deploy-drift.sh`  
   - Need `DRIFT_STATUS: OK`

**SUCCESS:** `PUBLISH_STATUS: OK` and `DRIFT_STATUS: OK`  
**DO NOT:** `cp` HTML into repo root manually; do not use legacy `echopedia_publish_loop.py`.

---

## P3 — FIX ONE PAGE LINKS

**GOAL:** First-mention + sources links for **one** page. No new biography.

**INPUT:** `PATH` like `people/albert-s-lai.md` (required).

**STEPS:**
1. `test -f /home/leedt/echo-system/content/$PATH || echo MISSING`  
   - If MISSING → FAIL STOP.
2. `python3 /home/leedt/.hermes/scripts/echopedia-link-hygiene.py --path $PATH`
3. Read hygiene lines. For each `LINK_UNLINKED_ENTITY` / `LINK_BODY_SPARSE` / `LINK_MISSING_SOURCE`:
   - Edit **only** `/home/leedt/echo-system/content/$PATH`
   - Add `[[slug|label]]` on **first** plain-text mention of that entity
   - If dissertation/work mentioned: ensure `[[sources/toward-a-community-of-hope|...]]` and GitHub archive link if missing (copy from any page that already has Sources callout)
4. Re-run: `python3 /home/leedt/.hermes/scripts/echopedia-link-hygiene.py --path $PATH`  
   - Prefer `findings=0` for that file
5. Do **not** publish unless user said publish → then run **P2**.

**SUCCESS:** hygiene findings=0 for that path OR only unfixable entities documented in Report.  
**DO NOT:** create new person pages in this playbook; do not expand life story.

---

## P4 — DRAIN JANITOR QUEUE (programmable only)

**GOAL:** Safe auto-fixes on queued pages (sources callout, last_reviewed). Not full prose rewrite.

**STEPS:**
1. `python3 -c "import json;q=json.load(open('/home/leedt/echo-system/echopedia/janitor-state.json')).get('queue',[]);print(len(q));[print(i.get('path'), i.get('findings')) for i in q[:5]]"`
2. `python3 /home/leedt/.hermes/scripts/echopedia-queue-drain.py`
3. Read `/home/leedt/echo-system/echopedia/drain-brief.md`
4. If user said `publish`: run **P2** steps 2–5.
5. If user said body links too: for each path in drain brief with remaining issues, run **P3** (max 5 pages).

**SUCCESS:** `DRAIN_STATUS: DONE`  
**DO NOT:** set `auto_apply_agent` true; do not invent bios.

---

## P5 — CI HEAL (L2/L3)

**GOAL:** Same as nightly 04:15 machine.

**STEPS:**
1. Dry-run first unless user said `live` or `push` or `full`:  
   `bash /home/leedt/.hermes/scripts/echopedia-ci-heal.sh --dry-run`
2. Show user KEY_OUTPUT from dry-run if they only wanted dry-run → STOP.
3. Live: `bash /home/leedt/.hermes/scripts/echopedia-ci-heal.sh`  
   (omit `--no-drain` unless user said no-drain)
4. Read `/home/leedt/echo-system/echopedia/ci-heal-brief.md`
5. `cat /home/leedt/echo-system/echopedia/last-good-deploy.json`

**SUCCESS:** `CI_STATUS: GREEN` or `HEALED_OR_WARN` without `FAIL`  
**FAIL:** `CI_STATUS: FAIL` → also run:  
`bash /home/leedt/.hermes/scripts/echopedia-incident.sh worker critical "P5 failed"` if not already logged.

**DO NOT:** hand-edit standards during P5 unless user asked P6.

---

## P6 — TOGGLE AUTONOMY FLAG

**GOAL:** Flip one boolean in standards.json.

**INPUT:** Flag name + true/false. Allowed flags only:
- `l2_auto_publish_on_drift`
- `l2_auto_drain_on_ci`
- `l2_auto_commit_on_heal`
- `l3_auto_push_on_green`
- `l2_auto_featured_on_publish`
- `l2_auto_site_design_heal`
- `l2_auto_site_design_featured`
- `l2_auto_site_design_publish`
- `l2_site_design_blocks_green`

**STEPS:**
1. Read current:  
   `python3 -c "import json;print(json.load(open('/home/leedt/echo-system/echopedia/standards.json'))['autonomy'])"`
2. Set flag with python (do not hand-mangle JSON):
```bash
python3 <<'PY'
import json
from pathlib import Path
p=Path("/home/leedt/echo-system/echopedia/standards.json")
d=json.loads(p.read_text())
# SET THESE TWO LINES FROM USER:
flag="l3_auto_push_on_green"
value=False
d.setdefault("autonomy",{})[flag]=value
d["updated"]=__import__("datetime").date.today().isoformat()
# bump version integer by 1 when changing autonomy rules
d["version"]=int(d.get("version",0))+1
p.write_text(json.dumps(d, indent=2)+"\n")
print("set", flag, value, "version", d["version"])
PY
```
3. Replace `flag=` and `value=` in the script to match user request before running.
4. `bash /home/leedt/.hermes/scripts/echopedia-system-status.sh`
5. Append one line under autonomy in WHERE_WE_ARE only if user asked to document: optional skip.

**SUCCESS:** printed set flag + new version  
**DO NOT:** change unrelated keys; do not delete smoke_urls.

---

## P7 — IMPROVEMENT PACK

**GOAL:** Meta sense (+ optional drain).

**STEPS:**
1. Without drain: `bash /home/leedt/.hermes/scripts/echopedia-improvement-collect.sh`  
   With drain if user said drain: `bash /home/leedt/.hermes/scripts/echopedia-improvement-collect.sh --drain`
2. `head -60 /home/leedt/echo-system/echopedia/improvement-brief.md`

**SUCCESS:** `IMPROVE_STATUS: OK`  
**DO NOT:** push unless user then orders P2/P5.

---

## P8 — EDIT PAGE CONTENT (thin rules)

**GOAL:** Expand/fix wiki page from **existing sources only**.

**INPUT:** `PATH`, what to add (must cite source file under `knowledge/` or existing page).

**STEPS:**
1. Confirm source exists: user must name a file under `/home/leedt/echo-system/knowledge/` or quote existing page. If no source → FAIL STOP ask human.
2. Read source **in chunks** if large (>1000 lines): do not load whole 400KB file; use `read_file` offset/limit or existing fact sheet.
3. Prefer fact sheet: `/home/leedt/echo-system/knowledge/research/*-facts.md` if present.
4. Edit only `/home/leedt/echo-system/content/$PATH`.
5. Keep sections: Identity Snapshot, body, Source Notes, Related Pages.
6. First-mention wikilinks for existing slugs only.
7. `python3 /home/leedt/.hermes/scripts/echopedia-link-hygiene.py --path $PATH`
8. Publish only if user said publish → **P2**.

**SUCCESS:** page updated; hygiene clean or reported; no unsourced claims.  
**DO NOT:** use web invent; do not mark verification_status published if only guessing.

---

## P9 — NEW SOURCE / WORK PAGE

**GOAL:** Create `content/sources/<slug>.md`.

**STEPS:**
1. User provides: slug, title, optional github archive path under knowledge/web-archives/.
2. `python3 /home/leedt/.hermes/scripts/echopedia-source-stub.py --help`  
   Then run stub with user args if CLI supports them; else write file matching existing  
   `/home/leedt/echo-system/content/sources/toward-a-community-of-hope.md` structure (shorter OK).
3. Link from related person/org pages only if user named them → first-mention + Related Pages.
4. Hygiene on those paths.
5. Publish if user said publish → **P2**.

**SUCCESS:** file exists under `content/sources/`.  
**DO NOT:** put full 400KB text into the source page; link to GitHub archive instead.

---

## P10 — COMMIT MESSAGE ONLY (after edits)

**GOAL:** Commit vault changes. No push unless user said push.

**STEPS:**
1. `cd /home/leedt/echo-system && git status --short`
2. `cd /home/leedt/echo-system && git add content/ people/ organizations/ sources/ tags/ public/ echopedia/ knowledge/ 2>/dev/null; true`
3. `cd /home/leedt/echo-system && git commit -m "echopedia: <user short reason>" || echo NOTHING_TO_COMMIT`
4. If user said push: `cd /home/leedt/echo-system && git push origin gh-pages`

**SUCCESS:** commit hash or NOTHING_TO_COMMIT  
**DO NOT:** force push; do not change git config.

---

## AUTOMATED CRONS (no LLM — do not reimplement)

These jobs are **`no_agent: true`**. The scheduler runs a **bash script only**.  
Worker models must **never** “interpret” cron prompts or invent steps for these.

| Job | Schedule | Script | Behavior |
|-----|----------|--------|----------|
| unified-watchdog | every 30m | `unified-watchdog.sh` | Silent OK; alert on fail |
| vllm-thermal-scaler | every 1m | `vllm-thermal-scaler.sh` | Adaptive silent / alert |
| kanban-sync | every 30m | `kanban-sync.sh` | Silent if no change |
| memory-audit | 05:00 daily | `memory-audit.sh` | Report if issues |
| echopedia-janitor | 04:00 | `echopedia-janitor-wrapper.sh` | Queue + log (local) |
| echopedia-nightly-audit | 04:00 | `echopedia-nightly-audit-wrapper.sh` | Alert if thresholds |
| **echopedia-ci-heal** | **04:15** | `echopedia-ci-heal-wrapper.sh` | L2/L3 heal + **site-design L1** + **only nightly push** |
| echopedia-weekly-improvement | Mon 05:00 | `echopedia-weekly-improvement.sh` | Pack+drain+heal |
| **echopedia-site-design** | **04:30** | `echopedia-site-design-wrapper.sh` | **Post-deploy audit-only** (heal lives inside ci-heal) |
| echopedia-digest | 09:00 | `echopedia-digest.sh` | Morning dashboard |

**Selfcheck:** `bash /home/leedt/.hermes/scripts/echopedia-cron-selfcheck.sh`  
Expect `CRON_STATUS: OK`.

### Worker rules for crons
1. Do **not** create agent cron jobs (`no_agent: false`) for Echopedia.
2. Do **not** put multi-step English procedures in cron `prompt` — only script path.
3. To change behavior: edit the **script** or `standards.json` flags — not the prompt.
4. Manual equivalent of nightly heal: playbook **P5**.
5. If cron fails: read `knowledge/operational/incidents/`, re-run the **script** with bash, fix script.

### P11 — CRON SELFCHECK
**STEPS:**
1. `bash /home/leedt/.hermes/scripts/echopedia-cron-selfcheck.sh`
2. If WARN about not executable: re-run (selfcheck chmods) or `chmod +x` the named script
3. If FAIL missing script: Report FAIL — human must fix jobs.json

**SUCCESS:** `CRON_STATUS: OK`  
**DO NOT:** enable LLM agent crons to “replace” these scripts.

---

## P12 — FEATURED REGENERATE

**STEPS:**
1. `python3 /home/leedt/echo-system/scripts/featured-regen.py --root /home/leedt/echo-system --dry-run`
2. Verify selected pages match expectations (pinned + recency, within caps)
3. `python3 /home/leedt/echo-system/scripts/featured-regen.py --root /home/leedt/echo-system --inject`
4. Verify `index.html` **and** `public/index.html` have `<!-- featured-start -->` / `<!-- featured-end -->` markers (single pair each)
5. Commit + publish via `echopedia-publish.sh` if user said publish

**DO NOT:** edit index.html manually; always use the script. Script lives in **`echo-system/scripts/`**, not `.hermes/scripts/`.

---

## P13 — SITE DESIGN (layout manager)

**GOAL:** Run the site designer loop from **`echopedia/SITE_DESIGN.md`**. Prefer scripts; local agent only for `AGENT_SUGGESTED` items.

**INPUT:** `audit` (default) | `heal` | `agent` (bounded fixes). Optional `publish`.

**STEPS:**
1. Read head of canon: `head -80 /home/leedt/echo-system/echopedia/SITE_DESIGN.md`
2. Audit only:  
   `python3 /home/leedt/.hermes/scripts/echopedia-site-design-audit.py`
3. If user said `heal` (or nightly equivalent):  
   `bash /home/leedt/.hermes/scripts/echopedia-site-design-heal.sh`  
   Dry-run: add `--dry-run`
4. Read `/home/leedt/echo-system/echopedia/site-design-brief.md`
5. **Agent branch only if user said `agent` or brief has AGENT_SUGGESTED and user allowed fixes:**  
   - Max **5** content files OR featured/marker repair only  
   - **Forbidden:** Quartz theme redesign, new nav IA, invent bios, bulk CSS  
   - Spelling: clear English typos only; never “fix” Chinese names  
   - Re-run audit after edits
6. If user said `publish`: run **P2** (or heal already published for parity)
7. Report → **STOP**

**SUCCESS:** `SITE_DESIGN_STATUS: OK` or `WARN` without CRITICAL after heal; brief updated.  
**DO NOT:** open-ended “make the site beautiful”; do not schedule agent crons for this.

---

## Anti-patterns (worker STOP)

| If you want to… | STOP — do this instead |
|-----------------|------------------------|
| Design new architecture | Report; human/smart model only |
| Load full Lai PDF/archive into context | Use fact sheet + chunks by name |
| Fix “all pages” | Max 5 per turn (queue order) |
| Merge skills | Never |
| Use Grok/frontier for nightly | Never in playbooks |
| Flatten quartz public/* to repo root | Never |

---

## Human → worker one-liners

```text
Worker: open /home/leedt/echo-system/echopedia/WORKER.md and run playbook P0 only.
```

```text
Worker: WORKER.md playbook P3 PATH=people/jonah-chang.md then STOP. No push.
```

```text
Worker: WORKER.md P5 live. Then Report.
```

```text
Worker: WORKER.md P6 set l3_auto_push_on_green=false
```

```text
Worker: WORKER.md P2 push. Message: fix drift
```

---

*Smart models: improve this file when procedures change. Workers: execute only.*

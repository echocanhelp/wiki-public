---
title: "Worker Guidelines — Echopedia"
type: reference
tags:
  - worker
  - guidelines
  - echopedia
  - 12-factor
  - graph-engineering
---

# Worker Guidelines

> Auto-generated from plan: `~/.hermes/plans/2026-07-19_12-factor-agents-implementation.md`  
> Last reviewed: 2026-08-17 (token split + TAH identity pitfalls)

## Who runs what (token split)

**Second purpose of this file:** keep **premium Grok tokens** on judgment; spend **free Laguna tokens** on playbook execution.

Live (2026-08-17): pinto `model.default` = `poolside/Laguna-S-2.1-NVFP4` `:8888`; `delegation.provider/model` = same Laguna. Grok appears when the operator `/model`s or this chat already fell over to xAI.

| Role | Model | May | Must not |
|------|-------|-----|----------|
| **Planner** (this chat if Grok) | premium | Classify, identity call (same person?), pick **one** playbook ID, write a self-contained card, patch *this file* if the recipe is wrong, verify worker output | Bulk `patch`/`write_file` on `content/people|organizations`, harvest loops, Quartz publish grind |
| **Worker** | Laguna (free) | **One** playbook, exact commands, Report, STOP | Redesign, new crons, identity guesses, `/model` hop |
| **Scripts / `no_agent`** | $0 tokens | Harvest, backfill, index-sync, collect | LLM in the loop |

**Hand-off (planner on Grok):**

1. Decide identity + playbook in this chat (short).
2. `hermes kanban create "P8 …" --body "WORKER.md P8 PATH=… SOURCE=…" --assignee pinto`  
   **or** `delegate_task(goal="WORKER P8 …", context="paths + gates")` — children already inherit Laguna.
3. Do **not** execute P8/P9/P3/P12 in the Grok turn.
4. Re-read the files the worker claims; then P1/P2 only if you must (P2 may stay planner if publish is one script).

**Stay on Grok for:** “same person?”, romanization collisions, CONTROL/process patches, architecture.  
**Force Laguna for:** apply tables, new thin pages, redirects, hub list rows, index-sync.

If you already started P8 on Grok this turn, **stop after the next file** and hand off the rest.

## Self-Contained Tasks (Factor 12 — Stateless Reducer)

Every kanban task must be self-contained. Workers load context files **explicitly** rather than relying on session context or prior turns.

### Requirements

1. **Every task body includes:**
   - Plan file path (absolute)
   - Source file paths (absolute)
   - Context file paths (absolute)
   - Any other artifacts the worker needs

2. **Workers must:**
   - Read plan files explicitly before starting work
   - Read source files explicitly before generating output
   - Not assume prior context exists

3. **Parent tasks must:**
   - Include all file paths in the task body
   - Not rely on the child worker remembering what files exist

### Example

```markdown
## Task: Deepen page for X

Plan: /home/leedt/.hermes/plans/2026-07-19_12-factor-agents-implementation.md
Source: /home/leedt/echo-system/knowledge/research/2017-tahs-publication.md
Section dump: /home/leedt/echo-system/knowledge/research/tahs-2017-section-dumps/x.md
Output: /home/leedt/echo-system/content/people/x.md

## Instructions
...
```

### Impact
- Tasks are reproducible — can be re-run from scratch without prior context
- Easier to debug — the full context is in the task body
- Easier to delegate — any worker can pick up the task
- No changes to successful tasks (they already work)

### Risk
- Larger kanban task bodies (mitigated by only including file paths, not file contents)
- Some context may be lost if the parent session had unique information (mitigated by documenting what was unique in the task body)

---

## Kanban Complete Metadata (Factor 5 — Unify State)

Every `hermes kanban complete` must include structured metadata linking execution state to business state.

### Required metadata fields

When completing a kanban task, include `--metadata` with:

```json
{
  "changed_files": ["content/people/x.md", "content/people/y.md"],
  "lines_added": 150,
  "lines_removed": 20,
  "new_pages": ["x.md", "y.md"],
  "deleted_pages": [],
  "git_commit": "abc1234"
}
```

### Optional metadata fields

```json
{
  "depth_before": 0.3,
  "depth_after": 0.9,
  "pages_processed": 2,
  "pages_skipped": 0,
  "errors": []
}
```

### Why

- Execution state (what the worker did) is inferable from git + metadata
- Business state (what changed in the wiki) is inferable from git + metadata
- One source of truth: the git log + kanban metadata

### Example

```bash
hermes kanban complete <task_id> \
  --result "Deepened x.md and y.md from 2KB to 8KB each." \
  --metadata '{"changed_files": ["content/people/x.md", "content/people/y.md"], "lines_added": 150, "lines_removed": 20, "new_pages": [], "deleted_pages": []}'
```

### Enforcement

- **Recommended** for now (advisory)
- **Not enforced** via tool call (kanban doesn't require metadata)
- **Documented** in this file and in task bodies
- **Review:** check metadata on every complete during review cycle

---

## Error Compacting (Factor 9)

When a kanban task fails and is retried, the failure output must be compacted into the retry context.

### How

1. On failure, the worker returns error output in the kanban `result` field
2. On retry, the worker loads the previous result and incorporates it
3. Workers should append failure context to the next attempt's body

### Example

```bash
# First attempt fails
hermes kanban complete <task_id> \
  --result "FAILED: git push rejected — force needed" \
  --metadata '{"error": "git push rejected"}'

# Retry: worker reads previous result and adapts
hermes kanban complete <task_id> \
  --result "RETRY: git push --force after reviewing rejection" \
  --metadata '{"error": "git push rejected", "action_taken": "force_push"}'
```

### Status
- **Not implemented** — kanban doesn't auto-include previous result on retry
- **Workaround:** workers must manually read previous result and incorporate
- **Future:** kanban should auto-include previous failure in retry context

### Investigation (2026-07-19)

Found two relevant mechanisms:

1. **`max_retries`** — circuit breaker, NOT retry-with-context. Trips after N failures and blocks the card for review. No automatic retry with context.

2. **`--goal` mode** — self-correcting loop within the SAME session. A judge checks the response against the card title/body and if not done, the worker keeps going until the judge agrees it's complete (or the turn budget runs out, which blocks the card for review). Best for open-ended cards one shot rarely completes.

**Recommendation:** Use `--goal` for self-correcting tasks where the worker should iterate until a judge agrees done. Use manual result-reading for cross-session retries.

**Status:** documented. No code changes needed — use `--goal` where applicable.

---

## Routing Table (Playbooks P0–P13)

| ID | Name | When | Steps |
|----|------|------|-------|
| P0 | Orient | Don't know state | 1. Read SYSTEM_STATUS.md 2. Read WHERE_WE_ARE.md 3. Report |
| P1 | Ops/drift/smoke | Check health | 1. `echopedia-ops-check.sh` 2. `echopedia-ci-heal.sh --dry-run` 3. `echopedia-smoke-test.sh` 4. Report |
| P2 | Publish/deploy | Push to live | 1. `echopedia-publish.sh --push` (rsync→quartz build→tree-copy + root index.html copy→featured regen→commit+push→CDN verify) 2. Verify smoke URLs 3. Report |
| P3 | One page links | Fix wikilinks | 1. Read page 2. Find broken wikilinks 3. Repair or redirect 4. Commit only (no publish) 5. Report |
| P4 | Janitor queue | Queue items | 1. Read janitor-brief.md 2. Process items per type 3. Romanization `--heal` is automatic in janitor-wrapper (lexicon-only) 4. Commit 5. Report |
| P5 | Heal/drift/smoke | Full heal | 1. `echopedia-ci-heal.sh` 2. Verify 3. Report |
| P6 | Toggle autonomy | Disable push | 1. Edit standards.json 2. Report |
| P7 | Improvement pack | Weekly | 1. Read improvement-brief.md 2. Process items 3. Report |
| **P8** | **Edit page content** | **New facts from source** | **1. Read source 2. Read target page 3. Apply edits with named source 4. Commit only (no publish) 5. Report** |
| P9 | New work page | Create stub | 1. Create page from template 2. Add frontmatter 3. Commit 4. Report |
| P10 | Commit/push git | Git ops | 1. `git add` 2. `git commit` 3. `git push` 4. Report |
| P11 | Docs selfcheck | Doc OS | 1. `bash ~/.hermes/scripts/echopedia-docs-sync.sh` 2. Check DOCS_STATUS 3. Fix any FAIL 4. Report |
| P12 | Featured regen | Homepage cards | 1. `featured-regen.py --dry-run` 2. Verify 3. `featured-regen.py --inject` 4. Commit + publish 5. Report |
| P13 | Site design | Layout issues | 1. Read site-design-brief.md 2. Run audit 3. Propose fixes (incl. root index.html copy from quartz build, Pages build type migration) 4. Report |
| **P14** | **Person-to-work linking** | **Ensure person pages list all works + articles link back** | **1. Run `echopedia-person-works-linker.py --all` 2. Verify ## Works section on sample page 3. Verify backlinks in sample articles 4. Commit** |

### P8 — Edit page content (content update)

**When:** You have new facts from a named source that need to be applied to an existing wiki page.

**Requirements:**
- Source path (absolute) — the file or URL providing the new facts
- Target path (absolute) — the page to edit
- Facts must come from a verifiable source

**Steps:**
1. Read the source file/URL to extract new facts
2. Read the target page (`content/<path>.md`)
3. Apply edits using `patch` tool — only add content that comes from the source
4. Add source to frontmatter `sources:` list if not already present
5. Update `last_reviewed` date
6. Add revision history entry
7. **Commit only** — do NOT publish (use P2 for publish)
8. Report changes

**Pitfalls:**
- Do NOT invent content — only apply what the source provides
- Do NOT remove existing content unless it contradicts the source
- Always cite the source in revision history
- Cross-reference with related pages to ensure consistency (e.g., if you edit family relations, check the related person's page)
- **TAH English slug ≠ identity.** `taiwaneseamericanhistory.org/person/<slug>/` matching an Echopedia filename is **not** a merge. Require 漢名 (or owner/roster confirm) before absorbing TAH tables onto a TAHS page. Same EN name + different 漢名 → **unmerge**: keep the TAHS page, create a separate `tah-whos-who` page (or encyclopedia page), add Disambiguation both ways. Examples 2026-08-17: TAH `paul-chen` = ophthalmologist (no 漢名) ≠ TAHS officer Paul Chen; TAH #1788 Paul Y. Chen 陳柏宇 is a third row unless owner says otherwise; TAH `rex-chen` = 陳財元 (d. 2003) ≠ TAHS 陳乃光 — do not decide without owner.
- **TAH WP slug may differ from our slug.** Absorb onto the existing TAHS page (`yee-phong-alan-thian` → `alan-thian`); leave a `redirect_to` stub at the TAH slug. Redirect stubs need `## Identity Snapshot` + `## Related Pages` or `verify_echopedia.py` fails.
- **Owner identity call beats harvest.** If owner says “X is not ours,” do not put TAH tables on the TAHS officer page even when 漢名 strings match.
- **P8 is commit-only.** go-router “Echopedia fact” still runs P1 then P2 after P8. Do not skip P1. New Pages slugs often CDN-404 for minutes; verify `raw.githubusercontent.com/echocanhelp/wiki-public/gh-pages/people/<slug>.html` = 200 before republishing.

**Example:**
```
WORKER.md playbook P8 PATH=content/people/ashton-hsu.md SOURCE="family memo pad (Teng-Lung Hsu, M.D. stationery, code 7CIM4107762)"
```

**Default workflow when user says "Echopedia <person> <fact>":**
1. **Grok (frontier):** identity judgment + assign WORKER **P8** card to Laguna worker
2. **Laguna (pinto/NVFP4):** P8 with the fact as source (commit only, no publish)
3. **Laguna:** P1 to verify (ops/drift/smoke)
4. **Laguna:** P2 to publish if green

**Grok does NOT execute P8/P9 bulk.** It assigns the card; the Laguna worker runs the playbook.

---

## Graph Engineering (from AGENT_GRAPH.md)

Our architecture follows a **two-graph** model:

1. **Org graph (stable):** profiles (`default`, `pinto`), cron jobs, Telegram delivery
2. **Work graph (dynamic):** kanban cards, cron ticks, depth-pass batches

### Model routing

| Context | Model (2026-08-17 live) |
|---------|-------|
| pinto profile default | Laguna `:8888` (`poolside/Laguna-S-2.1-NVFP4`); fallback Grok |
| This chat after `/model` Grok | premium — **plan + identity only**; spawn Laguna for playbooks |
| `delegate_task` | `delegation.*` → Laguna (already set) |
| `hermes kanban assign <task> pinto` | Laguna |
| `no_agent` cron | N/A (deterministic) |
| Vision | Grok auxiliary |
| **P8/P9 content edits** | **Grok assigns card; Laguna executes playbook** |
| **Identity judgment** | **Grok (frontier) — never delegated to Laguna** |

### Design principles

1. **Deterministic nodes first:** L0/L1 bulk work → `no_agent` bash/Python. LLM only at judgment edges.
2. **Human checkpoint at delivery:** All output → Telegram home. User reviews before approve.
3. **Git as artifact store:** All work nodes produce git-tracked artifacts.
4. **Org graph stable, work graph ephemeral:** Profiles/cron stable. Kanban/cron ticks ephemeral.
5. **Bounded graphs:** Every edge has known input/output shape → benchmarkable path cost.

---

*This document is part of the agent graph. Update it when topology changes.*
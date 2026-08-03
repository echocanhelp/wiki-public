# Echopedia User Manual

**Start here for commands.** For **how not to corrupt the system**, read **[CONTROL.md](CONTROL.md)** first.  
**Local workers use [WORKER.md](WORKER.md)** (numbered playbooks only).

| Doc | Who | Role |
|------|-----|------|
| **[CONTROL.md](CONTROL.md)** | Human + every model | Control surfaces, SSOT, safe usage, corruption blacklist |
| **[USER_MANUAL.md](USER_MANUAL.md)** (this) | Human + smart model | Command language; how to assign work |
| **[WORKER.md](WORKER.md)** | Local worker model | Execute one playbook, no design |
| **[FEATURE_ADD.md](FEATURE_ADD.md)** | Human + planner | Checklist when adding Google/tools/crons/etc. |
| [WHERE_WE_ARE.md](WHERE_WE_ARE.md) | Both (read) | Built vs remains |
| [SYSTEM_STATUS.md](SYSTEM_STATUS.md) | Both (read) | Live health (auto) |
| skill `echopedia-ops` | Agent | Routing map only |
| [standards.json](standards.json) | Both | Autonomy switches + version |

Vault: `/home/leedt/echo-system` · Live: https://echocanhelp.github.io/wiki-public/

---

## Architecture overview

```
┌─────────────┐    plan/review    ┌─────────────┐
│  default    │ ◄──────────────── │  pinto      │
│  profile    │   ← approve ←     │  profile    │
│  (frontier) │                   │  (worker)   │
│  Grok/     │                   │  NVFP4      │
│  NVFP4     │                   │  NVFP4      │
└─────┬───────┘                   └─────┬───────┘
      │                                 │
      │ delegate_task                   │ hermes -p pinto
      │ (delegation.*→pinto)            │ chat -q <task>
      ▼                                 ▼
┌──────────────────────────────────────────────────┐
│         DETERMINISTIC NODES                      │
│  no_agent cron jobs (bash/Python)                │
│  ci-heal · site-design · digest · janitor        │
└──────────────────────────────────────────────────┘
      │
      │ deliver
      ▼
┌──────────────────────────────────────────────────┐
│  Telegram home (6769573480)                      │
│  ← human checkpoint / review gate                │
└──────────────────────────────────────────────────┘
```

---

## Quick start (first time)

1. **Read this file** — it defines how to assign work.
2. **Say** `Echopedia website <domain>` — full pipeline: archive → absorb → publish.
3. **Review the digest** at 09:00 — morning brief of what the system did.

**Command decision tree:**

```
Do you have a…
├── Domain (website)? → “Echopedia website <domain>"
├── PDF (yearbook, publication)? → "Echopedia publication <name>"
├── Page to feature? → "Echopedia feature <name>"
├── Site layout issue? → "Echopedia site design"
├── Something broken? → Check SYSTEM_STATUS.md → pick a playbook
└── Not sure? → "Echopedia <site>" (defaults to website pipeline)
```

---

## Common workflows

### Ingest a new website
1. Say: `Echopedia website <domain>`
2. Review morning digest (09:00) for progress
3. Check SYSTEM_STATUS.md for any issues

### Add a new feature (Google, Twilio, media, etc.)
1. Follow FEATURE_ADD.md
2. Classify as A (tooling), B (scheduled), or C (integrated)
3. Implement + update only necessary docs

### Fix a broken page
1. Check SYSTEM_STATUS.md → find symptom
2. Pick playbook from troubleshooting table
3. Run worker playbook → verify → publish

### Disable auto-push
1. `Echopedia site design` → P6
2. Set `l3_auto_push_on_green=false`
3. Re-enable after fix

---

## First 24 hours — new user guide

This is the path for someone who just joined the Echopedia project. In 24 hours you should: understand the system, see the live site, run a check, and know where to start contributing.

### Hour 1 — Orientation (read-only)

1. **Read this file** (USER_MANUAL.md). It defines how to assign work.
2. **Read WHERE_WE_ARE.md** — mission progress and what remains.
3. **Read SYSTEM_STATUS.md** — auto machine snapshot (crons, queue, last green push).
4. **Load the routing skill:** `skill_view echopedia-ops` — the single map of scripts and topology.
5. **Open the live site:** https://echocanhelp.github.io/wiki-public/

**Goal:** You can answer "what does Echopedia do, and how do I know if it's healthy?"

### Hour 2 — Check the machine

```bash
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
# if FAIL or ACTION:
bash ~/.hermes/scripts/echopedia-ops-check.sh
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
```

Read the three briefs:
- `echopedia/janitor-brief.md` — queue + link hygiene
- `echopedia/ci-heal-brief.md` — last heal + push result
- `echopedia/improvement-brief.md` — daily improvement pack

**Goal:** You can tell whether the system is green or red, and what the last run did.

### Hours 3–4 — See how a page is built

Pick one live page, e.g. https://echocanhelp.github.io/wiki-public/people/albert-s-lai

1. Find its source: `content/people/albert-s-lai.md`
2. Read its frontmatter — note `last_reviewed`, `featured`, `sources` callouts.
3. Run `P0` (orient) then `P1` (ops/drift/smoke) to see what the worker checks.
4. Read WORKER.md playbook P3 (one page links) — this is how a single page gets fixed.

**Goal:** You understand the MD→HTML publish path and what "done" looks like for a page.

### Hours 5–12 — Pick your first task

Look at the **janitor queue** (depth is in SYSTEM_STATUS.md). Typical first tasks:

| Queue item | Playbook | What you do |
|------------|----------|-------------|
| Thin person/org page | P3 | Fix links, add first-mention body links |
| Broken wikilink | P3 | Repair or redirect |
| Stale `last_reviewed` | P3 | Review content, bump date |
| New source hub needed | P9 | Create `content/sources/<name>.md` |
| Publish needed | P2 | Rebuild HTML + push |

**Do not** pick: "improve linking across the wiki", "figure out the best architecture", "make it better". Pick a playbook ID + path.

**Goal:** You have one concrete page or fix assigned with a playbook ID.

### Hours 12–24 — Contribute

1. **Clone the repo** (if you haven't): `git clone` the echo-system repo.
2. **Make your edit** on a branch: `git checkout -b fix/<short-name>`
3. **Run the worker** with your chosen playbook:
   ```text
   WORKER.md playbook P3 PATH=content/people/<name>.md
   No publish. Report. STOP.
   ```
4. **Commit** your change (P10 if you need help).
5. **Ask for a publish** (P2) or let ci-heal pick it up at 04:15.

**Goal:** You've made one verified edit that follows the standards in `standards.json`.

### What to do next

- **Every morning at 09:00** — read the digest (delivered to your chat or `echopedia/digest-brief.md`).
- **Every day at 05:00** — the improvement pack runs; review `improvement-brief.md`.
- **When stuck** — check SYSTEM_STATUS.md → pick a playbook from the troubleshooting table.
- **When adding a feature** — follow FEATURE_ADD.md (Google, Twilio, media, tools, crons).

**Remember:** Humans set goals and approve plans. The worker runs one playbook exactly. The smart model plans and improves playbooks. You only intervene for content judgment, new sources, process design, or red alerts.

---

## Command language: what "Echopedia …" means

**Default (Leonard / Hsuperman):** saying **Echopedia** + a target means **live wiki**, not research-only.

**Default workflow when user says "Echopedia <person> <fact>":**
1. Run P8 with the fact as source
2. Run P1 to verify (ops/drift/smoke)
3. Run P2 to publish if green

**This runs automatically.** The planner does NOT need to ask the user for playbook IDs. The user only needs to say "Echopedia <target> <fact>".

| You say | System must do |
|---------|----------------|
|| **`Echopedia website <domain>`** | **Full-domain** archive + **absorb into wiki graph** + publish push — see **[WEBSITE_INGEST.md](WEBSITE_INGEST.md)** completeness bar |
|| `Echopedia publication <name>` | Multi-entity publication ingest (yearbook, 菁英錄-style) — see **[PUBLICATION_INGEST.md](PUBLICATION_INGEST.md)** |
| `Echopedia feature <name>` | Pin/unpin a page to homepage Featured section — see [Featured section docs](#featured-section) |
| `Echopedia refresh <url/site>` | Same as website when target is a site; else archive→apply→publish push for that URL’s entity |
| `Echopedia full-domain archive <site>` | Synonym of **website** (not archive-only) |
| `Echopedia <site>` / `Echopedia <name>` | Prefer full **website** pipeline if a domain; else entity refresh + publish push |

**“Website” completeness (not optional):**  
Tier2 MANIFEST for whole domain → **entities/facts sheet** → `content/sources/` hub → rich primary page → **thin pages / links for valuable people & orgs** → hygiene → **publish push**.  
Stopping after archives or a single summary page = **PARTIAL**, not done.

**Override only if you explicitly say otherwise:**

| Override | Stops at |
|----------|----------|
| `archive only` / `Tier2 only` | `knowledge/web-archives/` only |
| `primary page only` | Skip new person/org stubs; still publish primary |
| `no publish` / `no push` | Apply to `content/` only |
| `create all member org stubs` | Expand group-member list into many thin org pages |

**Done = viewable + linked:** live GitHub Pages URLs, not merely disk files.

Agents: **do not stop after archive.** Follow `WEBSITE_INGEST.md` until COMPLETE or explicit override.

---

---

## Adding a feature (Google, Twilio, media, tools, crons, APIs)

**Same procedure for every tool** — including future **Twilio (SMS/voice)** and **photo/video generation**.  
Do **not** invent a new doc tree per product.

→ Full checklist + patterns: **[FEATURE_ADD.md](FEATURE_ADD.md)**

| Class | Example | ~Files |
|-------|---------|--------|
| A Tooling only | Gmail; chat image gen; ad-hoc SMS tool | 1–3 |
| B Scheduled | Nightly sync; Twilio webhook worker; batch video | 5–8 |
| C Echopedia-integrated | Channel → Tier2/wiki; new publish step | 8–12 |

**Prompt:**
```text
Feature add per echopedia/FEATURE_ADD.md. Classify A/B/C. List files, then implement.
```

Messaging platforms ≠ wiki dump by default. Prefer existing media tools before new vendors.
---

## System architecture (visual)

The diagram below shows the full Human → Planner → Worker → Git → Telegram flow.

**Interactive HTML:** [architecture-diagram.html](CONTROL.md) (open in browser)

**Quick reference (ASCII):**

```
 ┌──────┐   assign work   ┌────────┐   kanban assign   ┌────────┐
 │Human │ ──────────────► │Planner │ ─────────────────► │Worker  │
 │(Leonard)│              │(default│                   │(pinto) │
 └──────┘                 │profile)│                   └────┬───┘
    ▲                     └────────┘                        │
    │                                                     │
    │ reply                                               │ git add/commit/push
    │                                                     ▼
    │                                               ┌──────────┐
    │                                               │   Git    │
    │                                               │(echo-    │
    │                                               │ system)  │
    │                                               └────┬─────┘
    │                                                    │
    │                                               diff summary
    │                                                    │
    │                                              ┌─────┴─────┐
    │                                              │  Worker   │
    │                                              │(receives  │
    │                                              │ feedback)  │
    │                                              └─────┬─────┘
    │                                                    │
    │                                              deliver result
    │                                                    ▼
    │                                              ┌──────────┐
    │                                              │Telegram  │
    │                                              │(home     │
    │                                              │6769573480)│
    │                                              └────┬─────┘
    │                                                   │
    │                                              review gate
    │                                                   │
    └───────────────────────────────────────────────────┘
```

**Nodes:**

| Node | Profile | Model | Role |
|------|---------|-------|------|
| Human | — | — | Goals, approve plans, flip autonomy flags |
| Planner | `default` | Grok → NVFP4 (sticky) | Architecture design, user-facing chat, admin tasks |
| Worker | `pinto` | NVFP4 only | Kanban execution, bounded template work, depth passes |
| Git | — | — | Shared artifact store (echo-system repo) |
| Telegram | delivery target | — | Human checkpoint / review gate (6769573480) |
| Kanban | — | — | Dynamic work graph (t_* cards) |

**Edges:**

| Flow | Direction | Trigger |
|------|-----------|---------|
| Human → Planner | User → Frontier | "Echopedia …" command |
| Planner → Worker | Frontier → Local | `hermes kanban assign <task> pinto` |
| Worker → Git | Local → Artifact store | `git add/commit/push` in task workspace |
| Git → Worker | Artifact store → Local | Diff summary feedback |
| Worker → Telegram | Local → Human | `deliver` on cron or kanban result |
| Telegram → Human | Delivery → Review | Review gate |
| Telegram → Planner | Human → Frontier | User reply in chat |

See also: [AGENT_GRAPH.md](AGENT_GRAPH.md) for the full topology including nightly cron pipelines and design principles.

---

## Division of labor

| Role | Does | Does not |
|------|------|----------|
| **You (human)** | Goals, approve plans, flip autonomy flags | Run every shell command |
| **Smart model (frontier)** | Orient, plan, improve playbooks/skills, hard debug | Nightly bulk rewrite |
| **Worker (local)** | Run **one** WORKER.md playbook exactly | Invent process, invent bios, redesign |

---

## Prompt the worker (copy-paste)

Always name a playbook ID from WORKER.md:

```text
Open /home/leedt/echo-system/echopedia/WORKER.md
Run playbook P0 only.
End with the Report template. STOP.
```

```text
WORKER.md playbook P3 PATH=people/jonah-chang.md
No publish. Report. STOP.
```

```text
WORKER.md playbook P5 live. Report. STOP.
```

```text
WORKER.md playbook P6 set l3_auto_push_on_green=false
Report. STOP.
```

```text
WORKER.md P2 push. Then Report. STOP.
```

**Bad prompts for workers:** “improve linking across the wiki”, “figure out the best architecture”, “make it better”.  
**Good:** playbook ID + path + push/no-push.

---

## Prompt the smart model (planning)

```text
Follow USER_MANUAL. You are planner (not worker).
1) Read WHERE_WE_ARE + SYSTEM_STATUS + standards autonomy
2) skill_view echopedia-ops if topology matters
3) Propose: which WORKER playbook(s) in order, or skill patch if process change
4) Do not implement until I say go — unless I said implement
Topic: <...>
```

```text
Implement: assign worker playbooks P3 for these paths: ...
Then P2 commit only. You may run them or emit exact worker prompts.
```

---

## Autonomy switches (no thinking required)

Edit `/home/leedt/echo-system/echopedia/standards.json` key `autonomy`, **or** worker **P6**.

Nightly automation is **100% bash** (`no_agent`). See WORKER.md **AUTOMATED CRONS**.  
Workers never “reason through” cron prompts — only run scripts or P5/P11.

| Flag | true means |
|------|------------|
| `l2_auto_publish_on_drift` | Nightly rebuild HTML trees when MD newer |
| `l2_auto_drain_on_ci` | Nightly programmable queue drain |
| `l2_auto_commit_on_heal` | Commit heal results |
| `l3_auto_push_on_green` | Push gh-pages when ops+drift+smoke green |
| `l2_auto_featured_on_publish` | Auto-regenerate Featured section on every publish |
| `l2_auto_site_design_heal` | Nightly site-design programmable heal (04:25) |
| `l2_auto_site_design_featured` | Site-design heal may re-inject featured |
| `l2_auto_site_design_publish` | Site-design heal may publish for MD↔HTML parity |
| `l2_site_design_blocks_green` | Escalate CRITICAL site-design (default false) |

Turn off all auto-push: P6 `l3_auto_push_on_green=false`.

Schedule: 04:00 janitor+audit · **04:15 ci-heal** (includes site-design heal + **only nightly push**) · **04:30 site-design audit** · 05:00 daily improvement · 09:00 digest · + infra watchdogs.

---

## What the machine already does (don't re-ask)

- Sense queue, audit, drift, smoke
- Heal drift + optional push (L2/L3)
- Morning digest with briefs
- **Self-improvement pipeline** — continuously discovers content quality gaps and generates remediation tasks (see below)

### Self-improvement pipeline (8-stage, deterministic)

The system runs a nightly pipeline that discovers content quality gaps on the live site and wiki, then generates prioritized remediation tasks for human review:

| Stage | Time | Script | Output |
|-------|------|--------|--------|
| Scout | 04:05 | `echopedia-scout-live.sh` | `knowledge/operational/scout/latest.json` |
| Filter | 04:00 | `echopedia-content-analyzer.py` | `echopedia/content-analysis-queue.json` |
| Extract | 04:10 | `echopedia-extract-actions.py` | `knowledge/operational/extracted/<date>.json` |
| Evaluate | 04:15 | `echopedia-evaluate-actions.py` | `knowledge/operational/evaluated/<date>.json` |
| Generate | 04:20 | `echopedia-generate-cards.py` | `knowledge/operational/generated/cards/*.md` |
| Review | 05:00 (daily) | `weekly-improvement.sh` | `improvement-brief.md` |
| Remediate | 04:00 | `echopedia-janitor` | janitor queue (P8/P3/P9) |
| Publish | 04:15 | `echopedia-ci-heal` | gh-pages deploy |

**Flow:** Scout monitors the live site for 404s/slow loads → Filter applies deterministic rules to find actionable gaps → Extract maps findings to specific actions → Evaluate scores by user impact (inbound wikilinks × page type × finding severity) → Generate creates kanban task cards → Review gate summarizes for human approval → Remediate applies fixes → Publish deploys.

**Key learnings:**
- Wiki pages start with `# Heading` after frontmatter — the analyzer must skip heading-only blocks when checking description accuracy
- Pinto profile cron resolves script paths relative to `~/.hermes/profiles/pinto/scripts/` — symlinks must use `../../../scripts/` not `../../scripts/`
- Not every decision should be made by an LLM — deterministic rules handle filtering, scoring, and card generation; humans only review at the gate
---

## When to intervene (decision matrix)

The system runs 24/7: 04:00 janitor, 04:15 ci-heal, 04:30 site-design audit, 09:00 digest. **You only intervene when the matrix below says so.** Each row maps a digest/system-status signal to a concrete action (or "do nothing").

|| Situation | Matrix trigger | Your action |
||-----------|---------------|-------------|
|| System healthy, no alerts | Morning digest shows `CI: OK` / `Drift: OK` / `Janitor: clean` | **Do nothing** — system is self-healing |
|| New content source found | User says "Echopedia website/domain/publication" | **Assign work** — see Command language (full pipeline) |
|| Janitor queue > 0 | Digest shows `Janitor: queue (N)` | **Review queue** — P4 if items need human judgment; otherwise let nightly drain handle safe fixes |
|| CI drift = ACTION | Digest shows `Drift: ACTION` | **Run P5** or `echopedia-publish.sh` to rebuild trees; if persistent, investigate source |
|| CI smoke FAIL | Digest shows `CI: FAIL` | **Run P1** — ops-check + smoke-test; file incident if live site broken |
|| Site-design CRITICAL/HIGH | Digest or 04:30 audit shows critical layout issues | **Run P13** with `site-design-brief.md` — bounded local agent pass |
|| Broken links > 0 | Link hygiene reports BROKEN | **Run P3** per path — fix wikilinks to existing slugs only |
|| Page needs content update | You have new facts from a source | **Run P8** with source path — worker edits only with named source |
|| New feature/tool needed | Google, Twilio, media, new cron, API | **Feature add** — see FEATURE_ADD.md (classify A/B/C, list files) |
|| Autonomy too aggressive | Nightly push published something wrong | **Run P6** — `l3_auto_push_on_green=false`; review, then re-enable |
|| Standards/rules changed | You changed linking/ingest rules | **Bump standards.json version** — janitor auto-resweeps next run |
|| Nothing in digest is actionable | All green, no new sources, no user requests | **Do nothing** — system is working as designed |

**Red flags (always intervene):**
- `OPS_STATUS: FAIL` — missing scripts/skills (run `echopedia-ops-check.sh`, fix)
- Smoke URLs returning non-200 — live site broken
- CDN serving stale 404s for newly published pages — auto-healed by `echopedia-cdn-verify.sh`
- Git push failed — check `knowledge/operational/incidents/`
- Standards version mismatch persists > 1 day — bump not caught

**Green flags (never intervene):**
- CI = GREEN, drift = OK, smoke = OK, janitor = clean
- Uncommitted files = 0, queue = 0
- All smoke URLs 200

---

## Key metrics to watch

SYSTEM_STATUS.md (auto, 04:15) and the 09:00 digest surface these. Know what each means and when to act.

### Content health
| Metric | Green | Yellow | Red | Source |
|--------|-------|--------|-----|--------|
| **Tier1** pages (people+orgs+sources) | stable/growing (~60+) | unexplained drop | collapse | digest / SYSTEM_STATUS |
| Tier2 archive md | informational only | — | — | `content/articles/` (not wiki pages) |
| Broken wikilinks | 0 | 1–5 | >5 | `echopedia-audit-collect.sh` (Tier1 only) |
| Structural missing (frontmatter/type/identity) | 0 | 1–5 | >5 | nightly audit **critical** alert |
| Stale 90D+ | <10 | 10–20 | >20 | nightly audit |
| Orphan pages (Tier1) | <20 | 20–40 | >40 | nightly audit (full list in log, not TG) |
| CDN verify | OK | CDN_LAG / PARTIAL | BROKEN_PAGES / HOME_DOWN | `cdn-verify-status.json` |

### Pipeline health
| Metric | Green | Yellow | Red | Source |
|--------|-------|--------|-----|--------|
| Janitor queue depth | 0–5 | 6–10 | >10 | SYSTEM_STATUS |
| Uncommitted files | 0 | 1 | >1 | `git status` |
| Drift (stale HTML) | 0 | 1–5 | >5 | ci-heal brief |
| Smoke URLs OK | all 4 pass | 1 fails | >1 fail | ci-heal brief |
| Site design issues | 0 critical | 1–2 medium | any critical | site-design brief |

### Self-improvement pipeline metrics
| Metric | Green | Yellow | Red | Source |
|--------|-------|--------|-----|--------|
| Pages scanned | >100 | 50–100 | <50 | content-analysis-queue.json |
| Pages queued | <5 | 5–10 | >10 | content-analysis-queue.json |
| Generated cards | >0 | 0 | — | generated/<date>.json |
| High-priority cards | <10 | 10–20 | >20 | generated/<date>.json |
| Live site 404s | 0 | 1–2 | >2 | scout/latest.json |

### Autonomy
| Metric | Green | Yellow | Red | Source |
|--------|-------|--------|-----|--------|
| L3 push on green | True | — | False | standards.json |
| Cron failures | 0 | 1 | >1 | improvement brief |
| Last good deploy | <24h ago | 1–3 days | >3 days | SYSTEM_STATUS |

**Red = intervene.** Yellow = monitor. Green = system is self-managing.

---

## Human daily check

```bash
cat /home/leedt/echo-system/echopedia/SYSTEM_STATUS.md
# if FAIL/ACTION:
bash /home/leedt/.hermes/scripts/echopedia-ops-check.sh
bash /home/leedt/.hermes/scripts/echopedia-ci-heal.sh --dry-run
```

---

## Script references

| Script | Path | Purpose |
|--------|------|---------|
| `echopedia-publish.sh` | `~/.hermes/scripts/` | Deploy + root index.html copy + featured regen + post-push CDN verify |
| `echopedia-ci-heal.sh` | `~/.hermes/scripts/` | Nightly heal + push (includes post-push CDN verify) |
| `echopedia-ops-check.sh` | `~/.hermes/scripts/` | Health check |
| `echopedia-cdn-verify.sh` | `~/.hermes/scripts/` | Post-publish CDN 404 detection + auto-heal |
| `echopedia-link-hygiene.py` | `~/.hermes/scripts/` | Link audit |
| `echopedia-site-design-audit.py` | `~/.hermes/scripts/` | Site design audit |
| `echopedia-index-sync.py` | `~/.hermes/scripts/` | Directory index sync (new pages missing from index.md) |
| `featured-regen.py` | `echo-system/scripts/` | Featured section regen |

### Self-improvement pipeline scripts

| Script | Path | Purpose |
|--------|------|---------|
| `echopedia-scout-live.sh` | `~/.hermes/scripts/` | Stage 1: Monitor live site for 404s, slow responses, server errors |
| `echopedia-content-analyzer.py` | `~/.hermes/scripts/` | Stage 2: Filter — apply deterministic rules to find actionable content gaps |
| `echopedia-extract-actions.py` | `~/.hermes/scripts/` | Stage 3: Map finding types to specific remediation actions |
| `echopedia-evaluate-actions.py` | `~/.hermes/scripts/` | Stage 4: Score actions by user impact (inbound links × type × severity) |
| `echopedia-generate-cards.py` | `~/.hermes/scripts/` | Stage 5: Generate structured kanban task cards from evaluated actions |
| `echopedia-review-gate.py` | `~/.hermes/scripts/` | Stage 6: Summarize generated cards for daily human review |
| `echopedia-weekly-improvement.sh` | `~/.hermes/scripts/` | Stage 6: Daily review gate + improvement pack + drain + ci-heal |

---

## Publish pipeline internals

The publish script (`echopedia-publish.sh`) does the following:

1. **rsync** `content/` → `quartz/content/` (Quartz source)
2. **Build** Quartz → `quartz/public/` (HTML output)
3. **Tree-copy** subdirectories: `people/`, `organizations/`, `sources/`, `events/`, `articles/`, `tags/` from `quartz/public/` → repo root
4. **Copy root `index.html`** from `quartz/public/index.html` → repo root (homepage with theme table, etc.)
5. **Featured regen** — `featured-regen.py --inject` adds featured cards to root `index.html`
6. **Commit + push** to `gh-pages`
7. **Post-push CDN verify** — `echopedia-cdn-verify.sh --heal`

**Critical step:** Step 4 (root `index.html` copy) is required because the tree-copy in step 3 only copies subdirectories. Without it, the homepage's "Explore by theme" table and other content from `content/index.md` never reaches the live site.

### GitHub Pages build types: legacy vs unified

The wiki-public repo currently uses the **legacy** build type, which has known CDN caching issues:

| Aspect | Legacy (current) | Unified (recommended) |
|--------|-----------------|----------------------|
| **Build source** | Pre-built HTML on `gh-pages` branch | Source files in `/.github` workflows |
| **CDN cache** | Aggressively caches 404s for new files (10+ min) | Proper cache invalidation on deploy |
| **Deploy trigger** | Direct push to `gh-pages` | GitHub Actions workflow |
| **Status API** | `errored`/`succeeded` on API | `built`/`disabled` |
| **Cache headers** | `cache-control: max-age=600`, `x-cache: HIT` on stale content | Proper ETag-based invalidation |
| **Migration effort** | — | Moderate: add `.github/workflows/pages.yml`, switch source to `/.github` |

**Migration path:**
1. Create `.github/workflows/pages.yml` with a build job that runs `echopedia-publish.sh` and uploads `public/` as artifact
2. Update Pages config via API: `build_type: "workflow"`
3. Remove direct push to `gh-pages` (let Actions handle it)
4. Update `echopedia-publish.sh` to not push directly (Actions handles deploy)

**Status:** Not yet migrated. CDN caching lag is mitigated by `echopedia-cdn-verify.sh` but not eliminated.

---

## Troubleshooting → playbook

| Symptom | Playbook |
|---------|----------|
| Don’t know state | **P0** |
| Ops/drift/smoke check | **P1** |
| Cron errors / missing script | **P11** then fix script path |
| Site HTML stale | **P2** or **P5** |
| One page bad links | **P3** |
| Janitor queue | **P4** |
| Full auto heal | **P5** |
| Disable push | **P6** |
| Meta reports | **P7** |
| Content mismatch (live ≠ repo) | **P5** + `references/ui-discrepancy-investigation.md` |
|| Homepage / layout / mobile / featured bugs | **P13** (+ `SITE_DESIGN.md`) |
|| Featured pin only | **P12** or `Echopedia feature <name>` |
|| Person page exists but not in directory | **P1** (audit shows INDEX SYNC) then `echopedia-index-sync.py --apply` |

### WORKER playbook reference

| ID | Name | When to use |
|----|------|-------------|
| P0 | Orient / status | Don't know current state |
| P1 | Ops/drift/smoke | Run audit checks |
| P2 | Publish/deploy | Rebuild HTML + push |
| P3 | One page links | Fix bad links on a single page |
| P4 | Janitor queue | Process queued items |
| P5 | Heal/drift/smoke | Full auto heal + push |
| P6 | Toggle autonomy | Enable/disable flags |
| P7 | Meta reports | Generate reports |
| P8 | Edit page content | Needs source path |
| P9 | New work page | Create a new content page |
| P10 | Commit/push git | Git operations |
| P11 | Cron self-check | Diagnose cron errors |
| P12 | Featured regen | Regenerate homepage featured |
| P13 | Site design | Layout / mobile / featured bugs |

---

## Featured section

The homepage shows **Featured people** and **Featured organizations** cards. These are auto-regenerated on every publish via `featured-regen.py`.

**Hybrid model:**
- **Pinned:** `featured: true` in frontmatter — stays forever, human-controlled
- **Recency:** `last_reviewed` within last 30 days — auto-featuring, self-cleaning
- **Cap:** 6 people, 3 orgs (prevents overflow)

**How to pin a page to Featured:**
1. Add `featured: true` to the page's frontmatter
2. Publish (script auto-regenerates)

**How to unpin:**
1. Remove `featured: true` from frontmatter
2. Publish (page drops off after recency window)

**`Echopedia feature <name>`** — add or remove `featured: true` from the named page's frontmatter, then publish.

---

## Site designer / layout manager (nightly)

**Canon:** [SITE_DESIGN.md](SITE_DESIGN.md) · **Worker:** WORKER **P13** · **Cron:** 04:30 audit-only · **Heal:** inside 04:15 ci-heal before L3 push

Keeps the live site usable after content changes:

| Layer | What |
|-------|------|
| L0 audit | MD↔HTML parity, featured markers, viewport/mobile signals, stub sample, spelling sample |
| L1 heal | runs **inside ci-heal** before the single nightly push (featured root+public, parity publish) |
| L2 verify | 04:30 audit-only after push — alert if still CRITICAL/HIGH |
| L3 agent | Only via P13 + brief `AGENT_SUGGESTED` — **no freeform redesign** |

**Push rule:** heal yes → push yes, but **one pusher** (`ci-heal` L3). Site-design never pushes alone.

**Commands:**

| You say | System does |
|---------|-------------|
| `Echopedia site design` / `site audit` | Audit → `site-design-brief.md` |
| `Echopedia site heal` | Audit + programmable heal |
| Worker P13 agent | Bounded local fixes from brief |

Morning digest includes the site-design brief head.

---

## Glossary

| Term | Definition |
|------|------------|
| **Tier2** | The archived, machine-indexed copy of source material (web archives, PDF chunks, raw source files) stored under `knowledge/`. Tier2 is the input layer: structured but not yet absorbed into the wiki graph. A full-domain website ingest always produces a Tier2 MANIFEST before generating the entities/facts sheet and content pages. |
| **drift** | The condition where a source Markdown file in `content/` is newer than its deployed HTML tree (stale HTML). Measured by `echopedia-deploy-drift.sh` via mtime comparison. Drift triggers the L2 publish step in `ci-heal`. |
| **smoke** | A post-deploy liveness check that curls the `smoke_urls` from `standards.json` and verifies HTTP 200 + minimum byte count. Run by `echopedia-smoke-test.sh`. A smoke failure blocks L3 auto-push even when ops and drift are green. |
| **heal** | The L1/L2 remediation step in `ci-heal` that resolves drift (publish), runs site-design fixes (featured inject, parity), and commits results. Heal is programmable (`no_agent`) — never a freeform LLM rewrite. |
| **ci-heal** | The 04:15 nightly orchestrator (`echopedia-ci-heal.sh`) that runs ops-check → optional drain → drift→publish → site-design L1 heal → broken-link gate → smoke → L3 green-push. It is the **only** nightly pusher. |
| **L0** | Sense layer. Audit-only: collects findings into a brief + state JSON. Examples: `echopedia-site-design-audit.py` (L0 site-design), `echopedia-nightly-audit` (structural). No writes. |
| **L1** | Heal layer. Programmable, deterministic fixes driven by L0 findings. Examples: `echopedia-site-design-heal.sh` (featured-regen, parity publish), `echopedia-publish.sh`. No LLM reasoning. |
| **L2** | Gate/commit layer. Decides whether to commit heal artifacts and whether site-design issues should block green. Flags: `l2_auto_commit_on_heal`, `l2_site_design_blocks_green`. |
| **L3** | Agent/push layer. The single nightly auto-push when green (`l3_auto_push_on_green`). Also the local-worker P13 bounded pass for site-design issues that L1 could not resolve. |

---

## Recovery procedures

When something breaks, follow these runbooks. Each starts from `SYSTEM_STATUS.md` + the failing script's output. All incidents are auto-logged to `knowledge/operational/incidents/`.

### R1 — CI heal aborted (ops FAIL)

**Symptom:** `ci-heal` exits 1 with `CI: ops-check FAIL`. Push did not happen.

**Recovery:**
```bash
# 1. See what failed
bash ~/.hermes/scripts/echopedia-ops-check.sh
# 2. Fix the missing script/skill/path the check names
# 3. Re-run (dry-run first)
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
bash ~/.hermes/scripts/echopedia-ci-heal.sh
```

**Common causes:** missing script in `~/.hermes/scripts/`, skill directory deleted, `content/people` or `quartz-v4` dir missing, standards version not seen by janitor.

---

### R2 — Drift remains after publish

**Symptom:** `DRIFT_STATUS: ACTION` after `ci-heal` ran publish. Stale HTML or missing HTML pages.

**Recovery:**
```bash
# 1. See which pages are stale
bash ~/.hermes/scripts/echopedia-deploy-drift.sh
# 2. Force rebuild (build trees only, no push)
bash ~/.hermes/scripts/echopedia-publish.sh
# 3. Re-check
bash ~/.hermes/scripts/echopedia-deploy-drift.sh
# 4. If still stale, push manually
bash ~/.hermes/scripts/echopedia-publish.sh --push
```

**Root cause:** `npx quartz build` may silently skip pages with malformed frontmatter. Check the page's YAML header for syntax errors.

---

### R3 — Smoke test failure

**Symptom:** `SMOKE_STATUS: FAIL` — live URLs returning non-200 or <500 bytes.

**Recovery:**
```bash
# 1. Which URL(s) failed
bash ~/.hermes/scripts/echopedia-smoke-test.sh
# 2. If just deployed, wait 30s for CDN then re-test
sleep 30 && bash ~/.hermes/scripts/echopedia-smoke-test.sh
# 3. If still failing: the page may be missing from the tree
#    Check if HTML exists locally
ls ~/echo-system/people/<slug>.html
# 4. If missing, run publish to rebuild trees
bash ~/.hermes/scripts/echopedia-publish.sh
```

**Note:** Smoke failure blocks L3 auto-push. After fixing, ci-heal will push on the next green cycle.

---

### R3b — CDN 404 lag (pages exist but live site returns 404)

**Symptom:** A page was just published but `curl https://echocanhelp.github.io/wiki-public/people/<name>` returns 404. The HTML file exists on `gh-pages` (raw.githubusercontent.com returns 200) but the live site is serving a stale CDN cache.

**Recovery:**
```bash
# 1. Verify it's CDN lag (not a real broken page)
bash ~/.hermes/scripts/echopedia-cdn-verify.sh --paths people/<name>.html

# 2. If CDN lag detected, force auto-heal
bash ~/.hermes/scripts/echopedia-cdn-verify.sh --heal --paths people/<name>.html

# 3. Or manually force a Pages rebuild
#    (append a cache-buster comment, commit, push)
echo "<!-- cache-refresh: $(date +%s) -->" >> ~/echo-system/people/<name>.html
cd ~/echo-system && git add people/<name>.html && git commit -m "cdn-heal: force cache invalidation" && git push origin gh-pages

# 4. Wait 30s for CDN propagation, then re-check
sleep 30 && curl -sS -o /dev/null -w "%{http_code}" -L "https://echocanhelp.github.io/wiki-public/people/<name>"
```

**Note:** This is automatically handled after every `echopedia-publish.sh --push` and `echopedia-ci-heal.sh` via the post-push CDN verification step. See skill `echopedia-cdn-heal`.

---

### R4 — Git push failure

**Symptom:** `git push origin gh-pages` fails in `ci-heal`. `last-good-deploy.json` is stale.

**Recovery:**
```bash
# 1. See the error
cd ~/echo-system
git push origin gh-pages 2>&1 | tail -20
# 2. Common: non-fast-forward — fetch and retry
git fetch origin
git push origin gh-pages
# 3. If auth: refresh gh CLI token
gh auth login
# 4. If still failing, push manually after publish
bash ~/.hermes/scripts/echopedia-publish.sh --push
```

---

### R5 — Broken wikilinks

**Symptom:** `echopedia-nightly-audit` or janitor reports broken `[[wikilinks]]`.

**Recovery:**
```bash
# 1. Run the audit to see broken links
bash ~/.hermes/scripts/echopedia-audit-collect.sh
# 2. Fix by editing the source page — correct the slug
#    Slug format: people/<kebab-name> or organizations/<kebab-name>
# 3. Verify the target page exists
ls ~/echo-system/content/people/<slug>.md
# 4. Re-run audit to confirm
```

**Tip:** Use `echopedia-link-hygiene.py` for bulk fixes. Worker playbook **P3** handles single-page link fixes.

---

### R6 — Site design / layout / featured bugs

**Symptom:** Homepage featured cards missing, mobile layout broken, HTML not matching MD.

**Recovery:**
```bash
# 1. Run site-design audit
bash ~/.hermes/scripts/echopedia-site-design-wrapper.sh
# 2. If CRITICAL/HIGH: run heal
bash ~/.hermes/scripts/echopedia-site-design-heal.sh
# 3. If featured cards stale: regenerate
python3 ~/echo-system/scripts/featured-regen.py --root ~/echo-system --inject
# 4. Publish to apply
bash ~/.hermes/scripts/echopedia-publish.sh --push
```

**Playbook:** **P13** for agent-assisted layout fixes. See `SITE_DESIGN.md`.

---

### R7 — Janitor queue stuck

**Symptom:** `janitor-state.json` queue depth growing across nights. Pages not draining.

**Recovery:**
```bash
# 1. Check queue
python3 -c "import json; d=json.load(open('~/echo-system/echopedia/janitor-state.json')); print(len(d.get('queue',[])))"
# 2. Run drain manually
python3 ~/.hermes/scripts/echopedia-queue-drain.py
# 3. Check brief for details
cat ~/echo-system/echopedia/janitor-brief.md
```

**Note:** Queue drain is programmable only (`auto_apply_agent: false`). If queue grows, either standards changed (bump version so janitor resweeps) or pages need manual review.

---

### R8 — Standards version mismatch

**Symptom:** `OPS_WARN: standards v6 not yet seen by janitor (seen=5)`.

**Recovery:**
```bash
# The next 04:00 janitor run will resweep. To force now:
bash ~/.hermes/scripts/echopedia-janitor-wrapper.sh
# Then verify
bash ~/.hermes/scripts/echopedia-ops-check.sh
```

---

### R9 — Quartz build failure

**Symptom:** `PUBLISH_FAIL` or `npx quartz build` errors during publish.

**Recovery:**
```bash
# 1. Run build manually to see full error
cd ~/quartz-v4
npx quartz build 2>&1 | tail -30
# 2. Common: malformed frontmatter in a content page
#    Check recently edited pages for YAML syntax
# 3. If a specific page fails, temporarily move it aside
mv ~/echo-system/content/people/bad-page.md /tmp/
# 4. Re-run publish
bash ~/.hermes/scripts/echopedia-publish.sh
# 5. Restore and fix the page
mv /tmp/bad-page.md ~/echo-system/content/people/
```

---

### R10 — Cron job failures

**Symptom:** `CRON_STATUS: FAIL` from cron selfcheck, or a cron job stopped delivering.

**Recovery:**
```bash
# 1. Run selfcheck
bash ~/.hermes/scripts/echopedia-cron-selfcheck.sh
# 2. Check specific job output
#    List jobs:
hermes cron list
# 3. Re-run a failed job
hermes cron run <job_id>
# 4. If script not executable:
chmod +x ~/.hermes/scripts/<script>
```

---

### R11 — Uncommitted files blocking clean push

**Symptom:** `ci-heal` commits heal but push fails on non-fast-forward, or `SYSTEM_STATUS` shows high uncommitted count.

**Recovery:**
```bash
cd ~/echo-system
# 1. See what's uncommitted
git status --short
# 2. Commit content changes
git add content/ people/ organizations/ sources/ echopedia/
git commit -m "manual: content sync"
# 3. Push
git push origin gh-pages
```

**Note:** `l3_auto_push_on_green` requires `require_clean_git_for_push: false` (current default). If you change that to true, uncommitted files will block push.

---

### R12 — Featured section not updating

**Symptom:** Homepage featured cards don't reflect `featured: true` in frontmatter.

**Recovery:**
```bash
# 1. Verify frontmatter has featured: true
grep -r "featured: true" ~/echo-system/content/
# 2. Regenerate featured section
python3 ~/echo-system/scripts/featured-regen.py --root ~/echo-system --dry-run
python3 ~/echo-system/scripts/featured-regen.py --root ~/echo-system --inject
# 3. Verify markers in index.html
grep -A2 "featured-start" ~/echo-system/index.html
# 4. Publish
bash ~/.hermes/scripts/echopedia-publish.sh --push
```

---

### Quick reference: recovery command order

```bash
# Start here — always
cat ~/echo-system/echopedia/SYSTEM_STATUS.md

# Then pick your scenario:
bash ~/.hermes/scripts/echopedia-ops-check.sh          # R1, R8
bash ~/.hermes/scripts/echopedia-deploy-drift.sh       # R2
bash ~/.hermes/scripts/echopedia-smoke-test.sh         # R3
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run  # R1, R2, R3
bash ~/.hermes/scripts/echopedia-publish.sh            # R2, R9
bash ~/.hermes/scripts/echopedia-publish.sh --push     # R2, R4
bash ~/.hermes/scripts/echopedia-cron-selfcheck.sh     # R10
ls ~/echo-system/knowledge/operational/incidents/      # all incidents
```

---

## Document ownership

| Change | Update |
|--------|--------|
| How human assigns work | **USER_MANUAL** |
| Exact worker steps | **WORKER.md** |
| New tool / Google / cron feature | **FEATURE_ADD.md** (+ only listed files) |
| Mission built/remains | **WHERE_WE_ARE** |
| Live health | auto **SYSTEM_STATUS** |
| Official script list / routing | skill **echopedia-ops** |
| Behavior flags | **standards.json** (+ version bump) |
| Full-domain website ingest | **WEBSITE_INGEST.md** |
| Publication (PDF) ingest | **PUBLICATION_INGEST.md** |
| Site design / layout | **SITE_DESIGN.md** |
| Org/work topology | **AGENT_GRAPH.md** |
| General ingestion protocol | skill **echopedia-ingestion-protocol** |
| Large document ingestion | skill **large-document-ingestion**

---

## Script path references

| Script | Path | When to run | Owner |
|--------|------|-------------|-------|
| `publish.sh` | `~/.hermes/scripts/echopedia-publish.sh` | Build HTML trees + tree-copy; `--commit` / `--push` / `--check` | Worker P2/P5 |
| `ci-heal.sh` | `~/.hermes/scripts/echopedia-ci-heal.sh` | Nightly L2/L3 heal + push (04:15); `--dry-run` / `--no-drain` | Worker P5 |
| `ops-check.sh` | `~/.hermes/scripts/echopedia-ops-check.sh` | Health check; exit 0 OK, 1 FAIL | Worker P1/P11 |
| `link-hygiene.py` | `~/.hermes/scripts/echopedia-link-hygiene.py` | Link quality audit; `--path <slug>` for single page | Worker P3 |

---

---

## Before you push

Run this checklist before any manual publish or when the nightly ci-heal push is about to fire. Each item has a one-line verification command.

### 1. System health

```bash
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
```

- [ ] `OPS_STATUS` is OK (no missing scripts/skills)
- [ ] `DRIFT_STATUS` is OK (no stale HTML)
- [ ] `SMOKE_STATUS` is OK (live URLs returning 200)
- [ ] `JANITOR_STATUS` is clean or draining
- [ ] No CRITICAL/HIGH in site-design brief

### 2. Git state

```bash
cd ~/echo-system && git status --short
```

- [ ] Working tree is clean, **or** dirty changes are intentional and committed
- [ ] `git log --oneline -3` shows expected recent commits
- [ ] Branch is `main` (or the intended publish branch)

### 3. Autonomy flags

```bash
grep l3_auto_push_on_green ~/echo-system/echopedia/standards.json
```

- [ ] `l3_auto_push_on_green` is `true` (unless you intentionally disabled it)
- [ ] `l2_auto_commit_on_heal` is `true` (unless you need manual commit control)
- [ ] `l2_auto_publish_on_drift` is `true`

### 4. Build verification

```bash
bash ~/.hermes/scripts/echopedia-publish.sh --check
```

- [ ] Build completes without errors
- [ ] No malformed frontmatter in recently edited pages
- [ ] HTML tree includes all expected pages

### 5. Smoke test

```bash
bash ~/.hermes/scripts/echopedia-smoke-test.sh
```

- [ ] All `smoke_urls` from `standards.json` return HTTP 200
- [ ] All smoke URLs return >500 bytes
- [ ] If just deployed, wait 30s for CDN then re-test

### 6. Featured section

```bash
python3 ~/echo-system/scripts/featured-regen.py --root ~/echo-system --dry-run
```

- [ ] `featured: true` pages are in frontmatter
- [ ] Recency-based candidates (last_reviewed ≤ 30 days) exist
- [ ] Featured section is not empty (if candidates exist)

### 7. Link hygiene

```bash
bash ~/.hermes/scripts/echopedia-link-hygiene.py --path all
```

- [ ] No broken `[[wikilinks]]`
- [ ] No broken external links in recently edited pages
- [ ] Slug format is correct: `people/<kebab-name>` or `organizations/<kebab-name>`

### 8. Final gate

- [ ] All above checks pass
- [ ] You have reviewed the diff summary
- [ ] Ready to push: `bash ~/.hermes/scripts/echopedia-publish.sh --push`

**If any check fails:** stop, fix the issue, and re-run the checklist. Do not push with `SMOKE_STATUS: FAIL` or `OPS_STATUS: FAIL`.

---

## Contract

1. Humans start at **USER_MANUAL**.  
2. Workers execute only **WORKER.md** playbooks.  
3. Smart models plan and improve playbooks; they don’t dump philosophy into the worker context mid-task.  
4. One lesson → one place (skill **or** WORKER step **or** script)—not all three.

---

*Keep USER_MANUAL short. Put execution detail only in WORKER.md.*

## Changelog

This section tracks manual changes to USER_MANUAL.md. Auto-generated content (briefs, SYSTEM_STATUS) is not listed here.

| Date | Change |
|------|--------|
| 2026-08-02 | Ops harden: restored missing canon docs. Nightly audit TG body hard-capped (~3.5KB; full log in `echopedia/logs/`). Digest/SYSTEM_STATUS/watchdog count **Tier1 only**. CDN verify absolute-path false BROKEN_PAGES fixed; `cdn-verify-status.json`. Dirty-tree gitignore for build HTML + Tier2 + ops briefs. `vault-search-index-rebuild` → no_agent Sun 05:30; restored `vault_search.py`. |
| 2026-07-31 | Content analyzer total_pages_scanned fix; nightly audit excludes `content/articles/`; ops-check REQUIRED_SCRIPTS expanded; standards auto_apply_programmable + auto_commit. |
| 2026-07-30 | Improvement pipeline weekly→daily (05:00). |
| 2026-07-21 | Consolidated intervene decision matrix. |
| 2026-07-19 | Site-design autonomy flags + 04:30 audit; P12/P13 troubleshooting. |
| 2026-07-18 | Hybrid featured + site design manager section. |
| 2026-07-17 | PUBLICATION_INGEST command + routing. |
| 2026-07-16 | Command language for website/publication/feature defaults. |
| 2026-07-15 | Initial operator entry point. |

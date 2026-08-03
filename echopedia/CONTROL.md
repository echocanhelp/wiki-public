# Echopedia / Pinto — Control, Management & Safe Usage

**Purpose:** How we **control**, **manage**, and **document** the system so it improves without corruption.  
**Audience:** Human operator (Hsuperman) + planner models + local workers.  
**Status:** Canon (2026-08-02). Update when control surfaces change — not on every bugfix.  
**Related:** [USER_MANUAL.md](USER_MANUAL.md) (commands) · [WORKER.md](WORKER.md) (playbooks) · [WHERE_WE_ARE.md](WHERE_WE_ARE.md) (mission) · `standards.json` (autonomy) · skill `echopedia-ops` (map only) · skill **`go-router`** (universal entry)

---

## 0. Universal entry (only surface you need to remember)

### You say:

```text
go <plain language>
```

Examples: `go status` · `go add fact about X from Y` · `go fix nightly audit` · `go` (alone = orient)

**You do not** pick CONTROL vs manual vs ops vs Echopedia vs P#.  
**The agent** loads skill `go-router`, applies this file’s invariants, auto-classifies, and touches **one SSOT**.

Bare messages without `go` on this system are treated the same as `go <message>` (user will forget the prefix).

| Your words | Agent routes to |
|------------|-----------------|
| status / healthy / broken / docs | health (SYSTEM_STATUS, docs-sync) |
| person/org + fact / source | Echopedia P8 content |
| website / domain | WEBSITE_INGEST |
| cron / nightly / job | cron SSOT + docs-sync |
| publish / ship | P2 / ci-heal |
| build / plan / epic | plan + kanban |
| turn off push / L3 | standards P6 |
| (unclear) | orient once, then act |

Full classifier: skill **`go-router`**.

---

## 1. Mental model (one sentence)

**Machine truth runs the system; thin docs steer humans; skills capture pitfalls; plans die after work.**

```
You say: go <intent>
        → go-router classifies
        → change ONE SSOT
        → scripts/crons execute
        → status/digest observe
        → skill pitfall OR standards bump (learn once)
```

If you change the same fact in three markdown files, you are **corrupting** the system (drift), even if every sentence is “true” today.

---

## 2. Control surfaces (how you actually steer)

Use the **highest** surface that can do the job. Never jump to freestyle edits when a surface exists.

| Priority | Surface | What it controls | How you use it |
|----------|---------|------------------|----------------|
| **1** | **Telegram commands** | Day-to-day content & ops | `Echopedia <entity> <fact>` · `Echopedia website <domain>` · `ops` / status (when wired) |
| **2** | **`standards.json`** | Autonomy level, auto-commit, auto-push, quality rules | Edit flags only via WORKER **P6** or explicit “set L3 off” |
| **3** | **Cron (`jobs.json` via hermes cron)** | Schedule, no_agent, script, deliver | `hermes cron list/edit` — **never** hand-duplicate tables into 4 docs |
| **4** | **Scripts under `~/.hermes/.../scripts/`** | Deterministic behavior | Patch script → test manually → commit if in repo |
| **5** | **WORKER playbooks P0–P13** | Bounded agent work | Assign **one** playbook + path; worker STOP after Report |
| **6** | **Kanban** | Multi-step work visibility | Create → claim → complete with result; link plans |
| **7** | **Git (`echo-system`)** | Published wiki + canon docs | Small commits; Tier1 paths; no secrets |
| **8** | **Skills** | Recurring how-to + pitfalls | Patch after hard bugs; not a second USER_MANUAL |
| **9** | **Plans (`~/.hermes/plans/`)** | One-off implementation | Execute → CLOSE; promote lesson to skill/script |

### What each role may touch

| Role | May | Must not |
|------|-----|----------|
| **Human** | Intent, approve L3 risks, P6 autonomy, content facts with source | Raw freestyle on prod scripts without verify |
| **Planner (frontier)** | Choose playbook IDs, patch WORKER/skills when process wrong, write plans | Bulk invent wiki prose; silent multi-file “cleanup” |
| **Worker (local)** | **One** WORKER playbook, exact commands | Redesign, new crons, rewrite USER_MANUAL, restart gateways in cron |
| **Cron (no_agent)** | Listed scripts only | LLM reasoning, gateway restart, unbounded git push except ci-heal rules |

---

## 3. Single sources of truth (SSOT)

| Fact | SSOT | Projections (read-only / generated) |
|------|------|-------------------------------------|
| Cron schedule & mode | pinto `cron/jobs.json` | SYSTEM_STATUS, digest, (future docs-sync) |
| Autonomy | `echopedia/standards.json` | SYSTEM_STATUS, ci-heal behavior |
| Wiki content | `content/people\|organizations\|sources` | Live site via publish/ci-heal |
| Live health | scripts → `SYSTEM_STATUS.md`, `cdn-verify-status.json`, `*-brief.md` | Morning digest |
| How to assign work | `USER_MANUAL.md` (thin) | — |
| Exact worker steps | `WORKER.md` | — |
| Mission / remains | `WHERE_WE_ARE.md` | — |
| Recurring pitfalls | **one** skill SKILL.md | — |
| User prefs | Hermes `MEMORY.md` / `USER.md` | — |
| Member/LINE private | identity + interactions (never public git) | — |

**Rule:** Change the SSOT. Regenerate or wait for cron to refresh projections. Do not “fix” a projection by hand and leave SSOT stale.

---

## 4. Safe usage methods (do this)

### 4.1 Daily operator (you)

1. Read morning **digest** (System group).  
2. **Green → do nothing.**  
3. Actionable line → one command or one kanban/playbook.  
4. New fact about a person/org →  
   `Echopedia <name> <fact>` (implies P8 → verify → publish path per USER_MANUAL).  
5. New website domain →  
   `Echopedia website <domain>` (full WEBSITE_INGEST bar, not Tier2-only).

### 4.2 “Something feels wrong”

```
1) SYSTEM_STATUS.md / digest
2) WORKER P0 or P1 (orient / ops-check dry-run)
3) Only then deep debug (skill + scripts)
```

Do **not** start by rewriting docs or adding crons.

### 4.3 Change behavior (code/ops)

```
1) Reproduce with one script command
2) Patch script (or WORKER step if process)
3) Manual run; confirm stdout/exit
4) If cron: hermes cron edit (pin no_agent + relative script)
5) One git commit if repo-owned
6) ONE doc/skill update at the true SSOT
7) Kanban complete with verify evidence
```

### 4.4 Change schedule

```
hermes cron list
hermes cron edit <id> --schedule '...' --no-agent --script name.sh
```
Then **either** wait for docs-sync **or** update WHERE_WE_ARE/WORKER cron section **once** — prefer generated inventory when docs-sync exists.

### 4.5 Document a lesson

| Lesson type | Write here | Example |
|-------------|------------|---------|
| Script footgun | skill `## Pitfalls` | CDN absolute paths |
| New human command | USER_MANUAL command table only | `Echopedia feature` |
| New worker steps | WORKER playbook only | P8 source required |
| Mission done/remaining | WHERE_WE_ARE | TJ archive status |
| Autonomy policy | standards.json | l3_auto_push_on_green |
| Preference | MEMORY/USER | “no HITL if possible” |
| One-off project | plan + kanban | then CLOSE |

**One lesson → one place.** If you write it thrice, delete two copies.

### 4.6 Publish / push

- Prefer **ci-heal 04:15** (only nightly pusher).  
- Manual: WORKER **P2** / `echopedia-publish.sh` path only — not ad-hoc `git push` of partial trees.  
- After push: CDN status file / smoke — not vibes.

### 4.7 Models / spend

- **Default local** (Laguna) for TAHS/private/LINE-adjacent.  
- **Grok** for architecture/planning when needed.  
- **Cron = no_agent** unless there is a written exception in this file.  
- Never leave agent crons unpinned after `/model` switches.

---

## 5. Corruption modes (do **not** do this)

| Corruption | Why it breaks things | Repair |
|------------|----------------------|--------|
| **Triple-write** same cron/metric in USER_MANUAL + WHERE + skill | Guaranteed drift | SSOT + delete copies |
| **Hand-edit SYSTEM_STATUS / briefs** as source of truth | Overwritten next cron; false confidence | Delete hand edits; re-run generator |
| **Count Tier2 articles as “pages”** | 29k false firehose | Tier1-only metrics in scripts |
| **Uncapped audit/connector dumps to Telegram** | Timeouts, alert fatigue | Caps + full log on disk |
| **Agent cron “run script then summarize”** | Skips tools / invents OK | no_agent wrapper |
| **Cron auto-restart gateway** | Scheduler blocks / loops | Alert only; human/delegate restart |
| **Symlink scripts into profile scripts/** | Security guard blocks | **File copy** |
| **Commit secrets / identity / .env** | Irreversible risk | gitignore + gitleaks |
| **Commit root HTML emit / public/** as content | Dirty tree forever | gitignore build outputs |
| **Freestyle worker redesign** | Inconsistent wiki + broken publish | One playbook STOP |
| **Invent biographies** | Trust death | Source-required P8 |
| **Legacy AGENTS.md / old bridges as live** | Wrong ports/models | Quarantine deprecated |
| **MEMORY.md for task logs / PATs** | Context rot + leaks | session_search + vault |
| **Plan forever, never CLOSE** | Zombie work | Complete kanban + stamp plan |
| **docs without verify** | Beautiful lies | Require command output in result |

---

## 6. Documentation management rules

### 6.1 Doc classes

| Class | Examples | Edit when | Max intent |
|-------|----------|-----------|------------|
| **Canon steer** | USER_MANUAL, WORKER, WHERE_WE_ARE, this file | Process/mission/control change | Short, stable |
| **Policy machine** | standards.json | Autonomy/quality | JSON only |
| **Generated** | SYSTEM_STATUS, *-brief, cdn-verify-status, audit-state | **Never hand-edit as SSOT** | Scripts only |
| **Domain runbook** | WEBSITE_INGEST, SITE_DESIGN, FEATURE_ADD | That domain changes | One topic |
| **Skill** | echopedia-*, cron-job-management | Pitfalls & commands | Executable truth |
| **Plan** | `.hermes/plans/*` | During implementation | Disposable |
| **Legacy** | AGENTS.md migration novel | Read-only archive | Don’t extend |

### 6.2 Definition of done for any change

- [ ] SSOT updated (not only a projection)  
- [ ] Script/cron verified with real output  
- [ ] At most **one** human doc or **one** skill patched for the lesson  
- [ ] Kanban completed with evidence  
- [ ] No new agent cron  
- [ ] No secrets  
- [ ] Tier1 git dirty only if intentional content  

### 6.3 Doc OS — `echopedia-docs-sync.sh` (shipped)

```bash
bash ~/.hermes/scripts/echopedia-docs-sync.sh          # sense
bash ~/.hermes/scripts/echopedia-ops-check.sh         # includes docs-sync gate
```

- Cron inventory **generated** from pinto `jobs.json` → `SYSTEM_STATUS` markers + `cron-inventory.generated.md`
- Link-check CONTROL/USER_MANUAL/WORKER/WHERE/FEATURE_ADD
- WORKER P0–P13 routing coverage
- Writes `docs-status.json` · digest shows **Docs:** line · actionables on FAIL/WARN
- Wired into `echopedia-system-status.sh` and `echopedia-ops-check.sh`
- Hand-edited generated cron blocks → overwritten on next sync (by design)

After cron edits: run docs-sync (or wait for system-status/ci-heal). Optional: still note mission impact in WHERE_WE_ARE once.

---

## 7. Operational cadence (manage without babysitting)

| When | System does | You do |
|------|-------------|--------|
| Continuous | Watchdog, thermal | Nothing if silent |
| 04:00–04:30 | Sense → heal → push path | Sleep |
| 05:00 | Review pack / memory audit | Skim if digest later flags |
| 09:00 | Digest | **Only** act on Actionables |
| Weekly Sun | Vault index rebuild | Nothing if silent |
| Ad hoc | — | Commands / one playbook / one plan epic |

**Intervention rule (from USER_MANUAL):**  
If digest is all green and you have no new source/fact → **do nothing**. That *is* management.

---

## 8. Correct patterns cheat-sheet

### Add automation
```
script in profiles/pinto/scripts/ (copy, +x)
→ manual bash script.sh (silent success / alert fail)
→ hermes cron edit/create --no-agent --script name.sh --deliver telegram:-5543616648
→ NOT an agent prompt
```

### Fix a bug found at 2am
```
reproduce → patch script → manual verify → skill pitfall one paragraph → commit
→ do not rewrite USER_MANUAL
```

### Improve the wiki
```
source-backed P8/P9 or website ingest
→ ci-heal or P2 publish
→ never bulk-edit 29k Tier2 as if Tier1
```

### Architecture change
```
plan file + kanban epic
→ implement with verify
→ WHERE_WE_ARE remains + standards if autonomy
→ CLOSE plan
```

### “Make docs better”
```
prefer delete/dedupe/generate over new essays
→ this CONTROL file for governance
→ USER_MANUAL stays the human cockpit only
```

---

## 9. Hard invariants (corruption = violation)

1. **ci-heal is the only nightly pusher** (site-design does not push alone).  
2. **Cron jobs that touch prod behavior are `no_agent`.**  
3. **Tier1 metrics ≠ Tier2 archive counts.**  
4. **Telegram messages stay small**; full logs on disk under `echopedia/logs/`.  
5. **Private identity / LINE / .env never in public git.**  
6. **Workers run one playbook and STOP.**  
7. **Deliver ops crons to System** `telegram:-5543616648`, not random DMs.  
8. **Profile scripts are real files**, not symlinks to global.  
9. **Generated status files are not hand SSOT.**  
10. **One lesson → one place.**

---

## 10. Quick reference paths

| Need | Path |
|------|------|
| This constitution | `echopedia/CONTROL.md` |
| Human commands | `echopedia/USER_MANUAL.md` |
| Worker steps | `echopedia/WORKER.md` |
| Mission | `echopedia/WHERE_WE_ARE.md` |
| Live health | `echopedia/SYSTEM_STATUS.md` |
| Autonomy | `echopedia/standards.json` |
| CDN last check | `echopedia/cdn-verify-status.json` |
| Map skill | `echopedia-ops` |
| Cron truth | `~/.hermes/profiles/pinto/cron/jobs.json` |
| Scripts | `~/.hermes/profiles/pinto/scripts/` + repo `echo-system/scripts/` |
| Plans | `~/.hermes/plans/` |

---

## 11. Bootstrap for a new session / new model

```
1. Read CONTROL.md (this file) — how not to corrupt
2. Read SYSTEM_STATUS.md — is it on fire?
3. If content work: USER_MANUAL command language → WORKER playbook
4. If infra work: cron list + scripts; no freestyle
5. Load echopedia-ops only as map, not as a second manual
```

---

*Control is not more documentation. Control is few surfaces, hard SSOTs, deterministic execution, and refusing duplicate truths.*

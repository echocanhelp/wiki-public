# Echopedia OS — Where We Are

*Living snapshot of the vibe-coded Echopedia system. Update when autonomy level, major crons, or mission status changes. Not a second copy of procedures — those live in skills / jobs.json.*

**Last reviewed:** 2026-08-09  
**Standards:** v8 · **Autonomy:** L3 · **Overnight crons:** all `no_agent` (agent=0)  
**Start here:** [USER_MANUAL.md](USER_MANUAL.md) · [CONTROL.md](CONTROL.md) · workers: [WORKER.md](WORKER.md)  
**Entry:** `go <plain language>` → skill `go-router`  
**Hub skill:** `echopedia-ops` · **Cron SSOT:** pinto `cron/jobs.json` (see generated inventory in SYSTEM_STATUS)

---

## Mission progress

| Layer | Status |
|-------|--------|
| **Content** | Albert / FPCLA / NTPC / co-founders / foreword authors; dissertation work page + GitHub full text |
| **Linking** | First-mention + sources callouts; deepeners write Timeline / Quotes / Network |
| **Large docs** | Archive → chunks → fact sheet → apply (not full PDF in context) |
| **Protocol hub** | `go-router` + `echopedia-ops` first → single map |
| **Nightly sense** | Content analysis → janitor queue + structural audit (local wall clock; see table) |
| **Self-improve** | Scout → Filter → Extract → Evaluate → Generate → Review → Remediate → Publish (deterministic) |
| **L2/L3 autonomy** | `ci-heal` heals drift, smoke, green → auto-push |
| **Human map** | **Morning brief** (NEED YOU) + digest + SYSTEM_STATUS + this file |
| **Telegram labels** | ✅ AUTO · 🟡 QUEUE · 🔴 NEED YOU · ℹ️ INFO — [cron-notify-labels.md](../knowledge/operational/cron-notify-labels.md) |
| **Live-site continuity** | Sunday **source-continuity** (TC · GSTPC · ITPC); registry lifecycle — [source-continuity.md](../knowledge/operational/source-continuity.md) |
| **First-answer card / next-ingest** | EVO-5: card UX + metrics; Sunday recommend ≤2 — [echopedia-first-path.md](../knowledge/operational/echopedia-first-path.md) |
| **Identity close-loop** | EVO-3: soft pending → QUEUE; CLI `identity-decide.py` — [identity-close-loop.md](../knowledge/operational/identity-close-loop.md) |
| **Clean URLs** | Tier1 trailing-slash → `slug/index.html` redirect (publish step) |

### Self-improvement pipeline (deployed)

All stages **`no_agent`** (no LLM in overnight path):

1. **Filter** (03:05) — content-analysis  
2. **Audit** (03:10) — nightly structural audit (alert-only critical)  
3. **Remediate queue** (03:50) — janitor prioritize / queue  
4. **Scout** (04:05) — live site UX  
5. **Extract → Evaluate → Generate** (04:15 / 04:20 / 04:25) — staggered  
6. **Deepen** (04:40–05:20) — backlink / quotes / timeline (content AUTO writes)  
7. **Publish** (08:00) — ci-heal L2/L3  
8. **Review** (Sun 07:05) — weekly-improvement pack + review gate  

**Human surface (last content brief):** `vault-morning-brief` **07:55** — NEED YOU ≤5 first.  
**Cron self-heal:** `cron-audit` 06:50 · `cron-self-audit` 08:30 (schedule restore + missed-run guards).

**Folded (paused as Telegram):** `vault-unfinished-threads`, `vault-connector-suggestions`, `vault-intelligence-digest` — collectors still run **via morning-brief** (disk), not separate spam.

**Pipeline outputs:** `knowledge/operational/scout/` → `echopedia/content-analysis-queue.json` → `extracted/` → `evaluated/` → `generated/` → briefs under `echopedia/*-brief.md`

---

## Live automation (local wall clock on pinto)

SSOT times: `hermes cron list` / SYSTEM_STATUS generated table. Narrative summary:

| When (local) | Job | Role |
|--------------|-----|------|
| every 1m | `vllm-thermal-scaler` | Adaptive GPU/thermals (silent when cool) |
| every 30m | `unified-watchdog` · `kanban-sync` | Health + board sync (silent OK) |
| 03:05 | content-analysis · output-rotate | Filter + log hygiene |
| 03:10 | nightly-audit | Structural sense (alert if critical) |
| 03:50 | janitor | Queue safe remediation candidates |
| 04:05–04:06 | scout · person-works-linker | Live UX + works links |
| 04:15–04:30 | extract · evaluate · generate · site-design | Pipeline + design |
| 04:40–05:20 | backlink · quotes · timeline | Page deepening AUTO |
| 05:30 Sun | vault-search-index-rebuild | Search index |
| **Sun 06:00** | **source-continuity** | **Live-site watch (TC/GSTPC/ITPC) → delta AUTO → next-ingest tips** |
| 06:50 | cron-audit | Empty-schedule / missed-run / deliver guards |
| **08:00** | **ci-heal** | **Only nightly pusher** (L2 heal + L3 green) |
| 07:10 | docs-sync | Doc OS sense + cron inventory regen |
| 07:20 | digest | System dashboard (tagged) |
| 07:50 | memory-audit | Silent unless MEMORY/USER issues |
| **07:55** | **vault-morning-brief** | **Primary human surface** (+ SOURCE CONTINUITY / NEXT INGEST) |
| 08:30 | cron-self-audit | Schedule integrity + sequence |
| Sun 07:05 | weekly-improvement | Review gate + pack |

### Autonomy flags (`echopedia/standards.json` → `autonomy`)
- L2: publish on drift, drain on CI, commit heal  
- L3: `l3_auto_push_on_green` when ops ≠ FAIL, drift OK, smoke OK  
- Turn off push: set `l3_auto_push_on_green: false`

### State files
| Path | Purpose |
|------|---------|
| `echopedia/standards.json` | Rules + autonomy version |
| `echopedia/SYSTEM_STATUS.md` | **Auto** machine snapshot (crons, queue, last good) |
| `echopedia/WHERE_WE_ARE.md` | **This** human narrative |
| `echopedia/janitor-state.json` | Queue |
| `echopedia/last-good-deploy.json` | Last green push |
| `echopedia/*-brief.md` | Janitor / CI / improvement / intake |
| `knowledge/operational/intelligence/` | Morning brief, NEED YOU, unfinished |
| `knowledge/operational/cron-notify-labels.md` | Telegram tag contract |
| `knowledge/operational/source-continuity.md` | Live-site watch lifecycle |
| `knowledge/operational/source-watch-registry.json` | Watched live sites SSOT |
| `knowledge/operational/echopedia-first-path.md` | First-answer → NEED YOU path |
| `knowledge/operational/incidents/` | Failures |

---

## What remains

### Owner judgment (recurring)
- **🔴 NEED YOU** in morning brief only (identity links, true FAILs) — ignore 🟡 QUEUE unless opening a batch epic  
- Current open example class: pending LINE/Echopedia identity confirms  

### Content (optional backlog)
- Janitor `NO_SAFE_ACT` body-link pages (agent/human batch)  
- Intake missing-page noise (~500 cross-refs — no auto-create)  
- Broken-link mass (~1.6k, parser noisy — gate skipped)  
- Timeline/quote over-match quality tune  
- Misfiled pages / GSTPC OCR / homepage dual inject  

### Autonomy gaps (L4+)
- Local agent body-link drain still programmable-only  
- P13 site-design agent pass remains human-triggered  
- Hard broken-link gate when parser is trustworthy  
- WORKER thin playbook **P14** (docs WARN only)

### Not autonomous (by design)
- Inventing biographies  
- Unbounded agents / frontier nightly rewrites  
- Auto thin-page creation from gaps without identity approve  

---

## If something is wrong

```bash
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
cat ~/echo-system/echopedia/WHERE_WE_ARE.md
bash ~/.hermes/profiles/pinto/scripts/echopedia-ops-check.sh
bash ~/.hermes/profiles/pinto/scripts/echopedia-ci-heal-wrapper.sh   # or ci-heal.sh --dry-run
ls ~/echo-system/knowledge/operational/incidents/
# cron SSOT
hermes cron list
python3 ~/.hermes/profiles/pinto/scripts/cron-audit.py
```

**Telegram rule:** only reply to **🔴 NEED YOU**. ✅ AUTO and 🟡 QUEUE are machine/backlog.  
**Canon:** `go <intent>` → go-router → one SSOT.  
**One-line:** Self-managing groundskeeper (sense → heal → smoke → push → report) + morning NEED YOU; remains = quality backlog, not rebuild.

---

## How to update this doc

| Change | Update |
|--------|--------|
| New cron / autonomy level | This file **once** + `standards.json`; schedule table comes from docs-sync → SYSTEM_STATUS |
| Daily queue / last push / uncommitted | Leave to **SYSTEM_STATUS.md** (auto) |
| Telegram label contract | `knowledge/operational/cron-notify-labels.md` |
| Procedure steps | Patch **canon skill** or script, not this essay |
| Ephemeral task status | kanban only |

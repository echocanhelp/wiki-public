# Echopedia OS — Where We Are

*Living snapshot of the vibe-coded Echopedia system. Update when autonomy level, major crons, or mission status changes. Not a second copy of procedures — those live in skills / jobs.json.*

**Last reviewed:** 2026-08-21  
**Standards:** v10 · **Autonomy:** L3 · **Overnight crons:** all `no_agent` (agent=0)  
**Start here:** [USER_MANUAL.md](USER_MANUAL.md) · [CONTROL.md](CONTROL.md) · workers: [WORKER.md](WORKER.md)  
**Entry:** `go <plain language>` → skill `go-router`  
**Hub skill:** `echopedia-ops` · **Cron SSOT:** pinto `cron/jobs.json` (see generated inventory in SYSTEM_STATUS)

---

## Mission progress

| Layer | Status |
|-------|--------|
| **Content** | Albert / FPCLA / NTPC / co-founders / foreword authors; dissertation work page + GitHub full text. **Inclusion:** CONTROL §1b (allies in archive, ≤1-layer thicken, no exclusion stamps) |
| **Linking** | First-mention + sources callouts; deepeners write Timeline / Quotes / Network |
| **Large docs** | Archive → chunks → fact sheet → apply (not full PDF in context) |
| **Protocol hub** | `go-router` + `echopedia-ops` first → single map |
| **Nightly sense** | Content analysis → janitor queue + structural audit (local wall clock; see table) |
| **Self-improve** | Scout → Filter → Extract → Evaluate → Generate → Review → Remediate → Publish (deterministic) |
| **L2/L3 autonomy** | `ci-heal` heals drift, smoke, green → auto-push |
| **Human map** | **Morning brief** (NEED YOU + AUTO ledger ≤8) + digest + SYSTEM_STATUS + this file |
| **Telegram labels** | ✅ AUTO · 🟡 QUEUE · 🔴 NEED YOU · ℹ️ INFO — [cron-notify-labels.md](../knowledge/operational/cron-notify-labels.md) |
| **Live-site continuity** | Sunday **source-continuity** (TC · GSTPC · ITPC · PCT · laijohn · TA.org story-corpus) — [source-continuity.md](../knowledge/operational/source-continuity.md) |
| **Story / book / social receive** | **Ingest** = wiki + **P2**. Magazines: vault + work pages A/B/C + **Stories**. `archive only` = vault. Hub-only = PARTIAL — [WEBSITE_INGEST.md](WEBSITE_INGEST.md) |
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

**Human surface (last content brief):** `vault-morning-brief` **08:15** — NEED YOU ≤5 first; AUTO strip from `autonomy-ledger.json`.  
**Cron self-heal:** `cron-audit` 06:00 · `cron-self-audit` 06:40 (schedule restore + missed-run guards).

**Folded (paused as Telegram):** `vault-unfinished-threads`, `vault-connector-suggestions`, `vault-intelligence-digest` — collectors still run **via morning-brief** (disk), not separate spam.

**Pipeline outputs:** `knowledge/operational/scout/` → `echopedia/content-analysis-queue.json` → `extracted/` → `evaluated/` → `generated/` → briefs under `echopedia/*-brief.md`

---

## Live automation (local wall clock on pinto)

SSOT times: `hermes cron list` / SYSTEM_STATUS generated table. Narrative summary:

| When (local) | Job | Role |
|--------------|-----|------|
| every 1m | `vllm-thermal-scaler` | Adaptive GPU/thermals (silent when cool) |
| every 30m | `unified-watchdog` · `kanban-sync` | Health + board sync (silent OK) |
| **01:10** | **content-analysis** | Daily content-quality audit (auto-heal) |
| 01:15 | nightly-audit | Structural sense (alert if critical) |
| **01:30** | **janitor** | Queue safe remediation candidates |
| 01:40 | scout-live | Live UX gaps (404s, slow) |
| 01:50 | backlink-auditor | Inbound link audit |
| **02:00** | **extract-actions** | Findings → actionable cards (pipeline) |
| 02:10 | evaluate-actions | Score by impact (pipeline) |
| 02:20 | generate-cards | Build remediation task cards (pipeline) |
| **02:30** | **person-works-linker** | Link people ↔ works (AUTO) |
| 02:40 | quote-extractor | Quote mining (AUTO) |
| **03:00** | **timeline-builder** | Deepen timelines (AUTO) |
| 03:15 | output-rotate | Log/output hygiene |
| **03:30** | **ci-heal** | **Only nightly pusher** (L2 heal + L3 green) |
| **03:45** | **site-design** | **Audit-only after ci-heal push** |
| **06:00** | **cron-audit** | Empty-schedule / missed-run / deliver guards |
| 06:10 | docs-sync | Doc OS sense + cron inventory regen |
| **06:20** | **digest** | System dashboard (tagged) |
| 06:30 | memory-audit | Silent unless MEMORY/USER issues |
| **06:40** | **cron-self-audit** | Schedule integrity + sequence |
| **Sun 05:30** | **vault-search-index-rebuild** | Search index rebuild |
| **Sun 07:00** | **source-continuity** | **Live-site watch (TC/GSTPC/ITPC/PCT) → delta AUTO → next-ingest tips** |
| Sun 07:15 | weekly-improvement | Review gate + pack |
| **08:15** | **vault-morning-brief** | **Primary human surface** (+ SOURCE CONTINUITY / NEXT INGEST) |
| `knowledge/operational/incidents/` | Failures |

---

## What remains

### Owner judgment (recurring)
- **🔴 NEED YOU** in morning brief only (identity links, true FAILs) — ignore 🟡 QUEUE unless opening a batch epic  
- Current open example class: pending LINE/Echopedia identity confirms  

### Content (optional backlog)
- Janitor HOLD leftovers only (SFTS-as-person, `LINK_BODY_SPARSE` section-order, already-linked) — not a body-link human batch  
- Intake missing-page noise (~500 cross-refs — no auto-create)  
- Broken-link mass (~1.6k, parser noisy — gate skipped)  
- Timeline/quote over-match quality tune  
- Misfiled pages / GSTPC OCR / homepage dual inject  

### Autonomy gaps (L4+)
- B auto-GO: gated kicker OK to code; do **not** fire untagged ready cards (pct.org.tw / bai-weiwei / TAH.org)
- C: archive ZH-B3–B6 only; do **not** retry ntpc/laijohn/ZH as-is
- D1 decay **shipped** in analyzer; D2 page enrich **not** enabled (identity)
- P13 site-design agent pass remains human-triggered

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

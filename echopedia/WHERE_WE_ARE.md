# Echopedia OS — Where We Are

*Living snapshot of the vibe-coded Echopedia system. Update when autonomy level, major crons, or mission status changes. Not a second copy of procedures — those live in skills.*

**Last reviewed:** 2026-08-02  
**Standards:** v8 · **Autonomy:** L3  
**Control:** [CONTROL.md](CONTROL.md) (how to steer without corruption)  
**Start here:** [USER_MANUAL.md](USER_MANUAL.md) · workers: [WORKER.md](WORKER.md)  
**Hub skill:** `echopedia-ops`  
**Live site:** https://echocanhelp.github.io/wiki-public/  
**Content shape:** Tier1 wiki ≈61 md (people/orgs/sources) · Tier2 archive ≈29k under `content/articles/` (not counted as wiki pages)

---

## Mission progress

| Layer | Status |
|-------|--------|
| **Content** | Albert / FPCLA / NTPC / co-founders / foreword authors; dissertation work page + GitHub full text |
| **Linking** | First-mention + sources callouts; `echopedia-link-hygiene.py` |
| **Large docs** | Archive → chunks → fact sheet → apply (not full PDF in context) |
| **Protocol hub** | `echopedia-ops` first → single map |
| **Nightly sense** | Janitor queue + structural audit (04:00) |
| **Self-improve** | **8-stage pipeline** (Scout → Filter → Extract → Evaluate → Generate → Review → Remediate → Publish) |
| **L2/L3 autonomy** | 04:15 `ci-heal`: heal drift, smoke, green → auto-push |
| **Human map** | This file + `SYSTEM_STATUS.md` (machine-generated) + morning digest |

### Self-improvement pipeline (Stage 1–5 deployed)

The system now continuously discovers content quality gaps and generates remediation tasks:

1. **Scout** (04:05) — `echopedia-scout-live.sh` monitors the live website for 404s, slow responses, server errors
2. **Filter** (04:00) — `echopedia-content-analyzer.py` applies deterministic rules to find actionable gaps (fixed: DESC_TOO_SHORT false positive eliminated)
3. **Extract** (04:10) — `echopedia-extract-actions.py` maps each finding to a specific remediation action
4. **Evaluate** (04:15) — `echopedia-evaluate-actions.py` scores actions by user impact (inbound wikilinks × page type × finding severity)
5. **Generate** (04:20) — `echopedia-generate-cards.py` creates structured kanban task cards
6. **Review** (05:00 daily) — `echopedia-weekly-improvement.sh` summarizes generated cards for human approval (name is historical; schedule is daily)
7. **Remediate** (04:00) — `echopedia-janitor` processes approved cards via P8/P3/P9 playbooks
8. **Publish** (04:15) — `echopedia-ci-heal` builds + deploys on green

**Pipeline outputs:** `knowledge/operational/scout/` → `echopedia/content-analysis-queue.json` → `knowledge/operational/extracted/` → `knowledge/operational/evaluated/` → `knowledge/operational/generated/` → `improvement-brief.md`

### Lai dissertation (planned ingest)
- Full text **archived** (Tier 2 + chunks)
- High-value knowledge **on wiki** (not every chapter as prose)
- Publish path **encoded** (`echopedia-publish.sh`)
- Nightly machine **keeps standards** without being asked

---

## Live automation

| When | Job | Role |
|------|-----|------|
| 04:00 | `echopedia-janitor` | Sense / prioritize / queue |
| 04:00 | `echopedia-nightly-audit` | Structural audit; **capped TG report** + full log under `echopedia/logs/` |
| 04:00 | `echopedia-content-analysis` | Filter: find actionable content gaps |
| 04:05 | `echopedia-scout-live` | Scout: monitor live site for UX issues |
| 04:10 | `echopedia-extract-actions` | Extract: map findings to remediation actions |
| 04:15 | `echopedia-evaluate-actions` | Evaluate: score by user impact |
| **04:15** | **`echopedia-ci-heal`** | L2 heal + **site-design L1** + L3 **single push** + CDN verify |
| 04:20 | `echopedia-generate-cards` | Generate: create kanban task cards |
| **04:30** | **`echopedia-site-design`** | Post-deploy **audit-only** (alerts; no push) |
| 05:00 daily | `echopedia-weekly-improvement` | Review gate + improvement pack (name historical) |
| Sun 05:30 | `vault-search-index-rebuild` | **no_agent** vault index rebuild (Tier1-focused) |
| 09:00 | `echopedia-digest` | Infra + **Tier1** wiki counts + CDN status + actionables |
| **On publish** | **`featured-regen`** | Hybrid featured: pinned + recency → homepage cards (root + public) |
| every 30m | `unified-watchdog` | Infra + **Tier1** git drift only |
| every 1m | `vllm-thermal-scaler` | Adaptive thermal (silent when cool) |

### Autonomy flags (`echopedia/standards.json` → `autonomy`)
- L2: publish on drift, drain on CI, commit heal
- L3: `l3_auto_push_on_green` when ops ≠ FAIL, drift OK, smoke OK
- Turn off push: set `l3_auto_push_on_green: false`

### State files
| Path | Purpose |
|------|---------|
| `echopedia/standards.json` | Rules + autonomy version |
| `echopedia/SYSTEM_STATUS.md` | **Auto** machine snapshot (crons, queue, last good) |
| `echopedia/WHERE_WE_ARE.md` | **This** human narrative (mission + remains) |
| `echopedia/janitor-state.json` | Queue |
| `echopedia/last-good-deploy.json` | Last green push |
| `echopedia/cdn-verify-status.json` | Last CDN verify (digest/SYSTEM_STATUS) |
| `echopedia/audit-state.json` | Nightly audit history |
| `echopedia/logs/nightly-audit-*.txt` | Full audit dump (not Telegram) |
| `echopedia/*-brief.md` | Janitor / CI / improvement / intake |
| `cache/cache.db` | Vault search index (local, gitignored) |
| `knowledge/operational/janitor-log/` | Run logs |
| `knowledge/operational/incidents/` | Failures |

---

## What remains

### Content (optional backlog)
- Janitor queue (body first-mentions, thin pages)
- Intake noise filters (false “entities”)
- More co-founders only if A-tier facts
- Short Ch I–III blurbs (archive OK today)
- `content/index.md` (Quartz home warning)
- Misfiled pages (SFTS / audiobook kits under people/)
- GSTPC flipbook OCR (PNG-only)

### Autonomy gaps (L4+)
- Local agent body-link drain (programmable only today)
- P13 site-design agent pass remains human-triggered (nightly is script-only)
- Log → auto skill patches
- Hard broken-link gate (parser noisy)
- Deprecate legacy `echopedia_publish_*` scripts (WARN only)
- Keep `standards_version_seen` in sync after bumps (next janitor run)
- Homepage still dual (`index.html` + Quartz `public/index.html`) — site-design keeps both featured-injected

### Self-improvement pipeline (completed)
- ✅ 8-stage pipeline deployed (Scout → Filter → Extract → Evaluate → Generate → Review → Remediate → Publish)
- ✅ All 8 stages are deterministic (`no_agent`) — no LLM in the pipeline
- ✅ Human review gate at daily improvement (05:00; job name still “weekly”)
- ✅ Metrics tracked in SYSTEM_STATUS.md (**Tier1 page counts**, not Tier2 archive)
- ✅ Documentation in USER_MANUAL.md + echopedia-ops skill
- ✅ 2026-08-02 ops harden: audit delivery cap, CDN path fix, dirty-tree policy, vault index no_agent
- ✅ All 21 pinto crons deliver to System `telegram:-5543616648`; agent crons = 0

### Not autonomous (by design)
- Inventing biographies
- Unbounded agents / frontier nightly rewrites
- Open-ended “self-evolving” wiki prose

---

## If something is wrong

```bash
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
cat ~/echo-system/echopedia/WHERE_WE_ARE.md
bash ~/.hermes/scripts/echopedia-ops-check.sh
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
ls ~/echo-system/knowledge/operational/incidents/
```

**Canon:** skill `echopedia-ops` → then the skill it names.  
**One-line:** Self-managing groundskeeper (sense → heal → smoke → push → report) + solid core pages; remains = quality backlog, not rebuild from zero.

---

## How to update this doc

| Change | Update |
|--------|--------|
| New cron / autonomy level | This file + `standards.json` + ops skill table |
| Daily queue / last push / uncommitted | Leave to **`SYSTEM_STATUS.md`** (auto) |
| Procedure steps | Patch **canon skill**, not this essay |
| Ephemeral task status | kanban only |

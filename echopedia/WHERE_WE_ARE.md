# Echopedia OS — Where We Are

*Living snapshot of the vibe-coded Echopedia system. Update when autonomy level, major crons, or mission status changes. Not a second copy of procedures — those live in skills.*

**Last reviewed:** 2026-07-15  
**Standards:** v5 · **Autonomy:** L3  
**Start here:** [USER_MANUAL.md](USER_MANUAL.md) · workers: [WORKER.md](WORKER.md)  
**Hub skill:** `echopedia-ops`

---

## Mission progress

| Layer | Status |
|-------|--------|
| **Content** | Albert / FPCLA / NTPC / co-founders / foreword authors; dissertation work page + GitHub full text |
| **Linking** | First-mention + sources callouts; `echopedia-link-hygiene.py` |
| **Large docs** | Archive → chunks → fact sheet → apply (not full PDF in context) |
| **Protocol hub** | `echopedia-ops` first → single map |
| **Nightly sense** | Janitor queue + structural audit (04:00) |
| **Self-improve** | Drift, freshness, intake, entity hints, weekly pack |
| **L2/L3 autonomy** | 04:15 `ci-heal`: heal drift, smoke, green → auto-push |
| **Human map** | This file + `SYSTEM_STATUS.md` (machine-generated) + morning digest |

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
| 04:00 | `echopedia-nightly-audit` | Structural audit; incident on fail |
| **04:15** | **`echopedia-ci-heal`** | L2 heal + L3 green push |
| Mon 05:00 | `echopedia-weekly-improvement` | Improvement pack + drain + ci-heal |
| 09:00 | `echopedia-digest` | Janitor + CI + SYSTEM_STATUS |

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
| `echopedia/*-brief.md` | Janitor / CI / improvement / intake |
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
- Log → auto skill patches
- Hard broken-link gate (parser noisy)
- Deprecate legacy `echopedia_publish_*` scripts (WARN only)
- Keep `standards_version_seen` in sync after bumps (next janitor run)

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

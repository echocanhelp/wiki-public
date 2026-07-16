# Echopedia User Manual

**This is your single starting point** for understanding and changing the system.

If you only open one file, open **this one**. Everything else is linked from here.

| Path | Role |
|------|------|
| **This manual** | How to operate & change the system |
| [WHERE_WE_ARE.md](WHERE_WE_ARE.md) | What’s built / what remains (mission) |
| [SYSTEM_STATUS.md](SYSTEM_STATUS.md) | Live health (auto-generated) |
| skill `echopedia-ops` | Agent routing map (load first) |
| [standards.json](standards.json) | Rules + autonomy switches |

Vault root: `~/echo-system` · Scripts: `~/.hermes/scripts/echopedia-*` · Live site: https://echocanhelp.github.io/wiki-public/

---

## 1. What this system is

Echopedia is TAHS’s wiki plus an **automated operating layer**:

- **Wiki content** → `content/people|organizations|sources/` → Quartz → GitHub Pages  
- **Knowledge (not all public)** → `knowledge/` (archives, fact sheets, interactions, logs)  
- **Agent map** → Hermes skill `echopedia-ops`  
- **Nightly machine** → janitor, audit, **ci-heal** (heal + optional auto-push)  
- **Morning brief** → `echopedia-digest` (Telegram/admin)

You do **not** need to remember every script. You need this manual + the three docs above.

---

## 2. Daily / weekly check (human)

```bash
# Morning or when curious
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
cat ~/echo-system/echopedia/WHERE_WE_ARE.md   # when planning work, not every day

# If digest said FAIL / ACTION
bash ~/.hermes/scripts/echopedia-ops-check.sh
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
ls ~/echo-system/knowledge/operational/incidents/
```

**Healthy:** silent crons, digest without FAIL, `last good deploy` recent, uncommitted ≈ 0.  
**Unhealthy:** open incidents, CI_STATUS FAIL, drift ACTION that won’t clear, ops FAIL.

---

## 3. How to talk to the agent (copy-paste)

### Always for system work

```text
Follow the Echopedia User Manual (echopedia/USER_MANUAL.md).

1) Orient: skill_view(echopedia-ops), read WHERE_WE_ARE + SYSTEM_STATUS + standards.json autonomy
2) Summarize control points and risks
3) Plan only — wait for my go unless I said implement
```

### Content work (pages, ingest, links)

```text
Echopedia content work per USER_MANUAL + echopedia-ops first.
Then: large-document-ingestion if big file, else echopedia-ingestion-protocol.
No invented bios. First-mention links + sources callouts. Publish via echopedia-publish.sh.
```

### Change automation / autonomy

```text
Per USER_MANUAL § Changes.
Orient first. Prefer a flag in standards.json autonomy over a new cron.
Verify with ops-check and ci-heal --dry-run. Document topology in ops; mission shift in WHERE_WE_ARE.
```

### Something broken

```text
Per USER_MANUAL § Troubleshooting.
Read SYSTEM_STATUS, ci-heal-brief, incidents. Run ops-check. Diagnose from script output. No drive-by refactors.
```

---

## 4. Point of control (what to change for what)

| I want to… | Change this |
|------------|-------------|
| Turn off auto-push to GitHub | `standards.json` → `autonomy.l3_auto_push_on_green: false` |
| Turn off auto rebuild on drift | `autonomy.l2_auto_publish_on_drift: false` |
| Turn off nightly queue drain in CI | `autonomy.l2_auto_drain_on_ci: false` |
| Force resweep of pages after new rules | Bump `standards.json` **`version`** |
| Change how pages are written/linked | Skill `echopedia-ingestion-protocol` / `wiki-linking` |
| Change large PDF process | Skill `large-document-ingestion` |
| Change routing / which script is official | Skill `echopedia-ops` |
| Mission “built vs remains” narrative | `WHERE_WE_ARE.md` |
| Live health snapshot | Auto → `SYSTEM_STATUS.md` (don’t hand-edit forever) |
| One-line agent preference | MEMORY only (tiny) |
| Task list | kanban |

**Behavior knobs = `standards.json`.**  
**Navigation = this manual + `echopedia-ops`.**

---

## 5. Making changes (correct sequence)

```
1. Orient (manual §3 prompt)
2. Plan (files, SoT, verify, rollback, standards bump?)
3. You say “go”
4. Implement ONE canon place
5. Verify: ops-check, hygiene, publish --check / ci-heal --dry-run
6. If rules/autonomy changed → bump standards version
7. If topology/cron/mission changed → ops + WHERE_WE_ARE
8. Report: what changed, how to disable, verify output
```

### Do / don’t

| Do | Don’t |
|----|--------|
| Start from **this manual** | Start from a random script name in chat |
| Prefer flags over new permanent jobs | Add a 5th publish script |
| Programmable heal before agent rewrite | Frontier model rewriting wiki at 4 AM |
| Tree copy publish (`echopedia-publish.sh`) | Flatten HTML to repo root |
| One lesson → one skill | Copy procedures into MEMORY and three READMEs |

---

## 6. Autonomy levels (what the machine does alone)

| Level | Does | Does not |
|-------|------|----------|
| **L1** | Sense + brief | Fix |
| **L2** (on) | Drift → rebuild; optional drain; commit heal | Invent bios |
| **L3** (on) | Push `gh-pages` when ops≠FAIL, drift OK, smoke OK | Push when red |

Schedule: **04:15** `echopedia-ci-heal`. Details: `WHERE_WE_ARE.md`, skill ops.

---

## 7. Common tasks (commands)

```bash
# Health
bash ~/.hermes/scripts/echopedia-ops-check.sh
bash ~/.hermes/scripts/echopedia-system-status.sh

# Links on one page
python3 ~/.hermes/scripts/echopedia-link-hygiene.py --path people/albert-s-lai.md

# Publish (build + tree copy; optional commit/push)
bash ~/.hermes/scripts/echopedia-publish.sh --check
bash ~/.hermes/scripts/echopedia-publish.sh --push -m "your message"

# Full L2/L3 cycle (or dry-run)
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
bash ~/.hermes/scripts/echopedia-ci-heal.sh

# Improvement pack + programmable drain
bash ~/.hermes/scripts/echopedia-improvement-collect.sh --drain

# New dissertation/work page stub
python3 ~/.hermes/scripts/echopedia-source-stub.py --help
```

---

## 8. Troubleshooting

| Symptom | Check |
|---------|--------|
| Site stale | `deploy-drift.sh` → `publish.sh` or wait for 04:15 ci-heal |
| Auto-push unwanted | `l3_auto_push_on_green: false` |
| Cron errors | `hermes cron list`; `knowledge/operational/incidents/` |
| Agent ignores process | Remind: “USER_MANUAL + echopedia-ops first” |
| Don’t know what’s left | `WHERE_WE_ARE.md` |
| Don’t know if healthy | `SYSTEM_STATUS.md` |
| Map vs scripts disagree | `ops-check.sh` |

---

## 9. Document map (anti-scatter)

```
USER_MANUAL.md          ← you start here (this file)
├── WHERE_WE_ARE.md     ← mission narrative
├── SYSTEM_STATUS.md    ← auto health
├── standards.json      ← switches + version
├── *-brief.md          ← last night’s work
└── (agent) echopedia-ops → canon skills → scripts
```

Update **this manual** when: how a *human* should operate changes.  
Update **WHERE_WE_ARE** when: built/remains story changes.  
Update **ops** when: topology/scripts/crons change.  
Leave **SYSTEM_STATUS** to automation.

---

## 10. One-line contract

> **Start from the User Manual → orient on WHERE_WE_ARE + SYSTEM_STATUS + ops + standards → plan → one canon change → verify with scripts → document only the map/mission if topology or story changed.**

---

*Maintainer note: keep this file short enough to read in 5 minutes. Link out; don’t paste full skill text here.*

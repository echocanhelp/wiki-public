# Echopedia System Status

*Generated: 2026-08-26 03:31 PDT*

## Orientation
- **Entry:** go <plain language> via go-router (auto-route) · **Control:** [CONTROL.md](CONTROL.md)
- **User manual (commands):** [USER_MANUAL.md](USER_MANUAL.md)
- **Worker playbooks:** [WORKER.md](WORKER.md)
- **Mission / remains:** [WHERE_WE_ARE.md](WHERE_WE_ARE.md)
- **This file:** auto machine snapshot (refreshed by system-status / ci-heal)

## Autonomy
- **Standards:** v10
- **Level:** L3
- **L2 auto-publish on drift:** True
- **L3 auto-push when green:** True
- **Last good deploy:** `0d231e9753`
- **Last night (ledger):** analyzer scanned 1 queued 0 suppressed 1765 · 🟡 QUEUE janitor HOLD leftover 40 · 🟡 QUEUE kanban blocked 6 · 🔴 NEED YOU cron fail: echopedia-janitor, cron-audit, cron-self-audit
- **Track SSOT:** `knowledge/operational/intelligence/autonomy-ledger.json`

## Content
|- **Tier1 pages:** 2848 (people 2402 / orgs 429 / sources 17) · Tier2 archive: 29103
|- **Janitor queue depth:** 40
|- **Uncommitted files:** 1895

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | 04:05 local | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | 03:05 local | 1 scanned, 0 queued |
|| Extract | echopedia-extract-actions | 04:15 local | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | 04:20 local | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | 04:25 local | 3 cards |
|| Review | weekly-improvement | Sun 07:05 local | improvement-brief.md |
|| Human | vault-morning-brief | 07:55 local | NEED YOU ≤5 |

## What runs automatically
See **Cron inventory (generated)** at bottom (SSOT: pinto \`jobs.json\` via \`echopedia-docs-sync.sh\`). Do not hand-edit.

## If something is wrong
```bash
bash ~/.hermes/scripts/echopedia-ops-check.sh
bash ~/.hermes/scripts/echopedia-deploy-drift.sh
bash ~/.hermes/scripts/echopedia-ci-heal.sh --dry-run
bash ~/.hermes/scripts/echopedia-publish.sh --check
cat ~/echo-system/echopedia/WHERE_WE_ARE.md
cat ~/echo-system/echopedia/SYSTEM_STATUS.md
ls ~/echo-system/knowledge/operational/incidents/
```

## Canon map
Load skill **echopedia-ops** first for any wiki work.

## Cron snapshot
```
    Name:      cron-output-rotate
    Schedule:  15 3 * * *
    Last run:  2026-08-26T03:15:02.329554-07:00  ok
    Name:      vault-morning-brief
    Schedule:  15 8 * * *
    Last run:  2026-08-25T08:15:21.339106-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-26T03:31:04.713969-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  10 1 * * *
    Last run:  2026-08-26T01:10:35.804641-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-26T03:14:02.484034-07:00  ok
    Name:      echopedia-digest
    Schedule:  20 6 * * *
    Last run:  2026-08-25T06:20:03.085483-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-26T03:05:06.165395-07:00  error: Script exited with code 1
    Name:      memory-audit
    Schedule:  30 6 * * *
    Last run:  2026-08-25T06:30:02.119068-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  15 1 * * *
    Last run:  2026-08-26T01:26:17.359355-07:00  ok
    Name:      echopedia-janitor
    Schedule:  30 1 * * *
    Last run:  2026-08-26T01:37:34.521961-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  15 7 * * 0
    Last run:  2026-08-23T07:19:03.747492-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  30 3 * * *
    Last run:  2026-08-25T03:34:24.922544-07:00  ok
    Name:      echopedia-site-design
    Schedule:  45 3 * * *
    Last run:  2026-08-25T03:46:00.488597-07:00  ok
    Name:      vault-search-index-rebuild
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=27 agent=0 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 2 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 0 3 * * * | `echopedia-timeline-builder` | no_agent | on | ok | `echopedia-timeline-builder-cron.sh` |
| 0 6 * * * | `cron-audit` | no_agent | on | error | `cron-audit.py` |
| 0 7 * * 0 | `echopedia-source-continuity` | no_agent | on | ok | `echopedia-source-continuity.sh` |
| 10 1 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 10 2 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 10 6 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 15 1 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 15 3 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 15 7 * * 0 | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 15 8 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 20 2 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 20 6 * * * | `echopedia-digest` | no_agent | on | ok | `echopedia-digest.sh` |
| 30 1 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 30 2 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 30 3 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 30 6 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 40 1 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 40 2 * * * | `echopedia-quote-extractor` | no_agent | on | ok | `echopedia-quote-extractor-cron.sh` |
| 40 6 * * * | `cron-self-audit` | no_agent | on | error | `cron-self-audit.py` |
| 45 3 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 50 1 * * * | `echopedia-backlink-auditor` | no_agent | on | ok | `echopedia-backlink-auditor-cron.sh` |
| 50 7 * * * | `echopedia-tier1-sweep` | no_agent | on | ok | `echopedia-tier1-sweep.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | error | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

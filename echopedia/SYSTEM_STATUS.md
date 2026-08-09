# Echopedia System Status

*Generated: 2026-08-09 11:52 PDT*

## Orientation
- **Entry:**  (auto-route) · **Control:** [CONTROL.md](CONTROL.md)
- **User manual (commands):** [USER_MANUAL.md](USER_MANUAL.md)
- **Worker playbooks:** [WORKER.md](WORKER.md)
- **Mission / remains:** [WHERE_WE_ARE.md](WHERE_WE_ARE.md)
- **This file:** auto machine snapshot (refreshed by system-status / ci-heal)

## Autonomy
- **Standards:** v8
- **Level:** L3
- **L2 auto-publish on drift:** True
- **L3 auto-push when green:** True
- **Last good deploy:** `1dd63bc20f`

## Content
|- **Tier1 pages:** 305 (people 207 / orgs 89 / sources 9) · Tier2 archive: 29103
|- **Janitor queue depth:** 5
|- **Uncommitted files:** 59730

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | daily 04:05 | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | daily 04:00 | 0 scanned, 0 queued |
|| Extract | echopedia-extract-actions | daily 04:10 | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | daily 04:15 | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | daily 04:20 | 0 cards |
|| Review | weekly-improvement | Mon 05:00 | improvement-brief.md |

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
    Schedule:  5 3 * * *
    Last run:  2026-08-09T11:36:03.348007-07:00  ok
    Name:      vault-morning-brief
    Schedule:  55 7 * * *
    Last run:  2026-08-08T05:05:26.632524-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-09T11:51:05.697013-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  5 3 * * *
    Last run:  2026-08-08T04:01:00.054844-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-09T11:25:03.294075-07:00  ok
    Name:      echopedia-digest
    Schedule:  20 7 * * *
    Last run:  2026-08-07T09:00:02.770749-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-09T11:38:04.481565-07:00  ok
    Name:      memory-audit
    Schedule:  55 7 * * *
    Last run:  2026-08-08T05:00:57.645655-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  10 3 * * *
    Last run:  2026-08-08T04:50:50.860577-07:00  ok
    Name:      echopedia-janitor
    Schedule:  50 3 * * *
    Last run:  2026-08-08T04:01:18.908303-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  5 7 * * *
    Last run:  2026-08-08T05:21:09.512029-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  0 7 * * *
    Last run:  2026-08-07T04:36:22.538968-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  50 6 * * *
    Last run:  2026-08-07T08:00:07.021065-07:00  ok
    Name:      vault-connector-suggestions
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=28 agent=9 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 5 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 0 5 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 0 5 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 0 5 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 0 7 * * * | `echopedia-ci-heal` | AGENT | on | ok | `—` |
| 10 3 * * * | `echopedia-nightly-audit` | AGENT | on | ok | `—` |
| 10 7 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 15 7 * * * | `vault-connector-suggestions` | AGENT | on | ok | `—` |
| 20 7 * * * | `echopedia-digest` | no_agent | on | ok | `echopedia-digest.sh` |
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 35 6 * * * | `echopedia-timeline-builder` | AGENT | on | ok | `—` |
| 45 8 * * * | `cron-self-audit` | no_agent | on | ok | `cron-self-audit.py` |
| 5 3 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 5 3 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 5 4 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 5 5 * * * | `echopedia-backlink-auditor` | AGENT | on | ok | `—` |
| 5 7 * * * | `echopedia-weekly-improvement` | AGENT | on | ok | `—` |
| 50 3 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 50 5 * * * | `echopedia-quote-extractor` | AGENT | on | ok | `—` |
| 50 6 * * * | `cron-audit` | no_agent | on | ok | `cron-audit.py` |
| 50 6 * * * | `vault-unfinished-threads` | no_agent | on | ok | `vault-unfinished-threads.py` |
| 55 7 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 55 7 * * * | `vault-morning-brief` | AGENT | on | ok | `—` |
| 6 4 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 6 7 * * * | `vault-intelligence-digest` | AGENT | on | ok | `—` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | ok | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

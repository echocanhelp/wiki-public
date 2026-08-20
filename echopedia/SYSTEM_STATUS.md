# Echopedia System Status

*Generated: 2026-08-20 08:06 PDT*

## Orientation
- **Entry:** go <plain language> via go-router (auto-route) · **Control:** [CONTROL.md](CONTROL.md)
- **User manual (commands):** [USER_MANUAL.md](USER_MANUAL.md)
- **Worker playbooks:** [WORKER.md](WORKER.md)
- **Mission / remains:** [WHERE_WE_ARE.md](WHERE_WE_ARE.md)
- **This file:** auto machine snapshot (refreshed by system-status / ci-heal)

## Autonomy
- **Standards:** v8
- **Level:** L3
- **L2 auto-publish on drift:** True
- **L3 auto-push when green:** True
- **Last good deploy:** `8b3b19ea94`

## Content
|- **Tier1 pages:** 2843 (people 2402 / orgs 427 / sources 14) · Tier2 archive: 29103
|- **Janitor queue depth:** 20
|- **Uncommitted files:** 1

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | 04:05 local | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | 03:05 local | 2848 scanned, 0 queued |
|| Extract | echopedia-extract-actions | 04:15 local | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | 04:20 local | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | 04:25 local | 0 cards |
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
    Schedule:  0 3 * * *
    Last run:  2026-08-20T03:00:52.378705-07:00  ok
    Name:      vault-morning-brief
    Schedule:  55 7 * * *
    Last run:  2026-08-20T07:56:06.337206-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-20T08:04:59.697548-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  5 3 * * *
    Last run:  2026-08-20T03:05:56.298234-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-20T08:02:00.608734-07:00  error: Script exited with code 1
    Name:      echopedia-digest
    Schedule:  20 7 * * *
    Last run:  2026-08-20T07:20:59.764120-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-20T08:03:59.606661-07:00  ok
    Name:      memory-audit
    Schedule:  50 7 * * *
    Last run:  2026-08-20T07:50:59.028939-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  10 3 * * *
    Last run:  2026-08-20T03:18:50.406058-07:00  ok
    Name:      echopedia-janitor
    Schedule:  50 3 * * *
    Last run:  2026-08-20T03:51:15.437122-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  5 7 * * 0
    Last run:  2026-08-16T07:28:56.895128-07:00  ok
    ⚠ Delivery failed: live adapter send to telegram:-5543616648 timed out before the coroutine was dispatched; delivery error: Telegram send failed: Timed out
    Name:      echopedia-ci-heal
    Schedule:  0 8 * * *
    Last run:  2026-08-19T08:05:26.989491-07:00  ok
    Name:      echopedia-site-design
    Schedule:  15 8 * * *
    Last run:  2026-08-19T08:15:02.732719-07:00  ok
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=26 agent=0 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 3 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 0 5 * * * | `echopedia-quote-extractor` | no_agent | on | ok | `echopedia-quote-extractor-cron.sh` |
| 0 6 * * 0 | `echopedia-source-continuity` | no_agent | on | ok | `echopedia-source-continuity.sh` |
| 0 8 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 10 3 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 10 7 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 15 4 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 15 8 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 20 4 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 20 5 * * * | `echopedia-timeline-builder` | no_agent | on | ok | `echopedia-timeline-builder-cron.sh` |
| 20 7 * * * | `echopedia-digest` | no_agent | on | ok | `echopedia-digest.sh` |
| 25 4 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 30 8 * * * | `cron-self-audit` | no_agent | on | ok | `cron-self-audit.py` |
| 40 4 * * * | `echopedia-backlink-auditor` | no_agent | on | ok | `echopedia-backlink-auditor-cron.sh` |
| 5 3 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 5 4 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 5 7 * * 0 | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 50 3 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 50 6 * * * | `cron-audit` | no_agent | on | ok | `cron-audit.py` |
| 50 7 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 55 7 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 6 4 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | ok | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | error | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

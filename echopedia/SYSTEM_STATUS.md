# Echopedia System Status

*Generated: 2026-08-07 05:10 PDT*

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
|- **Uncommitted files:** 628

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | daily 04:05 | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | daily 04:00 | 19 scanned, 0 queued |
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
    Name:      vault-morning-brief
    Schedule:  0 5 * * *
    Last run:  2026-08-07T05:03:03.267527-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-07T05:09:56.765727-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  0 4 * * *
    Last run:  2026-08-07T04:00:58.539261-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-07T04:45:56.305034-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 8 * * *
    Last run:  2026-08-06T09:01:00.360467-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-07T05:00:56.561432-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-08-07T05:00:57.280012-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-08-07T04:07:43.685613-07:00  ok
    Name:      echopedia-janitor
    Schedule:  0 4 * * *
    Last run:  2026-08-07T04:01:16.249707-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 5 * * *
    Last run:  2026-08-06T05:08:32.597505-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 7 * * *
    Last run:  2026-08-06T08:01:04.057702-07:00  ok
    Name:      vault-connector-suggestions
    Schedule:  0 8 * * *
    Last run:  2026-08-06T09:08:12.078738-07:00  ok
    ⚠ Delivery failed: live adapter send to telegram:-5543616648 timed out before the coroutine was dispatched; delivery error: Telegram send failed: Timed out
    Name:      vault-intelligence-digest
    Schedule:  0 7 * * *
    Last run:  2026-08-06T08:03:04.896334-07:00  ok
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=27 agent=3 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 4 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 0 4 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 0 4 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 0 4 * * * | `echopedia-timeline-builder` | AGENT | on | error | `—` |
| 0 5 * * * | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 0 5 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 0 5 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 0 6 * * * | `cron-audit` | no_agent | on | ok | `cron-audit.py` |
| 05 4 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 10 4 * * * | `echopedia-backlink-auditor` | AGENT | on | error | `—` |
| 10 4 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 10 5 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 15 4 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 15 4 * * * | `echopedia-quote-extractor` | AGENT | on | error | `—` |
| 20 4 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 30 4 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 5 4 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | ok | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |
| ? | `cron-output-rotate` | no_agent | OFF | ok | `cron-output-rotate.sh` |
| ? | `echopedia-ci-heal` | no_agent | OFF | ok | `echopedia-ci-heal-wrapper.sh` |
| ? | `echopedia-digest` | no_agent | OFF | ok | `echopedia-digest.sh` |
| ? | `vault-connector-suggestions` | no_agent | OFF | ok | `vault-connector-suggestions.py` |
| ? | `vault-intelligence-digest` | no_agent | OFF | ok | `vault-intelligence-digest.py` |
| ? | `vault-unfinished-threads` | no_agent | OFF | ok | `vault-unfinished-threads.py` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

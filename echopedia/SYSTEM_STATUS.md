# Echopedia System Status

*Generated: 2026-08-07 10:50 PDT*

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
|- **Uncommitted files:** 134

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
    Name:      vault-morning-brief
    Schedule:  0 5 * * *
    Last run:  2026-08-07T05:03:03.267527-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-07T10:50:04.917547-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  0 4 * * *
    Last run:  2026-08-07T04:00:58.539261-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-07T10:46:03.238209-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-07T10:31:03.318982-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-08-07T05:00:57.280012-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-08-07T04:07:43.685613-07:00  ok
    Name:      echopedia-janitor
    Schedule:  2 4 * * *
    Last run:  2026-08-07T04:01:16.249707-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  10 5 * * *
    Last run:  2026-08-07T05:12:09.609353-07:00  ok
    ⚠ Delivery failed: live adapter send to telegram:-5543616648 timed out before the coroutine was dispatched; delivery error: Telegram send failed: Timed out
    Name:      echopedia-site-design
    Schedule:  30 4 * * *
    Last run:  2026-08-07T04:30:56.706634-07:00  ok
    Name:      vault-search-index-rebuild
    Schedule:  30 5 * * 0
    Last run:  2026-08-02T05:12:46.979835-07:00  ok
    Name:      echopedia-scout-live
    Schedule:  5 4 * * *
    Last run:  2026-08-07T04:06:03.358950-07:00  ok
    Name:      echopedia-extract-actions
    Schedule:  10 4 * * *
    Last run:  2026-08-07T04:10:56.329001-07:00  ok
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=28 agent=3 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 30 8 * * * | `cron-self-audit` | no_agent | on | — | `cron-self-audit.py` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | ok | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |
| ? | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| ? | `cron-audit` | no_agent | on | ok | `cron-audit.py` |
| ? | `cron-output-rotate` | no_agent | OFF | ok | `cron-output-rotate.sh` |
| ? | `echopedia-backlink-auditor` | AGENT | on | error | `—` |
| ? | `echopedia-ci-heal` | no_agent | OFF | ok | `echopedia-ci-heal-wrapper.sh` |
| ? | `echopedia-digest` | no_agent | OFF | ok | `echopedia-digest.sh` |
| ? | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| ? | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| ? | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| ? | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| ? | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| ? | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| ? | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| ? | `echopedia-quote-extractor` | AGENT | on | error | `—` |
| ? | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| ? | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| ? | `echopedia-timeline-builder` | AGENT | on | error | `—` |
| ? | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| ? | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| ? | `vault-connector-suggestions` | no_agent | OFF | ok | `vault-connector-suggestions.py` |
| ? | `vault-intelligence-digest` | no_agent | OFF | ok | `vault-intelligence-digest.py` |
| ? | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| ? | `vault-unfinished-threads` | no_agent | OFF | ok | `vault-unfinished-threads.py` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

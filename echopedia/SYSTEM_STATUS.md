# Echopedia System Status

*Generated: 2026-08-02 05:05 PDT*

## Orientation
- **User manual (start here):** [USER_MANUAL.md](USER_MANUAL.md)
- **Worker playbooks:** [WORKER.md](WORKER.md)
- **Mission / remains:** [WHERE_WE_ARE.md](WHERE_WE_ARE.md)
- **This file:** auto machine snapshot (refreshed by system-status / ci-heal)

## Autonomy
- **Standards:** v8
- **Level:** L3
- **L2 auto-publish on drift:** True
- **L3 auto-push when green:** True
- **Last good deploy:** `ee53f41132`

## Content
|- **Markdown pages:** 29380
|- **Janitor queue depth:** 5
|- **Uncommitted files:** 418

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | daily 04:05 | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | daily 04:00 | 268 scanned, 0 queued |
|| Extract | echopedia-extract-actions | daily 04:10 | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | daily 04:15 | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | daily 04:20 | 0 cards |
|| Review | weekly-improvement | Mon 05:00 | improvement-brief.md |

## What runs automatically
|| When | Job | Role |
||------|-----|------|
|| 04:00 | echopedia-janitor | sense/queue/link hygiene priority |
|| 04:00 | echopedia-content-analysis | Filter: find actionable content gaps |
|| 04:05 | echopedia-scout-live | Scout: monitor live site for UX issues |
|| 04:10 | echopedia-extract-actions | Extract: map findings to remediation actions |
|| 04:15 | echopedia-evaluate-actions | Evaluate: score by user impact |
|| 04:15 | echopedia-ci-heal | L2/L3 heal: drift→publish, smoke, optional push |
|| 04:20 | echopedia-generate-cards | Generate: create kanban task cards |
|| 05:00 Mon | echopedia-weekly-improvement | Review gate + improvement pack + drain |
|| 09:00 | echopedia-digest | morning brief |

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
    Last run:  2026-08-02T03:10:44.168034-07:00  ok
    Name:      vault-morning-brief
    Schedule:  0 5 * * *
    Last run:  2026-08-02T05:02:56.841327-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-02T05:04:52.177677-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  0 4 * * *
    Last run:  2026-08-02T04:00:48.244585-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-02T04:43:51.674454-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 9 * * *
    Last run:  2026-08-02T03:10:45.268291-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-02T04:41:51.296439-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-08-02T05:00:52.629759-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-08-02T04:14:50.886736-07:00  ok
    ⚠ Delivery failed: live adapter send to telegram:-5543616648 timed out before the coroutine was dispatched; delivery error: Telegram send failed: Timed out
    Name:      echopedia-janitor
    Schedule:  0 4 * * *
    Last run:  2026-08-02T04:01:32.552858-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 5 * * *
    Last run:  2026-08-02T03:13:48.185968-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  15 4 * * *
    Last run:  2026-08-02T04:23:37.098832-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 8 * * *
    Last run:  2026-08-02T03:10:52.669411-07:00  ok
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=22 agent=0 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 3 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 0 4 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 0 4 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 0 4 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 0 5 * * * | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 0 5 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 0 5 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 0 8 * * * | `vault-intelligence-digest` | no_agent | on | ok | `vault-intelligence-digest.py` |
| 0 8 * * * | `vault-unfinished-threads` | no_agent | on | ok | `vault-unfinished-threads.py` |
| 0 9 * * * | `echopedia-digest` | no_agent | on | ok | `echopedia-digest.sh` |
| 0 9 * * * | `vault-connector-suggestions` | no_agent | on | ok | `vault-connector-suggestions.py` |
| 10 4 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 10 5 * * * | `echopedia-docs-sync` | no_agent | on | — | `echopedia-docs-sync-cron.sh` |
| 15 4 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 15 4 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 20 4 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 30 4 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 30 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 5 4 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `kanban-sync` | no_agent | on | ok | `kanban-sync.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

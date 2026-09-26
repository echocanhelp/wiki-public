# Echopedia System Status

*Generated: 2026-09-26 00:26 PDT*

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
- **Last good deploy:** `5cde2b2824`
- **Last night (ledger):** analyzer scanned 2910 queued 14 suppressed 2081 · 🟡 QUEUE janitor HOLD leftover 40 · 🟡 QUEUE kanban blocked 12 · 🔴 NEED YOU cron fail: echopedia-nightly-audit
- **Track SSOT:** `knowledge/operational/intelligence/autonomy-ledger.json`

## Content
|- **Tier1 pages:** 2876 (people 2409 / orgs 433 / sources 34) · Tier2 archive: 29103
|- **Janitor queue depth:** 51
|- **Uncommitted files:** 16

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | 04:05 local | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | 03:05 local | 2910 scanned, 11 queued |
|| Extract | echopedia-extract-actions | 04:15 local | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | 04:20 local | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | 04:25 local | no data |
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
    Schedule:  5 21 * * *
    Last run:  2026-09-25T21:05:50.094124-07:00  ok
    Name:      vault-morning-brief
    Schedule:  0 7 * * *
    Last run:  2026-09-25T07:00:51.629335-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-09-26T00:24:45.858546-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  10 21 * * *
    Last run:  2026-09-25T21:10:51.838053-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-09-26T00:12:48.746104-07:00  ok
    Name:      memory-audit
    Schedule:  50 0 * * *
    Last run:  2026-09-25T00:51:20.235984-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  15 21 * * *
    Last run:  2026-09-25T21:51:10.358753-07:00  ok
    Name:      echopedia-janitor
    Schedule:  30 21 * * *
    Last run:  2026-09-25T21:41:03.362124-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  15 22 * * 0
    Last run:  2026-09-20T22:24:46.922623-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  25 0 * * *
    Last run:  2026-09-25T00:27:06.951146-07:00  ok
    Name:      echopedia-site-design
    Schedule:  30 0 * * *
    Last run:  2026-09-25T00:31:08.723109-07:00  ok
    Name:      vault-search-index-rebuild
    Schedule:  0 21 * * 0
    Last run:  2026-09-20T21:00:44.250517-07:00  ok
    Name:      echopedia-scout-live
    Schedule:  40 21 * * *
    Last run:  2026-09-25T21:41:02.628583-07:00  ok
    Name:      echopedia-extract-actions
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=29 agent=0 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| */15 15-21 * * * | `echopedia-window-freeze` | no_agent | on | ok | `echopedia-window-freeze.sh` |
| 0 21 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 0 22 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 0 23 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 0 7 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 10 1 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 10 21 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 15 21 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 15 22 * * 0 | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 15 23 * * * | `echopedia-quote-extractor` | no_agent | on | ok | `echopedia-quote-extractor-cron.sh` |
| 20 22 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 20 6 * * * | `echopedia-digest` | no_agent | OFF | ok | `echopedia-digest.sh` |
| 25 0 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 30 0 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 30 21 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 30 22 1 * * | `go-router-monthly-audit` | AGENT | on | ok | `go-router` |
| 30 23 * * * | `echopedia-timeline-builder` | no_agent | on | ok | `echopedia-timeline-builder-cron.sh` |
| 40 0 * * * | `echopedia-tier1-sweep` | no_agent | on | ok | `echopedia-tier1-sweep.sh` |
| 40 21 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 40 22 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 45 0 * * * | `cron-audit` | no_agent | on | ok | `cron-audit-combined.sh` |
| 45 23 * * * | `pair-miner-growth` | no_agent | on | ok | `pair-miner-cron.sh` |
| 45 23 * * 0 | `echopedia-source-continuity` | no_agent | on | ok | `echopedia-source-continuity.sh` |
| 5 21 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 50 0 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| 50 21 * * * | `echopedia-backlink-auditor` | no_agent | on | ok | `echopedia-backlink-auditor-cron.sh` |
| 50 22 * * * | `echopedia-interaction-absorb` | no_agent | on | ok | `echopedia-interaction-absorb.py` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

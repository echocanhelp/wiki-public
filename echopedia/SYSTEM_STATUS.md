# Echopedia System Status

*Generated: 2026-10-28 00:42 PDT*

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
- **Last good deploy:** `47510bb769d`
- **Last night (ledger):** analyzer scanned 3016 queued 8 suppressed 2444 · 🟡 QUEUE janitor HOLD leftover 40 · 🟡 QUEUE kanban blocked 7 · 🔴 NEED YOU cron fail: memory-audit
- **Track SSOT:** `knowledge/operational/intelligence/autonomy-ledger.json`

## Content
|- **Tier1 pages:** 2986 (people 2465 / orgs 441 / sources 80) · Tier2 archive: 29103
|- **Janitor queue depth:** 47
|- **Uncommitted files:** 14155

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
| Stage | Script | Schedule (jobs.json) | Output |
|-------|--------|----------------------|--------|
| Scout | echopedia-scout-live | 21:40 | 44 checked, 0 broken, 0 slow |
| Filter | echopedia-content-analysis | 21:10 | 3019 scanned, 7 queued |
| Extract | echopedia-extract-actions | 22:00 | knowledge/operational/extracted/ |
| Evaluate | echopedia-evaluate-actions | 22:20 | knowledge/operational/evaluated/ |
| Generate | echopedia-generate-cards | 22:40 | no data |
| Review | weekly-improvement | Sun 22:15 | improvement-brief.md |
| Human | vault-morning-brief | 08:30 | NEED YOU ≤5 |

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
    Last run:  2026-10-27T21:05:19.592697-07:00  ok
    Name:      vault-morning-brief
    Schedule:  30 8 * * *
    Last run:  2026-10-27T08:30:43.524861-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-10-28T00:42:20.252706-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  10 21 * * *
    Last run:  2026-10-27T21:10:21.780724-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-10-28T00:39:17.175469-07:00  ok
    Name:      echopedia-digest
    Schedule:  20 6 * * *
    Last run:  2026-09-20T06:20:40.011944-07:00  ok
    Name:      memory-audit
    Schedule:  50 0 * * *
    Last run:  2026-10-27T00:50:18.402176-07:00  error: Script exited with code 1
    Name:      echopedia-nightly-audit
    Schedule:  15 21 * * *
    Last run:  2026-10-27T21:35:06.426665-07:00  ok
    Name:      echopedia-janitor
    Schedule:  30 21 * * *
    Last run:  2026-10-27T21:30:26.976649-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  15 22 * * 0
    Last run:  2026-10-25T22:29:13.007179-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  25 0 * * *
    Last run:  2026-10-27T00:40:51.326219-07:00  ok
    Name:      echopedia-site-design
    Schedule:  30 0 * * *
    Last run:  2026-10-28T00:30:18.770188-07:00  ok
    Name:      vault-search-index-rebuild
    Schedule:  0 21 * * 0
    Last run:  2026-10-25T21:00:06.648937-07:00  ok
    Name:      echopedia-scout-live
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=42 agent=1 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| */15 * * * * | `swarm-churn-sweep` | no_agent | on | ok | `swarm-churn-sweep-cron.sh` |
| */15 15-21 * * * | `echopedia-window-freeze` | no_agent | on | ok | `echopedia-window-freeze.sh` |
| 0 12 * * * | `echopedia-board-brief` | no_agent | on | ok | `echopedia-board-brief.py` |
| 0 21 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 0 22 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 0 23 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 10 1 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 10 21 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 15 21 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 15 22 * * 0 | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 15 23 * * * | `echopedia-quote-extractor` | no_agent | on | ok | `echopedia-quote-extractor-cron.sh` |
| every day at 3:15 | `taiwandaily-domain-cards` | no_agent | on | ok | `taiwandaily-domain-cron.sh` |
| 20 21 * * * | `hot-subjects-watch` | no_agent | on | ok | `hot-subjects-watch.sh` |
| 20 22 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 20 6 * * * | `echopedia-digest` | no_agent | OFF | ok | `echopedia-digest.sh` |
| 25 0 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 30 */4 * * * | `echopedia-news-digest` | no_agent | on | ok | `echopedia-news-digest.py` |
| 30 0 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 30 21 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 30 22 1 * * | `go-router-monthly-audit` | AGENT | on | ok | `go-router` |
| 30 23 * * * | `echopedia-timeline-builder` | no_agent | on | ok | `echopedia-timeline-builder-cron.sh` |
| 30 8 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 40 0 * * * | `echopedia-tier1-sweep` | no_agent | on | ok | `echopedia-tier1-sweep.sh` |
| 40 21 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 40 22 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 40 3 * * * | `swarm-churn-report` | no_agent | on | ok | `swarm-churn-report-cron.sh` |
| 45 0 * * * | `cron-audit` | no_agent | on | ok | `cron-audit-combined.sh` |
| 45 23 * * * | `pair-miner-growth` | no_agent | on | ok | `pair-miner-cron.sh` |
| 45 23 * * 0 | `echopedia-source-continuity` | no_agent | on | ok | `echopedia-source-continuity.sh` |
| 5 21 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 50 0 * * * | `memory-audit` | no_agent | on | error | `memory-audit.sh` |
| 50 21 * * * | `echopedia-backlink-auditor` | no_agent | on | ok | `echopedia-backlink-auditor-cron.sh` |
| 50 22 * * * | `echopedia-interaction-absorb` | no_agent | on | ok | `echopedia-interaction-absorb.py` |
| 55 21 * * * | `tahs-linkcheck` | no_agent | OFF | — | `tahs-linkcheck-cron.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `tier2-absorb` | AGENT | on | ok | `tier2-absorb-queue.py` |
| every 30m | `tier2-loop-watchdog` | no_agent | on | ok | `tier2-loop-watchdog.py` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |
| every 60m | `echopedia-news-scan` | no_agent | on | ok | `echopedia-news-scan.py` |
| every 60m | `swarm-vitals` | no_agent | on | error | `swarm-vitals.py` |
| once in 11m | `albert-caption-livecheck` | no_agent | OFF | ok | `albert-caption-livecheck.sh` |
| once in 13h | `albert-erratum-livecheck` | no_agent | OFF | ok | `albert-erratum-livecheck.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

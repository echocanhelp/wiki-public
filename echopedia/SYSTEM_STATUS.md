# Echopedia System Status

*Generated: 2026-08-31 21:14 PDT*

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
- **Last good deploy:** `358f46b6bc`
- **Last night (ledger):** analyzer scanned 2866 queued 2 suppressed 1763 · 🟡 QUEUE janitor HOLD leftover 40 · 🟡 QUEUE kanban blocked 60
- **Track SSOT:** `knowledge/operational/intelligence/autonomy-ledger.json`

## Content
|- **Tier1 pages:** 2848 (people 2402 / orgs 429 / sources 17) · Tier2 archive: 29103
|- **Janitor queue depth:** 41
|- **Uncommitted files:** 1794

## Self-improvement pipeline (Scout → Filter → Extract → Evaluate → Generate → Review)
|| Stage | Script | Last run | Output |
||-------|--------|----------|--------|
|| Scout | echopedia-scout-live | 04:05 local | 44 checked, 0 broken, 0 slow |
|| Filter | echopedia-content-analysis | 03:05 local | 2866 scanned, 2 queued |
|| Extract | echopedia-extract-actions | 04:15 local | knowledge/operational/extracted/ |
|| Evaluate | echopedia-evaluate-actions | 04:20 local | knowledge/operational/evaluated/ |
|| Generate | echopedia-generate-cards | 04:25 local | 11 cards |
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
    Last run:  2026-08-31T21:03:14.328923-07:00  ok
    Name:      vault-morning-brief
    Schedule:  0 7 * * *
    Last run:  2026-08-31T21:04:04.132315-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-31T21:15:23.862021-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  10 1 * * *
    Last run:  2026-08-30T01:10:33.900619-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-31T21:05:22.939996-07:00  ok
    Name:      echopedia-digest
    Schedule:  20 6 * * *
    Last run:  2026-08-30T06:20:59.427523-07:00  ok
    Name:      memory-audit
    Schedule:  50 4 * * *
    Last run:  2026-08-31T21:03:14.295911-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  15 1 * * *
    Last run:  2026-08-30T01:26:52.272034-07:00  ok
    Name:      echopedia-janitor
    Schedule:  30 1 * * *
    Last run:  2026-08-30T01:37:42.465667-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 6 * * 0
    Last run:  2026-08-30T07:20:35.576451-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  25 4 * * *
    Last run:  2026-08-30T03:34:14.239028-07:00  ok
    Name:      echopedia-site-design
    Schedule:  30 4 * * *
    Last run:  2026-08-30T03:45:56.249681-07:00  ok
    Name:      vault-search-index-rebuild
    Schedule:  0 5 * * 0
    Last run:  2026-08-30T05:31:04.146593-07:00  ok
    Name:      echopedia-scout-live
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

## Cron inventory (generated)
<!-- cron-inventory-start -->
<!-- cron-inventory-meta: count=26 agent=1 bad_deliver=0 -->
| Schedule | Job | Mode | En | Last | Script |
|----------|-----|------|----|------|--------|
| 0 4 * * * | `echopedia-evaluate-actions` | no_agent | on | ok | `echopedia-evaluate-actions.py` |
| 0 5 * * 0 | `vault-search-index-rebuild` | no_agent | on | ok | `vault-search-index-rebuild.sh` |
| 0 6 * * 0 | `echopedia-weekly-improvement` | no_agent | on | ok | `echopedia-weekly-improvement.sh` |
| 0 6 1 * * | `go-router-monthly-audit` | AGENT | on | ok | `go-router` |
| 0 7 * * * | `vault-morning-brief` | no_agent | on | ok | `vault-morning-brief.py` |
| 10 1 * * * | `Echopedia content analysis` | no_agent | on | ok | `echopedia-content-analysis-cron.sh` |
| 10 4 * * * | `echopedia-person-works-linker` | no_agent | on | ok | `echopedia-person-works-linker-cron.sh` |
| 10 6 * * * | `echopedia-docs-sync` | no_agent | on | ok | `echopedia-docs-sync-cron.sh` |
| 15 1 * * * | `echopedia-nightly-audit` | no_agent | on | ok | `echopedia-nightly-audit-wrapper.sh` |
| 15 3 * * * | `cron-output-rotate` | no_agent | on | ok | `cron-output-rotate.sh` |
| 15 4 * * * | `echopedia-quote-extractor` | no_agent | on | ok | `echopedia-quote-extractor-cron.sh` |
| 20 4 * * * | `echopedia-timeline-builder` | no_agent | on | ok | `echopedia-timeline-builder-cron.sh` |
| 20 6 * * * | `echopedia-digest` | no_agent | on | ok | `echopedia-digest.sh` |
| 25 4 * * * | `echopedia-ci-heal` | no_agent | on | ok | `echopedia-ci-heal-wrapper.sh` |
| 30 1 * * * | `echopedia-janitor` | no_agent | on | ok | `echopedia-janitor-wrapper.sh` |
| 30 4 * * * | `echopedia-site-design` | no_agent | on | ok | `echopedia-site-design-wrapper.sh` |
| 30 5 * * 0 | `echopedia-source-continuity` | no_agent | on | ok | `echopedia-source-continuity.sh` |
| 30 6 * * * | `echopedia-tier1-sweep` | no_agent | on | ok | `echopedia-tier1-sweep.sh` |
| 35 1 * * * | `echopedia-extract-actions` | no_agent | on | ok | `echopedia-extract-actions.py` |
| 40 1 * * * | `echopedia-scout-live` | no_agent | on | ok | `echopedia-scout-live.sh` |
| 45 4 * * * | `cron-audit` | no_agent | on | ok | `cron-audit-combined.sh` |
| 5 4 * * * | `echopedia-generate-cards` | no_agent | on | ok | `echopedia-generate-cards.py` |
| 50 1 * * * | `echopedia-backlink-auditor` | no_agent | on | ok | `echopedia-backlink-auditor-cron.sh` |
| 50 4 * * * | `memory-audit` | no_agent | on | ok | `memory-audit.sh` |
| every 1m | `vllm-thermal-scaler` | no_agent | on | ok | `vllm-thermal-scaler.sh` |
| every 30m | `unified-watchdog` | no_agent | on | ok | `unified-watchdog.sh` |

*SSOT: `~/.hermes/profiles/pinto/cron/jobs.json` · generated by docs-sync · do not hand-edit this table*
<!-- cron-inventory-end -->

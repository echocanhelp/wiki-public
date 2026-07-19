# Echopedia System Status

*Generated: 2026-07-19 04:15 PDT*

## Orientation
- **User manual (start here):** [USER_MANUAL.md](USER_MANUAL.md)
- **Worker playbooks:** [WORKER.md](WORKER.md)
- **Mission / remains:** [WHERE_WE_ARE.md](WHERE_WE_ARE.md)
- **This file:** auto machine snapshot (refreshed by system-status / ci-heal)

## Autonomy
- **Standards:** v6
- **Level:** L3
- **L2 auto-publish on drift:** True
- **L3 auto-push when green:** True
- **Last good deploy:** `8bb3642`

## Content
- **Markdown pages:** 207
- **Janitor queue depth:** 5
- **Uncommitted files:** 587

## What runs automatically
| When | Job | Role |
|------|-----|------|
| 04:00 | echopedia-janitor | sense/queue/link hygiene priority |
| 04:00 | echopedia-nightly-audit | structural audit |
| 04:15 | echopedia-ci-heal | L2/L3 heal: drift→publish, smoke, optional push |
| 05:00 Mon | echopedia-weekly-improvement | improvement pack + drain |
| 09:00 | echopedia-digest | morning brief |

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
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-07-19T04:10:43.393750-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 9 * * *
    Last run:  2026-07-18T09:00:50.829152-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-07-19T03:48:42.974864-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-07-18T05:00:44.535657-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-07-19T04:14:43.483736-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-07-19T04:00:56.376533-07:00  ok
    Name:      echopedia-janitor
    Schedule:  0 4 * * *
    Last run:  2026-07-19T04:00:44.305309-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 5 * * 1
    Name:      echopedia-ci-heal
    Schedule:  15 4 * * *
    Last run:  2026-07-18T04:15:49.714497-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 8 * * *
    Last run:  2026-07-18T08:00:48.689958-07:00  error: Script exited with code 1
    Name:      vault-connector-suggestions
    Schedule:  0 9 * * *
    Last run:  2026-07-18T09:00:49.924423-07:00  ok
    Name:      vault-intelligence-digest
    Schedule:  0 8 * * *
    Last run:  2026-07-18T08:00:48.788849-07:00  ok
    Name:      echopedia-site-design
    Schedule:  30 4 * * *
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

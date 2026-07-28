# Echopedia System Status

*Generated: 2026-07-28 04:20 PDT*

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
- **Last good deploy:** `1a9fb3792`

## Content
- **Markdown pages:** 29367
- **Janitor queue depth:** 94
- **Uncommitted files:** 1847

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
    Last run:  2026-07-28T04:11:48.704723-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 9 * * *
    Last run:  2026-07-27T09:00:56.170346-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-07-28T03:56:48.303028-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-07-27T05:00:53.982714-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-07-28T04:19:48.617362-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-07-28T04:10:56.172077-07:00  ok
    Name:      echopedia-janitor
    Schedule:  0 4 * * *
    Last run:  2026-07-28T04:01:23.687422-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 5 * * 1
    Last run:  2026-07-27T05:01:08.194786-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  15 4 * * *
    Last run:  2026-07-27T04:16:10.672203-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 8 * * *
    Last run:  2026-07-27T08:00:55.267504-07:00  ok
    Name:      vault-connector-suggestions
    Schedule:  0 9 * * *
    Last run:  2026-07-27T09:00:56.115202-07:00  ok
    Name:      vault-intelligence-digest
    Schedule:  0 8 * * *
    Last run:  2026-07-27T08:00:55.333936-07:00  ok
    Name:      echopedia-site-design
    Schedule:  30 4 * * *
    Last run:  2026-07-27T04:30:52.565057-07:00  ok
    Name:      LINE OA plan upgrade reminder
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

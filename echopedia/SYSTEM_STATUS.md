# Echopedia System Status

*Generated: 2026-07-31 05:07 PDT*

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
- **Last good deploy:** `1faf0aca0f`

## Content
|- **Markdown pages:** 29380
|- **Janitor queue depth:** 5
|- **Uncommitted files:** 1939

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
    Last run:  2026-07-31T03:00:42.559483-07:00  ok
    Name:      vault-morning-brief
    Schedule:  0 5 * * *
    Last run:  2026-07-31T05:02:49.586250-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-07-31T05:05:45.135975-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  0 4 * * *
    Last run:  2026-07-31T04:00:45.174666-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-07-31T05:06:45.341309-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 9 * * *
    Last run:  2026-07-30T09:00:51.926745-07:00  error: Blocked: script path resolves outside the scripts directory (/home/leedt/.hermes/profiles/pinto/scripts): 'echopedia-digest.sh'
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-07-31T04:38:45.194728-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-07-31T05:00:46.505037-07:00  ok
    Name:      echopedia-nightly-audit
    Schedule:  0 4 * * *
    Last run:  2026-07-31T04:18:20.821224-07:00  ok
    ⚠ Delivery failed: live adapter send to telegram:-5543616648 timed out before the coroutine was dispatched; delivery error: Telegram send failed: Timed out
    Name:      echopedia-janitor
    Schedule:  0 4 * * *
    Last run:  2026-07-31T04:01:28.755053-07:00  ok
    Name:      echopedia-weekly-improvement
    Schedule:  0 5 * * *
    Last run:  2026-07-27T05:01:08.194786-07:00  ok
    Name:      echopedia-ci-heal
    Schedule:  15 4 * * *
    Last run:  2026-07-31T04:26:11.575164-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 8 * * *
    Last run:  2026-07-30T08:00:50.593402-07:00  error: Blocked: script path resolves outside the scripts directory (/home/leedt/.hermes/profiles/pinto/scripts): 'vault-unfinished-threads.py'
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

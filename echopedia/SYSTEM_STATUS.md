# Echopedia System Status

*Generated: 2026-08-02 04:22 PDT*

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
- **Last good deploy:** `5281e68c48`

## Content
|- **Markdown pages:** 29380
|- **Janitor queue depth:** 5
|- **Uncommitted files:** 2553

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
    Last run:  2026-08-02T03:12:49.859168-07:00  ok
    Name:      vllm-thermal-scaler
    Schedule:  every 1m
    Last run:  2026-08-02T04:22:51.111149-07:00  ok
    Name:      Echopedia content analysis
    Schedule:  0 4 * * *
    Last run:  2026-08-02T04:00:48.244585-07:00  ok
    Name:      unified-watchdog
    Schedule:  every 30m
    Last run:  2026-08-02T04:12:52.560942-07:00  ok
    Name:      echopedia-digest
    Schedule:  0 9 * * *
    Last run:  2026-08-02T03:10:45.268291-07:00  ok
    Name:      kanban-sync
    Schedule:  every 30m
    Last run:  2026-08-02T04:11:50.181883-07:00  ok
    Name:      memory-audit
    Schedule:  0 5 * * *
    Last run:  2026-08-02T03:10:44.850925-07:00  ok
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
    Last run:  2026-08-02T03:15:04.806742-07:00  ok
    Name:      vault-unfinished-threads
    Schedule:  0 8 * * *
    Last run:  2026-08-02T03:10:52.669411-07:00  ok
```

## Briefs
- Janitor: `echopedia/janitor-brief.md`
- Improvement: `echopedia/improvement-brief.md`
- CI heal: `echopedia/ci-heal-brief.md`

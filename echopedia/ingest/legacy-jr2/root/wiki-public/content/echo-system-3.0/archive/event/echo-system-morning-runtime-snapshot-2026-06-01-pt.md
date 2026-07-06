---
title: "Echo System Morning Runtime Snapshot (2026-06-01 PT)"
slug: echo-system-morning-runtime-snapshot-2026-06-01-pt
tags: [echo-system, runtime, gateway, autoloop, operations, morning-briefing]
source: [evidence.checks.utc_now, evidence.checks.gateway_active, evidence.checks.autoloop_active, evidence.checks.gateway_status, evidence.checks.gateway_restarts_total, evidence.checks.disk_root, evidence.checks.memory, evidence.checks.cron_list, evidence.checks.public_healthz, evidence.derived.gateway_log_metrics.recent_warning_lines, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-06-01"
---

- Collection window evidence shows `hermes-gateway` and `echo-autoloop` both `active`.
- `hermes-gateway` restart count: `4` (nonzero caution).
- Repeated gateway error: `/root/.hermes/kanban.db` not a valid SQLite database; dispatcher paused/quarantined.
- Resource snapshot: root disk `79%` used (`20G/15G/4.0G`), memory line indicates `4096 MB` total with substantial available memory.
- `hermes cron list` shows 5 active scheduled jobs, each listing last run `ok`.
- Public ngrok probe result for `/healthz`: HTTP `404`.
- Telegram transport warnings indicate transient network failures with reconnect attempts (`Bad Gateway`, `Timed out`).

---
title: "Echo System Morning State Verification - 2026-05-31 (PT)"
slug: echo-system-morning-state-verification---2026-05-31-pt
tags: [echo-system, autonomous-loop, operations, verification, morning-state, 2026-05-31]
source: [evidence.checks.utc_now, evidence.checks.gateway_active, evidence.checks.autoloop_active, evidence.checks.gateway_restarts_total, evidence.checks.autoloop_restarts_total, evidence.checks.disk_root, evidence.checks.memory, evidence.checks.ports, evidence.checks.public_healthz, evidence.checks.cron_list, evidence.pulse.system_health_score, evidence.pulse.overall_status, evidence.issues, evidence.cautions, evidence.derived]
description: "Archived by Echo System Archivist on 2026-05-31"
---

- Evidence collection time: `2026-05-31T05:30:29.040973-07:00`.
- `hermes-gateway`: active.
- `echo-autoloop`: active.
- Pulse status: `🟠 Autonomous loop degraded` with health score `20`.
- Active issue: `public MCP watchdog cron missing`.
- Active caution: `hermes-gateway has nonzero restart count`.
- Restart counters: gateway `3`, autoloop `0`.
- Root disk snapshot: `15G/20G` used (`77%`).
- Listening ports observed: `127.0.0.1:8080`, `0.0.0.0:8090`.
- Public probe: `https://bucked-diabetes-shucking.ngrok-free.dev/healthz` returned HTTP `404`.
- Listed cron jobs in evidence were active with last-run status `ok`.

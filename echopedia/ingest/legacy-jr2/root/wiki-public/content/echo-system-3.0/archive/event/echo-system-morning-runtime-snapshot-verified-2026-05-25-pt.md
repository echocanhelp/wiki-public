---
title: "Echo System Morning Runtime Snapshot (Verified) — 2026-05-25 PT"
slug: echo-system-morning-runtime-snapshot-verified-2026-05-25-pt
tags: [operations, runtime, system-health, verified]
source: [evidence.checks.utc_now, evidence.checks.gateway_active, evidence.checks.autoloop_active, evidence.checks.gateway_restarts_total, evidence.checks.autoloop_restarts_total, evidence.checks.disk_root, evidence.checks.memory, evidence.checks.ports]
description: "Archived by Echo System Archivist on 2026-05-25"
---

- Collected at `2026-05-25T05:30:17.934727-07:00` (UTC command output: `2026-05-25T12:30:17+00:00`).
- `hermes-gateway` status: `active`; restarts: `0`.
- `echo-autoloop` status: `active`; restarts: `0`.
- Root disk usage: `70%` (`20G total`, `13G used`, `5.8G free`).
- Memory snapshot (`free -m`): `4096 MB total`, `1288 MB used`, `1708 MB free`, `2807 MB available`.
- Listening ports observed: `127.0.0.1:8080`, `0.0.0.0:8090`.

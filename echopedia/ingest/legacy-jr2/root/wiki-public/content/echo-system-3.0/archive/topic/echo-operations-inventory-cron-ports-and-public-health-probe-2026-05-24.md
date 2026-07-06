---
title: "Echo Operations Inventory: Cron, Ports, and Public Health Probe (2026-05-24)"
slug: echo-operations-inventory-cron-ports-and-public-health-probe-2026-05-24
tags: [cron, ports, healthz, ngrok, mcp, operations]
source: [evidence.checks.cron_list, evidence.checks.ports, evidence.checks.public_healthz, evidence.issues, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-05-24"
---

- Cron inventory shows 5 active scheduled jobs with last run marked `ok` in the provided listing.
- Open/listening ports in check output:
  - `8090` on `0.0.0.0`
  - `8080` on `127.0.0.1`
- Public probe result:
  - `curl https://bucked-diabetes-shucking.ngrok-free.dev/healthz` returned HTTP `404`.
- Listed issue remains: `public MCP watchdog cron missing`.

Publication model: publish to both private and public wiki, then community moderation on public wiki.

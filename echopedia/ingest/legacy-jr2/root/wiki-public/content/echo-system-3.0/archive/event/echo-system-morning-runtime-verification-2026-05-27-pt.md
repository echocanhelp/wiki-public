---
title: "Echo System Morning Runtime Verification — 2026-05-27 (PT)"
slug: echo-system-morning-runtime-verification-2026-05-27-pt
tags: [runtime-verification, systemd, operations, morning-state, historian-approved]
source: [evidence.checks.gateway_active, evidence.checks.autoloop_active, evidence.checks.gateway_restarts_total, evidence.checks.autoloop_restarts_total, evidence.checks.disk_root, evidence.checks.ports, evidence.upstream_artifacts.historian]
description: "Archived by Echo System Archivist on 2026-05-27"
---

Verified live checks at 2026-05-27T05:30:27-07:00 show `hermes-gateway` and `echo-autoloop` both active. Restart counters were `hermes-gateway=1` and `echo-autoloop=0`. Root filesystem usage was `76%` on `/dev/loop0` (20G total, 4.7G free). Observed listening sockets included `127.0.0.1:8080` and `0.0.0.0:8090`; no `:8079` listener appeared in the same check output. This item is approved for publication under limited-claim reuse.

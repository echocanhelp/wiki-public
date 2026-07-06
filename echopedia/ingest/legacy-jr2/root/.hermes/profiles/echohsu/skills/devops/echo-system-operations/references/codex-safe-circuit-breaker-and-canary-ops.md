# Codex Safe Circuit-Breaker + Canary Ops (EchoHsu)

## When to apply
- Codex remains user-mandated primary model, but logs show repeated malformed stream shapes.
- Goal is stability without switching primary provider.

## Safe-mode strategy (no primary switch)
1. Keep `model.provider=openai-codex` and primary model unchanged.
2. Add log-driven circuit-breaker that only reroutes **auxiliary** lanes to `xai` when degradation threshold is exceeded.
3. Restart gateway once on state transition `ok -> triggered`.
4. Alert operator with compact reason (`fallback_count` or `hardfail_count`).

## Threshold pattern used
- Window: last 400 lines of `agent.log`
- Trigger if either:
  - hard-failure signatures >= 1, OR
  - fallback-recovery signatures >= 25

Hard-failure signatures:
- `Invalid API response after 3 retries`
- `Codex response remained incomplete after 3 continuation attempts`
- `Non-retryable client error: 'NoneType' object is not iterable`

Recovery signature:
- `Codex parse error recovery succeeded via fallback create path`

## Auxiliary lanes pinned during trigger
- `auxiliary.vision.provider`
- `auxiliary.title_generation.provider`
- `auxiliary.compression.provider`
- `auxiliary.approval.provider`
- `auxiliary.mcp.provider`
- `auxiliary.skills_hub.provider`
- `auxiliary.triage_specifier.provider`
- `auxiliary.kanban_decomposer.provider`
- `auxiliary.profile_describer.provider`
- `auxiliary.curator.provider`

Set all above to `xai`.

## Canary stack
Use silent-on-pass watchdog scripts and only notify on failure.

1. `echohsu-codex-hardfail-watchdog` (10m)
   - watches hard-failure signatures only.
2. `echohsu-codex-browser-canary` (30m)
   - simple Codex response check + browser navigation title check.
3. `echohsu-echopedia-canary` (60m)
   - browser navigate + structured summary output (`TITLE` + 3 bullets).

## OpenClaw decommission checklist (when OpenClaw is test-only)
1. Stop/disable service.
2. Remove unit file and daemon-reload.
3. Kill residual OpenClaw/Codex app-server processes.
4. Uninstall global npm package `openclaw`.
5. Remove `/root/.openclaw`.
6. Verify no matching processes/services remain.

## Hermes update safety notes
- Before update, archive both profile state and Hermes code tree.
- During `hermes update`, local defensive patches may be autostashed when upstream changed same files.
- If conflicts occur, preserve stash ref and run canaries before deciding whether to re-apply local deltas.
- Treat “fallback recoveries present but hard failures zero” as degraded-but-stable, not fully healthy.

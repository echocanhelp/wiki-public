# Codex Provider Hardening + OpenClaw Decommission (Echo profile)

When Codex-backed Hermes sessions are stable-but-noisy (recoverable parse warnings) and OpenClaw was only test-installed, apply this deterministic hardening sequence.

## Trigger
- Repeated log warnings like `'NoneType' object is not iterable` in Codex stream parsing
- Recovery fallback succeeds, but warnings are frequent
- OpenClaw is not needed for production path

## Execution Sequence
1. Remove OpenClaw runtime from host
   - Stop/disable OpenClaw user service
   - Kill remaining OpenClaw/Codex app-server processes
   - Uninstall global `openclaw` package
   - Remove `~/.openclaw` state
   - Verify: no openclaw unit files, no openclaw/codex app-server processes

2. Reduce high-risk tool surface for messaging platforms
   - In `platform_toolsets` for active channels (api_server/telegram), remove heavy lanes not required for normal operations:
     - `browser`
     - `computer_use`
     - `web`
   - Keep core operational toolsets only (file/terminal/skills/memory/delegation/etc.)

3. Route noisy auxiliary lanes away from Codex
   - Set `auxiliary.vision.provider` to a non-codex provider
   - Set `auxiliary.title_generation.provider` to a non-codex provider
   - Goal: preserve Codex for main turns while reducing malformed auxiliary stream exposure

4. Add hard-failure watchdog (not warning spam)
   - Monitor `agent.log` incrementally (stateful line cursor)
   - Alert only on terminal signatures:
     - `Invalid API response after 3 retries`
     - `Codex response remained incomplete after 3 continuation attempts`
     - `Non-retryable client error: 'NoneType' object is not iterable`
   - Schedule as a quiet cron script (silent when no hits)

5. Restart and validate
   - Restart profile gateway
   - Run a one-shot ping through profile (`chat -q ...`) and verify successful final response
   - Confirm no OpenClaw residue and watchdog job scheduled

## Verification Checklist
- `hermes doctor` / `hermes status --all` healthy
- Main query returns success
- No openclaw service/process/package residue
- Toolset reduction persisted in config
- Auxiliary provider overrides persisted
- Watchdog job exists and runs silently without hard-failure hits

## Pitfalls
- Treating recoverable parse warnings as immediate outage (focus on hard-failure signatures)
- Leaving OpenClaw unit/process residue after uninstall
- Keeping broad toolsets enabled for public-facing channels when not operationally necessary
- Routing all auxiliary lanes through the same fragile provider during incident windows

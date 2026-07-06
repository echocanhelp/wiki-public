# Healer autonomous loop artifact

- Timestamp: 2026-05-27T03:31:25.149793-07:00
- Profile: healer
- Exit code: 0
- Issues seen: 1
- Cautions seen: 1

## Model Output

### Repairs Applied By Daemon
- **None evidenced.**
  - `repairs: []`
  - Sentinel/agent metrics repeatedly show `auto_fixes_applied: 0` and `repairs_attempted: 0` in this snapshot set.

### Remaining Issues
- **Open issue:** `public MCP watchdog cron missing` (explicitly in `issues`).
- **Active caution:** `hermes-gateway has nonzero restart count` (`NRestarts=1`).
- **Contract mismatch to monitor:** public probe to  
  `https://bucked-diabetes-shucking.ngrok-free.dev/healthz` returned **404** (`curl` exit shows HTTP 404), so current public health path is not confirmed healthy.
- **State context:** core services are currently `active` (`hermes-gateway`, `echo-autoloop`), so this is degraded/partial rather than full outage.

### Exact Safe Next Repairs
1. **Restore missing watchdog job (non-destructive):**
   - Add/re-enable the public MCP watchdog cron on a 5-minute cadence.
   - Verify by checking `hermes cron list` includes the watchdog entry and next run time.
2. **Fix health endpoint contract:**
   - Either expose `/healthz` on the ngrok-served upstream **or** update watchdog to probe the actual valid public path.
   - Verify with `curl -fsS <public-url>/<path>` returning HTTP 200.
3. **Stability hygiene for gateway restart:**
   - Inspect `hermes-gateway` logs around `2026-05-27 07:09 UTC` to confirm whether restart was operator-initiated vs fault.
   - If expected/manual, record as benign; if unexpected, keep restart-rate alerting.
4. **Keep resource guardrails in place:**
   - Disk is `76%` used (`4.7G` free). No immediate repair required, but keep threshold monitoring active.

### Verification Notes
- Evidence timestamp: `2026-05-27T03:30:52.682017-07:00` (PT), UTC check `2026-05-27T10:30:52+00:00`.
- Service checks:
  - `hermes-gateway`: `active`, restart count `1`
  - `echo-autoloop`: `active`, restart count `0`
- Network/ports:
  - `127.0.0.1:8080` listening
  - `0.0.0.0:8090` listening
  - `/healthz` public probe returned 404 (not healthy by current probe contract)
- Cron posture:
  - 5 active jobs listed; watchdog named in issue list is still reported missing in this evidence bundle.

## Runtime Cautions

- hermes-gateway has nonzero restart count

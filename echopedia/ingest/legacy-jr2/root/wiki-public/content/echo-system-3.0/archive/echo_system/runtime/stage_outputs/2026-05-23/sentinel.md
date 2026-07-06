# Sentinel autonomous loop artifact

- Timestamp: 2026-05-23T03:00:53.162000-07:00
- Profile: sentinel
- Exit code: 0
- Issues seen: 1
- Cautions seen: 1

## Model Output

## Status
- **Overall:** Degraded but running.
- **Core loop services:** `hermes-gateway` = active (running ~16h), `echo-autoloop` = active.
- **Primary concern:** External public endpoint health check failed (`404` at `/healthz`), and one scheduled audit job is currently failing.
- **Declared issue signal:** `public MCP watchdog cron missing` (from snapshot `issues`).

## Key Findings
1. **Service uptime is stable, but not clean**
   - `hermes-gateway` restart count is nonzero (`NRestarts=1`), flagged as caution.
   - `echo-autoloop` restart count is `0`.

2. **Public control-plane health check is failing**
   - `curl https://bucked-diabetes-shucking.ngrok-free.dev/healthz` returned HTTP `404` (exit shows curl error 22).

3. **Scheduled jobs mostly healthy; one critical audit failed**
   - `echo-system-deployment-reality-audit` last run: **error (exit code 1)**.
   - Its own output reports: `"status": "drift_detected"`, `"drift_count": 18`.

4. **Model/profile reality diverges from expected topology**
   - Profile list shows many profiles on `gpt-5.3-codex` and several Grok models, with multiple specialist profiles stopped.
   - This aligns with the audit’s `drift_detected` output and observed local model mix.

5. **Host resource state is acceptable**
   - Disk `/` at `61%` used (`12G/20G`).
   - Memory: `717 MiB` used / `4096 MiB` total (with substantial available/cache).

## Metrics
- **Collection time (PT):** 2026-05-23T03:00:17-07:00  
- **UTC now check:** 2026-05-23T10:00:17+00:00  
- **Gateway active:** yes  
- **Autoloop active:** yes  
- **Gateway restarts total:** 1  
- **Autoloop restarts total:** 0  
- **Disk root used:** 61%  
- **Memory (MiB):** total 4096, used 717, free 2269, buff/cache 3378  
- **Ports 8079/8080/8090 listeners:** only `0.0.0.0:8080` observed  
- **Public `/healthz` result:** HTTP 404  
- **Cron jobs active:** 5 listed; 4 last-run `ok`, 1 last-run `error`  
- **Derived counts:** `issue_count=1`, `caution_count=1`

## Recommended Repairs
1. **Restore external health contract**
   - Either expose a valid `/healthz` route on the public ngrok target, or update watchdog probes to a valid endpoint.
   - Re-run the public MCP watchdog once endpoint semantics are corrected.

2. **Fix failing deployment reality audit cron**
   - Inspect `echo_system_deployment_reality_audit_cron.sh` failure path and reconcile the `drift_count: 18` mismatches it detected.
   - Validate next scheduled run exits `0`.

3. **Reconcile model/profile configuration drift**
   - Compare live `hermes profile list` against intended architecture policy and normalize assignments.
   - Prioritize specialist lane mapping and required running/stopped states per design.

4. **Investigate gateway restart cause**
   - Since `NRestarts=1`, review preceding gateway logs around restart time to confirm whether transient or recurring.
   - Keep as caution until restart count remains stable across subsequent intervals.

## Runtime Cautions

- hermes-gateway has nonzero restart count

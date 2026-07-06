# Sentinel autonomous loop artifact

- Timestamp: 2026-05-21T03:00:59.251946-07:00
- Profile: sentinel
- Exit code: 0
- Issues seen: 1
- Cautions seen: 0

## Model Output

**Status**  
Gateway (`hermes-gateway`) and autoloop (`echo-autoloop`) services both active with 0 restarts. Public MCP endpoint returns 404. One cron job (deployment-reality-audit) last run reported `drift_detected` (count=2). Multiple agent threads hitting timeouts on local vLLM.

**Key Findings**  
- Repeated `skill_manage` failures: “old_string is required for 'patch'” (count ≥4).  
- Local model timeouts: `ReadTimeout`, `APITimeoutError`, and stream drops on `Qwen/Qwen3.6-27B-FP8` (http://192.168.7.1:8001/v1).  
- Public healthz 404 on ngrok URL; “public MCP watchdog cron missing” listed as sole issue.  
- Deployment audit shows 2 model-distribution drifts; several profiles remain stopped.  
- No redaction, Telegram, or protocol errors in recent gateway logs.

**Metrics**  
- Disk: 58% (11 G / 20 G)  
- Memory: 857 MiB used / 4 GiB total (~21 %)  
- Gateway uptime: 3 h 46 min (since 06:13 UTC)  
- Active crons: 5 (one with prior error)  
- Listening ports: 8079, 8080  
- Running profiles: default, archivist, echohsu, orchestrator (9 stopped)

**Recommended Repairs**  
- Supply `old_string` (or switch to non-patch mode) for all `skill_manage` calls.  
- Add missing public-MCP watchdog cron and restore `/healthz` response.  
- Investigate vLLM timeout root cause (queue length, concurrency, or model reload).  
- Reconcile the 2 deployment-reality drifts reported in latest audit JSON.

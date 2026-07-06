# Sentinel Health Report — 2026-05-14 03:00 PT

## Status
DEGRADED — Core services operational, but public MCP endpoint unreachable. Telegram on fallback. Memory stores at capacity.

## Key Findings

### Critical
1. **Public MCP endpoint returning HTTP 500** — ngrok tunnel is active (pid 280) and correctly routing to localhost:8079, but the mux on 8079 returns 500 for /healthz and /mcp. Previous pulse showed healthz=ok. Root cause: MCP server process (previously pid 278 on port 8090) is no longer listening. Port 8090 is absent from ss output. The hermes-http-mux on 8079 serves the dashboard HTML but /healthz and /mcp paths return empty/500.

2. **MCP server process crashed/not running** — Previous SystemPulse (May 9) showed `mcp-server` active on port 8090 (pid 278). Current ports show only 8079 (python pid 278) and 8080 (hermes pid 1700). Port 8090 is missing entirely. The process that was on 8090 may have restarted on 8079, but the /mcp and /healthz endpoints are non-functional.

3. **Telegram on sticky fallback IP** — Primary api.telegram.org unreachable since May 14 05:10 UTC. Gateway now using fallback IP 149.154.166.110. This is functional but represents degraded external connectivity.

4. **Persistent memory stores at capacity** — Three separate memory tool errors logged in gateway (06:46-06:56 UTC). User memory at 1307/1375 chars (95%), system memory at 2099/2200 chars (95%). New memory writes are being silently rejected.

### Warnings
5. **Title generator timeouts** — Two failures (04:53, 05:46 UTC). Likely model inference timeout on local vLLM.

6. **search_files tool bug** — Type comparison error: `'>' not supported between instances of 'str' and 'int'` (05:14 UTC). Hermes tool code bug.

7. **Deployment reality audit failing** — Cron job `echo-system-deployment-reality-audit` exited with code 1, reporting 9 drift items. All 10 profiles now on Qwen/Qwen3.6-27B-FP8 (previously `default` was gpt-5.4).

8. **Disk usage trending up** — 50% used (9.1G/20G), up from 41% (7.6G) on May 9. Growth rate ~1.5G/5 days.

### Observations (no action needed)
- Cron jobs restored: 3 active jobs found live (gateway watchdog, docs sync, deployment audit). Evidence snapshot showed none, but live check confirms recovery.
- `public-hermes-mcp-watchdog` cron from previous pulse is still absent — replaced by `gateway-platform-ownership-watchdog`.
- Gateway uptime: 1d 15h with 0 restarts. Memory stable at 361M.
- echo-autoloop active, 0 restarts.
- 3 of 13 profiles running (default, echohsu, orchestrator).

## Metrics

| Metric                          | Current       | Previous (May 9) | Delta      |
|---------------------------------|---------------|--------------------|------------|
| Gateway uptime                  | 1d 15h        | 1h 38m             | + (restart) |
| Gateway restarts                | 0             | 0                  | —          |
| Gateway memory                  | 361M          | 89.5M              | +271.5M    |
| Disk / used                     | 50% (9.1G)    | 41% (7.6G)         | +9%        |
| RAM used                        | 41% (1666/4096) | 51% (1043/2048)  | improved   |
| Swap used                       | 4.2M          | 118.9M             | -114.7M    |
| Public MCP healthz              | HTTP 500      | ok                 | DEGRADED   |
| MCP server port 8090            | DOWN          | UP (pid 278)       | CRITICAL   |
| ngrok tunnel                    | UP (pid 280)  | UP (pid 281)       | pid changed|
| Telegram connectivity           | fallback IP   | normal             | degraded   |
| Memory store capacity           | 95%           | —                  | CRITICAL   |
| Running profiles                | 3/13          | 2/13               | +1         |
| Active cron jobs                | 3             | 2                  | +1         |
| Deployment audit                | FAIL (9 drift)| —                  | NEW        |

## Recommended Repairs

### Immediate (Healer)
1. **Restart/reinstall MCP server** — Port 8090 is not listening. Investigate whether hermes-http-mux on 8079 now handles MCP or if a separate MCP server needs to be restored. Check journalctl for MCP server crash logs: `journalctl --user -u hermes-gateway --since "2026-05-13"`

2. **Diagnose /healthz 500 on port 8079** — The mux responds with HTML dashboard but /healthz returns empty. The public-facing healthz endpoint is broken regardless of MCP state. Check mux configuration.

3. **Trim persistent memory stores** — Both user and system memory are at ~95% capacity. Remove stale entries (especially session-specific task logs) to reclaim headroom. Priority: prune entries older than 7 days that reference completed tasks.

### Short-term (Evolver)
4. **Fix search_files type comparison bug** — The tool is comparing str to int somewhere in its filter logic. File a bug report against the hermes-agent search_files tool implementation.

5. **Investigate title_generator timeouts** — Likely a model inference timeout on local vLLM. Consider increasing timeout or adding retry logic.

6. **Resolve deployment drift** — 9 drift items detected. Primary: all profiles now on local Qwen3.6-27B-FP8 instead of mixed topology (default on gpt-5.4). Decide if this is intentional and update the baseline, or if frontier profiles need to be reconfigured.

### Monitoring
7. **Recreate public-hermes-mcp-watchdog cron** — The previous 5-minute MCP watchdog was removed. Create a replacement that monitors `https://bucked-diabetes-shucking.ngrok-free.dev/healthz` and alerts on non-200 responses.

8. **Telegram fallback monitoring** — Primary api.telegram.org is unreachable. This may be a regional/network issue. Monitor for recovery and alert if fallback persists beyond 24h.

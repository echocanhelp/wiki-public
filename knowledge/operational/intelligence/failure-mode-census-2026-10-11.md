# Failure-mode census — 2026-10-11 (Phase 1)

Evidence pass only. **Promote nothing.** Constitution heal whitelist stays empty (`none graduated 2026-10-11`). A mode is L2+ only when detect, act, AND verify were all quoted from a live run.

Measured this session (2026-10-11 ~23:50 PDT):

- `jobs.json`: 32 jobs, ok=30, error=2. Errors: `unified-watchdog` (`c2b62d335405`, exit 1 — swap>50% signal, see M6) and `go-router-monthly-audit` (`5c12ada40cb6`, `RuntimeError: Connection error.`, last run 2026-10-01).
- Engine: `/health` ok, served id `universal`, unit `qwen38-flash-next-tf.service`. `boot_verify_up_failed` is absent from mode state (None) — no stale boot flag to clear.
- Swap at write time: 4.2Gi/15Gi ≈ 28%. The watchdog's own 23:46 run reported 60%. Transient, not structural.
- Journal 48h: 14 CDP-supervisor reconnect lines, ending `stopped after 5 failed reconnect attempts`. No `boot_verify` lines.

## Matrix

### M1 — cron missed run / schedule drift
- Evidence: `cron-audit-combined.sh` (job `cron-audit`, `45 0 * * *`)
- detect: yes (job-set + mirror diff)
- act: partial — script hygiene + mirror check; no schedule restore path quoted from this run
- verify: **no** — the wrapper ends `exit 0` unconditionally (`set -uo pipefail`, no `-e`). A failing `cron-audit.py` does not fail the job, so a finding is printed but the job status stays ok.
- degrade: findings visible only in stdout, not in `last_status`
- level: L1 (detect-without-act; act exists but is not gated by verify)
- promote: no

### M2 — stale `last_error` on `last_status=ok`
- Evidence: `cron-audit.py` lines ~34–53 emit `STALE_ERROR:...` with a 24h cutoff
- detect: yes
- act: no — flags only. The self-clearing wrapper is a skill pattern (`cron-self-evolution`), not quoted live.
- verify: no
- level: L1
- promote: no

### M3 — CI/CDN drift (nightly publish)
- Evidence: `echopedia-ci-heal-wrapper.sh`; last run 2026-10-11T00:34 ok
- detect: yes (`CI_STATUS: FAIL` grep)
- act: yes — "heal script owns republish"
- verify: partial — greps `CI_STATUS: GREEN|green=1|L3 pushed`; no independent CDN re-probe quoted this session
- degrade: publish delayed one night; no user-visible break
- level: L2 (detect+act, verify is a status grep not a re-fetch)
- promote: no — needs a re-fetch probe before it can graduate

### M4 — content-analysis auto-heal
- Evidence: `echopedia-content-analysis-cron.sh`, lines 21/23 `exit 0`
- detect: labels only; act: none in this script; verify: no
- level: L1
- promote: no

### M5 — live-site 404 / ghost page
- Evidence: `~/echo-system/scripts/echopedia-gap-scan.py` — classifies `live404` vs `ghost (self-healed / client-resolved)`
- detect: yes; act: no (classification only); verify: the live probe itself is the verify of its own classification, but it remediates nothing
- level: L1 (detect-only)
- promote: no

### M6 — swap usage > 50%
- Evidence: `unified-watchdog.sh` lines ~212–214 sets `EXIT_CODE=1`; job error at 23:46
- detect: yes; act: no (advisory — the MemoryMin fix line says `sudo systemctl set-property`, never run by the script); verify: none
- level: L1
- promote: no — and acting on it means sudo/systemd changes, which is operator territory, not a heal whitelist entry

### M7 — CDP browser supervisor give-up
- Evidence: journal 48h, 14 lines, `stopped after 5 failed reconnect attempts`
- detect: yes (log); act: no; verify: no
- level: L0–L1
- promote: no — constitution explicitly excludes supervisor revive from the whitelist

### M8 — stale boot-verify flag
- Evidence: `pinto-llm-mode.json` — flag absent this run (`None`); boot policy `force_up_on_reboot`, generation 192
- detect: n/a (not present); act: n/a; verify: would be `curl :8888/health`
- level: n/a
- promote: no — **no candidate.** The Phase 4 "likely nominee" (clear flag while health is up) is NOT justified by this census. The flag was not observed set.

### M9 — semantic skill drift (doc contradicts live knob)
- Evidence: `ssot-drift-check.sh` contains the stale-clock invariant; nothing on the schedule invokes it. `cron-audit-combined.sh` never calls `ssot-drift-check.sh`.
- detect: script exists, trigger missing
- act: no; verify: the script's own invariants
- level: L1
- promote: no — this is Phase 3's wiring job, not a heal

### M10 — Tier1 uncommitted drift
- Evidence: watchdog treats it as soft INFO; `echopedia-tier1-sweep.sh` owns the nightly commit
- Not a heal mode. The sweep is the act. No promote.

## Findings to carry forward (not fix)

1. `cron-audit-combined.sh` always `exit 0`. Phase 3 wiring must print, not flip the exit.
2. `unified-watchdog` is currently the only live error source, and it is a threshold signal, not a broken subsystem. Do not "fix" the error status by clearing last_error.
3. `go-router-monthly-audit` connection error: L0 human. No retry cron.
4. The Phase 4 whitelist nominee is off the table until a mode is observed set-and-recoverable with a verify probe. None was.

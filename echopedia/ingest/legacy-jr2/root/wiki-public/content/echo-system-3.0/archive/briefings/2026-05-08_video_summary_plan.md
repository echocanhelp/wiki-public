# Morning Briefing Video Production Plan
Date: 2026-05-08 PT

## Render Readiness
Status: Not render-ready.

Evidence is insufficient for rendering a morning briefing video at this time.

Why blocked:
- Historian artifact explicitly says `approved_for_media: false`.
- `echo-autoloop` status is materially contradictory:
  - direct check: `inactive`
  - pulse snapshot: `active`
- No consent or release artifact is included.
- No repair receipts or contradiction-resolution evidence are included.
- No approved production package is included from Content containing:
  - approved final script
  - verified portrait/images
  - style references
  - voiceover asset approval

Evidence-backed facts that are safe to reference internally:
- `hermes-gateway` was active at collection time and showed `NRestarts=0`.
- Public `/healthz` returned `ok`.
- Two watchdog cron jobs were active and last run `ok`.
- Root disk usage was `41%`.
- Cautions present:
  - secret redaction disabled
  - intermittent Telegram network/protocol errors with reconnect behavior
- Issue present:
  - `echo-autoloop inactive` in direct checks

## Scene Plan
Provisional only. Do not render or publish from this plan without approval.

1. Hook: Split-State Morning Snapshot
- Visual: operations dashboard with gateway green and autoloop status split/ambiguous
- Voiceover concept: the public edge is reachable, but autonomy health is not fully verified
- Evidence base: gateway active, `/healthz` ok, autoloop contradiction

2. Gateway Stability
- Visual: terminal-style card showing `hermes-gateway active`, running since `2026-05-09 04:48:07 UTC`, restarts `0`
- Voiceover concept: gateway path is live and stable in the sampled window
- Evidence base: `gateway_status`, `gateway_restarts_total`

3. External Reachability
- Visual: ngrok/public endpoint animation ending in `ok`
- Voiceover concept: external health check succeeded at collection time
- Evidence base: `public_healthz`

4. Watchdog Coverage
- Visual: two active job cards for `public-hermes-mcp-watchdog` and `gateway-platform-ownership-watchdog`
- Voiceover concept: watchdog monitoring remained active with last runs `ok`
- Evidence base: `cron_list`, pulse cron section

5. Risk Overlay
- Visual: restrained warning overlays for disabled secret redaction and Telegram reconnect noise
- Voiceover concept: caution signals remain present and must not be ignored
- Evidence base: cautions and derived gateway log metrics

6. Verification Gate Close
- Visual: side-by-side `inactive` vs `active` autoloop labels with a blocked-render stamp
- Voiceover concept: verification blocks a confidence claim until contradiction and consent gaps are resolved
- Evidence base: direct autoloop check, Historian media block

## Assets Needed
Missing required production inputs:
- Approved final script for VideoForge
- Verified stills/portraits or approved visual source pack
- Style references for the briefing
- Approved voiceover text and narration settings
- Subtitle file or approved caption text
- Music selection/approval
- End screen copy with approved attribution language
- Verification badge level approved for this artifact
- Consent/release artifact for media use
- Historian media approval after contradiction resolution

Optional internal-only visual assets that would support later rendering:
- Dashboard background
- Terminal-style status overlays
- Health endpoint visualization
- Watchdog status cards
- Warning/log visual treatment
- Verification gate end card

## Blocking Gaps
Render is blocked until these evidence gaps are closed:
1. Media approval is currently denied by Historian.
2. `echo-autoloop` contradiction is unresolved.
3. No consent/release evidence is present.
4. No evidence-backed final script package is present.
5. No approved image/portrait/style bundle is present.
6. No evidence of remediation or post-contradiction recheck is present.
7. No downstream VideoForge input manifest is present.

## Delivery Checklist
Before rendering:
- [ ] Historian updates gate to media-approved
- [ ] `echo-autoloop` status contradiction resolved with corroborated evidence
- [ ] Consent/release artifact attached
- [ ] Approved script delivered by Content
- [ ] Verified image/style asset pack delivered
- [ ] Voiceover and subtitle text approved
- [ ] Attribution/end-screen copy approved
- [ ] Verification level for the video explicitly assigned
- [ ] Final source list frozen for archival traceability

Current conclusion:
This is an internal planning draft only. Based on the provided evidence, a morning briefing video should not be rendered yet.

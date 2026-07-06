# Production Plan: Morning Briefing Video (2026-05-09 PT)

## Render Readiness
Not render-ready from the supplied evidence.

Evidence supports an internal operational draft only, not a publishable morning briefing render. The strongest blockers are:
- direct state conflict: `checks.autoloop_active` is `inactive` while `pulse.services.echo-autoloop.status` says `active`
- media approval is explicitly blocked in `upstream_artifacts.historian`
- the evidence contains an active security caution: secret redaction disabled
- no approved final narration package, voiceover file, subtitle file, or visual asset bundle is present in the evidence

## Scene Plan
1. `hook-access-layer`
   - Visual: dark ops board with gateway active, `/healthz` green, watchdog jobs marked `ok`
   - Voiceover: "This morning, the access layer held: the gateway stayed active, the public health endpoint answered, and the watchdog jobs kept running."

2. `autoloop-failure-signal`
   - Visual: terminal crop showing `echo-autoloop` direct check returning `inactive`
   - Voiceover: "But one direct service check changed the story: the autonomous loop itself was inactive."

3. `source-of-truth-conflict`
   - Visual: split-screen of raw check `inactive` versus pulse card `active`
   - Voiceover: "The evidence then split in two: the raw service check showed inactive, while the synthesized pulse still showed active."

4. `verified-foundations`
   - Visual: compact montage of ports `8079`, `8080`, `8090`, plus both cron jobs with last run `ok`
   - Voiceover: "Supporting systems were still visible: core listeners were open, and both watchdog cron jobs last ran successfully."

5. `security-caution`
   - Visual: amber warning card summarizing redaction-disabled warnings without exposing sensitive text
   - Voiceover: "A separate caution remained in place: secret redaction was disabled, creating exposure risk without proving any actual leak."

6. `disciplined-close`
   - Visual: restrained title card reading `Evidence over assumption`
   - Voiceover: "So the evidence-backed conclusion is disciplined: core access was alive, autonomy was degraded, and no repair should be claimed without new proof."

## Assets Needed
- approved final script/narration text
- approved voiceover recording or TTS output
- subtitle file aligned to the approved narration
- style reference for the operations-briefing visual language
- scene image plates or approved text-to-video prompts for each scene
- end screen copy with source attribution and verification badge treatment
- background music selection cleared for use
- explicit approval on whether this is internal-only or public-facing

## Blocking Gaps
Evidence is insufficient for rendering a final video.

Missing requirements:
- reconciled source of truth for `echo-autoloop`
- explicit media approval after the raw-vs-pulse conflict is resolved
- approved production script package beyond draft status
- actual render assets: voiceover, subtitles, visuals, music
- final publication posture for the secret-redaction caution
- verification that any end-screen source language is approved for public reuse

## Delivery Checklist
- confirm briefing remains internal-only unless media approval changes
- obtain fresh direct service evidence for `echo-autoloop`
- resolve raw-check vs pulse conflict in the approved narrative
- lock final script, VO, subtitles, and scene prompts
- prepare end screen with source attribution and verification level
- verify no repair or recovery claim appears without direct evidence
- verify no sensitive runtime details are exposed in visuals or captions

```json
{
  "render_ready": false,
  "blocked_reasons": [
    "Direct evidence conflict remains unresolved: checks.autoloop_active reports inactive while pulse.services.echo-autoloop.status reports active.",
    "upstream_artifacts.historian explicitly marks approved_for_media as false.",
    "Active security caution remains present: secret redaction disabled warnings in gateway logs.",
    "No approved final production asset package is present in the evidence bundle (voiceover, subtitles, scene renders, music, end screen).",
    "No verified repair receipt or fresh direct check resolves the degraded autonomous-loop state."
  ],
  "output_basename": "2026-05-09-morning-briefing-ops-degraded-draft",
  "scenes": [
    {
      "slug": "hook-access-layer",
      "visual": "Dark operations dashboard showing hermes-gateway active, public healthz ok, and two watchdog cron jobs marked ok.",
      "voiceover": "This morning, the access layer held: the gateway stayed active, the public health endpoint answered, and the watchdog jobs kept running."
    },
    {
      "slug": "autoloop-failure-signal",
      "visual": "Terminal close-up highlighting the direct service result that echo-autoloop is inactive.",
      "voiceover": "But one direct service check changed the story: the autonomous loop itself was inactive."
    },
    {
      "slug": "source-of-truth-conflict",
      "visual": "Split-screen comparison between the raw service check showing inactive and the synthesized pulse showing active.",
      "voiceover": "The evidence then split in two: the raw service check showed inactive, while the synthesized pulse still showed active."
    },
    {
      "slug": "verified-foundations",
      "visual": "Minimal terminal montage showing listeners on ports 8079, 8080, and 8090, plus both cron jobs with last run status ok.",
      "voiceover": "Supporting systems were still visible: core listeners were open, and both watchdog cron jobs last ran successfully."
    },
    {
      "slug": "security-caution",
      "visual": "Amber warning card summarizing that secret redaction is disabled, without exposing any secret material.",
      "voiceover": "A separate caution remained in place: secret redaction was disabled, creating exposure risk without proving any actual leak."
    },
    {
      "slug": "disciplined-close",
      "visual": "Clean archival title card reading Evidence over assumption, with labels for gateway active, healthz ok, and autoloop inactive by direct check.",
      "voiceover": "So the evidence-backed conclusion is disciplined: core access was alive, autonomy was degraded, and no repair should be claimed without new proof."
    }
  ],
  "asset_requirements": [
    "Approved final narration script",
    "Voiceover audio file or approved TTS render",
    "Subtitle file aligned to final narration",
    "Approved visual style reference for an operations briefing",
    "Scene backgrounds or approved text-to-video prompts for all scenes",
    "Background music cleared for use",
    "End screen copy with source attribution and verification treatment",
    "Internal/public distribution approval"
  ],
  "delivery_checklist": [
    "Confirm internal-only versus public-facing release scope.",
    "Obtain a fresh direct service check for echo-autoloop.",
    "Resolve the raw-check versus pulse status conflict before final narration lock.",
    "Lock final script, voiceover, subtitles, and visual prompts.",
    "Add end screen source attribution and verification label.",
    "Verify that no repair, recovery, or all-clear claim appears without direct evidence.",
    "Verify that no sensitive runtime details are exposed in captions, overlays, or logs shown on screen."
  ],
  "source_refs": [
    "collected_at",
    "checks.gateway_active",
    "checks.autoloop_active",
    "checks.cron_list",
    "checks.ports",
    "checks.public_healthz",
    "issues",
    "cautions",
    "derived.gateway_log_metrics.recent_warning_lines",
    "upstream_artifacts.content",
    "upstream_artifacts.historian",
    "upstream_artifacts.archivist",
    "pulse.services.echo-autoloop.status",
    "pulse.overall_status",
    "pulse.cautions"
  ]
}
```

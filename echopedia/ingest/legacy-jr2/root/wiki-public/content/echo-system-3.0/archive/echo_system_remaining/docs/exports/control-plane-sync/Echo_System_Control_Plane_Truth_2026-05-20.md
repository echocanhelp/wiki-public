# Echo System Control-Plane Truth Bundle

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


- Generated_at: 2026-05-20T07:45:03.747142-07:00
- Bundle_scope: control_plane_truth

## Control-Plane Files

---
# EnvironmentOracle.json
_SHA256: 4cf82985a798a2f003a83cf770b1a998cae202bb1a7b3817ec48ceb146aab3e0_

{
  "system": "Echo System 3.0",
  "status": "autonomous-loop-active",
  "timestamp_basis": "local machine state at rebuild time",
  "architecture_note": "Lean 13-profile model (v1.5.1): Director and ToolGateway permanently removed. Media pipeline restored with 5 new profiles (content, videoforge, audioforge, voice, vision) using xAI grok-imagine model family. All profiles use xai-oauth provider.",
  "public_endpoints": {
    "dashboard": "https://bucked-diabetes-shucking.ngrok-free.dev",
    "mcp": "https://bucked-diabetes-shucking.ngrok-free.dev/mcp",
    "healthz": "https://bucked-diabetes-shucking.ngrok-free.dev/healthz"
  },
  "runtime": {
    "gateway_dispatcher": "embedded in gateway",
    "standalone_dispatcher": "disabled/preferred-off",
    "main_profiles": [
      "orchestrator",
      "echohsu",
      "sentinel",
      "healer",
      "evolver",
      "archivist",
      "historian",
      "profiler",
      "content",
      "videoforge",
      "audioforge",
      "voice",
      "vision"
    ],
    "profile_models": {
      "orchestrator": "grok-4.3",
      "echohsu": "grok-4.3",
      "sentinel": "grok-4.3",
      "healer": "grok-4.3",
      "evolver": "grok-4.3",
      "archivist": "grok-4.3",
      "historian": "grok-4.3",
      "profiler": "grok-4.3",
      "content": "grok-imagine-image-quality",
      "videoforge": "grok-imagine-video",
      "audioforge": "grok-imagine-audio",
      "voice": "grok-tts-1",
      "vision": "grok-2-vision-latest"
    },
    "provider": "xai-oauth",
    "self_management_loop": {
      "service": "echo-autoloop.service",
      "scheduler": "systemd user service with internal America/Los_Angeles stage schedule",
      "stages": [
        "sentinel",
        "healer",
        "evolver",
        "orchestrator",
        "docsync",
        "historian",
        "archivist",
        "content",
        "audioforge",
        "voice",
        "videoforge",
        "vision",
        "echohsu"
      ]
    },
    "paths": {
      "cache_documents": "/root/.hermes/cache/documents",
      "architecture_root": "/root/echo_system",
      "system_pulse": "/root/echo_system/system_pulse/SystemPulse.json",
      "environment_oracle_json": "/root/echo_system/environment/EnvironmentOracle.json",
      "environment_oracle_md": "/root/echo_system/environment/EnvironmentOracle.md"
    }
  },
  "known_gaps": [
    "No recovered prototype .py files were found in the local filesystem during this repair.",
    "No live Google Drive/wiki entity pipeline was reconstructed in this step; this repair restores architecture state, prompts, and canonical files.",
    "Kanban board currently has no ready/running worker tasks after rebuild.",
    "Media profiles (content, videoforge, audioforge, voice, vision) created and configured but not yet verified with live API calls \u2014 requires valid xai-oauth token"
  ],
  "wiki_memory": {
    "content_path": "/root/wiki-public/content/",
    "format": "Quartz v4.5.2 with wikilinks",
    "repository": "/root/wiki-public",
    "public_url": "https://echocanhelp.github.io/wiki-public",
    "content_pages": [
      "index.md",
      "love_note.md",
      "notable-taiwanese-americans.md",
      "status/automation.md"
    ]
  },
  "data_sources": {
    "wikipedia_api": {
      "endpoint": "https://en.wikipedia.org/w/api.php",
      "method": "curl + JSON parsing via Python",
      "reliability": "high",
      "notes": "API endpoint is reliable; browser has bot detection issues"
    },
    "taiwaneseamerican_org": {
      "url": "https://www.taiwaneseamerican.org",
      "content": "Community orgs, stories, interviews, creative writing prizes, book club",
      "reliability": "moderate - browser sometimes blank, curl fallback needed",
      "value": "rich community data for wiki enrichment"
    }
  },
  "extraction_notes": "Wikipedia API (curl+JSON) is the reliable method for structured data. Browser browsing has bot detection issues without residential proxies. Local wiki content files are the primary memory architecture \u2014 no GitHub push required.",
  "line_channel": {
    "status": "live",
    "activated": "2026-05-10",
    "bridge": "/root/line_bridge_fresh.py (fresh text-only)",
    "role": "primary public-facing channel for EchoHsu (replaces SMS as primary)",
    "features": [
      "Quick Replies",
      "Flex Messages",
      "Carousels",
      "Rich Menus",
      "Buttons",
      "Postbacks"
    ],
    "quota_tiers": {
      "free": "~200 messages/month per recipient",
      "light": "~5,000 messages/month per recipient",
      "standard": "~30,000 messages/month per recipient + paid extras (~JPY 3 each)"
    },
    "quota_notes": "Reply messages (user-initiated) are quota-efficient. Push, multicast, narrowcast, broadcast consume quota heavily."
  },
  "channel_status": {
    "line": "live - primary EchoHsu public channel",
    "twilio_sms": "active - secondary EchoHsu public channel",
    "telegram": "active - default/root developer support",
    "discord": "active - orchestrator/kanban operations"
  },
  "documentation_state": {
    "canonical_docs_version": "1.0.0-draft",
    "canonical_docs": [
      {
        "doc_id": "master_index",
        "path": "docs/Echo_System_Master_Index.md",
        "owner": "Archivist",
        "version": "1.5.0",
        "sha256": "78331cdbb1acee36cfc05dfe0348be7f66a2da632b783597c4725c4dea74cafd",
        "size_bytes": 17729,
        "last_updated": "2026-05-20T10:11:42.473444+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "vision_architecture",
        "path": "docs/Echo_System_Vision_Architecture.md",
        "owner": "Orchestrator",
        "version": "1.3.0",
        "sha256": "a527f2696151575d09651ab240694977bef05e1296c8fb5273d5522d3ace8d84",
        "size_bytes": 23357,
        "last_updated": "2026-05-20T10:02:06.950021+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "agent_prompts",
        "path": "docs/Echo_System_Agent_Prompts.md",
        "owner": "Orchestrator",
        "version": "1.4.0-draft",
        "sha256": "ee98a95a77cb6a7957373827d7189b7e09359271d31c6fc436cc07738a7adfcd",
        "size_bytes": 86450,
        "last_updated": "2026-05-20T10:11:42.403445+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "knowledge_core",
        "path": "docs/Echo_System_Knowledge_Core.md",
        "owner": "Archivist + Historian",
        "version": "1.4.1",
        "sha256": "4eda62863d8efbab69699228e6fe0f06d3c97be303f879c25e5311c70dd1425a",
        "size_bytes": 47882,
        "last_updated": "2026-05-20T06:56:27.601974+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "runtime_self_management",
        "path": "docs/Echo_System_Runtime_and_Self_Management.md",
        "owner": "Orchestrator + Sentinel",
        "version": "1.0.0-draft",
        "sha256": "419063679e0463b1b791b22a4910993f6d7161627df64061e001284898729117",
        "size_bytes": 30898,
        "last_updated": "2026-05-20T07:18:59.649890+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "operations_guide",
        "path": "docs/Echo_System_Operations_Guide.md",
        "owner": "ToolGateway + Orchestrator",
        "version": "1.2.4",
        "sha256": "e7ae50817839d120ff1fe027d127dc074e2d0bb1d8607b2eca30be75d1b6ad2d",
        "size_bytes": 79266,
        "last_updated": "2026-05-20T10:11:42.438445+00:00",
        "runtime_alignment_status": "pending_review"
      }
    ],
    "deprecated_docs": [],
    "last_docsync_at": "2026-05-20T07:15:42.932100-07:00",
    "last_docsync_receipt": "",
    "last_drift_count": 6,
    "last_drift_summary": "master_index: hash changed (last synced); vision_architecture: hash changed (last synced); agent_prompts: hash changed (last synced); knowledge_core: hash changed (last synced); runtime_self_management: hash changed (last synced); operations_guide: hash changed (last synced)"
  },
  "profiles_active": [
    "orchestrator",
    "echohsu",
    "archivist",
    "historian",
    "profiler",
    "sentinel",
    "healer",
    "evolver"
  ],
  "deprecated_profiles": [
    "director",
    "toolgateway"
  ]
}

---
# EnvironmentOracle.md
_SHA256: 7551f9a17cc7553bed09c5023fd780a7c445f3e81a87b24835c77b0441bd3b57_

# EnvironmentOracle

Status: autonomous-loop-active

This file is the reconstructed technical self-model for Echo System 3.0.

Key facts
- Architecture root: /root/echo_system
- Restored cache docs: /root/.hermes/cache/documents
- Shared heartbeat file: /root/echo_system/system_pulse/SystemPulse.json
- Shared oracle file: /root/echo_system/environment/EnvironmentOracle.json
- Public dashboard: https://bucked-diabetes-shucking.ngrok-free.dev
- Public MCP endpoint: https://bucked-diabetes-shucking.ngrok-free.dev/mcp
- Public MCP health endpoint: https://bucked-diabetes-shucking.ngrok-free.dev/healthz
- Active dispatcher model: gateway-embedded kanban dispatcher
- Active self-management loop process: `python3 /root/echo_system/runtime/echo_autonomous_loop.py` (persistent process; not yet a verified same-named systemd unit)
- Gateway cleanup read-back (2026-05-10 UTC): root/default active with Telegram connected; orchestrator active with Telegram + Discord connected; echohsu active with Telegram + SMS + API server connected
- Verified live Telegram token placement after cleanup: `/root/.hermes/.env` -> prefix `8527210510`; `/root/.hermes/profiles/orchestrator/.env` -> prefix `8630404747`; `/root/.hermes/profiles/echohsu/.env` -> prefix `8532762733`
- Gateway conflict evidence: journald for `hermes-gateway.service` recorded `Telegram bot token already in use (PID 30393). Stop the other gateway first.` during the failed restart loop

Canonical conversational profiles (12)
- orchestrator
- echohsu
- sentinel
- healer
- evolver
- archivist
- historian
- profiler
- content
- videoforge
- director
- toolgateway

Compatibility specialist profiles
- none (legacy compatibility profiles were removed during cleanup)

Rebuild notes
- Recovered architecture documents from Hermes session history and restored them into cache/doc archives.
- Removed non-canonical compatibility profiles: researcher, analyst, writer, reviewer, ops.
- Created missing canonical Echo profiles and injected recovered role prompts.
- Repaired invalid specialist model configs and promoted all canonical profiles to the working gpt-5.4 / openai-codex model.
- Activated a persistent autonomous loop for Sentinel, Healer, Evolver, and Orchestrator via systemd.
- Preserved EnvironmentOracle as shared state rather than a separate conversational profile to resolve the 12-vs-13 mismatch in the original source docs.

LINE channel activation (2026-05-10)
- LINE Official Account is now live and active as the primary public-facing channel for EchoHsu.
- LINE bridge: /root/line_bridge_fresh.py (fresh text-only) (aiohttp webhook server + BOT API client).
- LINE replaces Twilio/SMS as the primary EchoHsu public channel (SMS remains active secondary).
- Quota-aware messaging: Free/Light/Standard tier limits apply per recipient; reply messages are quota-efficient; push/multicast/narrowcast/broadcast consume quota heavily.
- Rich interaction features enabled: Quick Replies, Flex Messages, Carousels, Rich Menus, Buttons, Postbacks.
- EchoHsu persona enriched: personal/community secretary for Leonard and inner circle; LINE-first design with low cognitive load and high delight.

---
# SystemPulse.json
_SHA256: c6af3b9bd6628f96e6abf67f31b1c0271e00c5178bd03dd37aa3f06c9e2dc55b_

{
  "timestamp": "2026-05-20T07:00:27.983063-07:00",
  "system_health_score": 20,
  "overall_status": "🟠 Autonomous loop degraded",
  "scan_agent": "sentinel",
  "previous_pulse": {
    "timestamp": "2026-05-15T04:07:54.725127-07:00",
    "health_score": 55,
    "status": "DEGRADED: Major recovery from CRITICAL — autoloop active, public healthz OK, cro"
  },
  "services": {
    "hermes-gateway": {
      "status": "active",
      "pid": 12889,
      "uptime": "2 days 11 hours (since 2026-05-12T18:28:35 UTC)",
      "restarts_total": 0,
      "memory": "209.1M (peak: 706.9M, swap: 62.6M)",
      "cpu_total": "12min 44.833s",
      "new_warnings_since_0500_utc": 0
    },
    "echo-autoloop": {
      "status": "CRASH_LOOP - restarts every ~23 minutes",
      "restarts_total": 120,
      "crash_interval_minutes": 23,
      "last_crash": "2026-05-15T11:30:37 UTC",
      "error": "TypeError: 'str' object does not support item assignment at echo_autonomous_loop.py:1101",
      "root_cause": "data.setdefault(summary, {}) returns existing string value from previous pulse; code then tries dict item assignment"
    },
    "hermes-dashboard": {
      "status": "active",
      "pid": 1700,
      "port": 8080
    },
    "hermes-http-mux": {
      "status": "active",
      "pid": 49950,
      "port": 8079
    },
    "mcp-server": {
      "status": "port 8090 NOT listening"
    },
    "ngrok-tunnel": {
      "status": "RUNNING",
      "healthz": "OK - all upstreams healthy",
      "url": "https://bucked-diabetes-shucking.ngrok-free.dev"
    }
  },
  "resources": {
    "disk_root": {
      "total": "20G",
      "used": "9.8G",
      "free": "8.8G",
      "pct": 53
    },
    "memory": {
      "total_mb": 4096,
      "used_mb": 1262,
      "free_mb": 1197,
      "available_mb": 2833,
      "pct": 31
    }
  },
  "cron_jobs": {
    "scheduled": 3,
    "all_healthy": true,
    "missing": [
      "public-mcp-watchdog (5-min)"
    ]
  },
  "profiles": {
    "total": 13,
    "running": [
      "default",
      "echohsu",
      "orchestrator"
    ],
    "stopped_count": 10
  },
  "ports": {
    "8079": "LISTENING (python PID 49950)",
    "8080": "LISTENING (hermes PID 1700)",
    "8090": "NOT LISTENING"
  },
  "issues": [
    {
      "id": "I-AUTO-003",
      "severity": "critical",
      "component": "echo-autoloop",
      "description": "DETERMINISTIC CRASH LOOP: TypeError at echo_autonomous_loop.py:1101. data.setdefault(summary, {}) returns existing string from previous pulse JSON. Code then does summary[compatibility_profiles_repaired] = [] which crashes on str type. Crash cycle is ~23 minutes. Restart count: 120 and climbing.",
      "root_cause": "SystemPulse.json top-level summary field is a string; autoloop expects dict",
      "first_seen": "2026-05-15T04:07 PT",
      "fix": "Patch line 1100 to: summary = data.get(\"summary\"); if not isinstance(summary, dict): summary = data[\"summary\"] = {}"
    },
    {
      "id": "I-TEL-002",
      "severity": "medium",
      "component": "telegram",
      "description": "Telegram connectivity degraded 23+ hours. Primary DNS and fallback IP 149.154.166.110 both failing. No new warnings since 15:58 UTC May 14.",
      "persistent": true
    },
    {
      "id": "I-MCP-002",
      "severity": "medium",
      "component": "mcp-server",
      "description": "Port 8090 not listening but ngrok healthz returns OK. Public MCP watchdog cron missing.",
      "persistent": true
    },
    {
      "id": "I-MEM-001",
      "severity": "medium",
      "component": "agent-memory",
      "description": "Persistent memory at capacity: user profile 1307/1375 (95%), memory notes 2099/2200 (95%).",
      "persistent": true
    }
  ],
  "baseline_comparison": {
    "vs_previous_pulse": {
      "health_score_change": "-15 (55 -> 40)",
      "degradation": "Confirmed deterministic crash loop in autoloop. Root cause identified and fixable.",
      "stable": [
        "gateway (0 restarts)",
        "public healthz",
        "disk (53%)",
        "memory (31%)",
        "cron (3/3 healthy)"
      ],
      "worsening": [
        "autoloop restarts: 119 -> 120 (+1 in 23min cycle)"
      ]
    }
  },
  "recommended_repairs": [
    {
      "priority": 1,
      "action": "Fix autoloop crash loop",
      "file": "/root/echo_system/runtime/echo_autonomous_loop.py",
      "line": 1100,
      "current": "summary = data.setdefault(\"summary\", {})",
      "fix": "summary = data.get(\"summary\"); if not isinstance(summary, dict): summary = data[\"summary\"] = {}",
      "reason": "Root cause of crash loop. Previous pulse wrote summary as string; autoloop expects dict."
    },
    {
      "priority": 2,
      "action": "Remove top-level summary string from SystemPulse.json",
      "reason": "The string summary field at line 258 triggers the autoloop crash. Either remove it or rename it to pulse_summary_text."
    },
    {
      "priority": 3,
      "action": "Investigate Telegram connectivity",
      "commands": [
        "nslookup api.telegram.org",
        "curl -v --max-time 10 https://api.telegram.org/getMe"
      ]
    },
    {
      "priority": 4,
      "action": "Create public MCP watchdog cron (5-min interval)"
    },
    {
      "priority": 5,
      "action": "Enable secret redaction",
      "command": "export HERMES_REDACT_SECRETS=true"
    }
  ],
  "agents": {
    "sentinel": {
      "status": "🟡",
      "last_scan": "2026-05-20T03:00:39.642965-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/sentinel.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/sentinel.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "healer": {
      "status": "🔴",
      "last_scan": "2026-05-20T03:30:53.445319-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/healer.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/healer.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "evolver": {
      "status": "🔴",
      "last_scan": "2026-05-20T04:31:06.658093-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/evolver.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/evolver.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "orchestrator": {
      "status": "🟡",
      "last_scan": "2026-05-20T05:00:36.645507-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/orchestrator.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/orchestrator.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "docsync": {
      "status": "🔴",
      "last_scan": "2026-05-20T05:15:39.446066-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/docsync.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/docsync.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/docsync.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/docsync.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/docsync.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/docsync.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "historian": {
      "status": "🔴",
      "last_scan": "2026-05-20T05:15:54.076472-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/historian.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/historian.gate.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/historian.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/historian.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/historian.gate.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/historian.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "archivist": {
      "status": "🟡",
      "last_scan": "2026-05-20T05:31:39.272858-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/archivist.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/archivist.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/archivist.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/archivist.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/archivist.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/archivist.receipt.json",
        "executor_status": "executed",
        "executor_success": true,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "content": {
      "status": "🔴",
      "last_scan": "2026-05-20T06:00:54.244797-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/content.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/content.manifest.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/content.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/content.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/content.manifest.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/content.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "videoforge": {
      "status": "🔴",
      "last_scan": "2026-05-20T06:31:01.285648-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/videoforge.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "echohsu": {
      "status": "🟡",
      "last_scan": "2026-05-20T07:00:27.983063-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.delivery.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.delivery.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-20/echohsu.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    }
  },
  "summary": {
    "compatibility_profiles_repaired": [],
    "autonomous_loop": {
      "service": "echo-autoloop.service",
      "timezone": "America/Los_Angeles",
      "stages": [
        "sentinel",
        "healer",
        "evolver",
        "orchestrator",
        "docsync",
        "historian",
        "archivist",
        "content",
        "videoforge",
        "echohsu"
      ],
      "last_updated": "2026-05-20T07:00:27.983063-07:00",
      "runtime_signals": {
        "gateway_restarts_total": 0,
        "autoloop_restarts_total": 0,
        "redaction_disabled_warnings": 0,
        "remote_protocol_errors": 0,
        "telegram_network_errors": 0,
        "recent_warning_lines": []
      },
      "health_penalties": [
        "sentinel reported 1 issue(s)",
        "healer exit code 1",
        "healer reported 1 issue(s)",
        "evolver exit code 1",
        "evolver reported 1 issue(s)",
        "orchestrator reported 1 issue(s)",
        "docsync exit code 1",
        "docsync reported 1 issue(s)",
        "historian exit code 1",
        "historian reported 1 issue(s)",
        "archivist reported 1 issue(s)",
        "content exit code 1",
        "content reported 1 issue(s)",
        "videoforge exit code 1",
        "videoforge reported 1 issue(s)",
        "echohsu reported 1 issue(s)"
      ]
    }
  }
}

---
# SystemPulse.md
_SHA256: 7443db434af3c980ff8c35d1aaf9a3f8404d14aae89789ab4d07911e30dde052_

# Echo System Pulse

- Timestamp: 2026-05-20T07:00:27.983063-07:00
- Health score: 20
- Status: 🟠 Autonomous loop degraded

## Agents
- sentinel: 🟡 | last_scan=2026-05-20T03:00:39.642965-07:00 | issues=1 | cautions=0 | auto_fixes=0
- healer: 🔴 | last_scan=2026-05-20T03:30:53.445319-07:00 | issues=1 | cautions=0 | auto_fixes=0
- evolver: 🔴 | last_scan=2026-05-20T04:31:06.658093-07:00 | issues=1 | cautions=0 | auto_fixes=0
- orchestrator: 🟡 | last_scan=2026-05-20T05:00:36.645507-07:00 | issues=1 | cautions=0 | auto_fixes=0
- docsync: 🔴 | last_scan=2026-05-20T05:15:39.446066-07:00 | issues=1 | cautions=0 | auto_fixes=0
- historian: 🔴 | last_scan=2026-05-20T05:15:54.076472-07:00 | issues=1 | cautions=0 | auto_fixes=0
- archivist: 🟡 | last_scan=2026-05-20T05:31:39.272858-07:00 | issues=1 | cautions=0 | auto_fixes=0
- content: 🔴 | last_scan=2026-05-20T06:00:54.244797-07:00 | issues=1 | cautions=0 | auto_fixes=0
- videoforge: 🔴 | last_scan=2026-05-20T06:31:01.285648-07:00 | issues=1 | cautions=0 | auto_fixes=0
- echohsu: 🟡 | last_scan=2026-05-20T07:00:27.983063-07:00 | issues=1 | cautions=0 | auto_fixes=0

## Autonomous Loop
- Service: echo-autoloop.service
- Timezone: America/Los_Angeles
- Stages: sentinel, healer, evolver, orchestrator, docsync, historian, archivist, content, videoforge, echohsu
- Last updated: 2026-05-20T07:00:27.983063-07:00
- Gateway restarts: 0
- Autoloop restarts: 0
- Redaction warnings: 0
- Remote protocol errors: 0
- Telegram network warnings: 0

## Health Penalties
- sentinel reported 1 issue(s)
- healer exit code 1
- healer reported 1 issue(s)
- evolver exit code 1
- evolver reported 1 issue(s)
- orchestrator reported 1 issue(s)
- docsync exit code 1
- docsync reported 1 issue(s)
- historian exit code 1
- historian reported 1 issue(s)
- archivist reported 1 issue(s)
- content exit code 1
- content reported 1 issue(s)
- videoforge exit code 1
- videoforge reported 1 issue(s)
- echohsu reported 1 issue(s)

---
## Latest DocSync Receipt

```json
{
  "bundle_bytes": 286293,
  "bundle_path": "/root/echo_system/docs/exports/daily-sync/Echo_System_Canonical_Docs_Daily_Sync_2026-05-20.md",
  "bundle_scope": "canonical_docs_only",
  "bundle_sha256": "d14f1240a38ad2c5a6ac8952c047a29a866cd2bcc2b037432785803b9b9df904",
  "canonical_docs": [
    "Echo_System_Master_Index.md",
    "Echo_System_Vision_Architecture.md",
    "Echo_System_Agent_Prompts.md",
    "Echo_System_Knowledge_Core.md",
    "Echo_System_Runtime_and_Self_Management.md",
    "Echo_System_Operations_Guide.md"
  ],
  "date_key": "2026-05-20",
  "drive_file": {
    "id": "1oLv5if76la13UgZ8rdj4Hu1X9S6IafQ4",
    "mimeType": "text/markdown",
    "name": "Echo_System_Canonical_Docs_Daily_Sync_2026-05-20.md",
    "parents": [
      "0ABhqZwu84cYbUk9PVA"
    ],
    "size": "286293",
    "webViewLink": "https://drive.google.com/file/d/1oLv5if76la13UgZ8rdj4Hu1X9S6IafQ4/view?usp=drivesdk"
  },
  "drive_folder_id": "0ABhqZwu84cYbUk9PVA",
  "environment_oracle": {
    "canonical_docs_tracked": 6,
    "drift_count": 6,
    "drift_summary": "master_index: hash changed (last synced); vision_architecture: hash changed (last synced); agent_prompts: hash changed (last synced); knowledge_core: hash changed (last synced); runtime_self_management: hash changed (last synced); operations_guide: hash changed (last synced)",
    "updated": true
  },
  "generated_at": "2026-05-20T07:15:42.932100-07:00",
  "source_count": 6,
  "source_manifest": [
    {
      "bytes": 17729,
      "path": "Echo_System_Master_Index.md",
      "sha256": "78331cdbb1acee36cfc05dfe0348be7f66a2da632b783597c4725c4dea74cafd"
    },
    {
      "bytes": 23357,
      "path": "Echo_System_Vision_Architecture.md",
      "sha256": "a527f2696151575d09651ab240694977bef05e1296c8fb5273d5522d3ace8d84"
    },
    {
      "bytes": 86450,
      "path": "Echo_System_Agent_Prompts.md",
      "sha256": "ee98a95a77cb6a7957373827d7189b7e09359271d31c6fc436cc07738a7adfcd"
    },
    {
      "bytes": 47882,
      "path": "Echo_System_Knowledge_Core.md",
      "sha256": "4eda62863d8efbab69699228e6fe0f06d3c97be303f879c25e5311c70dd1425a"
    },
    {
      "bytes": 30898,
      "path": "Echo_System_Runtime_and_Self_Management.md",
      "sha256": "419063679e0463b1b791b22a4910993f6d7161627df64061e001284898729117"
    },
    {
      "bytes": 79266,
      "path": "Echo_System_Operations_Guide.md",
      "sha256": "e7ae50817839d120ff1fe027d127dc074e2d0bb1d8607b2eca30be75d1b6ad2d"
    }
  ],
  "source_root": "/root/echo_system/docs",
  "status": "uploaded",
  "verification": {
    "remote_name_matches": true,
    "remote_parent_matches": true,
    "remote_size_matches": true
  },
  "verified": true
}
```

---
## Cron Inventory

*Could not retrieve cron inventory.*

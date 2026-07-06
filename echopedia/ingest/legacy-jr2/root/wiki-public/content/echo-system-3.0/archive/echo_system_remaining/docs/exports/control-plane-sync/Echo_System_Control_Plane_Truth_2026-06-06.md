# Echo System Control-Plane Truth Bundle

- Generated_at: 2026-06-06T07:45:57.388248-07:00
- Bundle_scope: control_plane_truth

## Control-Plane Files

---
# EnvironmentOracle.json
_SHA256: 7a4b5b4c8af4532c47396360ee2ca82094e6daf2db4ba29e3d58b0f7b2438b0e_

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
    "bridge": "/root/line_bridge.py",
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
        "sha256": "c9ebc287532d2182cd7cd22e4e1a987cab9269da52e3f46c8bc0110bcdc1646a",
        "size_bytes": 21216,
        "last_updated": "2026-05-26T23:08:30.200210+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "vision_architecture",
        "path": "docs/Echo_System_Vision_Architecture.md",
        "owner": "Orchestrator",
        "version": "1.3.0",
        "sha256": "eec5354406f27e1b0cf5295bca14057ac5a2ffd16b082ec91489d8c3d230015c",
        "size_bytes": 24009,
        "last_updated": "2026-05-24T06:12:33.246563+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "agent_prompts",
        "path": "docs/Echo_System_Agent_Prompts.md",
        "owner": "Orchestrator",
        "version": "1.4.0-draft",
        "sha256": "1c8bed3b98c937ce2b0529bf41c9a0b875dd6b112799021221ad449bbb9b02fa",
        "size_bytes": 89026,
        "last_updated": "2026-05-26T23:17:24.432007+00:00",
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
        "sha256": "ce8de8f130ac9c1b4e93f94643477d88d1aabaf15eda5a6fe4b12557e699a492",
        "size_bytes": 31931,
        "last_updated": "2026-05-26T23:17:02.199223+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "operations_guide",
        "path": "docs/Echo_System_Operations_Guide.md",
        "owner": "ToolGateway + Orchestrator",
        "version": "1.2.4",
        "sha256": "510a795fd45d7049c28cb6819612a85407ecb23d1aa849f9fdec183798d73433",
        "size_bytes": 82993,
        "last_updated": "2026-05-26T23:17:14.648102+00:00",
        "runtime_alignment_status": "pending_review"
      }
    ],
    "deprecated_docs": [],
    "last_docsync_at": "2026-06-06T07:15:57.024430-07:00",
    "last_docsync_receipt": "",
    "last_drift_count": 0,
    "last_drift_summary": "No drift detected"
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
- LINE bridge: /root/line_bridge.py (aiohttp webhook server + BOT API client).
- LINE replaces Twilio/SMS as the primary EchoHsu public channel (SMS remains active secondary).
- Quota-aware messaging: Free/Light/Standard tier limits apply per recipient; reply messages are quota-efficient; push/multicast/narrowcast/broadcast consume quota heavily.
- Rich interaction features enabled: Quick Replies, Flex Messages, Carousels, Rich Menus, Buttons, Postbacks.
- EchoHsu persona enriched: personal/community secretary for Leonard and inner circle; LINE-first design with low cognitive load and high delight.

---
# SystemPulse.json
_SHA256: 6b7d3a6a8c0a00dcc40913bf5701782395cd0cffb2ea0d164422684d485703ae_

{
  "timestamp": "2026-06-06T07:01:04.105620-07:00",
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
      "last_scan": "2026-06-06T03:00:58.024550-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/sentinel.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/sentinel.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "healer": {
      "status": "🟡",
      "last_scan": "2026-06-06T03:31:08.099685-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/healer.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/healer.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "evolver": {
      "status": "🟡",
      "last_scan": "2026-06-06T04:30:18.988537-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/evolver.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/evolver.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
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
      "last_scan": "2026-06-06T05:00:39.668294-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/orchestrator.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/orchestrator.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
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
      "last_scan": "2026-06-06T05:15:42.452419-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/docsync.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/docsync.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/docsync.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/docsync.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/docsync.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/docsync.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "historian": {
      "status": "🟡",
      "last_scan": "2026-06-06T05:15:52.591085-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/historian.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/historian.gate.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/historian.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/historian.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/historian.gate.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/historian.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "archivist": {
      "status": "🟡",
      "last_scan": "2026-06-06T05:31:03.501003-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/archivist.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/archivist.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/archivist.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/archivist.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/archivist.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/archivist.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "content": {
      "status": "🟡",
      "last_scan": "2026-06-06T06:00:15.801362-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/content.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/content.manifest.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/content.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/content.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/content.manifest.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/content.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "videoforge": {
      "status": "🔴",
      "last_scan": "2026-06-06T06:30:35.925515-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/videoforge.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "echohsu": {
      "status": "🟡",
      "last_scan": "2026-06-06T07:01:04.105620-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.md. Structured: /root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.delivery.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.delivery.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/echohsu.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "audioforge": {
      "status": "🔴",
      "last_scan": "2026-06-06T06:15:25.089932-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/audioforge.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/audioforge.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "voice": {
      "status": "🔴",
      "last_scan": "2026-06-06T06:15:30.414533-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/voice.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/voice.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "vision": {
      "status": "🔴",
      "last_scan": "2026-06-06T06:45:41.507518-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 1,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-06-06/vision.md. Issues: ['public MCP watchdog cron missing']. Cautions: ['hermes-gateway has nonzero restart count']",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-06-06/vision.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 1,
        "structured_path": "",
        "receipt_path": "",
        "executor_status": "",
        "executor_success": false,
        "executor_blocked": false,
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
        "audioforge",
        "voice",
        "videoforge",
        "vision",
        "echohsu"
      ],
      "last_updated": "2026-06-06T07:01:04.105620-07:00",
      "runtime_signals": {
        "gateway_restarts_total": 5,
        "autoloop_restarts_total": 0,
        "redaction_disabled_warnings": 0,
        "remote_protocol_errors": 0,
        "telegram_network_errors": 2,
        "recent_warning_lines": [
          "2026-06-06 01:01:17,660 WARNING gateway.platforms.telegram: [Telegram] Telegram network error, scheduling reconnect: httpx.ReadError: ",
          "2026-06-06 01:01:17,662 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 1/10), reconnecting in 5s. Error: httpx.ReadError: "
        ]
      },
      "health_penalties": [
        "sentinel reported 1 issue(s)",
        "sentinel reported 1 caution(s)",
        "healer reported 1 issue(s)",
        "healer reported 1 caution(s)",
        "evolver reported 1 issue(s)",
        "evolver reported 1 caution(s)",
        "orchestrator reported 1 issue(s)",
        "orchestrator reported 1 caution(s)",
        "docsync exit code 1",
        "docsync reported 1 issue(s)",
        "docsync reported 1 caution(s)",
        "historian reported 1 issue(s)",
        "historian reported 1 caution(s)",
        "archivist reported 1 issue(s)",
        "archivist reported 1 caution(s)",
        "content reported 1 issue(s)",
        "content reported 1 caution(s)",
        "videoforge exit code 1",
        "videoforge reported 1 issue(s)",
        "videoforge reported 1 caution(s)",
        "echohsu reported 1 issue(s)",
        "echohsu reported 1 caution(s)",
        "audioforge exit code 1",
        "audioforge reported 1 issue(s)",
        "audioforge reported 1 caution(s)",
        "voice exit code 1",
        "voice reported 1 issue(s)",
        "voice reported 1 caution(s)",
        "vision exit code 1",
        "vision reported 1 issue(s)",
        "vision reported 1 caution(s)",
        "2 Telegram network warning(s)",
        "gateway restart count 5"
      ]
    }
  }
}

---
# SystemPulse.md
_SHA256: 2beee239d34e5ff579660e817c827971fd1208889a0129b47ba90bf6bbe8b648_

# Echo System Pulse

- Timestamp: 2026-06-06T07:01:04.105620-07:00
- Health score: 20
- Status: 🟠 Autonomous loop degraded

## Agents
- sentinel: 🟡 | last_scan=2026-06-06T03:00:58.024550-07:00 | issues=1 | cautions=1 | auto_fixes=0
- healer: 🟡 | last_scan=2026-06-06T03:31:08.099685-07:00 | issues=1 | cautions=1 | auto_fixes=0
- evolver: 🟡 | last_scan=2026-06-06T04:30:18.988537-07:00 | issues=1 | cautions=1 | auto_fixes=0
- orchestrator: 🟡 | last_scan=2026-06-06T05:00:39.668294-07:00 | issues=1 | cautions=1 | auto_fixes=0
- docsync: 🔴 | last_scan=2026-06-06T05:15:42.452419-07:00 | issues=1 | cautions=1 | auto_fixes=0
- historian: 🟡 | last_scan=2026-06-06T05:15:52.591085-07:00 | issues=1 | cautions=1 | auto_fixes=0
- archivist: 🟡 | last_scan=2026-06-06T05:31:03.501003-07:00 | issues=1 | cautions=1 | auto_fixes=0
- content: 🟡 | last_scan=2026-06-06T06:00:15.801362-07:00 | issues=1 | cautions=1 | auto_fixes=0
- videoforge: 🔴 | last_scan=2026-06-06T06:30:35.925515-07:00 | issues=1 | cautions=1 | auto_fixes=0
- echohsu: 🟡 | last_scan=2026-06-06T07:01:04.105620-07:00 | issues=1 | cautions=1 | auto_fixes=0
- audioforge: 🔴 | last_scan=2026-06-06T06:15:25.089932-07:00 | issues=1 | cautions=1 | auto_fixes=0
- voice: 🔴 | last_scan=2026-06-06T06:15:30.414533-07:00 | issues=1 | cautions=1 | auto_fixes=0
- vision: 🔴 | last_scan=2026-06-06T06:45:41.507518-07:00 | issues=1 | cautions=1 | auto_fixes=0

## Autonomous Loop
- Service: echo-autoloop.service
- Timezone: America/Los_Angeles
- Stages: sentinel, healer, evolver, orchestrator, docsync, historian, archivist, content, audioforge, voice, videoforge, vision, echohsu
- Last updated: 2026-06-06T07:01:04.105620-07:00
- Gateway restarts: 5
- Autoloop restarts: 0
- Redaction warnings: 0
- Remote protocol errors: 0
- Telegram network warnings: 2

## Health Penalties
- sentinel reported 1 issue(s)
- sentinel reported 1 caution(s)
- healer reported 1 issue(s)
- healer reported 1 caution(s)
- evolver reported 1 issue(s)
- evolver reported 1 caution(s)
- orchestrator reported 1 issue(s)
- orchestrator reported 1 caution(s)
- docsync exit code 1
- docsync reported 1 issue(s)
- docsync reported 1 caution(s)
- historian reported 1 issue(s)
- historian reported 1 caution(s)
- archivist reported 1 issue(s)
- archivist reported 1 caution(s)
- content reported 1 issue(s)
- content reported 1 caution(s)
- videoforge exit code 1
- videoforge reported 1 issue(s)
- videoforge reported 1 caution(s)
- echohsu reported 1 issue(s)
- echohsu reported 1 caution(s)
- audioforge exit code 1
- audioforge reported 1 issue(s)
- audioforge reported 1 caution(s)
- voice exit code 1
- voice reported 1 issue(s)
- voice reported 1 caution(s)
- vision exit code 1
- vision reported 1 issue(s)
- vision reported 1 caution(s)
- 2 Telegram network warning(s)
- gateway restart count 5

---
## Latest DocSync Receipt

```json
{
  "bundle_bytes": 297768,
  "bundle_path": "/root/echo_system/docs/exports/daily-sync/Echo_System_Canonical_Docs_Daily_Sync_2026-06-06.md",
  "bundle_scope": "canonical_docs_only",
  "bundle_sha256": "07aff3cb0a467a4047a7a87f66dffec646699a29ee900077cf25a150d1ff1f85",
  "canonical_docs": [
    "Echo_System_Master_Index.md",
    "Echo_System_Vision_Architecture.md",
    "Echo_System_Agent_Prompts.md",
    "Echo_System_Knowledge_Core.md",
    "Echo_System_Runtime_and_Self_Management.md",
    "Echo_System_Operations_Guide.md"
  ],
  "date_key": "2026-06-06",
  "drive_file": {
    "id": "175Chaj6yPkmzS0PSJ61XHDZsd18ZvOLd",
    "mimeType": "text/markdown",
    "name": "Echo_System_Canonical_Docs_Daily_Sync_2026-06-06.md",
    "parents": [
      "0ABhqZwu84cYbUk9PVA"
    ],
    "size": "297768",
    "webViewLink": "https://drive.google.com/file/d/175Chaj6yPkmzS0PSJ61XHDZsd18ZvOLd/view?usp=drivesdk"
  },
  "drive_folder_id": "0ABhqZwu84cYbUk9PVA",
  "environment_oracle": {
    "canonical_docs_tracked": 6,
    "drift_count": 0,
    "drift_summary": "No drift detected",
    "updated": true
  },
  "generated_at": "2026-06-06T07:15:57.024430-07:00",
  "source_count": 6,
  "source_manifest": [
    {
      "bytes": 21216,
      "path": "Echo_System_Master_Index.md",
      "sha256": "c9ebc287532d2182cd7cd22e4e1a987cab9269da52e3f46c8bc0110bcdc1646a"
    },
    {
      "bytes": 24009,
      "path": "Echo_System_Vision_Architecture.md",
      "sha256": "eec5354406f27e1b0cf5295bca14057ac5a2ffd16b082ec91489d8c3d230015c"
    },
    {
      "bytes": 89026,
      "path": "Echo_System_Agent_Prompts.md",
      "sha256": "1c8bed3b98c937ce2b0529bf41c9a0b875dd6b112799021221ad449bbb9b02fa"
    },
    {
      "bytes": 47882,
      "path": "Echo_System_Knowledge_Core.md",
      "sha256": "4eda62863d8efbab69699228e6fe0f06d3c97be303f879c25e5311c70dd1425a"
    },
    {
      "bytes": 31931,
      "path": "Echo_System_Runtime_and_Self_Management.md",
      "sha256": "ce8de8f130ac9c1b4e93f94643477d88d1aabaf15eda5a6fe4b12557e699a492"
    },
    {
      "bytes": 82993,
      "path": "Echo_System_Operations_Guide.md",
      "sha256": "510a795fd45d7049c28cb6819612a85407ecb23d1aa849f9fdec183798d73433"
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

# Echo System Control-Plane Truth Bundle

> **Historical Snapshot Notice:** This file is a dated export for traceability and is **non-authoritative**. Use canonical docs in `/root/echo_system/docs/` and live runtime/config read-back for operational decisions.


- Generated_at: 2026-05-17T07:45:42.271566-07:00
- Bundle_scope: control_plane_truth

## Control-Plane Files

---
# EnvironmentOracle.json
_SHA256: de08f979e9742d012e79bb2f64e8325e8c63fc43e4770b5956157dfa9bc67a71_

{
  "system": "Echo System 3.0",
  "status": "autonomous-loop-active",
  "timestamp_basis": "local machine state at rebuild time",
  "architecture_note": "Master prompt claims 12 agents but lists 13 components; runtime rebuild uses 12 conversational profiles plus EnvironmentOracle as shared state/model.",
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
      "director",
      "toolgateway"
    ],
    "compatibility_profiles": [],
    "self_management_loop": {
      "service": "echo-autoloop.service",
      "scheduler": "systemd user service with internal America/Los_Angeles stage schedule",
      "stages": [
        "sentinel",
        "healer",
        "evolver",
        "orchestrator"
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
    "Downstream autonomous stages for Archivist, Content, VideoForge, and EchoHsu are not yet wired into the systemd loop."
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
        "version": "1.3.0",
        "sha256": "e0469fa81e8fce386406fc73956d4d58b6c3f85bfb75872ce0f47f6319744c0e",
        "size_bytes": 15761,
        "last_updated": "2026-05-17T13:42:38.259352+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "vision_architecture",
        "path": "docs/Echo_System_Vision_Architecture.md",
        "owner": "Orchestrator",
        "version": "1.0.0-draft",
        "sha256": "9acbf79433ed5f70e788deafef23eac579e34faa7f559132d835fd1138803d91",
        "size_bytes": 21735,
        "last_updated": "2026-05-15T05:19:53.459707+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "agent_prompts",
        "path": "docs/Echo_System_Agent_Prompts.md",
        "owner": "Orchestrator",
        "version": "1.0.1-draft",
        "sha256": "f26d7b28f44dce15ce68a89de1ca491174ee287bf05b00c060f709e4dfb6515e",
        "size_bytes": 57161,
        "last_updated": "2026-05-17T11:18:20.546360+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "knowledge_core",
        "path": "docs/Echo_System_Knowledge_Core.md",
        "owner": "Archivist + Historian",
        "version": "1.0.1-draft",
        "sha256": "7383c7a143154bceae9c499eda7a983e6101bf6f991eb16d0606318a316e085d",
        "size_bytes": 45862,
        "last_updated": "2026-05-17T13:34:00.592541+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "runtime_self_management",
        "path": "docs/Echo_System_Runtime_and_Self_Management.md",
        "owner": "Orchestrator + Sentinel",
        "version": "1.0.0-draft",
        "sha256": "095524c9cab2ee9a4a03d0f691fe4b6edd50b600d6e516d825b072ad1508e8c9",
        "size_bytes": 29047,
        "last_updated": "2026-05-15T05:19:53.465130+00:00",
        "runtime_alignment_status": "pending_review"
      },
      {
        "doc_id": "operations_guide",
        "path": "docs/Echo_System_Operations_Guide.md",
        "owner": "ToolGateway + Orchestrator",
        "version": "1.0.1-draft",
        "sha256": "cb371eb26b2050f523eb9d297c34770fc54c474bbb8efe3eb391cd5c5599efa1",
        "size_bytes": 69200,
        "last_updated": "2026-05-17T13:11:02.041990+00:00",
        "runtime_alignment_status": "pending_review"
      }
    ],
    "deprecated_docs": [],
    "last_docsync_at": "2026-05-17T07:15:24.319333-07:00",
    "last_docsync_receipt": "",
    "last_drift_count": 4,
    "last_drift_summary": "master_index: hash changed (last synced); agent_prompts: hash changed (last synced); knowledge_core: hash changed (last synced); operations_guide: hash changed (last synced)"
  }
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
_SHA256: 3234aeb2269150e8d2b99e41f618bc452d478474dc724ad03c185ef5430efa6b_

{
  "timestamp": "2026-05-17T07:08:00.824809-07:00",
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
      "last_scan": "2026-05-17T03:21:12.956596-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/sentinel.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/sentinel.md",
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
      "status": "🟡",
      "last_scan": "2026-05-17T03:40:04.839148-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/healer.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/healer.md",
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
    "evolver": {
      "status": "🟡",
      "last_scan": "2026-05-17T04:41:44.542432-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/evolver.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/evolver.md",
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
    "orchestrator": {
      "status": "🟡",
      "last_scan": "2026-05-17T05:17:17.835563-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/orchestrator.md. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/orchestrator.md",
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
      "last_scan": "2026-05-17T05:18:20.140486-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/docsync.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/docsync.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/docsync.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/docsync.md",
        "profile_exit_code": 1,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/docsync.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/docsync.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "historian": {
      "status": "🟡",
      "last_scan": "2026-05-17T05:34:27.928599-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/historian.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/historian.gate.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/historian.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/historian.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/historian.gate.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/historian.receipt.json",
        "executor_status": "executed",
        "executor_success": true,
        "executor_blocked": false,
        "verified_handles_count": 0
      }
    },
    "archivist": {
      "status": "🟡",
      "last_scan": "2026-05-17T05:45:23.094746-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/archivist.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/archivist.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/archivist.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/archivist.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/archivist.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/archivist.receipt.json",
        "executor_status": "executed",
        "executor_success": true,
        "executor_blocked": false,
        "verified_handles_count": 2
      }
    },
    "content": {
      "status": "🟡",
      "last_scan": "2026-05-17T06:15:43.983381-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/content.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/content.manifest.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/content.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/content.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/content.manifest.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/content.receipt.json",
        "executor_status": "executed",
        "executor_success": true,
        "executor_blocked": false,
        "verified_handles_count": 1
      }
    },
    "videoforge": {
      "status": "🟡",
      "last_scan": "2026-05-17T06:43:39.044648-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.plan.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.plan.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/videoforge.receipt.json",
        "executor_status": "blocked",
        "executor_success": false,
        "executor_blocked": true,
        "verified_handles_count": 0
      }
    },
    "echohsu": {
      "status": "🟡",
      "last_scan": "2026-05-17T07:08:00.824809-07:00",
      "issues_found": 1,
      "auto_fixes_applied": 0,
      "cautions_found": 0,
      "notes": "Artifact: /root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.md. Structured: /root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.delivery.json. Receipt: /root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.receipt.json. Issues: ['public MCP watchdog cron missing']. Cautions: []",
      "key_metrics": {
        "artifact_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.md",
        "profile_exit_code": 0,
        "repairs_attempted": 0,
        "runtime_issue_count": 1,
        "runtime_caution_count": 0,
        "structured_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.delivery.json",
        "receipt_path": "/root/echo_system/runtime/stage_outputs/2026-05-17/echohsu.receipt.json",
        "executor_status": "executed",
        "executor_success": true,
        "executor_blocked": false,
        "verified_handles_count": 1
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
      "last_updated": "2026-05-17T07:08:00.824809-07:00",
      "runtime_signals": {
        "gateway_restarts_total": 0,
        "autoloop_restarts_total": 1,
        "redaction_disabled_warnings": 0,
        "remote_protocol_errors": 0,
        "telegram_network_errors": 0,
        "recent_warning_lines": []
      },
      "health_penalties": [
        "sentinel reported 1 issue(s)",
        "healer reported 1 issue(s)",
        "evolver reported 1 issue(s)",
        "orchestrator reported 1 issue(s)",
        "docsync exit code 1",
        "docsync reported 1 issue(s)",
        "historian reported 1 issue(s)",
        "archivist reported 1 issue(s)",
        "content reported 1 issue(s)",
        "videoforge reported 1 issue(s)",
        "echohsu reported 1 issue(s)",
        "autoloop restart count 1"
      ]
    }
  }
}

---
# SystemPulse.md
_SHA256: af4def5424682a0121501061d301694d4b79172fe8250ecf9f74f099d1b87d48_

# Echo System Pulse

- Timestamp: 2026-05-17T07:08:00.824809-07:00
- Health score: 20
- Status: 🟠 Autonomous loop degraded

## Agents
- sentinel: 🟡 | last_scan=2026-05-17T03:21:12.956596-07:00 | issues=1 | cautions=0 | auto_fixes=0
- healer: 🟡 | last_scan=2026-05-17T03:40:04.839148-07:00 | issues=1 | cautions=0 | auto_fixes=0
- evolver: 🟡 | last_scan=2026-05-17T04:41:44.542432-07:00 | issues=1 | cautions=0 | auto_fixes=0
- orchestrator: 🟡 | last_scan=2026-05-17T05:17:17.835563-07:00 | issues=1 | cautions=0 | auto_fixes=0
- docsync: 🔴 | last_scan=2026-05-17T05:18:20.140486-07:00 | issues=1 | cautions=0 | auto_fixes=0
- historian: 🟡 | last_scan=2026-05-17T05:34:27.928599-07:00 | issues=1 | cautions=0 | auto_fixes=0
- archivist: 🟡 | last_scan=2026-05-17T05:45:23.094746-07:00 | issues=1 | cautions=0 | auto_fixes=0
- content: 🟡 | last_scan=2026-05-17T06:15:43.983381-07:00 | issues=1 | cautions=0 | auto_fixes=0
- videoforge: 🟡 | last_scan=2026-05-17T06:43:39.044648-07:00 | issues=1 | cautions=0 | auto_fixes=0
- echohsu: 🟡 | last_scan=2026-05-17T07:08:00.824809-07:00 | issues=1 | cautions=0 | auto_fixes=0

## Autonomous Loop
- Service: echo-autoloop.service
- Timezone: America/Los_Angeles
- Stages: sentinel, healer, evolver, orchestrator, docsync, historian, archivist, content, videoforge, echohsu
- Last updated: 2026-05-17T07:08:00.824809-07:00
- Gateway restarts: 0
- Autoloop restarts: 1
- Redaction warnings: 0
- Remote protocol errors: 0
- Telegram network warnings: 0

## Health Penalties
- sentinel reported 1 issue(s)
- healer reported 1 issue(s)
- evolver reported 1 issue(s)
- orchestrator reported 1 issue(s)
- docsync exit code 1
- docsync reported 1 issue(s)
- historian reported 1 issue(s)
- archivist reported 1 issue(s)
- content reported 1 issue(s)
- videoforge reported 1 issue(s)
- echohsu reported 1 issue(s)
- autoloop restart count 1

---
## Latest DocSync Receipt

```json
{
  "bundle_bytes": 239477,
  "bundle_path": "/root/echo_system/docs/exports/daily-sync/Echo_System_Canonical_Docs_Daily_Sync_2026-05-17.md",
  "bundle_scope": "canonical_docs_only",
  "bundle_sha256": "c9a88f4a2ee4e64456d44a1ad69986383ff5be0ba3e6387e68e6109eaccec2ca",
  "canonical_docs": [
    "Echo_System_Master_Index.md",
    "Echo_System_Vision_Architecture.md",
    "Echo_System_Agent_Prompts.md",
    "Echo_System_Knowledge_Core.md",
    "Echo_System_Runtime_and_Self_Management.md",
    "Echo_System_Operations_Guide.md"
  ],
  "date_key": "2026-05-17",
  "drive_file": {
    "id": "1481f9BZTHwyooGy7sj2um7_CnoaHTbUp",
    "mimeType": "text/markdown",
    "name": "Echo_System_Canonical_Docs_Daily_Sync_2026-05-17.md",
    "parents": [
      "0ABhqZwu84cYbUk9PVA"
    ],
    "size": "239477",
    "webViewLink": "https://drive.google.com/file/d/1481f9BZTHwyooGy7sj2um7_CnoaHTbUp/view?usp=drivesdk"
  },
  "drive_folder_id": "0ABhqZwu84cYbUk9PVA",
  "environment_oracle": {
    "canonical_docs_tracked": 6,
    "drift_count": 4,
    "drift_summary": "master_index: hash changed (last synced); agent_prompts: hash changed (last synced); knowledge_core: hash changed (last synced); operations_guide: hash changed (last synced)",
    "updated": true
  },
  "generated_at": "2026-05-17T07:15:24.319333-07:00",
  "source_count": 6,
  "source_manifest": [
    {
      "bytes": 15761,
      "path": "Echo_System_Master_Index.md",
      "sha256": "e0469fa81e8fce386406fc73956d4d58b6c3f85bfb75872ce0f47f6319744c0e"
    },
    {
      "bytes": 21735,
      "path": "Echo_System_Vision_Architecture.md",
      "sha256": "9acbf79433ed5f70e788deafef23eac579e34faa7f559132d835fd1138803d91"
    },
    {
      "bytes": 57161,
      "path": "Echo_System_Agent_Prompts.md",
      "sha256": "f26d7b28f44dce15ce68a89de1ca491174ee287bf05b00c060f709e4dfb6515e"
    },
    {
      "bytes": 45862,
      "path": "Echo_System_Knowledge_Core.md",
      "sha256": "7383c7a143154bceae9c499eda7a983e6101bf6f991eb16d0606318a316e085d"
    },
    {
      "bytes": 29047,
      "path": "Echo_System_Runtime_and_Self_Management.md",
      "sha256": "095524c9cab2ee9a4a03d0f691fe4b6edd50b600d6e516d825b072ad1508e8c9"
    },
    {
      "bytes": 69200,
      "path": "Echo_System_Operations_Guide.md",
      "sha256": "cb371eb26b2050f523eb9d297c34770fc54c474bbb8efe3eb391cd5c5599efa1"
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

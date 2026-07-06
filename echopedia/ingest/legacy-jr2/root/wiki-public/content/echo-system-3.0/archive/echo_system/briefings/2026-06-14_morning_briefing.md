**Echo Morning Briefing — 2026-06-14**

**System Health Score**  
20 (🟠 Autonomous loop degraded)

**Agent Status Table** (evidenced runs only)

Stage | Status | Last Scan | Issues | Cautions | Notes
---|---|---|---|---|---
sentinel | 🟡 | 2026-06-14 03:01 | 1 | 1 | Artifact present; API retry failure
healer | 🟡 | 2026-06-14 03:30 | 1 | 1 | Artifact present; empty model reply
evolver | 🟡 | 2026-06-14 04:30 | 1 | 1 | Artifact present; empty model reply
orchestrator | 🟡 | 2026-06-13 05:00 | 1 | 1 | Prior artifact only
docsync | 🔴 | 2026-06-13 05:15 | 1 | 1 | Exit 1, blocked
historian | 🟡 | 2026-06-13 05:15 | 1 | 1 | Blocked
archivist | 🟡 | 2026-06-13 05:30 | 1 | 1 | Blocked
content | 🟡 | 2026-06-13 06:01 | 1 | 1 | Blocked
videoforge | 🔴 | 2026-06-13 06:30 | 1 | 1 | Exit 1, blocked
echohsu | 🟡 | 2026-06-13 07:01 | 1 | 1 | Executed (1 handle)
audioforge | 🔴 | 2026-06-13 06:15 | 1 | 1 | Exit 1
voice | 🔴 | 2026-06-13 06:15 | 1 | 1 | Exit 1
vision | 🔴 | 2026-06-13 06:45 | 1 | 1 | Exit 1

**Key Risks**  
- kanban.db invalid SQLite (gateway dispatch paused, repeated errors)  
- hermes-gateway: 5 restarts, kanban dispatcher blocked  
- echo-autoloop degraded (prior crash loop evidence)  
- 10/13 profiles stopped  
- public MCP watchdog cron missing  
- disk 73%, memory pressure high  

**Auto-fixes**  
None recorded in current pulse or upstream artifacts.

**Next Actions**  
1. Restore/repair kanban.db and restart gateway.  
2. Investigate gateway kanban dispatcher failures.  
3. Verify autoloop service health.  
4. Address missing public MCP watchdog cron.  
5. Review stopped media profiles (audioforge, videoforge, voice, vision).

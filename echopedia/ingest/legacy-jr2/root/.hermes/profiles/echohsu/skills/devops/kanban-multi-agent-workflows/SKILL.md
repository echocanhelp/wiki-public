---
name: kanban-multi-agent-workflows
description: "Umbrella for Hermes Kanban orchestrator and worker lifecycle, decomposition, handoffs, and edge cases."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
environments: [kanban]
metadata:
  hermes:
    tags: [kanban, multi-agent, orchestration, worker, collaboration, hermes]
---

# Kanban Multi-Agent Workflows

Use this umbrella when operating inside or designing Hermes Kanban workflows: orchestrator decomposition, worker execution, handoffs, blocking, completion, and retry diagnostics.

## Roles

### Orchestrator

- Decompose work into independently completable tasks.
- Assign based on configured profiles; do not assume a fixed worker roster.
- Route work through the board instead of doing specialist implementation yourself when in orchestrator mode.
- Write acceptance criteria, workspace expectations, and dependencies clearly.

### Worker

- Orient from the task, workspace, linked tasks, and comments.
- Do the assigned work only; create follow-up tasks for out-of-scope discoveries.
- Heartbeat during long runs, block with actionable diagnostics when stuck, and complete only after verification.
- Leave a concise handoff: changed files/artifacts, tests run, blockers, and next steps.

## Shared lifecycle

1. Inspect task and workspace.
2. Identify dependencies and whether the task is ready.
3. Execute or decompose according to role.
4. Verify with real outputs.
5. Update the board: comment, block, create child tasks, or complete.

## Pitfalls

- Basic lifecycle guidance may be auto-injected by Hermes; load this skill for deeper examples and edge cases.
- Avoid duplicate work: check existing linked tasks before creating new ones.
- Do not mark complete based solely on intent or partial progress.
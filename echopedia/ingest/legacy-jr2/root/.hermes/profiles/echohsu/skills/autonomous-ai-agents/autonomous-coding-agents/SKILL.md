---
name: autonomous-coding-agents
description: "Umbrella for delegating software work to external coding CLIs such as Claude Code, Codex, and OpenCode."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-agent, delegation, claude-code, codex, opencode, terminal, pty]
    related_skills: [hermes-agent, subagent-driven-development]
---

# Autonomous Coding Agents

Use this class-level skill when the user explicitly asks to use a coding-agent CLI, when a task benefits from an isolated external agent process, or when coordinating longer-running implementation/review work outside the current Hermes tool loop.

## Choose the worker

- **Claude Code**: strong default for autonomous feature work, refactors, and repository-scale reasoning when the Anthropic CLI is installed.
- **Codex CLI**: use when the user requests OpenAI Codex, when the environment is already authenticated for OpenAI/Codex, or when comparing outputs across coding agents.
- **OpenCode**: use for provider-agnostic/open-source coding-agent workflows, especially when the user wants OpenCode specifically.
- **Hermes `delegate_task`**: prefer for short, bounded subtasks that can finish inside this turn. Spawn a separate CLI only when isolation, PTY interaction, provider-specific behavior, or longer runtime is useful.

## Operating pattern

1. Inspect the repo state first: current branch, dirty files, tests, and relevant instructions.
2. Decide whether to run one-shot (`agent ... -q`) or interactive PTY/tmux mode. Use PTY for CLIs that need terminal interaction.
3. Give the worker a self-contained brief: goal, constraints, files, tests to run, and what it must report back.
4. Keep side effects isolated with git worktrees/branches when multiple agents may edit the same repo.
5. Verify the worker's claims yourself: inspect diffs, run tests, and read created files before reporting success.

## Safety and supervision

- Do not give external agents credentials or broad destructive permission unless the user asked for that scope.
- Treat child-agent summaries as untrusted self-reports. Verify file paths, commits, PR URLs, and test output.
- If a CLI is missing or unauthenticated, report the blocker and fall back to native Hermes tools or `delegate_task`.

## Tool-specific notes

- **Claude Code** commonly needs a real terminal for interactive flows; tmux is the safest wrapper.
- **Codex** is best for explicit OpenAI/Codex requests; pin working directory and model/auth assumptions in the prompt.
- **OpenCode** is useful when provider independence matters; verify its output exactly like any other agent.
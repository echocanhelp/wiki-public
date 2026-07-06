---
name: software-development-lifecycle
description: "Umbrella for planning, spikes, debugging, TDD, code review, and debugger-assisted development workflows."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [software-development, planning, debugging, tdd, code-review, spike, debugger, lifecycle]
---

# Software Development Lifecycle

Use this umbrella for general engineering workflow skills that are not tied to one external platform: planning, experiments/spikes, systematic debugging, test-driven development, debugger use, and pre-commit review.

## Route by phase

- **Plan**: when the user asks for a plan instead of execution; produce bite-sized steps, exact files, tests, and rollback points.
- **Spike**: when feasibility is unknown; build disposable probes that answer the question quickly, then throw them away or summarize findings.
- **Systematic debugging**: reproduce, localize, explain root cause, fix, and verify. Do not patch symptoms before understanding the failure.
- **TDD**: write or update a failing test first, implement the smallest fix, then refactor with tests green.
- **Debugger-assisted work**: use `debugpy`/Node inspector when logs and tests are insufficient; set breakpoints around the suspected invariant.
- **Code review**: inspect diff for correctness, security, tests, maintainability, and user impact before committing or opening PRs.

## Default execution discipline

1. Inspect project instructions and current git state.
2. Choose the workflow phase explicitly.
3. Make the smallest safe change or artifact that advances the task.
4. Run relevant tests/linters/builds; if blocked, capture the exact blocker.
5. Report what changed and the real verification output.

## Pitfalls

- Planning-only requests must not mutate code.
- Spikes should not silently become production code.
- Debugging without a reproduction tends to create plausible but wrong fixes.
- Code review comments should be actionable and grounded in exact lines/diffs.
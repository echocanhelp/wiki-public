# Agent Graph — Echopedia / Hermes

> Auto-generated from plan: `~/.hermes/plans/2026-07-19_12-factor-agents-implementation.md`
> Last reviewed: 2026-07-19

## Org Graph (stable topology)

The org graph defines **who exists**, **what they own**, and **how they connect**. It is versioned and stable; only changes on redeploy.

```
┌─────────────────────────────────────────────────────────┐
│                    ORG GRAPH                            │
│                                                         │
│  ┌──────────┐    plan/review     ┌──────────┐          │
│  │  default │ ◄──────────────────│  pinto   │          │
│  │  profile │   ← approve ←      │  profile │          │
│  │  (frontier) │                │  (worker) │          │
│  │  Grok/   │   ← approve ←    │  NVFP4   │          │
│  │  NVFP4   │                │  NVFP4   │          │
│  └────┬─────┘                └────┬─────┘          │
│       │                           │                 │
│       │ delegate_task             │ hermes -p pinto │
│       │ (delegation.*→pinto)      │ chat -q <task>  │
│       ▼                           ▼                 │
│  ┌──────────────────────────────────────────┐      │
│  │         DETERMINISTIC NODES              │      │
│  │  no_agent cron jobs (bash/Python)        │      │
│  │  ci-heal · site-design · digest · janitor│      │
│  └──────────────────────────────────────────┘      │
│       │                                             │
│       │ deliver                                     │
│       ▼                                             │
│  ┌──────────────────────────────────────────┐      │
│  │  Telegram home (6769573480)               │      │
│  │  ← human checkpoint / review gate         │      │
│  └──────────────────────────────────────────┘      │
│                                                   │
│  Kanban board (t_*) — dynamic work graph          │
│  Git repo (echo-system) — shared artifact store   │
└─────────────────────────────────────────────────┘
```

### Nodes

| Node | Profile | Model | Role | Mandate |
|------|---------|-------|------|---------|
| `default` | default | Grok → NVFP4 (sticky) | Planner / frontier ops | Architecture design, user-facing chat, admin tasks |
| `pinto` | pinto | NVFP4 only | Worker | Kanban execution, bounded template work, depth passes |
| `ci-heal` | `no_agent` | N/A (bash) | L0/L1 ops | Nightly site audit, drain, drift, publish |
| `site-design` | `no_agent` | N/A (bash) | L1 heal | Post-deploy site design audit |
| `digest` | `no_agent` | N/A (bash) | L0 report | Daily digest generation |
| `janitor` | `no_agent` | N/A (bash) | L0 cleanup | Nightly disk cleanup |
| Telegram home | delivery target | N/A | Human checkpoint | User review, approval gates, feedback |

### Edges

| Edge | Direction | Trigger | Failure route |
|------|-----------|---------|---------------|
| default → pinto | Planner → Worker | `hermes kanban assign <task> pinto` | Card stays blocked if default is Grok |
| pinto → Git | Worker → Artifact store | `git add/commit/push` in task workspace | Fail → blocked kanban card |
| pinto → Telegram | Worker → Human | `deliver` on cron or kanban result | Silent if delivery fails |
| `no_agent` → Telegram | Script → Human | Cron deliver field | Silent |
| Telegram → default | Human → Planner | User reply in chat | N/A |
| Kanban → pinto | Board → Worker | `hermes kanban assign <task> pinto` | Card stays ready/blocked |

---

## Work Graphs (dynamic — what's running now)

### Nightly pipeline (primary)

```
04:00 ──► janitor (disk cleanup, no_agent)
         │
         ▼ (04:15)
04:15 ──► ci-heal (site audit, drain, drift, publish, smoke, L3 push)
         │
         ▼ (04:30)
04:30 ──► site-design audit-only (no deploy, verify post-push)
         │
         ▼ (09:00)
09:00 ──► digest (daily report)
```

Each step: input artifacts in `echo-system/`, output in `echo-system/`, delivery to `telegram:6769573480`.

### Publication depth pass (epic: t_6e7cccd4)

```
K0 (pinto profile) ──► G1 (AGENT_GRAPH.md)
                         │
                         ▼
                       F5 (metadata) ──► F12 (stateless bodies)
                         │
                         ▼
                       F9 (error compact)
                         │
                         ▼
                       G2 (path-cost, deferred)
```

### Kanban work graph (example: TAHS 2017 depth)

```
T0 facts-clean ──► T1 missing pages ──► T2 deepen batches (P0, P1)
                                            │
                                            ▼
                                         T3 hub links
                                            │
                                            ▼
                                         T4 matrix + commit
```

Each kanban card is a **work node** with:
- Input: plan file path, source file paths, context files
- Owner: `pinto` assignee
- Output: changed files in `echo-system/`
- Failure: blocked card with error in result

---

## Design principles

1. **Deterministic nodes first:** L0/L1 bulk work goes through `no_agent` bash/Python scripts. LLM only at judgment edges (T2 deepen, architecture review).
2. **Human checkpoint at delivery:** All cron/kanban output delivers to Telegram home. User reviews before approve.
3. **Git as artifact store:** All work nodes produce git-tracked artifacts. Kanban result = git diff summary.
4. **Org graph stable, work graph ephemeral:** Profiles and cron jobs are stable. Kanban cards and cron ticks are ephemeral.
5. **Bounded graphs:** Every edge has a known input/output shape. Amcalar's principle: bounded graphs → benchmarkable path cost.

---

## Model routing rules

| Context | Model |
|---------|-------|
| `default` profile chat | Grok → NVFP4 (sticky) |
| `pinto` profile chat | NVFP4 only |
| `delegate_task` | `delegation.provider/model` → pinto NVFP4 |
| `hermes kanban assign <task> pinto` | NVFP4 only |
| `no_agent` cron jobs | N/A (deterministic) |
| Vision analysis | Grok (auto, via auxiliary.vision) |

---

## Open / future

- **G2 path-cost tagging:** Add `path_id` + step duration to nightly cron output; surface in digest.
- **More deterministic nodes:** Identify L2/L3 tasks that could be scripted (currently all go through LLM).
- **Dynamic work graph mutation:** Kanban parent-child spawning is already a form of dynamic graph mutation (see factor 10: small focused agents).

---

*This document is part of the agent graph. Update it when topology changes.*
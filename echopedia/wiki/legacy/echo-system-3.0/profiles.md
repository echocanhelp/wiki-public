---
title: "Echo System 3.0 — Active Profiles"
type: reference
tags:
  - echo-system
  - profiles
  - architecture
---

# Echo System 3.0 — Active Profiles

**Version**: 1.1  
**Last Updated**: 2026-06-23

## Purpose

This document defines the **intended and current active profiles** in Echo System 3.0 after cleanup.

## Core Active Profiles

| Profile | Primary Role | Status |
|---------|--------------|--------|
| **echohsu** | Main system interface & coordination | Active (primary) |
| **historian** | Historical research & Echopedia governance | Active |
| **archivist** | Long-term preservation & documentation standards | Active |
| **content** | Written content generation | Active |
| **videoforge** | Video content production | Active |
| **orchestrator** | Workflow coordination & subagent management | Active |
| **echonomics** | Isolated operations | Active (intentionally isolated) |

## Archived Profiles

The following profiles have been archived as they did not align with current design intent or showed minimal differentiation:

- `audioforge`
- `evolver`
- `healer`
- `profiler`
- `sentinel`
- `vision`
- `voice`
- `echohsu-staging`

**Archive Location**: `/root/.hermes/profiles/.archive/`

## Design Principles

- Each active profile must have a **clear, distinct purpose**.
- **echonomics** remains fully isolated from GBrain and cross-profile federation.
- Profiles should support the **5-layer architecture**.
- Unused or redundant profiles are archived to maintain clarity.

## Related Documents

- [[echo-system-3.0/index|Echo System 3.0 Overview]]
- [[echo-system-3.0/architecture|Architecture]]
- [[cross-profile-memory-federation|Cross-Profile Memory Federation]]

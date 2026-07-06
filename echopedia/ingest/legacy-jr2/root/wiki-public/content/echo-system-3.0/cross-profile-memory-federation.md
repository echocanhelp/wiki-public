---
title: "Cross-Profile Memory Federation"
type: concept
tags:
  - gbrain
  - federation
  - architecture
---

# Cross-Profile Memory Federation

**Status**: Design Phase  
**Version**: 0.1  
**Last Updated**: 2026-06-23

## Goal

Enable GBrain to selectively share knowledge across Hermes profiles while maintaining strong isolation (especially for `echonomics`).

## Principles

- **Default Isolation**: Each profile only sees its own data unless explicitly shared.
- **Explicit Federation**: Sharing must be deliberately configured.
- **echonomics Exclusion**: This profile remains completely isolated from GBrain federation.
- **Auditability**: All cross-profile access should be logged.

## Proposed Model

### 1. Profile Scopes
- Each profile has its own **scope** in GBrain.
- Default behavior: A profile can only access its own scope.

### 2. Federation Rules
- Federation is defined per scope or per page type.
- Example rules:
  - `echohsu` can read from `historian` scope on `type:person` pages.
  - `archivist` can write to a shared `public` scope.

### 3. Implementation Options

| Option | Description | Complexity |
|--------|-------------|------------|
| **A** | GBrain scopes with access control lists | Medium |
| **B** | Separate GBrain instances per profile + sync layer | High |
| **C** | Tag-based access control on individual pages | Medium |

## Recommended Starting Point

Start with **Option A** (scoped access) using GBrain’s existing source/page model:
- Define profile-specific sources
- Use GBrain’s permission system (when available) or wrapper scripts

## Next Steps

1. Define scope naming convention
2. Identify which profiles need federation
3. Pilot with 2–3 profiles (excluding `echonomics`)
4. Build simple access rules and logging

## Related Documents

- [[echo-system-3.0/index|Echo System 3.0 Overview]]
- [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]

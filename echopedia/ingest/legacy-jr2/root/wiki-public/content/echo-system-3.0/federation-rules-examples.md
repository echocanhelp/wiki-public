---
title: "GBrain Federation Rules Examples"
type: reference
tags:
  - gbrain
  - federation
  - rules
---

# GBrain Federation Rules Examples

**Version**: 0.1  
**Last Updated**: 2026-06-23

## Purpose

Provide concrete examples of how cross-profile memory federation can be configured.

## Assumptions

- Each profile has its own GBrain scope (e.g., `profile-echohsu`)
- `echonomics` is completely excluded from all federation
- Federation is read-only by default

## Example Rules

### 1. echohsu ↔ historian

- `profile-echohsu` can **read** `type:person` pages from `profile-historian`
- `profile-historian` can **read** `type:person` pages from `profile-echohsu`
- No write access in either direction

### 2. echohsu ↔ archivist

- `profile-echohsu` can **read** `type:person` and `type:ingestion-wave` from `profile-archivist`
- `profile-archivist` can **read** `type:person` from `profile-echohsu`

### 3. content ↔ videoforge

- `profile-content` and `profile-videoforge` can share `type:content` and `type:video` pages
- Both can **read** from a shared `shared-public` scope

### 4. No Federation

- `profile-echonomics` has **no** federation rules with any profile
- `profile-sentinel` has no federation (monitoring only)

## Implementation Notes

- Rules can be stored in a central config file
- Enforcement can be done via wrapper scripts around GBrain queries
- Start simple (read-only between 2–3 profiles) before expanding

## Related Documents

- [[federation-scope-standard|GBrain Federation Scope Standard]]
- [[cross-profile-memory-federation|Cross-Profile Memory Federation]]

---
title: "GBrain Federation Scope Standard"
type: standard
tags:
  - gbrain
  - federation
  - standard
---

# GBrain Federation Scope Standard

**Version**: 0.1  
**Last Updated**: 2026-06-23

## Purpose

Define a consistent naming convention for GBrain scopes used in cross-profile memory federation.

## Scope Naming Convention

Format: `profile-<profile-name>`

### Examples
- `profile-echohsu`
- `profile-historian`
- `profile-archivist`
- `profile-content`

## Special Scopes

| Scope | Purpose | Access |
|-------|---------|--------|
| `profile-echonomics` | Fully isolated | No federation |
| `shared-public` | Public or semi-public content | Controlled access |
| `shared-identity` | Verified identity data | Limited federation |

## Rules

- Every profile gets its own scope by default.
- Federation between scopes must be explicitly configured.
- `echonomics` scope is never included in any federation.
- All cross-scope access should be logged where possible.

## Implementation Notes

- Use GBrain source configuration to define scopes.
- Access control can be enforced via wrapper scripts or future GBrain permission features.
- Start with read-only federation between trusted profiles.

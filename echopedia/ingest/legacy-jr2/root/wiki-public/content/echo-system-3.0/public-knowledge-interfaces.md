---
title: "Public Knowledge Interfaces"
type: concept
tags:
  - public
  - interface
  - echopedia
  - gbrain
---

# Public Knowledge Interfaces

**Status**: Design Phase  
**Version**: 0.1  
**Last Updated**: 2026-06-23

## Goal

Define controlled public access to Echopedia and GBrain content while protecting sensitive or unverified information.

## Principles

- **Default Private**: Nothing is public unless explicitly marked.
- **Granular Control**: Public access should be configurable at page or scope level.
- **Provenance**: Public views must clearly indicate source and verification status.
- **echonomics Isolation**: This profile remains fully private.

## Proposed Tiers

| Tier | Access | Examples | Control |
|------|--------|----------|---------|
| **Internal** | Full access | All GBrain + Echopedia | Default |
| **Contributor** | Read + limited write | Verified person pages, ingestion status | Role-based |
| **Public** | Read-only selected content | Published articles, verified biographies | Explicit marking |

## Recommended Starting Point

Begin with a small public view containing:
- Selected high-quality Echopedia person pages
- Basic topic overviews
- Clear disclaimers and source links

## Technical Considerations

- Use GBrain scopes or tags to mark public content
- Simple static site or read-only API for public access
- Rate limiting and caching for public endpoints

## Related Documents

- [[echo-system-3.0/index|Echo System 3.0 Overview]]
- [[cross-profile-memory-federation|Cross-Profile Memory Federation]]
- [[gbrain-echopedia-integration-protocol|GBrain ↔ Echopedia Integration Protocol]]

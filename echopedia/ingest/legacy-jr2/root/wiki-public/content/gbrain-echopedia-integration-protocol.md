---
title: "GBrain ↔ Echopedia Integration Protocol"
type: concept
tags:
  - echopedia
  - gbrain
  - integration
  - operations
  - taiwanese-american
---

# GBrain ↔ Echopedia Integration Protocol

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-06-23  
**Owner**: Echo System / TAHS

## 1. Purpose

This protocol defines how **GBrain** (the active memory and synthesis layer) interacts with **Echopedia** (the canonical historical record) to maintain accuracy, provenance, identity integrity, and scalability.

## 2. Core Principles

1. **Echopedia is canonical** — Human-curated historical truth.
2. **GBrain is the active layer** — Queryable memory, entity resolution, and synthesis.
3. **One person = one canonical page** (in both systems).
4. **Provenance must be preserved** at every step.
5. **Automation is preferred**, but human oversight remains on identity and governance decisions.

## 3. Identity Management

### 3.1 Canonical Person Pages
- Every verified person must have exactly one `type: person` page in both Echopedia and GBrain.
- GBrain person pages should include:
  - English + Chinese + romanized names
  - Structured facts (including LINE user IDs)
  - Verification state and confidence
  - Links to Echopedia page

### 3.2 LINE ↔ Echopedia Linking
- LINE user IDs are stored as facts on GBrain person pages.
- The LINE ↔ Echopedia Identity Linking Decision Tree remains the authoritative human workflow.
- GBrain supports this by surfacing existing links during chat.

### 3.3 Collision Detection
- GBrain runs periodic queries to detect potential duplicate or colliding person records.
- Suspected collisions are flagged for human review before canonicalization.

## 4. Ingestion Workflow

| Stage | Echopedia Action | GBrain Action | Automation |
|-------|------------------|---------------|------------|
| Pre-ingestion | Source review | — | Manual |
| Import | Add to wiki | gbrain import --no-embed | Semi |
| Embedding | — | gbrain embed --stale | Yes |
| Post-ingestion governance | Duplication & canonical checks | Run collision detection queries | Partial |
| Person depth upgrade | Testimony & context enrichment | Extract facts & timeline | Partial |

## 5. Automation Points

- **GBrain MCP Server** — Runs as systemd service (persistent).
- **Retrieval-Reflex Skill** — Enables automatic entity detection and page injection during natural chat.
- **Daily Health Monitoring** — Cron job runs gbrain doctor.
- **New Profile Onboarding** — Use enable-gbrain.sh <profile>.
- **Embedding Pipeline** — Conservative settings for free-tier Voyage usage.

## 6. Governance & Audit

- All major ingestion waves should be tracked as GBrain "wave" pages.
- Periodic audits should verify:
  - One canonical person page per individual
  - No broken identity links
  - Testimony and source provenance preserved

## 7. Feedback Loop

When new verified information is discovered in GBrain:
1. Agent proposes update.
2. Human reviewer validates.
3. Echopedia page is updated (if appropriate).
4. GBrain page is enriched with new facts.

## 8. Exclusions

- The echonomics profile is intentionally excluded from GBrain.
- No GBrain MCP or skills are configured for it.

## 9. Related Documents

- Echopedia Person Recordation Framework
- Echopedia Post-Ingestion Governance and Person-Depth Standard
- LINE ↔ Echopedia Identity Linking Decision Tree
- Echopedia Person Identity Collision and Canonicalization Procedure

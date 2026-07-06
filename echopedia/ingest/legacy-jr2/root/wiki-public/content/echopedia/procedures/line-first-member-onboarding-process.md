---
title: "LINE-First Member Onboarding Process"
type: process
tags:
  - onboarding
  - line
  - echopedia
  - process
---

# LINE-First Member Onboarding Process

**Status**: Active  
**Version**: 1.0  
**Last Updated**: 2026-06-23

## Purpose

Define a consistent, efficient process for onboarding new members via LINE while maintaining strong identity governance and Echopedia integration.

## Trigger

A new person appears in a LINE group or direct message.

## Process Steps

### 1. Initial Signal Collection
- Capture LINE user ID and display name
- Note the group(s) they appear in
- Record timestamp

### 2. Identity Verification
- Check against existing `identity_links.json` or GBrain person pages
- Use the LINE ↔ Echopedia Identity Linking Decision Tree
- Determine if this is a new or returning person

### 3. Identity Linking / Creation
- If existing: Link LINE ID to canonical Echopedia person page
- If new: Create minimal Echopedia person page (or mark for later enrichment)
- Create/update corresponding GBrain person page with LINE data

### 4. Onboarding Communication
- Send welcome message via LINE
- Provide relevant Echopedia links or resources
- Explain data handling and consent (per existing consent rules)

### 5. Record & Sync
- Update `identity_links.json` (or GBrain equivalent)
- Log onboarding event
- Trigger any relevant automations (e.g., add to relevant groups or lists)

## Automation Opportunities

| Step | Automation | Feasibility |
|------|------------|-------------|
| Signal Collection | LINE webhook / bot | Medium |
| Identity Check | GBrain query | High |
| Person Page Creation | Template + script | Medium |
| Welcome Message | LINE bot | High |
| Logging | GBrain page or audit log | High |

## Related Documents

- [[line-echopedia-identity-linking-decision-tree|LINE ↔ Echopedia Identity Linking Decision Tree]]
- [[gbrain-to-echopedia-feedback-loop|GBrain → Echopedia Feedback Loop]]
- [[echopedia-ingestion-wave-closure-process|Echopedia Ingestion Wave Closure Process]]
- LINE Identity Storage Standard (GBrain)
# EchoHsu Phase 1 Updates & Implementation Guide

**Date:** 2026-05-16
**Version:** 1.2
**Purpose:** Complete package of updates for EchoHsu behavior, Operations Guide, Instant Hide feature, Archivist protocols, and instructions for updating canonical documents.

---

## 1. Overview

This document contains all changes needed to improve EchoHsu on LINE (especially in groups), add privacy and task discipline, implement the Instant Hide feature, and update related protocols.

**Contents:**
- Condensed EchoHsu Prompt
- New Operations Guide sections
- Instant Hide Implementation (Phase 1)
- Updated Archivist Verification Protocols
- New Publication Gate Design
- How to update canonical documents
- Delivery instructions

---

## 2. Condensed EchoHsu Prompt

Replace the current EchoHsu section in `Echo_System_Agent_Prompts.md` with this:

```markdown
## 12. EchoHsu — Public Community Interface

**Core Identity**
You are **Echo**, the discreet and culturally-aware public-facing agent of the Echo System for the Taiwanese American Historical Society. You serve as a trusted assistant to Leonard and the community.

**Non-Negotiable Guardrails**
- Be silent by default. Only respond when directly addressed.
- Never send internal thoughts or reasoning to users.
- Treat all personal data as private by default.
- In group chats: silent observer mode unless directly addressed.
- Record entities silently and create tasks via Orchestrator when valuable.
- Never reveal what you know or what tasks you've created.
- Do not assume identity or auto-link unknowns.

**LINE-Specific Rules**
- Prioritize user-initiated messages due to quota costs.
- Only send high-value updates if previously requested.

**Group Chat Rules**
- Default to silent observer mode.
- Silently record context from unknown participants.
- Route all corrections and identity suggestions through Orchestrator.

**Self-Reference**
- Refer to yourself as **Echo**.
```

---

## 3. New Sections for Operations Guide

Add these sections to `Echo_System_Operations_Guide.md`:

### LINE Group Chat Procedures
### Identity Linking Process (LINE ID ↔ Private Wiki)
### Public Contribution & Redaction Workflow (Phase 1)
### Privacy Guardrails for Public Settings
### Task Metadata Standards & Orchestrator Routing Rules for EchoHsu

*(Use the detailed versions we prepared earlier for each of these sections.)*

---

## 4. Instant Hide Implementation (Phase 1)

### Webhook Payload
### Website Code (with Error Handling)
### Task Structure for `redaction_request`

*(Include the payload format, JavaScript code with error handling, and task metadata we defined.)*

---

## 5. Updated Archivist Verification Protocols

Archivist's role is shifting from publisher + rapid corrector + key updates.

**Key Updates:**
- Create basic entities more quickly when context exists.
- Use "Potential Match" records for group chat identity suggestions.
- Apply minor corrections faster; route major ones to Historian.
- Support the Instant Hide flow.
- Use clear labels on the public wiki (`Community Sourced`, `Unverified`).

---

## 6. New Publication Gate Model

**Model:** Publish by Default + Fast Correction

- Publish basic, low-risk content quickly.
- Use visible labels for transparency.
- Rely on Instant Hide + task system for fast correction.
- Keep stricter review for sensitive or historically important content.

This model is reflected in the updated Archivist protocols.

---

## 7. How to Update Canonical Documents

### Echo_System_Agent_Prompts.md
- Replace the EchoHsu section with the new condensed prompt.
- Update the revision history.

### Echo_System_Operations_Guide.md
- Add the new sections listed in Part 3.
- Update the revision history.

### Echo_System_Knowledge_Core.md
- Update Archivist responsibilities and Publication Gate section to reflect the new model.

### Echo_System_Master_Index.md
- Bump version to 1.3.0.
- Add a Change Log entry.

After editing:
- Create Orchestrator tasks for Archivist.
- Run DocSync.

---

## 8. Delivery Instructions

Recommended Steps:

1. Optional: Test the condensed prompt in the echohsu profile first.
2. Send this file to the orchestrator profile.
3. Ask orchestrator to create Orchestrator tasks for all changes.
4. Update the canonical documents as described in Section 7.
5. Run DocSync after updates.

Suggested Orchestrator Tasks to Create:
- Update EchoHsu prompt
- Add new Operations Guide sections
- Implement Phase 1 Instant Hide
- Update Archivist protocols and publication gates
- Update Master Index

---

## 9. Change Log Entry

## Change Log

- **1.3.0** (2026-05-16) — EchoHsu Phase 1 Updates:
  - Condensed EchoHsu prompt with stronger LINE and group discipline.
  - Added multiple new sections to Operations Guide.
  - Implemented Phase 1 Instant Hide feature.
  - Updated Archivist verification protocols and introduced "Publish by Default + Fast Correction" model.
  - Added instructions for updating canonical documents.

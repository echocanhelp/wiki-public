---
title: "LINE Identity Storage Standard"
type: standard
tags:
  - gbrain
  - identity
  - line
---

# LINE Identity Storage Standard (GBrain)

**Purpose**: Ensure consistent storage of LINE user and group information on GBrain person pages.

## Recommended Structure

Add the following section to GBrain person pages:

```markdown
## LINE Identity
- **User IDs**: [list]
- **Groups Seen**: [list]
- **Last Seen**: [date]
```

## Example

```markdown
## LINE Identity
- **User IDs**: ["U0b1b4329eb17c7ec32c0f3c469eff01f"]
- **Groups Seen**: ["C12d20c0b0ddbf3d2f767e3d4a7799dde"]
- **Last Seen**: 2026-05-25
```

## Notes
- Only store LINE IDs when consent for profile linking has been granted.
- Keep this section updated when new LINE activity is observed.
- This data supports the LINE ↔ Echopedia Identity Linking process.
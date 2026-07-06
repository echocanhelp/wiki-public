---
name: apple-ecosystem-automation
description: "Class-level workflows for Apple/macOS automation: Notes, Reminders, iMessage, Find My, and computer-use tasks."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [apple, macos, automation, notes, reminders, imessage, findmy, computer-use]
---

# Apple Ecosystem Automation

Use this umbrella when a task involves Apple's local apps or macOS UI automation: Notes, Reminders, Messages/iMessage, Find My, Finder/System Settings, Shortcuts, or general computer-use on macOS.

## Routing

- **Notes**: search, read, create, append, or organize notes. Prefer app-supported APIs/AppleScript/Shortcuts when available; fall back to UI automation only when the app has no reliable scripting surface.
- **Reminders**: create/update reminders and lists; preserve due dates, recurrence, priority, and list names explicitly.
- **Messages/iMessage**: treat sends as side effects. Resolve recipient identity carefully before sending, and avoid exposing private message content unnecessarily.
- **Find My**: location/status lookups are privacy-sensitive. Report uncertainty and timestamps; do not infer real-time location beyond the data returned.
- **macOS computer use**: for GUI workflows, first identify the app/window state, then use the smallest number of UI actions, and verify the visible result.

## General procedure

1. Resolve the concrete app/data target and the safest available automation interface.
2. For read-only tasks, gather only the minimum needed context.
3. For writes/sends/deletes, summarize the intended side effect and get confirmation unless the user has already made the target and content unambiguous.
4. Execute using AppleScript, Shortcuts, CLI helpers, or computer-use tools as appropriate.
5. Verify by reading back the created/changed object or checking UI state.

## Pitfalls

- App databases and sync state may lag iCloud. Include timestamps when reporting synced data.
- Contact-name ambiguity is common; resolve to an exact handle before sending messages or reminders to shared lists.
- GUI automation is brittle. Prefer semantic APIs over coordinate clicks whenever possible.
- Do not assume the Hermes runtime host is the user's Mac; check live tool availability before using macOS-specific commands.
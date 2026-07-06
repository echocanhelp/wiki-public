---
name: productivity-document-workflows
description: "Umbrella for workspace apps and documents: Google Workspace, Office/PowerPoint, PDFs/OCR, Notion, Airtable, maps, and meeting pipelines."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [productivity, documents, google-workspace, powerpoint, pdf, ocr, notion, airtable, maps, meetings]
---

# Productivity & Document Workflows

Use this umbrella for office/productivity tasks: email/calendar/drive/docs/sheets, presentations, PDFs/OCR, Notion, Airtable, maps/location lookups, and meeting-summary operations.

## Route by target

- **Google Workspace**: Gmail, Calendar, Drive, Docs, Sheets, Contacts; check OAuth token/client-secret prerequisites and use least-privilege reads.
- **Presentations**: `.pptx` read/edit/create/export; preserve layouts, notes, media, and template structure.
- **PDFs and OCR**: extract text from digital PDFs first; use OCR/marker tools for scans; use editing tools only for explicit PDF modification requests.
- **Notion/Airtable**: API/database CRUD; inspect schemas before creating/updating records.
- **Maps/location**: geocode, route, POIs, distance/timezone; cite sources and avoid over-precision.
- **Meetings**: Teams/Graph pipelines; inspect status/replay jobs/subscriptions before changing automation.
- **Notes / Obsidian**: vault search, note creation, linking, and markdown maintenance belong in the document-workflow class when the user asks for knowledge capture or note editing.

## General procedure

1. Identify the external system, credentials, object ID/path, and side-effect level.
2. For databases/docs, inspect schema/structure before writing.
3. For generated documents, create a real file and verify it opens/parses.
4. For sends, invites, updates, and deletes, confirm recipient/object/content unless already unambiguous.
5. Return durable handles: file path, URL, record ID, event ID, or command output.

## Pitfalls

- OAuth tokens and API keys are per-profile/environment; check live availability.
- Office and PDF files are structured packages, not plain text. Use dedicated parsers/editors.
- External app APIs may paginate; fetch enough pages before claiming absence.

## Consolidated app/tool subworkflows

### Google Workspace and email
- Google Workspace covers Gmail, Calendar, Drive, Docs, Sheets, Contacts, OAuth setup, profile-scoped credentials, and read-back verification after writes.
- Himalaya-style IMAP/SMTP email workflows belong here when the task is generic mail search/read/send rather than Google-specific. Confirm account/profile and draft before sending.

### Presentations and Office packages
- Treat `.pptx` as a zipped XML package. Preserve layouts, slide masters, media, notes, and relationships; verify by opening/parsing the generated deck or inspecting package contents.
- Create real deck files and report absolute paths; do not stop at an outline unless the user only asked for an outline.

### PDFs, OCR, and document extraction
- Prefer native text extraction for digital PDFs; use OCR/marker-style pipelines for scanned or layout-heavy documents.
- For cloud preview links (Drive/OneDrive/etc.), download or use API access when previews truncate content; cite extraction limits.

### Notion and structured workspaces
- Inspect database/page schemas before writes. Preserve block hierarchy and property types; return page/database IDs and URLs after changes.

### Maps and location work
- Use geocoding/routing/POI/timezone lookups with provenance and timestamps. Avoid false precision; distinguish straight-line distance, route distance, and travel time.

### Generic productivity rule
- Every external side effect needs a durable handle plus read-back verification when the API makes it possible.
# Echopedia Public Filtering UI Specification
# Section 8 of Echopedia System Redesign Execution Plan v2.0

## Purpose

Allow public users of Echopedia to filter content by Source Type and Verification Level
for quick identification and rollback of false-positive contributions.

This gives the community transparency into where information comes from and how well it
is verified — a core principle of the "Public First + Fast Correction" philosophy.

---

## 1. Filterable Fields

### 1.1 Source Type (Required)

```
Filter name:  "Source"
Field:        source_type
Type:         Multi-select checkbox group
Options:
  [ ] Book / Published Reference
  [ ] User Interview
  [ ] EchoFeelings (Synthesized Memory)
  [ ] Community Record
Default:      All selected (no filtering)
```

Each source type should display a tooltip on hover/click:

| Source Type | Tooltip |
|---|---|
| Book | "Published book, academic paper, or printed reference material" |
| User Interview | "Direct conversation recorded from a community member (LINE, SMS, in-person)" |
| EchoFeelings | "Emotional/narrative memory synthesized by AI from community interactions" |
| Community Record | "Official document, archive entry, or organizational record" |

### 1.2 Verification Level (Required)

```
Filter name:  "Verification"
Field:        verification_level
Type:         Range slider or star selector
Scale:        1-5 stars (★)
Default:      ≥ 2 stars (hides AI-speculative content)
Options:
  ★☆☆☆☆ — AI-Generated / Speculative
  ★★☆☆☆ — Plausible Inference
  ★★★☆☆ — Community Consensus
  ★★★★☆ — Multi-Source Corroborated
  ★★★★★ — Primary Source
```

The filter should be a minimum threshold — selecting 3 stars shows levels 3, 4, and 5.

### 1.3 Implicit Filter (Always Applied)

```
public_eligibility: approved
```

Content with `rejected`, `pending_review`, or `revision_requested` is NEVER shown
in public filtering results, regardless of user filter selections.

---

## 2. Sort Options

```
Sort by:
  [Most Recent ▼]
  [Verification (High → Low)]
  [Verification (Low → High)]
  [Contributor (A → Z)]
```

Default sort: Most Recent (created_at descending).

---

## 3. Display Format (Per Content Item)

Each search result / content card shows:

```
┌──────────────────────────────────────────────────────┐
│  [Title]                                             │
│                                                       │
│  [Source badge] [Verification stars] [Contributor]     │
│  Book              ★★★★        lin-meiling           │
│                                                       │
│  [Snippet / first 2 lines of content]                │
│                                                       │
│  Created: 2026-05-20  |  Reviewed: 2026-05-21        │
│  [Source reference link]                              │
└──────────────────────────────────────────────────────┘
```

### Badges:

| Source Type | Badge Style |
|---|---|
| Book | 📗 Blue |
| User Interview | 🎙 Green |
| EchoFeelings | 💜 Purple |
| Community Record | 📋 Gray |

### Verification Stars:
- Level 5: ★★★★★ (green)
- Level 4: ★★★★☆ (blue)
- Level 3: ★★★☆☆ (yellow)
- Level 2: ★★☆☆☆ (orange)
- Level 1: ★☆☆☆☆ (red) — hidden from public by default

---

## 4. Active Filter Display

When filters are applied, show a filter bar at top of results:

```
Active filters: [Source: User Interview ×] [Verification: ≥3★ ×]  Clear all
```

Each active filter chip has an × to remove it. "Clear all" resets to defaults.

---

## 5. Empty State

When no results match the filters:

```
No content matches your current filters.
[Clear all filters] or try broadening your search.
```

---

## 6. False-Positive Rollback

For moderators and Archivist:

1. Filter by any Source Type + Verification Level combination
2. Each card has a "Flag" button (visible to authenticated users)
3. Flagged items get `public_eligibility: pending_review` immediately
4. Archivist reviews flags in next editorial cycle
5. If false-positive confirmed: item set to `rejected` with `rejection_reasons` recorded

This is the "Fast Correction" part of "Public First + Fast Correction".

---

## 7. Implementation Notes

### Frontend (Markdown / Wiki Rendering)

For a static Markdown-based wiki (like GitHub Wiki or Google Drive):

- Use YAML frontmatter on every page (see `echopedia-content-template.md`)
- A filtering index page can parse frontmatter and render filtered results
- Tags/labels can serve as fallback if full frontmatter parsing isn't available

### API (JSON endpoint)

If a JSON API serves content:

```json
GET /echopedia/api/content?source_type=user_interview&min_verification=3&sort=created_at_desc

{
  "results": [...],
  "total": 42,
  "filters_applied": {
    "source_type": ["user_interview"],
    "min_verification": 3
  }
}
```

### Discord / Telegram Integration

For messaging platform users:

- Command: `/filter source:user_interview verification:3`
- Returns filtered list as inline buttons or message cards

---

## 8. YAML Frontmatter Template

Every Echopedia content page starts with this frontmatter:

```yaml
---
title: "Content Title"
source_tracking:
  source_type: "book"                    # book | user_interview | EchoFeelings | community_record
  source_reference: "Hsu, L. (2024)..."  # citation / link / identifier
  contributor: "lin-meiling"              # who contributed
  verification_level: 4                   # 1-5
  public_eligibility: "approved"          # approved | rejected | pending_review | revision_requested
extended:
  rejection_reasons: []
  archivist_reviewed_at: "2026-05-21T00:00:00Z"
  historian_verified: false
  labels_applied: []
  aggregation_group: null
  created_at: "2026-05-20T00:00:00Z"
  updated_at: "2026-05-21T00:00:00Z"
---
```

See `echopedia-content-template.md` for the full template.

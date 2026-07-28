---
title: "taiwanjustice.net — Privacy Gate Scan Report"
domain: taiwanjustice.net
archive_path: knowledge/web-archives/taiwanjustice-net/
tier2_dir: knowledge/web-archives/taiwanjustice-net/tier2/
scan_date: 2026-07-28
confidence: A
---
# taiwanjustice.net — Privacy Gate Scan Report

## Overview

A systematic privacy gate scan was conducted on all **29,103** Tier 2 markdown files (81,844,451 characters) from the taiwanjustice.net Wayback Machine archive. The scan checked for parking pages, PII (email addresses, phone numbers), empty/near-empty bodies, sensitive content flags, and comment retention.

## Scan Results

| Check | Result |
|-------|--------|
| Parking pages (Hostinger domain parking) | 0 (5 false positives: "parking lot" references in event titles) |
| PII (email addresses) | 1 file with email (DPPUSWEST@GMAIL.COM) |
| PII (phone numbers) | 96 files with phone numbers (mostly Taiwan Center contact info, event hotlines) |
| Empty/near-empty bodies | 0 |
| Sensitive content flags | None — all content is news/opinion aggregation |
| Comment retention | 658 files contain WordPress comments (retained per owner decision) |

## Detailed Findings

### Parking Pages

The site was Hostinger-parked at the time of archive, but the Wayback Machine captures contain actual content. The parking detection logic correctly identified Hostinger parking markers and skipped them before extraction. **0 actual parking pages** were found in the Tier 2 output.

**False positives (5):** The string "parking lot" appeared in 5 event titles (e.g., "parking lot availability at venue"), which were correctly converted as content.

### PII — Email Addresses

**1 file** contained an email address: `DPPUSWEST@GMAIL.COM`. This appears in the context of a contact email for a community organization announcement, not a private individual's personal email. The email was already publicly published on the original website.

### PII — Phone Numbers

**96 files** contained phone numbers. These fall into the following categories:

| Category | Count | Context |
|----------|------:|---------|
| Taiwan Center contact info | ~40 | Official organizational phone numbers |
| Event hotlines | ~30 | Public event announcement hotlines |
| Community organization | ~15 | Public-facing organizational numbers |
| Miscellaneous | ~11 | Other public contact numbers |

All phone numbers are in the context of public-facing organizational or event contact information, not private individuals.

### Empty/Near-Empty Bodies

**0 files** had empty or near-empty bodies. All 29,102 successfully converted files (1 skip was a 0-character robots.txt) contain substantive content.

### Sensitive Content Flags

**None.** The scan checked for:
- Explicit violence descriptions
- Hate speech markers
- Personal threat content
- Financial fraud indicators
- Medical misinformation

All content is news/opinion aggregation from mainstream media sources (BBC, VOA, Central Daily News, etc.) and original column articles. No sensitive content was found.

### Comment Retention

**658 files** contain WordPress comment sections. These are retained per the owner's decision (Freeman Huang). The comments are public-facing and were part of the original website. The Trafilatura extraction pipeline correctly excluded comment reply forms but preserved actual comment content.

## Privacy Gate Decision

**Content is safe to publish.**

### Rationale

1. **No private individual data:** All PII (phone numbers, emails) is in the context of public-facing organizational or event contact information. No private residential addresses, personal phone numbers, or personal emails were found.

2. **Public-facing context:** Phone numbers and the single email address are for community organizations, event hotlines, and public announcements — all of which were already published on the public website.

3. **No sensitive content:** The archive contains only news aggregation and opinion content. No hate speech, threats, or sensitive personal information.

4. **Comment retention:** WordPress comments are retained per the owner's explicit decision. These are public comments that were already published.

5. **Disambiguation safety:** The column authors are public figures (columnists, political commentators) whose names and roles are already public. Thin people pages are created with only name, role, and article count — no private details.

### Recommendations

- No content redaction required
- Phone numbers and emails can remain in the archive
- Comment sections can remain in the archive
- Thin people pages should continue to include only name, role, and article count (no personal details)

## Scan Methodology

The scan was conducted using a Python script that:
1. Iterated over all 29,103 markdown files in `knowledge/web-archives/taiwanjustice-net/tier2/`
2. Checked frontmatter for parking markers
3. Searched body text for email patterns (`[\w.+-]+@[\w-]+\.[\w.-]+`)
4. Searched body text for phone number patterns (Taiwan and US formats)
5. Checked for empty/near-empty body content (< 10 characters)
6. Checked for sensitive content markers
7. Checked for WordPress comment indicators

## Source

- **Archive:** `knowledge/web-archives/taiwanjustice-net/tier2/`
- **Entities sheet:** `knowledge/research/taiwanjustice-net-entities.md`
- **Scan script:** `knowledge/web-archives/taiwanjustice-net/gap_fill.py` (privacy gate module)
- **Scan date:** 2026-07-28
- **Confidence:** A (systematic scan of all files)

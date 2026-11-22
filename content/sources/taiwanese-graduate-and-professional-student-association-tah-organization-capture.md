---
title: "TAH organization directory capture — Taiwanese Graduate and Professional Student Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese Graduate and Professional Student Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 588
- wikilinks: 1


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/taiwanese-graduate-and-professional-student-association|Taiwanese Graduate and Professional Student Association (TGAPSA)]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-graduate-and-professional-student-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-and-professional-student-association/](https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-and-professional-student-association/)
- **Record id:** 77555 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:21 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45, 1,619 bytes)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77555`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, two paragraphs):**
  1. "The Taiwanese Graduate and Professional Student Association (TGAPSA), also referred to as
     UPenn TSA, is a graduate-level Taiwanese student organization at the University of
     Pennsylvania. It is listed on both the Penn Clubs platform and the PAACH Student Communities
     directory. The organization explicitly distinguishes itself from the undergraduate Penn
     Taiwanese Society, noting that it serves “graduate and professional students
     university-wide.”"
  2. "TGAPSA holds monthly events and programs designed to foster cultural enrichment and
     community among its members and the broader Penn community. Documented event types include a
     Lunar New Year Celebration, film screenings, intercollegiate exchange activities, sports
     events, workshops, networking socials, and festival parties. The organization also maintains
     an active relationship with Penn's Graduate and Professional Student Assembly (GAPSA) as part
     of its commitment to university-wide unity."

## Harvest note
Paragraph 2 was **absent from the org page body** before card t_c7658760 (2026-11-14) — the page
carried only paragraph 1. The unabsorbed paragraph 2 (monthly programming, the seven documented
event types, and the GAPSA relationship claim) is the real harvest of this card.

## Twin check (2026-11-14, card t_c7658760)
The `tah_organization` JSON class has no story-dump `posts/` twin here: `grep -ril 'TGAPSA'
knowledge/web-archives/taiwaneseamericanhistory-org/posts/` returns zero files, so no profile-vs-dump
containment check is possible and the record is one editable self-report → `alleged`.

Same-batch campus siblings (one editor, same minute — NOT corroboration), with the bidirectional
containment check on tag-stripped/quote-folded `content_html`:
- `organization/penn-taiwanese-student-association.json` — id **77554**, `modified`
  **2026-06-09T17:23:21** (byte-identical timestamp). Its own record text names "the graduate-level
  TGAPSA" in a distinctness ruling; containment: neither body is a substring of the other → two
  distinct self-reports of one authoring session, one evidentiary tier.
- `organization/upenn-tesol-taiwanese-student-association.json` — id **77558**, `modified`
  **2026-06-09T17:23:22**.
- `organization/penn-taiwanese-society.json` — undergrad PTS, referenced by TGAPSA's paragraph 1.

## Whole-corpus sweep (2026-11-14, card t_c7658760)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF 'TGAPSA' content knowledge` → 6 files: this org page; `penn-taiwanese-student-association.md`
  + its capture page (the reciprocal distinctness ruling); `taiwanese-dental-association.md` (sibling
  FLOOR-ANCHOR close-note cross-reference only); the two org JSONs above. No narrative record.
- `grep -rlF 'Taiwanese Graduate and Professional Student Association' content knowledge` → org page,
  `content/organizations/index.md` and `content/sources/taiwaneseamericanhistory-org.md` directory index
  lines, plus machine indexes only (`knowledge/research/taiwanjustice-net-priority-lexicon.json`,
  `ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`).
- `grep -rlF 'UPenn TSA' content knowledge` → org page + Penn TSA page/capture + this org JSON (the
  alternate-name claim), nothing else.
- Prior deepen-x stamps on the org page (6, 2026-09-20 → 2026-10-09) grepped only `works/` +
  `articles/` (+ later `sources/events/topics`); this sweep covered all of `content/` + `knowledge/`
  and found no additional citable narrative source.

## Gaps / NEED YOU
Not archived on this box (would close the gaps): Penn Clubs listing for TGAPSA; PAACH Student
Communities directory entry; Penn GAPSA affiliate roster; any TGAPSA founder submission or event
announcement in future TAH story-corpus dumps.

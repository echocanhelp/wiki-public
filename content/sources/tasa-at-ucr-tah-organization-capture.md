---
title: "TAH organization directory capture — TASA @ UCR"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — TASA @ UCR

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 760
- wikilinks: 2


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/taiwanese-american-student-association-at-ucr|Taiwanese American Student Association at UCR]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-american-student-association-at-ucr.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-american-student-association-at-ucr/](https://taiwaneseamericanhistory.org/organization/taiwanese-american-student-association-at-ucr/)
- **Record id:** 77539 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:19 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45, MANIFEST `fetched_at` 2026-08-17, method `wp-json`)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77539`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, two paragraphs):**
  1. "The Taiwanese American Student Association at UCR (TASA @ UCR) is a student cultural
     organization at the University of California, Riverside. It is listed as an officially
     recognized cultural organization under the umbrella of UCR's Asian Pacific Student Programs
     (APSP), which coordinates Asian American and Pacific Islander student groups on campus.
     TASA @ UCR maintains an Instagram presence at @ucr.tasa and a Facebook page, and has a
     listing in UCR's official student organization directory, HighlanderLink."
  2. "The organization focuses on the Taiwanese American student community at UCR. No founding
     year or formal mission statement was located in available first-party sources. Its
     affiliation with APSP indicates participation in campus-wide AAPI programming, which
     includes cultural shows, heritage month events, and peer mentorship opportunities."

## Single-source status
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md`
  encyclopedia-dump twin (unlike Who's Who person records), so no twin/containment check against a dump
  is possible; every field above is one editable self-report → label `alleged` on the org page.
- **Same-batch neighbor is NOT corroboration:** the other UCR Taiwanese student-org record,
  [[organizations/ucr-united-taiwanese-student-association|UCR United Taiwanese Student Association]],
  is directory record id **77540** — one id above this record — with `modified`
  **2026-06-09T17:23:20**, one second later. Both are one editor's same-minute directory batch, so
  UTSA's text does not corroborate this record's text and vice versa. Bidirectional containment check
  on the two `content_html` bodies (tag-stripped, whitespace-collapsed, 2026-11-14): 733 vs 629
  normalized chars, md5 `6189f0073c23c68c5af74ae21d5a3c68` vs `d67a74ac166168d645bf1f3bf9d201b5`,
  neither is a substring of the other → two distinct self-reports of one authoring session, i.e. one
  evidentiary tier (`alleged`), not two. Whether TASA @ UCR and UCR UTSA are distinct clubs needs the
  HighlanderLink directory, which is not archived on this box.

## Whole-corpus sweep (2026-11-14, card t_32103a34)
Checked `content/` + `knowledge/` per name/token form (machine indexes `ee-vault-index*`,
`content-analysis/*.jsonl`, `units.jsonl`, `taiwanjustice-net-priority-lexicon.json` excluded as
indexes; `content/media/*.mp3` byte noise excluded after inspection):
- `grep -rilF 'TASA @ UCR'` → only this org page + the org JSON above. No narrative record.
- `grep -rilF 'HighlanderLink'` → this org page, the org JSON above, and the UTSA JSON
  (`organization/ucr-united-taiwanese-student-association.json`, where UTSA's record says **no**
  HighlanderLink listing was found for it — absence evidence, not coverage of this org).
- `grep -rilF 'ucr.tasa'` → only this org page + the org JSON above.
- `grep -rilF 'Asian Pacific Student Programs'` → only this org page + the org JSON above.
- `grep -rilF 'APSP'` → the two above plus taiwanjustice-net article prose and audiobook mp3 byte
  noise (substring coincidences, pre-classified, not about this org).
- `grep -rlF 'UCR'` broad sweep → beyond the org's own page/JSON: `organizations/index.md` (directory
  index row), the sibling UTSA page/JSON, and `UC Riverside` mentions in unrelated records
  (`ourjourneys274` NATMA Cambodia medical-mission memoir — unaffiliated UCR undergrads, ruling
  already recorded in ## Disambiguation; `american-chinese-dance-association`, `weiko-lin`,
  `lung-wen-tsai`, `prof-michi-fu`, `justin-lai` — Education/venue fields only). No UCR TASA material.
- Prior deepen-x stamps (2026-09-23 → 2026-10-09) grepped `works/` + `articles/` (+ later
  `sources/events/topics`); this sweep covered all of `content/` + `knowledge/` and found no
  additional citable narrative source.

## Gaps / NEED YOU
Sources checked on this box (all negative for founding year, officers, events, and Chinese name):
TAH org directory JSON 77539 + same-batch neighbor 77540; whole-corpus `content/` + `knowledge/`
greps for `TASA @ UCR` / `ucr.tasa` / `HighlanderLink` / `Asian Pacific Student Programs` / `APSP` /
`UCR`. What would close the gaps:
- **UCR HighlanderLink** listing for TASA @ UCR (the directory itself names it as the official
  student-organization directory) — not archived on this box; needs a live fetch.
- **UCR APSP** (Asian Pacific Student Programs) recognized-organization listing — not archived.
- The **@ucr.tasa** Instagram and Facebook pages — not archived on this box.
- Any TASA @ UCR founder submission or campus-event record in future TAH story-corpus dumps.

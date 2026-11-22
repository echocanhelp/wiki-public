---
title: "TAH Who's Who profile capture — 920. Serena Chen"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
subject: "[[people/serena-chen]]"
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 920. Serena Chen

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 441
- wikilinks: 1


Primary capture of the subject's self-reported TAH Foundation Who's Who record, archived on this
box as two distinct artifacts under `knowledge/web-archives/taiwaneseamericanhistory-org/`.
Preserved in full because the biographical fields are self-reported and the live site is editable.

## Subject
- [[people/serena-chen|Serena Chen]] — TAH Who's Who record #920

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/serena-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/serena-chen/](https://taiwaneseamericanhistory.org/person/serena-chen/)
- **Record id:** 73484 · **type:** `tah_person` · **`modified` on source:** 2026-06-02T17:20:19 ·
  page size 52,067 bytes (`page_bytes`)
- **Profession taxonomy (`class_list`):** `person_profession-physician`, `person_profession-surgeon`
  — the **surgeon** tag is absent from the sidecar roles list (`sidecar.roles: [physician]`).
- **Verbatim fields (self-reported):** Name Serena Chen · Birth Year `-` · Birth Place `-/-/-` ·
  Address `Livingston, NJ`
- **Family:** `1. Husband:-` `2.Daughter:-` `3.Son:-` — all blank; `family_filled: false`
- **Education:** `1. Duke University` `=` `Degree and major` (degree/major left blank)
- **Employment:** `1. Reproductive Medicine at IRMS at Saint Barnabas` `Present` `Director` ·
  `2. Johns Hopkins Bayview Medical Center` `–` `Residents`
- **Accomplishment:** `1. Top Fertility Doc, NY Magazine and NJ Monthly`
- **Publication (Non-professional ones):** `–` · **Hobby:** `–` · **Website or Blog:** `–`
- **`content_html` empty / `page_text` chrome-only:** the captured profile page body carries no
  biography prose beyond site navigation — the form fields in capture 2 are the whole record.

## Capture 2 — Who's Who post render
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho920.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho920/](https://taiwaneseamericanhistory.org/whoswho920/)
- **Title:** 「920. Serena Chen」 — same field roster as capture 1 (Name/Birth Year/Birth Place/
  Address/Family/Education/Employment/Accomplishment/Publication/Hobby/Website).

## Twin check
- Normalized (frontmatter + `#`/whitespace stripped): `page_text` capture 1,318 chars vs post dump
  capture 2,474 chars. md5 differs (`10cc9660…` vs `6cffa50d…`) **and** containment fails both
  directions — capture 1's normalized text includes repeated site-navigation chrome capture 2 omits,
  so neither is a substring of the other. This is expected here: capture 2 is the richer artifact
  for form content, capture 1 for taxonomy/metadata (`class_list`, `page_bytes`, `modified`).
- The two artifacts are two serializations of **one editable self-report**, so agreement across them
  is NOT corroboration — that is what keeps the record's own `Top Fertility Doc` print citation at
  `alleged` on the person page.

## Skipped / not merged
- No Chinese name (sidecar `hanzi: null`); no birth year, birthplace, spouse/children names asserted.
- No `Source from <org>` submission-provenance line present on this record.
- Other "Serena" hits in the corpus archive are same-name false positives, ruled 2026-11-14:
  `posts/652.md` "Serena Yeh Wang" (Wang family photo caption, 2015),
  `posts/austin-tx-taiwanese-association.md` "Serena Chao (Treasurer)",
  `posts/mtsc-1994.md` "Serena Tsuang" (registration contact),
  `posts/my-stories-858.md` "Serena Williams" (tennis). None merged.
- Machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`,
  `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`) are not
  sources and were excluded.

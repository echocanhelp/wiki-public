---
title: "TAH Who's Who profile capture — Prof. F. S. Shih (謝復生教授)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — Prof. F. S. Shih (謝復生教授)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 499
- wikilinks: 2


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-f-s-shih|Prof. F. S. Shih 謝復生教授]] — TAH Who's Who profile
  (WordPress post id 74234, type `tah_person`)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-f-s-shih.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-f-s-shih/](https://taiwaneseamericanhistory.org/person/prof-f-s-shih/)
- **Record id:** 74234 · **type:** `tah_person` · **profession taxonomy**
  (`person_profession-*`): educator, politician, professor, researcher, scholar
  (the `politician` and `scholar` tags are absent from the lean sidecar roles
  `professor, educator` — taxonomy richer than sidecar)
- **`modified` on source:** 2026-06-19T16:54:32 (page renders "Last updated: June 19, 2026") · page size 54,645 bytes
- **Verbatim fields (self-reported):** Birth Year `--` · Birth Place Taiwan ·
  First year/city/State in U.S. `-/-/-` · Address `—`
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: —` — all blank;
  sidecar `family_filled: false`, `family: []`
- **Education:** National Taiwan Univ. 1974 B.A., Political Science ·
  Univ. of Rochester 1979 M.A., Political Science · 1982 Ph.D., Political Science
- **Employment:** National Chengchi Univ. (政治大學) — Professor and Dean, Dept. of
  Political Science · Univ. of South Carolina — Professor, Dept. of Political
  Science; Director of the Center for Asian Studies (no year ranges filled)
- **Accomplishment / Hobby:** `—` in both fields (label-inflation check: no withheld
  accomplishment or hobby content in the record)
- **`content_html` on the profile JSON is empty** — the site-rendered `page_text` is the
  only narrative layer of this capture.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1719-f-s-shih.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1719-f-s-shih/](https://taiwaneseamericanhistory.org/whos-who-1719-f-s-shih/)
- **Title:** `1719. Prof. F. S. Shih 謝復生教授` (TAH encyclopedia sequence #1719)
- Field set identical to Capture 1 (same education rows, same two employment rows),
  **plus** the `Publication` field, which Capture 1's render omits:
  1. 政治學的範圍與方法, 2000
  2. 實證政治理論, 2013
  `Accomplishment`/`Hobby` `—` in both.

## Twin check (2026-11-14)
Captures 1–2 are two serializations of **one self-report record family** on
taiwaneseamericanhistory.org. Containment test run rather than naive md5: every field
in Capture 1 appears verbatim in Capture 2, and Capture 2 is the **richer** artifact —
it carries the two Publication titles and years that Capture 1's `page_text` render
drops (Capture 1 is richer only in metadata: `modified` stamp, profession taxonomy,
`page_bytes`). Agreement across two serializations of one editable self-report is
**not corroboration**: every biographical fact is labeled `alleged` on the subject page.

## Other corpus hits (2026-11-14 whole-corpus sweep)
`grep -rlF '謝復生' content knowledge` and case-insensitive
`grep -rliF 'F. S. Shih' content knowledge` return the identical hit set: this
capture's two artifacts plus `people/prof-f-s-shih.md`, the work-entity page
[[works/taiwaneseamericanhistory-org/whos-who-1719-f-s-shih]], the `people/index.md`
and `sources/taiwaneseamericanhistory-org.md` hubs, and machine indexes
(`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`,
`taiwaneseamericanhistory-org-family.json`, `ee-vault-index.v1–v5.json`) — indexes are
not sources. Publication-title greps `政治學的範圍與方法` / `實證政治理論` return only
these two capture artifacts. **No memoir, story-corpus article, or third-party record
names him** (surname-only `Shih` hits are other people: Paul Pai-Shih Lee, Shih-Yaw Lai).

---
title: "TAH Who's Who profile capture — 1605. Richard Wang"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1605. Richard Wang

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 753
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/richard-wang|Richard Wang]] — TAH Who's Who record #1605

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/richard-wang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/richard-wang/](https://taiwaneseamericanhistory.org/person/richard-wang/)
- **Record id:** 74129 · **type:** `tah_person` · **profession taxonomy (class_list):** `activist`, `community leader`, `researcher`, `scientist` — the sidecar keeps only `roles: ['scientist']`, so the activist/community-leader tags are taxonomy detail the sidecar drops
- **`modified` on source:** 2026-06-02T17:22:50 · page size 55,631 bytes · rendered `Last updated: June 2, 2026`
- **Verbatim fields (self-reported):** Name `Dr. Richard Wang` (hanzi blank) · Birth Year `-` · Birth Place `-/-/-` · Address `Los Angeles/CA`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; `family_filled: false`
- **Education:** 1. UCLA — 1998 — B.S. neuroscience · 2. UCLA — 2010 — Ph.D. Genomics
- **Employment:** 1. UCLA — 2015–present — Staff Research Scientist · 2. UCLA Center for Duchenne Muscular Dystrophy — 2010–present — Postdoctoral Researcher
- **Accomplishment:** 1. founding member of UCLA's Taiwanese American Union · 2. Editor in Chief of UCLA's Pacific Ties · 3. National Vice President of Taiwanese American Citizen League (TACL) · 4. National President of TACL from 2002–2004
- **Notable Accomplishments:** the same four strings repeated verbatim in a second field
- **Publication (Non-professional) / Hobby / Website or Blog:** all `-`
- **Submission provenance line printed on the page:** `Source from TACL.org`

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1605.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1605/](https://taiwaneseamericanhistory.org/whoswho1605/)
- **Title:** `1605.  Richard Wang / 2017/04` · work record [[works/taiwaneseamericanhistory-org/whoswho1605|TAH #1605]] published 2017-04-14
- Field set identical to Capture 1 (Name/Education/Employment/Accomplishment/blank Publication/Hobby/Website, same `Source from TACL.org` footer).

## Twin check (2026-11-14)
Whitespace-stripped, frontmatter-excluded body md5 `b44fc329fff5` (2,988 norm chars, the crawled
profile page incl. site chrome, the repeated Notable Accomplishments block and the 2026-06-02
`modified` stamp) vs `9ec7c3ba1462` (568 norm chars, the encyclopedia-entry dump). Containment
test run both directions: neither is a substring of the other — they are two serializations of the
same editable self-report, and the richer one is Capture 1. Agreement across two serializations of
one self-report is **not** corroboration; that is what keeps the record's own `Source from TACL.org`
provenance at `alleged`.

## Second, independent community records (not self-report)
- **SETAA 2004 speaker roster** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/setaa-2004.md`
  (repost of 台灣公論報 第2026 期, 6/15/2004 + 南佛州台灣同鄉會會訊 06/2004) lists among 講員:
  「Richard Wang：第二代成功案例(The emerging leadership of Taiwanese American 2nd generation)」 at
  第廿六屆美東南區台灣人夏令會, July 9–11 2004, Furman University, Greenville, SC, theme 「台灣向前行」.
  Same-name disambiguation: the same roster separately lists 「台美公民協會總會長王克勝先生」 introducing
  「台美新生代領導人物面面觀」 — if 王克勝 is the Chinese name of this Richard Wang, the roster carries
  **two** TACL-president entries for 2004 and the identification is **unconfirmed** (no hanzi in either
  capture; `hanzi: null`). The speaker row is therefore recorded `alleged`.
- **TAITA-SV panel roster** — `knowledge/web-archives/taiwaneseamerican-org/taita-sv-panel-presentation-opportunities-for-the-new-decade.md`
  (source_url `https://www.taiwaneseamerican.org/2010/01/taita-sv-panel-presentation-opportunities-for-the-new-decade/`)
  lists panelist 「Richard Wang, Vice President, Parah Capital Management Inc.」 at the 2010-01 panel
  「Opportunities for the New Decade」, Silicon Valley Center at Fenwick and West LLP, Mountain View, CA.
  Identity conflict with the TAH self-report (which shows UCLA research employment 2010–present): either
  same-name different person or parallel roles, **unconfirmed**; recorded `alleged` pending a third record.
  Work page [[works/taiwaneseamerican-org/taita-sv-panel-presentation-opportunities-for-the-new-decade|TAITA-SV panel]]
  carries `Parah Capital` uniquely on this box (`grep -rln 'Parah' content knowledge` → this dump only).

## What this capture does NOT establish
- No Chinese name, birth year, or birthplace — blank in both artifacts.
- The TACL national presidency 2002–2004 appears only in the subject's own editable record; the TACL
  organization page names other presidents (Li-Pei Wu 1985-, 周實 1986-, Ben Ling 2010) and does not
  name this subject, so the presidency stays `alleged`.
- No connection between the SETAA 2004 speaker and the TAITA-SV 2010 panelist can be established from
  local records.

## Gaps / NEED YOU
Sources checked on this box for this subject (whole-corpus + whole-`knowledge/`, `grep -rlF 'Richard Wang'`,
plus '王克勝', 'Parah'): own TAH records (person JSON + whoswho1605 post + works page), the TACL 25-year
legacy article, the SETAA 2004 roster post, the TAITA-SV 2010 panel dump, the taiwanjustice lexicon
(machine index), and the family-research JSON. Outside these no third-party record names Richard Wang.
Wanted: 台美公民協會 2002–2004 會長 roster or 通訊 naming him (would upgrade the presidency to
`documented`); hanzi confirmation (would settle the 王克勝 question); any Parah Capital record to
resolve the 2010 identity conflict.

---
title: "TAH organization directory capture — CWRU TASA (Case Western Reserve University)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — CWRU TASA (Case Western Reserve University)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 713
- wikilinks: 4


Capture page minted for the FLOOR-ANCHOR pass on
[[organizations/taiwanese-american-student-association-at-case-western-reserve-university]]
(card t_3ff0d586, 2026-11-14). It archives the one machine record this organization has on this
box, plus the checked-and-empty sweep, so the next pass does not re-grep.

## Captured machine record (the organization's own directory entry)
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-american-student-association-at-case-western-reserve-university.json`
- Record id **77619**, `type: tah_organization`, `status-publish`, taxonomy class slug
  `organization_type-student`; `person_profession` is the empty list `[]`, `excerpt` is null.
- `modified` stamp on source: **2026-06-09T17:23:27**. On-disk capture mtime: **2026-08-17 00:45:26 -0700**
  (wp-json crawl batch; `MANIFEST.json` `fetched_at: 2026-08-17`). File size 2,086 bytes.
- Live URL of the same record: https://taiwaneseamericanhistory.org/organization/taiwanese-american-student-association-at-case-western-reserve-university/
- `content_html` (three paragraphs, self-reported and site-editable), verbatim in substance:
  1. CWRU TASA is a student organization based in Cleveland, Ohio, focused on the Taiwanese
     American community on campus; its mission, as stated on its official university portal, is to
     empower and inspire the Taiwanese American community, work with other cultural groups at Case
     to promote diversity, and help develop personal friendships and professional networking
     through events and resources that explore Taiwanese American identity.
  2. Flagship events each academic year: a fall **Night Market** — modeled after traditional
     Taiwanese night markets, featuring food and drink booths, games, prizes, and student
     performances — and a spring event called **Plum Blossom**. The organization is recognized by
     CWRU's official newsroom and maintains an active Facebook page and Instagram presence under
     the handle **@cwru_tasa**.
  3. Engagement with the broader campus through partnerships with other cultural student
     organizations and speaker programming addressing Taiwanese American identity and culture;
     affiliated with Case Western Reserve University's student community platform and listed in the
     university's club directory.
- Label: `alleged`. `content_html` is the only substantive field on the record (no excerpt, no
  profession terms), so every fact above traces to one editable self-report, not to corroboration.

## No `posts/` twin
- Sweep of `knowledge/web-archives/taiwaneseamericanhistory-org/posts/` for a same-slug twin
  (`case-western` / `cwru` / `tasa`) found no story-corpus dump of this record → the JSON is the
  only serialization; the twin/containment check against a story dump is N/A (sibling class
  precedent: the `tah_organization` JSON records generally have no `posts/` twin).
- The `TASA`-named posts in that dir (`15-通信月刊 by 南加州台灣人長老化TASA`, ITASA items, `5-itasa`,
  `history-of-itasa`, etc.) are other organizations (ITASA / SoCal TASA), pre-classified as
  false positives.

## Campus-name-neighbor check: CWRUTSA (record 77618)
- Sibling record `knowledge/web-archives/taiwaneseamericanhistory-org/organization/cwru-taiwanese-student-association.json`
  — record id **77618**, same `modified` **2026-06-09T17:23:27**, same `organization_type-student`
  taxonomy, same Cleveland campus.
- Body-length comparison measured on disk 2026-11-14 (tags stripped, whitespace folded):
  **1,146** chars for TASA (77619) vs **763** for CWRUTSA (77618), and neither string contains the
  other → two separately authored directory records captured in one crawl batch, **not** two
  serializations of one self-report. The sibling capture page
  [[sources/cwru-tsa-tah-organization-capture|CWRUTSA directory capture]] (card t_0fae50ac,
  2026-11-14) independently measured the same pair and reached the same ruling.
- Identity boundary: neither record states any relationship to the other. The vault keeps them as
  two pages ([[organizations/taiwanese-american-student-association-at-case-western-reserve-university|CWRU TASA]])
  and [[organizations/cwru-taiwanese-student-association|CWRUTSA]]; same-batch authorship is
  **not** corroboration. Shared campus, city and crawl batch are recorded as an
  identity-collision hazard for a future merge/dedup decision (resolver needs the CWRU club
  directory, not archived on this box).

## Checked and empty (sweeps re-run 2026-11-14, `grep -ril` over `content/` + `knowledge/`)
- `Case Western` → own page + CWRUTSA page + `organizations/index.md` + the 2026-01-23
  taiwanjustice-net presidential-debate article (campus as debate **venue**) + 8 person pages
  (ta-fu-ho, steven-j-hsu, t-t-dean-su, lai-ting-yu, prof-chao-yuan-huang, mike-lin, po-hu,
  dr-sebo-koh — Enrollment/Employment fields only) + source/registry pages
  (`sources/taiwaneseamericanhistory-org.md`, `sources/cwru-tsa-tah-organization-capture.md`,
  `sources/tah-whoswho-c-w-wu-capture.md`, `sources/mike-lin-capture.md`).
- TAH `posts/` files where Case Western appears only in a person's Education field —
  `237-min-shiu-lee`, `whoswho1134`, `623-黃昭淵-201509`, `whsoswho1354`,
  `whos-who-2115-wen-yaw-chan`, `whos-who-770-sebo-koh`, `mystories206` (林健華 industrial-engineering
  PhD narrative), `tacec-2000` (a 1987–1989 graduate narrative naming a Rutgers 台灣研究社, not a
  CWRU club) — none mentions any Taiwanese student association at Case Western.
- `CWRU TASA` / `cwru_tasa` / `TASA at Case` → only the two org pages, the sibling capture page,
  and machine indexes.
- `凱斯西儲` → the same debate article, `people/c-w-wu.md` + its capture, `posts/whoswho954.md`
  (Enrollment fields; campus, not club).
- Machine indexes (`ee-vault-index*.json`, `content-analysis/*.jsonl`,
  `taiwanjustice-net-priority-lexicon.json`, `taiwanjustice-net/raw-html` location strings,
  `cdx-unique-urls.jsonl`) excluded as indexes, not sources.
- Prior deepen-x SKIP stamps 2026-09-18 → 2026-10-09 (incl. slices 10052158-15, 10070717-25)
  stand: no memoir, club magazine, or press material about CWRU TASA exists in the corpus.

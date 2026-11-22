---
title: "TAH Who's Who profile capture — 1585. Ehin-Lin Guo 郭青齡"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1585. Ehin-Lin Guo 郭青齡

Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived on
this box as two distinct artifacts. Preserved in full because every biographical field on
[[people/ehin-lin-guo|Ehin-Lin Kuo 郭青齡博士]] traces to these two files, the live site is
editable, and the self-report now demonstrably **conflicts** with the subject's own institutional
record on degree years — which is precisely why the verbatim directory fields need to survive
here ([[sources/sinica-iop-guo-chin-lin-capture|the Academia Sinica institutional capture]]).

## Subject
- [[people/ehin-lin-guo|Ehin-Lin Kuo 郭青齡博士]] — TAH Who's Who encyclopedia record #1585,
  published 2017-03-26 (publication date is **not** on the profile page; it comes from the corpus
  archive copy and the category listing, see Capture 2 and Corroboration below).

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ehin-lin-guo.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ehin-lin-guo/](https://taiwaneseamericanhistory.org/person/ehin-lin-guo/)
- **Record id:** 74112 · **type:** `tah_person` · **slug:** `ehin-lin-guo` ·
  **title as stored:** `Ehin-Lin Guo 郭青齡`
- **Profession taxonomy — four tokens, not two.** `person_profession: [2230, 2237, 1813, 2225]` and
  the `class_list` carries the matching four tokens `person_profession-physician`… specifically:
  `person_profession-physicist`, `person_profession-professor`,
  `person_profession-researcher`, `person_profession-scientist`. The crawl's own `sidecar`
  compresses this to `roles: ["scientist", "professor"]` — the sidecar is the lossy rendering, and
  the earlier vault page copied the sidecar rather than the taxonomy. **physicist** and
  **researcher** are recorded by the site and were missing from the vault page.
- **`content_html` and `excerpt` are both empty strings** — the record has no free-text biography.
  Everything below is a table field.
- **`modified` on source:** 2026-06-19T16:52:19 (`page_bytes`: 53,483 raw HTML; `page_text` is the
  trafilatura-extracted text)
- **Site-rendered header:** `Who's Who Taiwanese American Profile · Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** `Name 郭青齡 博士` / `Prof. Ehin-Lin Guo` ·
  Birth Year `-` · Birth Place `台灣` ·
  `First year, first city and state arrived in the U.S.` `-/San Diego/CA` · Address `台灣`
- **Family (verbatim):** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three rows present and
  empty; the structured `family` array is `[]` and `family_filled: false`. This is an **absence of
  record**, not a record of no family.
- **Education (verbatim):** `1.台灣大學 / - / B.S.` · `2. UCSD / 1994 / M.S.` ·
  `3. UCSD / 1996 / Ph.D.` — the institution/year pairing in this field is what the institutional
  record contradicts (see Conflicts).
- **Employment (verbatim):** `1.Cal Tech / 2006-2014 / Assistant professor` ·
  `2.中央研究院物理研究所 / present / 副研究員`
- **Withheld / empty fields:** `Accomplishment -` · `Publication(Non-professional ones) -` ·
  `Hobby -` · `Website or Blog -`. The directory withholds nothing from this page; those four
  fields are empty at the source.
- **Named provenance of the submission:** `Source from 北美洲台灣人教授協會2013 annual meeting` —
  the North American Taiwanese Professors Association (NATPA) 2013 annual meeting. This is the
  submission channel, recorded by TAH itself, and it is why the record's frame is
  professorial/academic.
- **Trailing repeat block:** the profile renders the same identity/education/position data a second
  time under `Source from 北美洲台灣人教授協會2013 annual meeting` (`Hanzi Name 郭青齡博士` ·
  `Birthplace 台灣` · `Residence 台灣` · `Education 台灣大學 B.S. / UCSD M.S. (1994) / UCSD Ph.D.
  (1996)` · `Position Cal Tech Assistant Professor (2006-2014) / 中央研究院物理研究所 副研究員`).
  Same self-report, one record, two renderings — not a second source.

## Capture 2 — corpus encyclopedia record
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1585.md`
- **Vault record page:** [[works/taiwaneseamericanhistory-org/whoswho1585|1585. Ehin-Lin Guo 郭青齡 / 2017/03]]
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1585/](https://taiwaneseamericanhistory.org/whoswho1585/)
- **Front matter:** `source_url: https://taiwaneseamericanhistory.org/whoswho1585/` · `fetched: auto`
- **Title:** `1585. Ehin-Lin Guo \t郭青齡 / 2017/03` — the `/ 2017/03` suffix is the corpus's own
  year/month stamp on the record.
- This copy carries the same field table as Capture 1 (`### 郭青齡 博士` / `### Prof. Ehin-Lin Guo` /
  `### 台灣` / `### -/San Diego/CA` / Education `1.台灣大學`, `2. UCSD 1994`, `3. UCSD 1996` /
  Employment `1.Cal Tech 2006-2014`, `2.中央研究院物理研究所`), i.e. the field-level self-report
  exists twice on this box in two artifact families.
- **Relationship to Capture 1:** both artifacts descend from one editable self-report by the same
  subject, so agreement between them corroborates transcription fidelity, **not** the underlying
  facts. Independent corroboration is
  [[sources/sinica-iop-guo-chin-lin-capture|the Academia Sinica institutional record]].

## Corroboration — publication date
- Category listing [TAH Who's Who, page 73](https://taiwaneseamericanhistory.org/category/whos-who/page/73/)
  renders `1585. Ehin-Lin Guo 郭青齡 / 2017/03` with date line `March 26, 2017`.
- Profession archive listings agree to the day:
  [scientist, page 16](https://taiwaneseamericanhistory.org/person_profession/scientist/page/16/) and
  [professor, page 24](https://taiwaneseamericanhistory.org/person_profession/professor/page/24/)
  both list `Ehin-Lin Guo 郭青齡 — March 26, 2017`.
- So the publication date `2017-03-26` is carried by **three independent site renderings** (record
  title suffix, category page, two taxonomy pages), while the profile page itself carries none.

## Conflicts with the institutional record
The subject's Academia Sinica Institute of Physics directory states
`B.S., National Taiwan University, 1994; M.S., 1996; Ph.D., University of California (San Diego)`
— i.e. the NTU **B.S. is dated 1994** and the **M.S. 1996**, with no year on the Ph.D. The TAH
self-report instead leaves the NTU B.S. year `-` and puts `1994` on the UCSD M.S. and `1996` on the
UCSD Ph.D. Same three degrees, same institutions, three years shifted by two years across
institutions. Full transcription and both readings
([[sources/sinica-iop-guo-chin-lin-capture|here]]); neither is silently preferred on the person
page.

## Label inflation check (2026-11-12, this pass)
Education, Employment and Family rows on the person page trace one-for-one to the two archive
copies above, with no year or institution added. The `physicist` / `researcher` roles trace to the
`class_list` taxonomy tokens, not to inference. Nothing on the person page asserts a honour,
publication, or community office the source does not carry.

## Source Notes
- `knowledge/web-archives/taiwaneseamericanhistory-org/person/ehin-lin-guo.json` — crawled profile,
  id 74112, `modified` 2026-06-19T16:52:19, 53,483 page bytes, both artifacts opened 2026-11-12.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1585.md` — corpus encyclopedia
  record copy, same field table.
- Live originals: [person/ehin-lin-guo](https://taiwaneseamericanhistory.org/person/ehin-lin-guo/),
  [whoswho1585](https://taiwaneseamericanhistory.org/whoswho1585/).
- Publication-date corroborations:
  [category/whos-who page 73](https://taiwaneseamericanhistory.org/category/whos-who/page/73/),
  [person_profession/scientist page 16](https://taiwaneseamericanhistory.org/person_profession/scientist/page/16/),
  [person_profession/professor page 24](https://taiwaneseamericanhistory.org/person_profession/professor/page/24/).
- Cross-source counterparty: [[sources/sinica-iop-guo-chin-lin-capture|郭青齡 / 副研究員 — Academia Sinica Institute of Physics capture]].

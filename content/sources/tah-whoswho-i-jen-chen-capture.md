---
title: "TAH Who's Who profile capture — 1452. I-Jen Chen 陳一仁"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1452. I-Jen Chen 陳一仁

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/i-jen-chen|I-Jen Chen 陳一仁醫師]] — TAH Who's Who record #1452

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/i-jen-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/i-jen-chen/](https://taiwaneseamericanhistory.org/person/i-jen-chen/)
- **Record id:** 73985 · **type:** `tah_person` · **profession taxonomy:** `community leader`,
  `physician`, `public health` (`person_profession-community-leader`,
  `person_profession-physician`, `person_profession-public-health`; term ids
  `person_profession: [2242, 2234, 348]`)
- **`modified` on source:** 2026-06-19T16:49:56 · page size 51,636 bytes
- **Site-rendered line:** `Who's Who Taiwanese American Profile — Last updated: June 19, 2026` ·
  name line `I-Jen Chen 陳一仁` · profession lines `community leader` / `physician` / `public health`
- **Verbatim fields (self-reported):** Name 陳一仁 醫師 / Dr. I-Jen Chen · Birth Year `-` ·
  Birth Place `台灣` · First year, first city and state arrived in the U.S. `-/-/-` ·
  Address `Seattle/WA`
- **Family:** `1. Wife: -` · `2.Daughter: -` · `3.Son:` — all three blank (the `Son` field is not
  even dash-filled); structured `family: []`, `family_filled: false`
- **Education:** 1. 中國醫藥學院 — `-` — `M.S.` · 2. `-` — `-` — `M.S.公共衛生`
- **Employment:** `-` / `-` / `-` — blank in all three sub-fields
- **Accomplishment:** `成立西雅圖"老人活動中心"`
- **Notable Accomplishments (site-rendered second block):** `成立西雅圖「老人活動中心」`
  followed by the site's own English gloss `(Founded the Seattle Senior Activity Center)`
- **Publication (Non-professional) / Hobby / Website or Blog:** all `-`
- **Site-rendered encyclopedia digest inside the page:** `Hanzi Name 陳一仁醫師` ·
  `Birthplace 台灣` · `Residence Seattle, WA` ·
  `Education 中國醫藥學院 / M.S. / M.S. 公共衛生`
- **`content_html` / `excerpt`:** both empty — the page's data lives in the taxonomy terms and the
  rendered field table, not in a post body.
- **`sidecar` field:** `{"hanzi": "陳一仁醫師", "birth_year": "-", "birthplace": "台灣", "roles": ["physician"]}` —
  note the crawler's sidecar **drops** the `community leader` and `public health` taxonomy terms
  and the entire `Accomplishment` field that the raw `page_text` carries. The sidecar is a
  reduction of the same record, not a second observation.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1452.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1452/](https://taiwaneseamericanhistory.org/whoswho1452/)
- **Title:** `1452. I-Jen Chen 陳一仁 / 2017/01` · **published:** 2017-01-15 (per the works record)
- Field set identical to Capture 1 (`Name` / `Birth Year –` / `Birth Place 台灣` /
  `First year… -/-/-` / `Address Seattle/WA` / three blank `Family` fields /
  `Education 1.中國醫藥學院 – M.S.` + `2. – M.S.公共衛生` / blank `Employment` /
  `Accomplishment 成立西雅圖"老人活動中心"` / blank `Publication` `Hobby` `Website or Blog`).

## Twin check (2026-11-12)
The two artifacts are **distinct records, not archive twins**: whitespace-stripped,
frontmatter-excluded body md5 `07bcc9e1039c` (1,170 chars — the crawled profile page incl. site
chrome, the three-term profession taxonomy, the `Last updated: June 19, 2026` line, the
site-rendered `Notable Accomplishments` block with its English gloss, the site-rendered
encyclopedia digest and the `modified` stamp) vs `99a434f69a67` (292 chars — the
encyclopedia-entry dump). The post dump is heading-padded (`###` on every line), which is why a
naive md5 differs trivially; the normalization above strips `#` and whitespace.

Every biographical string the two captures share is the subject's single self-report restated in
two serializations of one editable record, so field agreement across the two captures is **not**
independent corroboration. The one field the encyclopedia dump omits relative to the profile page
is the English gloss `(Founded the Seattle Senior Activity Center)`, which appears only in the
site-rendered second block of Capture 1 — it is the site editor's rendering of the subject's own
`Accomplishment` string, not an outside source.

## What this capture does NOT establish
- No birth year and no birth date — `Birth Year` is `-` in both artifacts; only `Birth Place 台灣`
  is filled.
- No year, city, or state of first arrival in the U.S. (`-/-/-`); the only U.S. locator is the
  self-reported `Address Seattle/WA` / digest `Residence Seattle, WA`.
- No spouse, daughter, or son — all three `Family` fields are blank and `family_filled: false`,
  so this is a recorded gap, not a claim that he has no family.
- No degree-granting dates, no dissertation or field beyond `M.S.公共衛生`, and no second
  institution name — the `2.` education row carries only `M.S.公共衛生` with an empty institution
  cell, so whether the two M.S. lines are one institution or two **cannot be read here**.
- No employer, title, practice location, specialty, or medical licence — `Employment` is blank in
  all three sub-fields. `醫師`/`Dr.` is the subject's own name-line honorific, not a verified
  credential row, and no clinical specialty is recorded anywhere in either artifact.
- `Publication (Non-professional)`, `Hobby` and `Website or Blog` are blank, so no publication or
  hobby fact is being withheld by the record.
- The `Accomplishment` string names no founding year, legal form, or incorporation date for the
  Seattle senior centre; the founding narrative and its dates live in the subject's own memoir,
  not in this profile.
- The works page [[works/taiwaneseamericanhistory-org/whoswho1452|TAH #1452]] is a
  bibliographic-only record (`value_band: B`, "Bibliographic record only. Full text stays in the
  vault") and carries none of the biographical fields above.

## Related
- [[people/i-jen-chen|I-Jen Chen 陳一仁醫師]] — the subject
- [[organizations/asian-senior-concerns-foundation|Asian Senior Concerns Foundation 亞裔銀髮族關懷基金會]] — the Seattle organisation he founded
- [[works/taiwaneseamericanhistory-org/whoswho1452|1452. I-Jen Chen 陳一仁 / 2017/01]] — bibliographic record
- [[works/taiwaneseamericanhistory-org/ourjourneys281|281. 如是，我為：自己的老年狄斯耐樂園自己建造！]] — founder's own memoir
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org]] — source hub

---
title: "TAH Who's Who profile capture — 753. Prof. Wentai Liu 劉文泰教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 753. Prof. Wentai Liu 劉文泰教授

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as three distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/prof-wentai-liu|Prof. Wentai Liu 劉文泰教授]] — TAH Who's Who record #753

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-wentai-liu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-wentai-liu/](https://taiwaneseamericanhistory.org/person/prof-wentai-liu/)
- **Record id:** 73319 · **type:** `tah_person`
- **Profession taxonomy (`class_list`):** 7 terms — `bioengineering`, `educator`, `electrical engineer`, `engineer`, `inventor`, `professor`, `researcher` (numeric `person_profession` ids `[1087, 2248, 323, 2227, 2233, 2237, 1813]`; no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The harvest `sidecar` keeps only `engineer`, `professor`, `educator` — `inventor`, `electrical engineer`, `researcher`, and `bioengineering` are **dropped by the sidecar** and survive only in `class_list`.
- **`modified` on source:** 2026-06-19T16:38:00 · `page_bytes`: 57,665 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** English Name `Prof. Wentai Liu` · Hanji Name `劉文泰教授` · Birth Year `1948` · Birth Place `Tainan, Taiwan`
- **U.S. arrival:** `-/-/-` — first year, first city and state unfilled on the record
- **Address:** `CA` — the footer block restates it as `Residence: CA`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` · JSON parses this as `family: []`, `family_filled: false` — no relative is named anywhere on the record.
- **Education (3 rows):** `1. National Chiao Tung Univ.` — `-` — `B.S.` · `2. National Taiwan Univ.` — `-` — `M.S.` · `3. Univ. of Michigan` — `1983` — `Ph.D.` (only the Michigan row carries a year)
- **Employment (3 rows):** `1. UCLA` — `2011-` — `Professor, Department of Bioengineering` · `2. National Science Society (NSF) Bionic Microelectronic System Engineering Research` — `2011` — `Director of UC Santa Cruz Branch` (the footer block restates the funder as `National Science Foundation (NSF)`; the printed form is quoted as-is) · `3. Univ. of California, Santa Cruz` — `2003-2011` — `Professor of Electronic Engineering`
- **Accomplishment (8 rows, self-reported, `alleged` — one editable record):**
  1. `Inventor of the Artificial Retina for Blind People, One of the Greatest Technical Breakthroughs of the 21 Century` (sic, "21 Century")
  2. `Father of Bionic Eye`
  3. `Distinguished Professor of The Bioengineering Dept. of UCLA`
  4. `IEEE (Institute of Electrical and Electronics Engineers) Fellow, 2016`
  5. `Popular Mechanics Breakthrough Award, 2010`
  6. `Associate Editor, IEEE Trans. on Biomedical Engineering`
  7. `Chair Professorship and Founder/Honorary Director of Biomimetic Systems Research Center, National Chiao-Tung Univ./Taiwan`
  8. `Outstanding Taiwanese American Elected by T.A. Archives in 04/2019`
- **Publication / Hobby:** `--` — unfilled. The two unfilled fields are themselves the record: no publication or hobby fact is being withheld elsewhere on this capture.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on abby-hong), this record carries no upstream-source attribution, so no external article can be traced from it.
- **Footer summary block (same page, rendered below the form):** Hanzi `劉文泰教授` · Birth Year `1948` · Birthplace `Tainan, Taiwan` · Residence `CA` · Education (3 rows, Ph.D. `(1983)`) · Position (3 rows: UCLA `(2011-)`, NSF `(2011-2011)`, UCSC `(2003-2011)`) plus a `Notable Accomplishments` restatement of the 8 accomplishment rows. Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump (#753)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-753-wentai-liu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-753-wentai-liu/](https://taiwaneseamericanhistory.org/whos-who-753-wentai-liu/)
- **Title:** `753. Prof. Wentai Liu 劉文泰教授` · **published:** 2016-01-09 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 23939) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-753-wentai-liu|TAH #753]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place, Address, Family, Education, Employment, Accomplishment, blank Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Capture 3 — Outstanding T.A. entry dump (#280)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/ota-280.md`
- **Original:** [https://taiwaneseamericanhistory.org/ota-280/](https://taiwaneseamericanhistory.org/ota-280/)
- **Title:** `280. Prof. Wentai Liu 劉文泰教授` · **published:** 2019-04-22 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 56165) · vault work record: [[works/taiwaneseamericanhistory-org/ota-280|TAH #280]], `value_band: B`
- The dump body carries **no** new biographical prose: the rendered fields are all `-` placeholders plus site nav chrome, and the only content beyond the title is the taxonomy label `Scholar`, the date `04/22/2019`, and the cross-reference heading `#753. The Bio Information of Prof. Wentai Liu 劉文泰教授`. The 04/2019 `Outstanding Taiwanese American` election asserted in Capture 1's accomplishment row 8 is therefore the same TAH editorial act this dump timestamps 2019-04-22 — same publisher, same record family, **not** corroboration.
- Sibling roster: `knowledge/web-archives/taiwaneseamericanhistory-org/pages/ota.md` line 30 lists `- 280. Prof. Wentai Liu 劉文泰教授` in the Outstanding T.A. index — bibliography-only listing, no new fact.

## Harvest provenance
- All three captures come from the `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`.

## Twin & cross-check (2026-11-14)
Whole-vault sweep this pass — single-pattern grep per name form (`劉文泰`, `Wentai`, case-insensitive `wentai`), controls counted:
`劉文泰` → 4 files in `content/` (own page, own 2 work pages, source hub), 15 in `knowledge/`; `Wentai`/`wentai` → same 4 in `content/`, 26 in `knowledge/`.
Every non-index hit is one of: his own three TAH captures (`person/prof-wentai-liu.json`, `posts/whos-who-753-wentai-liu.md`, `posts/ota-280.md`), the Outstanding-T.A. index page `pages/ota.md`, the two vault work pages, the [[sources/taiwaneseamericanhistory-org|source hub]], or crawler/analysis indexes (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `scout/*.jsonl`, `incidents/2026-09-1x.md`, `tahots-merge.jsonl`, `work-linker-state.jsonl`, `tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`, `posts/index.jsonl`, floor findings). Machine indexes checked for content-bearing mentions and found to carry only title/index rows (`content-analysis` rows are lint records for this very page; the lexicon/family/title hits are name-index entries, not prose).
**No memoir (《Our Journeys》 / My Stories `mystoriesNNN`), taiwandaily/TJJ article, church, org, or event record names him.** The 2016-01-09 #753 post date is the closest thing the corpus carries to a "first recorded" timestamp.

**Twin / containment check (2026-11-14):** Capture 1 `page_text` (4,611-byte JSON) is a superset of Capture 2 (1,474-byte dump): the dump's form fields appear verbatim inside the profile page text, and Capture 1 additionally carries the site chrome, the `Last updated: June 19, 2026` line, the 7-term profession taxonomy class list, the footer summary block, and the `modified` timestamp. Capture 3 is a third rendering of the same editable payload with its fields blanked. The form fields shared across the three artifacts are one self-reported payload, so shared fields are **not** corroboration; each artifact contributes only its own metadata (post dates 2016-01-09 / 2019-04-22, `modified` 2026-06-19, taxonomy terms, `family_filled: false`, blank Publication/Hobby).

## What this capture does NOT establish
- No year of U.S. arrival and no first city/state (`-/-/-` on the record), and no dates for the NCTU/NTU degrees or for the start of the UCLA/UCSC careers beyond the printed ranges.
- Whether the `2011-` UCLA affiliation is current is not stated (`modified` 2026-06-19 is an edit timestamp, not a career date).
- No spouse, daughter, or son names (fields present, blank; `family_filled: false`).
- No independent verification of the **Artificial Retina / Father of Bionic Eye** attribution, the **IEEE Fellow 2016** election, or the **Popular Mechanics Breakthrough Award 2010** — all three come from this one editable self-report; no IEEE-, journal-, or award-side record is archived on this box.
- The `National Science Society (NSF)` vs footer `National Science Foundation (NSF)` restatement of the same row inside one capture is unresolved (one editable publisher, two renderings).

## Related
- [[people/prof-wentai-liu|Prof. Wentai Liu 劉文泰教授]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-753-wentai-liu|753. Prof. Wentai Liu 劉文泰教授]] — vault work record
- [[works/taiwaneseamericanhistory-org/ota-280|280. Prof. Wentai Liu 劉文泰教授]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher

---
title: "TAH Who's Who profile capture — 2224. Jennifer Rorie Cheng"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 2224. Jennifer Rorie Cheng

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1153
- wikilinks: 8


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names her (see Twin & cross-check below).

## Subject
- [[people/jennifer-rorie-cheng|Jennifer Rorie Cheng]] — TAH Who's Who record #2224

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/jennifer-rorie-cheng.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/jennifer-rorie-cheng/](https://taiwaneseamericanhistory.org/person/jennifer-rorie-cheng/)
- **Record id:** 74718 · **type:** `tah_person` · **profession taxonomy:** `physician` (`person_profession-physician` in `class_list`; numeric term id `person_profession: [2234]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form)
- **`modified` on source:** 2026-06-02T17:25:00 · `page_bytes`: 50,824 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 2, 2026` line sit in the raw HTML, not the extracted text)
- **`content_html` is empty** (`""`) and `excerpt` is empty — the profile page carries no narrative prose; every biographical fact below comes from the structured form fields, not from a written bio.
- **Verbatim fields (self-reported):** English Name `Jennifer Rorie Cheng` · Hanji Name `--` · Birth Year `1971` · Birth Place `--`
- **U.S. arrival:** `-/-/-` — first year, first city and state unfilled on the record
- **Address:** `--` — unfilled
- **Family:** `1. Husband: Hsinlin Cheng` · `2. Daughter: --` · `3. Son: --`. JSON parses this as `family: [{rel: "husband", name: "Hsinlin Cheng"}]`, `family_filled: true`. The two children fields are present and blank — a recorded gap, not proof of no children.
- **Education (1 row, no year range):** `1. Univ. of Michigan` — `2004` — degree/major `-` (blank)
- **Employment (1 row, no year range):** `1. Massachusetts General` — `--` — `Nurse Practitioner Specialist`
- **Accomplishment / Publication / Hobby:** all `--` — unfilled. The three unfilled fields are themselves the record: no publication, award, or hobby fact is being withheld elsewhere on this capture.
- **Footer summary block (same page, rendered below the form):** Birth Year `1971` · Education `University of Michigan (2004)` · Position `Massachusetts General — Nurse Practitioner Specialist`. Restatement within one capture is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on abby-hong), this record carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2224-jennifer-rorie-cheng.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2224-jennifer-rorie-cheng/](https://taiwaneseamericanhistory.org/whos-who-2224-jennifer-rorie-cheng/)
- **Title:** `2224. Jennifer Rorie Cheng` · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2224-jennifer-rorie-cheng|TAH #2224]], `value_band: B`, `license: all-rights`, record dated **2019-11-06 (published)**
- The dump reproduces the Capture 1 form fields verbatim (English/Hanji Name, Birth Year, Birth Place, `-/-/-` arrival, Address, Family incl. blank Daughter/Son, the single Education row `Univ. of Michigan / 2004 / –`, the single Employment row `Massachusetts General / – / Nurse Practitioner Specialist`, blank Accomplishment/Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Spouse cross-record — the one cross-field corroboration on this box
- Husband's own TAH record #2223 ([[people/dr-hsinlin-cheng|Dr. Hsinlin Cheng 鄭新霖醫師]]), captures `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-hsinlin-cheng.json` (id 74717, `modified` 2026-06-19T17:03:11) and `…/posts/whos-who-2223-hsinlin-cheng.md`, published **2019-11-06** — the same publication date as #2224.
- His Family field names his wife **`Jennifer Rosie Cheng`** — note the spelling drift: **`Rosie`** on #2223 vs **`Rorie`** on #2224 and on both of her own captures. Same publisher, two editable records. The marriage pairing (his record lists her, her record lists him, entries are adjacent, published the same day) is the corroborated fact; the given-name spelling is not settled by it.
- #2223 also carries shared-institution context his record alone states: both spouses attended **Univ. of Michigan** (his Ph.D., M.D.; her 2004 row) and both are at **Massachusetts General** (he: Director of H and N Pain Unit, Dept. Neurology, and Harvard Medical School – MGH Assistant Professor of Neurology). Context from his self-report, not hers — labeled on her page as `inferred` (two records agreeing), never as her own `sourced` fact.
- Full-field transcription of the spouse record: [[sources/tah-whoswho-dr-hsinlin-cheng-capture|capture #2223]].

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- The profile JSON's `modified` (2026-06-02T17:25:00) and the in-page `Last updated: June 2, 2026` line agree — the record was last edited by the publisher before our harvest; the encyclopedia dump carries no separate edit stamp.

## Twin & cross-check (2026-11-13)
- **Twin check between the two captures** (frontmatter stripped, `#`/whitespace normalized, per the lane convention): Capture 2 normalized body md5 `7c71d7fc42d5772adda78f79c6ccbf6e`, 429 chars. Capture 1's `content_html` is empty so no bio-text twin test is possible on the prose side; its `page_text` is the site-rendered superset (nav chrome + footer block + the same form fields), and the dump's normalized body is **not** a substring of it (dash-character divergence `–` vs `-`), so they are two serializations of the same self-reported payload, each richer in a different layer (JSON: `modified`, taxonomy ids, parsed `family`; dump: clean form layout). Agreement across two serializations of one editable self-report is **not corroboration** — that is what keeps every field below at `alleged`.
- **Whole-corpus sweep this pass** — single-pattern `grep -rlF` / `grep -rli` per name form, controls counted (`Massachusetts General` = 8 files under `content/people`, non-vacuous): `Jennifer Rorie Cheng` → 6 files in `content/` + machine indexes in `knowledge/`; `Rorie` (case-insensitive) → same set plus deepen-x slice logs; `Jennifer Rosie Cheng` → 2 files (`people/dr-hsinlin-cheng.md`, `sources/tah-whoswho-dr-hsinlin-cheng-capture.md`) plus the #2223 captures; `Hsinlin` / `鄭新霖` → 6 files in `content/`, all spouse-derived. Every non-index hit is one of: her own two captures/work record, her person page, `people/index.md`, the `sources/taiwaneseamericanhistory-org.md` name index, the spouse page #2223 and its capture page. Machine indexes (`units.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, deepen-x slice files, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`) are not sources.
- **PDF near-miss checked and excluded:** the only other `Jennifer` hit inside `knowledge/web-archives` that could plausibly be a community photo caption is `2023-tahs-publication-p066-130.pdf` — its pages name **`Jennifer Chow`** (with 楊小娜, 鄭炳全, 秦雪華), a different Jennifer; not our subject, excluded.

## GAPS / NEED YOU — sources checked, nothing third-party found
Checked on this box 2026-11-13: whole `content/` + `knowledge/` sweeps for `Jennifer Rorie Cheng`, `Rorie`, `Jennifer Rosie Cheng`, `Hsinlin`, `鄭新霖` (hit sets above); `content/articles/**` (0 `Rorie` hits); the TAH story corpus work records #2224/#2223; the two `knowledge/web-archives/taiwaneseamericanhistory-org/` capture pairs; both TAH publication PDFs + their md mirrors; `Nurse Practitioner` corpus-wide (sole hit: her own page).
Not yet checked (outside this lane): **zh.wikipedia / en.wikipedia / Wikidata** (WEB-PASS lane), and the live MGH provider directory (an official-site arm; not archived on this box).

## Related
- [[people/jennifer-rorie-cheng|Jennifer Rorie Cheng]] — subject of this capture
- [[people/dr-hsinlin-cheng|Dr. Hsinlin Cheng 鄭新霖醫師]] — spouse, TAH #2223
- [[organizations/tah-foundation|TAH Foundation]] — publisher of the Who's Who program
- [[sources/tah-whoswho-dr-hsinlin-cheng-capture|TAH Who's Who capture #2223 (spouse)]]

---
title: "TAH Who's Who profile capture — 750. Shoei-Sheng Chen 陳水生"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 750. Shoei-Sheng Chen 陳水生

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 863
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community
record elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/shoei-sheng-chen|Shoei-Sheng Chen 陳水生]] — TAH Who's Who record #750

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/shoei-sheng-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/shoei-sheng-chen/](https://taiwaneseamericanhistory.org/person/shoei-sheng-chen/)
- **Record id:** 73317 · **type:** `tah_person`
- **Profession taxonomy:** `civil engineer`, `engineer`, `mechanical engineer`, `professor`, `researcher` (`person_profession-*` slugs in `class_list`; numeric term ids `person_profession: [2238, 2227, 2229, 2237, 1813]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note: the person-page sidecar keeps only `roles: [engineer, professor]` — the civil/mechanical/researcher tags were dropped by the sidecar and are recovered here.
- **`modified` on source:** 2026-06-19T16:37:58 · `page_bytes`: 54,479 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the rendered page block)
- **Verbatim fields (self-reported):** Name `陳水生教授` / `Dr. Shoei-Sheng Chen` · Birth Year `1940` · Birth Place `台灣宜蘭東山鄉`
- **U.S. arrival:** blank (`First year, first city and state arrived in the U.S.` — no value)
- **Address:** `-/CA` — the footer block restates it as `Residence: CA`
- **Family:** `1. Wife: —` · `2. Son: —` · `3. Daughter: —` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (2 rows):** `1 National Taiwan University` — `1963` — `B.S. Engineering` · `2. University of Princeton` — `1968-` — `Ph.D. Engineering` (open-ended year; completion year not stated)
- **Employment (1 row, no year range):** `Argonne National Laboratory in Darien, Illinois.` — `civil and mechanical engineer`
- **Accomplishment (2 items, footer-repeated):** `1. Received a distinguished performance award from the University of Chicago, 1986` · `2. Received a medal from the American Society of Mechanical Engineers, 2001`
- **Publication (Non-professional ones):** `Flow-Induced Vibration of Circular Cylindrical Structures, 1987`
- **Hobby / Website or Blog:** `--` — unfilled
- **`content_html` and `excerpt` are empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** Hanzi `陳水生` · Birth Year `1940` · Birthplace `台灣宜蘭東山鄉` · Residence `CA` · the same Education, Employment and honors restated (`Published: Flow-Induced Vibration of Circular Cylindrical Structures, 1987`). Restatement within one capture is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on abby-hong), this record carries no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/750-shoei-sheng-chen-%e9%99%b3%e6%b0%b4%e7%94%9f-201512.md`
- **Original:** [https://taiwaneseamericanhistory.org/750-shoei-sheng-chen-%e9%99%b3%e6%b0%b4%e7%94%9f-201512/](https://taiwaneseamericanhistory.org/750-shoei-sheng-chen-%e9%99%b3%e6%b0%b4%e7%94%9f-201512/)
- **Title:** `750. Shoei-Sheng Chen 陳水生 / 2015/12` · vault work record: [[works/taiwaneseamericanhistory-org/750-shoei-sheng-chen-e9-99-b3-e6-b0-b4-e7-94-9f-201512|TAH #750]], `value_band: B`, published 2015-12-27
- The dump reproduces the Capture 1 form fields verbatim (Name through Publication/Hobby/Website). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
Normalization (frontmatter stripped, all `#`/whitespace removed) before hashing:
- profile `page_text` normalized: md5 `d105197f628e21f9c15c64e1609b4d3d`, 1,801 chars
- post dump normalized: md5 `061733ded84dd8c967346cc666123870`, 727 chars
- Containment test: neither is a substring of the other (the profile JSON is the **richer** artifact — it carries the rendered footer/honors block and the `Last updated: June 19, 2026` stamp that the post dump omits; the post dump adds nothing beyond the same form fields).
Agreement across two serializations of one editable self-report is **not** corroboration — which is why the record's own `Accomplishment` / `Publication` items stay labeled `alleged` on the person page.

## Harvest provenance
Both captures come from the `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`.

## Twin & cross-check (2026-11-14)
Whole-vault sweep this pass — `grep -rlF 'Shoei-Sheng Chen'` and `grep -rlF '陳水生'` over `content/` + `knowledge/` (controls non-vacuous: earlier same-day sibling passes confirm the grep method returns hits). Hits are only: his own two TAH captures above, the [[works/taiwaneseamericanhistory-org/750-shoei-sheng-chen-e9-99-b3-e6-b0-b4-e7-94-9f-201512|TAH #750 work page]], `people/shoei-sheng-chen.md`, the `sources/taiwaneseamericanhistory-org.md` hub, and machine indexes (`units.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `posts/index.jsonl`, `taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`, `tdm-page-title-index.json`) — indexes are not sources.
Institution sweeps (`Argonne`, `d105197f` aside): grep for `Argonne` in `content/` returns no community article naming him. No taiwandaily/TJJ article, memoir (《Our Journeys》/My Stories), or org record names him.

## What this capture does NOT establish
- No year or city of U.S. arrival (field present, blank).
- No year range on the Argonne employment row; whether the role is current or past is not stated.
- No completion year for the Princeton Ph.D. (`1987-`-style open field: `1968-`).
- No wife/children names (fields present, blank), no family record.
- The 1986 University of Chicago award and 2001 ASME medal are self-reported and footer-repeated only — no third-party program/roster record is archived on this box.
- `Flow-Induced Vibration of Circular Cylindrical Structures` (1987) is listed under "Publication (Non-professional ones)" with no publisher; the Cambridge-series attribution is not on the record and was **not** invented here.

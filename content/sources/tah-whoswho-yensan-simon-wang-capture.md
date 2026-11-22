---
title: "TAH Who's Who profile capture — 1132. Yensan (Simon) Wang 王燕山"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1132. Yensan (Simon) Wang 王燕山

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1061
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

Subject died 2006 (per his own record's birth/death fields), so any record after 2006
would have to be third-party; none exists on this box.

## Subject
- [[people/yensan-simon-wang|Yensan (Simon) Wang 王燕山]] — TAH Who's Who record #1132

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yensan-simon-wang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yensan-simon-wang/](https://taiwaneseamericanhistory.org/person/yensan-simon-wang/)
- **Record id:** 73683 · **type:** `tah_person` · **profession taxonomy:** `architect` (`person_profession-architect` in `class_list`; `person_profession: [402]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form)
- **`modified` on source:** 2026-06-19T16:44:38 · `page_bytes`: 52,194 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text)
- **Verbatim fields (self-reported):** Name `王燕山` / `Yensan (Simon) Wang` · Birth Year `1945-2006` · Birth Place `台灣新竹`
- **U.S. arrival:** `1972/New York/NY` — first year, first city and state
- **Address:** `El Monte/CA` — the footer block restates it as `Residence: El Monte, CA`
- **Family (filled):** `1. Wife: 王傅美伶` · `2. Daughter: 王潔伶` · `3. Son: Jeff王傑俐` — JSON parses to `family: [wife 王傅美伶, daughter 王潔伶, son Jeff王傑俐]`, `family_filled: true`
- **Education (2 rows, no year ranges):** `1. 東海大學` — `B.S.建築` · `2. Syracuse大學` — `M.S.建築`
- **Employment:** `Architect` (single role row, no employer, no year range)
- **Accomplishment / Publication(Non-professional ones) / Hobby:** `–` — unfilled
- **Website or Blog:** `–` — unfilled; no self-published web arm exists to chase
- **Provenance line:** `Source from:www. Taiwandaily.net` · `Post in 07/2016` — the record declares an upstream publication attribution to 台灣日報 (Taiwandaily), submitted/posted 2016-07. The upstream article itself is **not archived on this box** (see cross-check), so the attribution is printed but unverifiable here.
- **Footer summary block (same page, rendered below the form):** Hanzi `王燕山` · Birth Year `1945` · Birthplace `台灣新竹` · Residence `El Monte, CA` · Passed Away `2006` · Education (東海大學 B.S. 建築 / Syracuse University M.S. 建築) · Position `Architect`. Restatement within one capture is not corroboration.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1132.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1132/](https://taiwaneseamericanhistory.org/whoswho1132/)
- **Title:** `1132. Yensan (Simon) Wang 王燕山 / 2016/07` · **published:** 2016-07-10 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 31416) · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1132|TAH #1132]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year `1945-2006`, Birth Place, arrival `1972/New York/NY`, Address `El Monte/CA`, Family, Education, Employment, blank Accomplishment/Publication/Hobby, `Source from:www. Taiwandaily.net`, `Post in 07/2016`).

## Twin check (2026-11-14)
Run on the profile page's **content block** (`page_text` sliced from `Who's Who Taiwanese American Profile` to the `Travel the roads paved…` footer line), not the raw page_text — per the theodore-ted-wing rule, raw page_text carries ~1 KB of site chrome that breaks both containment directions.
- Profile content block: normalized 575 chars, md5 `b5ef615428fd8cf967b3312ffdd33bbe`
- Post dump: normalized 460 chars, md5 `142df79756e1bfa137ed6294e4939953` (frontmatter stripped; normalization strips `#` and all whitespace)
- md5 differ; containment neither direction. The delta is field **labels/chrome**, not facts: the profile block adds the site heading, `Last updated: June 19, 2026`, the `architect` tag line and the footer summary block; the dump adds its own H1 numbering line.
- Per-field presence diff: every fact field (Birth Year, Birth Place, arrival, Address, the three family names, both Education rows, Architect, `Source from…Taiwandaily.net`, `Post in 07/2016`) is present in **both** serializations.
- Ruling: two serializations of **one editable self-report**, not two independent records. This is why the record's own `Source from www.Taiwandaily.net` print attribution stays `alleged` here — restatement ≠ corroboration.

## Number-collision ruling (2026-11-14)
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications1132.md` shares the subject's number but is `1132. Cosplay in America V2 / Ejen Chuang / 2015/Art/藝術` — a Publications post with zero biographical fields about him (all form fields render `-`). Per the jyh-fa-kuo rule, read the H1 before counting a same-number artifact as a sibling source: **not** a source for this subject. Recorded here so future passes do not re-open it.

## Harvest provenance
Both captures come from the `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`.

## Twin & cross-check sweep (2026-11-14)
Whole-corpus sweeps this pass (single-pattern `-F` per name form over `content/` + `knowledge/`; non-vacuous controls: `Architect` matches broadly across the corpus, so the zero results below are instrument-checked, and prior deepen-x slices 09232337-2 / 09251054-1 / 09261405-22 / 10070714-5 all re-grepped ZH+EN with the same result):
- `王燕山`: only his own person page, the [[works/taiwaneseamericanhistory-org/whoswho1132|TAH #1132 work page]], the `sources/taiwaneseamericanhistory-org.md` hub, machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `tdm-page-title-index.json` — a title→page index over vault pages, i.e. his own pages echoed back, not a source), the two crawl artifacts above, and the disambiguation note on [[people/wang-yao-ting|王耀廷]] (#1133, adjacent number, different person — the page already warns 王燕山 ≠ 王耀廷).
- `Yensan` (EN, case-insensitive): same file set, plus the deepen-x slice lists that target this page.
- `王傅美伶` / `王潔伶` / `王傑俐` (family names): hit list is **only this person's own page** — no family member is named anywhere else in the corpus, so no memoir/obituary path exists on this box.
- 台灣日報 corpus (`knowledge/web-archives/taiwandaily-net/`, ~thousands of archived articles): `grep -rlF '王燕山'` → **0 files**. The record's printed `Source from www.Taiwandaily.net` upstream article is not in the archived slice on this box.
- TDM index (`tdm-page-title-index.json`): only title forms pointing at his own pages.
- No memoir (My Stories / 《Our Journeys》), org record, or event roster names him. Machine indexes are not sources.

## What this capture does NOT establish
- No named employer or firm for the `Architect` role; no employment years.
- No years for either degree (東海大學, Syracuse).
- No accomplishments, publications, or hobbies (fields present, blank `–`).
- The upstream 台灣日報 article behind `Source from:www. Taiwandaily.net` is not on this box — the print attribution is printed but unverifiable locally, hence `alleged` on the person page.
- All names/dates above are self-reported (subject died 2006; the record was submitted/posted 2016-07, likely by family or the foundation, but the submitter is not identified on the record).

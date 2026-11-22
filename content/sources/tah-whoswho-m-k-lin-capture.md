---
title: "TAH Who's Who profile capture — 1538. M. K. Lin 林明昆"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1538. M. K. Lin 林明昆

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two artifacts. Preserved because the biographical fields are
self-reported and the live site is editable. This capture is **not** the only source on
this box for this person: a 2017-02-09 filial memoir by his son 林榮松 names him in full —
see `## Independent record` below.

## Subject
- [[people/m-k-lin|M. K. Lin 林明昆醫師]] — TAH Who's Who record #1538

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/m-k-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/m-k-lin/](https://taiwaneseamericanhistory.org/person/m-k-lin/)
- **Record id:** 74067 · **type:** `tah_person` · **profession taxonomy:** `calligrapher`, `physician` (`person_profession-calligrapher` / `person_profession-physician` in `class_list`; numeric term ids `person_profession: [2268, 2234]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the profile taxonomy carries **`calligrapher`** where the person page's Identity Snapshot listed `physician` only — the class list is the fuller self-reported role set.
- **`modified` on source:** 2026-06-19T16:51:29 · `page_bytes`: 51,836 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `林明昆醫師` / `M. K. Lin` · Birth Year `1918-2017` · Birth Place `台灣高雄`
- **U.S. arrival:** `1979/-/-` (first year / first city / first state) — the person page carried **none** of these three fields before this capture was opened.
- **Address:** `San Diego/CA` — the footer block restates it as `Residence: San Diego, CA`
- **Family:** `1. Wife:許金英` · `2.Son:Simon林榮松` · `3.Daughter:April林素卿` — JSON parses this as `family: [{wife: 許金英}, {son: Simon林榮松}, {daughter: April林素卿}]`, `family_filled: true`. The form gives the children English given names + Chinese surnames only; full Chinese names are not stated.
- **Education:** `1.台北帝國大學附屬醫院專門部` `-` `B.S.` (one row; the year range is unfilled on the form)
- **Employment:** `1.開設杏林婦產科` `-` `-` (one row; no dates, no location)
- **Accomplishment:** `--` — unfilled.
- **Publication (Non-professional ones):** `--` — unfilled.
- **Hobby:** `書法,栽培蘭花` — the person page carried no Hobby field before this capture.
- **Website or Blog:** `--` — unfilled.
- **Footer block (restates the form):** `Dr. M. K. Lin` · Hanzi `林明昆醫師` · Birth Year `1918` · Birthplace `台灣高雄` · Residence `San Diego, CA` · Passed Away `2017` · Education `台北帝國大學附屬醫院專門部 B.S.` · Position `杏林婦產科 開設 (Founder/Physician)`. Restatement within one editable record is not corroboration; the `Founder/Physician` gloss is site template text, not the subject's words.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on other profiles), this record carries no upstream-source attribution.

## Capture 2 — form-field dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1538.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1538/](https://taiwaneseamericanhistory.org/whoswho1538/)
- **Title:** `1538. M. K. Lin 林明昆 / 2017/02` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1538|TAH #1538]]
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year, Birth Place, arrival, Address, Family, Education, Employment, Accomplishment `--`, Publication `--`, Hobby, Website `--`). It is a second rendering of the same self-reported payload, not an independent source.
- **Twin check** (run 2026-11-14, in-process, frontmatter stripped + `#`/whitespace normalized): profile `page_text` = 1,162 normalized chars, md5 `3c29855d7ab665bcd87466640a348af2`; dump body = 314 normalized chars, md5 `adbfdd9daa17cbe6c41de4cd6f8606ae`. Neither contains the other — the difference is **not** biographical: the dump drops the site chrome and the site-generated footer block (`Passed Away 2017`, the `Dr. M. K. Lin` English block) that survive only in the JSON's `page_text`. The JSON is the richer serialization; both are two serializations of **one** editable self-report and do not corroborate each other.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug does **not** appear in that manifest's `weak.person` list, i.e. the harvest grader did not mark this profile's payload thin at fetch time.

## Independent record (the reason this capture is not the sole source)
- [[works/taiwaneseamericanhistory-org/mystories515|515. 父親完整地走完了他的一生 / 林榮松 / 02/2017]] — a filial memoir written and bylined by his son 林榮松 (Simon Lin, the novelist), published 2017-02-09. Raw dump: `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories515.md`; original: [https://taiwaneseamericanhistory.org/mystories515/](https://taiwaneseamericanhistory.org/mystories515/). It names 林明昆 by full name, gives an exact birth date (1918-12-17 / 大正七年), a village-level birthplace (高雄州岡山郡湖內庄頂茄萣), parents' names (祖父林騫, 祖母林蔡鴦), the school sequence (成功小學 → 台南州立第二中學校 → 台北帝國大學附屬醫學專門部), the 1946-03-01 Hainan marriage to the 田獨礦山病院 nurse 許金英, the 228-era 茄萣漁會診所 post, the 1953 鹽埕 move, the 1954 founding of 杏林婦產科, the 1979 retirement and U.S. immigration, the 2000 wife's death, the 2010 dialysis start, and the 2017-01-14 death in San Diego.
  - **Upstream provenance of that memoir:** the dump's footer prints `Source from Taiwan Daily 美洲台灣日報` and `Posted in 02/2017` — i.e. this TAH story post restates a Taiwan Daily publication. It is family-written (a son about his father), so it is treated here as a **family record**, not an independent press record: see the person page's `## Source Notes` for the label policy.
  - **Identity tie:** Hanzi 林明昆 + 高雄 origin + 台北帝大醫專 + 杏林婦產科 + wife 許金英 + children Simon林榮松 / April林素卿 + San Diego residence + 2017 death all agree between the two records. No conflict found.
  - **One divergence, noted not merged:** the Who's Who form says Education `台北帝國大學附屬醫院專門部`; the memoir says `台北帝國大學附屬醫學專門部`. Held as the same institution with the form-field name form preserved on the person page.

## What this capture does NOT establish
- Any date for the 台北帝大 study years (form row is `--`).
- Founding date or address of 杏林婦產科 (form row is `--`); the 1954 date comes only from the family memoir.
- Whether `calligrapher` is a formal role (club membership, exhibition) or a self-tag — the only evidence is the site taxonomy plus the `Hobby: 書法,栽培蘭花` field and the memoir's `書法寫得很好`.
- Full Chinese names of the children (`Simon林榮松` / `April林素卿` are English-given-name forms; the memoir bylines the son as 林榮松).
- The memoir's upstream Taiwan Daily article itself is **not archived on this box** (see `## Online arms` on the person page).

## Related
- [[people/m-k-lin|M. K. Lin 林明昆醫師]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whoswho1538|1538. M. K. Lin 林明昆 / 2017/02]] — vault work record of the profile
- [[works/taiwaneseamericanhistory-org/mystories515|515. 父親完整地走完了他的一生]] — son's memoir, 2017-02-09
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[sources/taiwaneseamericanhistory-org-story-corpus|TAH story corpus hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher

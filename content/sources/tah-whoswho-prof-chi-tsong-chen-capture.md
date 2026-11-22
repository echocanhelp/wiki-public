---
title: "TAH Who's Who profile capture — 2173. Prof. Chi-Tsong Chen 陳啓宗教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2173. Prof. Chi-Tsong Chen 陳啓宗教授

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two serializations. Preserved because the biographical fields are
self-reported and the live site is editable. This capture is **not** the only source on
this box for this person: a 2018-01-18 first-person memoir by a former Stony Brook
classmate names him and independently attributes two textbooks to him — see
`## Independent record` below.

## Subject
- [[people/prof-chi-tsong-chen|Prof. Chi-Tsong Chen 陳啓宗教授]] — TAH Who's Who record #2173

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-chi-tsong-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-chi-tsong-chen/](https://taiwaneseamericanhistory.org/person/prof-chi-tsong-chen/)
- **Record id:** 74664 · **type:** `tah_person` · **profession taxonomy:** `author`, `educator`, `electrical engineer`, `engineer`, `professor`, `researcher` (`person_profession-*` slugs in `class_list`; numeric term ids `person_profession: [2231, 2248, 323, 2227, 2237, 1813]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the profile taxonomy carries **six** roles where the person page's Identity Snapshot listed `engineer, professor, educator` only — `author`, `electrical engineer` and `researcher` exist only in the site class list.
- **`modified` on source:** 2026-06-19T17:02:17 · `page_bytes`: 56,479 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **`content_html`:** `""` and **`excerpt`:** `""` — the profile carries no free-text bio; every biographical fact is in form fields.
- **Verbatim fields (self-reported):** Name `Prof. Chi-Tsong Chen` / `陳啓宗教授` · Birth Year `1936` · Birth Place `Kaohsiung, Taiwan`
- **U.S. arrival:** `1962/New York/NY` (first year / first city / first state) — the person page carried **none** of these three fields before this capture was opened.
- **Address:** `NY` — the footer block restates it as `Residence: NY`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — JSON parses this as `family: []`, `family_filled: false`. Consistent with the person page's `_No filled family fields on the TAH profile._`
- **Education (3 rows, self-reported):** `1. National Taiwan Univ.` `1954-1958` `B.S., Mechanical Engineering` · `2. Hsinchu Chaio Tong Univ.` `1958-1960` `M.S., Electrical Engineering` (form misspelling of 新竹交通大學 / Chiao Tung) · `3. Univ. of California, Berkeley` `1962-1966` `Ph.D., Electrical Engineering`
- **Employment (1 company, 3 rank rows, self-reported):** `1. Stony Brook Univ./SUNY` — `1966-1969` `Assistant Professor` · `1969-1974` `Associate Professor` · `1974-2011` `Professor`
- **Accomplishment:** `1. Published four textbooks. One of them has been a standard in the field since 1970.`
- **Publication (Non-professional):** `1. A free book entitled "Signals and Systems: A Fresh Look" (2011), can be downloaded from my website ctchen.me.`
- **Hobby:** `--` — unfilled.
- **Footer block (restates the form):** `Prof. Chi-Tsong Chen` · Hanzi `陳啓宗教授` · Birth Year `1936` · Birthplace `Kaohsiung, Taiwan` · Residence `NY` · the three Education rows · the three Position rows. Restatement within one editable record is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on other profiles), this record carries no upstream-source attribution.
- **Note on the Berkeley row:** the form gives `1962-1966` for the Ph.D. while the same form gives U.S. arrival `1962` — internally consistent; the M.S. (1958-1960) therefore predates the stated arrival year, which the subject left unexplained. Held as reported, not corrected.

## Capture 2 — form-field dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2173-chi-tsong-chen.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2173-chi-tsong-chen/](https://taiwaneseamericanhistory.org/whos-who-2173-chi-tsong-chen/)
- **Title:** `2173. Prof. Chi-Tsong Chen 陳啓宗教授` · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2173-chi-tsong-chen|TAH #2173]]
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year, Birth Place, arrival, Address, Family `--`, Education, Employment, Accomplishment, Publication, Hobby `—`). It is a second rendering of the same self-reported payload, not an independent source.
- **Twin check** (run 2026-11-14, in-process, frontmatter stripped + `#`/whitespace normalized): profile `page_text` = 2,139 normalized chars, md5 `3ccc25908cced7581bcfa83d6f4a7165`; dump body = 770 normalized chars, md5 `64ab238d2db01a324973b77454e137a3`. Containment test run both ways: neither string contains the other — the difference is **not** biographical: the dump drops the site chrome and the site-generated footer block (the `Prof. Chi-Tsong Chen` English restatement block, the mission/footer boilerplate) that survive only in the JSON's `page_text`. The JSON is the richer serialization; both are two serializations of **one** editable self-report and do not corroborate each other.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, `counts`/`expected`: 2,212 person / 339 org).
- This slug **does** appear in that manifest's `weak.person` list (`prof-chi-tsong-chen`), i.e. the harvest grader already flagged this profile's payload as thin at fetch time — consistent with the empty `content_html` / `excerpt` above. The payload is form fields only; nothing was lost in extraction.

## Independent record (the reason this capture is not the sole source)
- [[works/taiwaneseamericanhistory-org/mystories619|619. 那些年，我們一起留學美國的日子 / 施永強 / 01/2018]] — a first-person memoir bylines 施永強 (Prof. Frank Shih), published 2018-01-18. Raw dump: `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories619.md`; original: [https://taiwaneseamericanhistory.org/mystories619/](https://taiwaneseamericanhistory.org/mystories619/). It names him 陳啟宗（Chi-Tsong Chen） and states he is at Stony Brook and 「著有暢銷書『信號與系統』Signals and Systems與『線性系統理論與設計』Linear System Theory and Design」.
  - **Independence:** the author is not the subject and did not edit the subject's profile. The author arrived at Stony Brook in **1983** as an M.S. student — i.e. *after* the subject's 1974 professorial promotion — so this is a junior-observer recollection, not a peer record.
  - **Identity tie:** Hanzi (陳啟宗 variant of 陳啓宗) + English name + Stony Brook ECE + authorship of *Signals and Systems* all agree between the two records. No conflict found.
  - **One divergence, noted not merged:** the memoir titles a book 「信號與系統」 *Signals and Systems*; the subject's own form lists *Signals and Systems: A Fresh Look* (2011) under non-professional publication and names no title under Accomplishment. Held as reported on both sides.

## What this capture does NOT establish
- Titles/publishers of the four textbooks — the form states the count, not the names.
- Whether 1962 arrival and the 1962-1966 Berkeley Ph.D. row are consistent (the form has him arriving the year the Ph.D. begins, while an M.S. is listed 1958-1960). Not reconcilable from this box.
- Any community, club, or diaspora activity — the profile records no organization, and the memoir only lists him as a faculty member.
- Whether he is the Hong Kong developer 陳啟宗 (Ronnie Chan, Harvard donation, 中美交流基金會) appearing in `knowledge/web-archives/taiwandaily-net-79716-79716.md` — **different person** (same Hanzi, different English name, occupation, and geography); recorded here so future passes do not merge them.

## Related
- [[people/prof-chi-tsong-chen|Prof. Chi-Tsong Chen 陳啓宗教授]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-2173-chi-tsong-chen|2173. Prof. Chi-Tsong Chen 陳啓宗教授]] — vault work record of the profile
- [[works/taiwaneseamericanhistory-org/mystories619|619. 那些年，我們一起留學美國的日子]] — 施永強 memoir, 2018-01-18
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[sources/taiwaneseamericanhistory-org-story-corpus|TAH story corpus hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher

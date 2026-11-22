---
title: "TAH Who's Who profile capture — 1593. Ming Jer Kuo 郭明哲"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1593. Ming Jer Kuo 郭明哲

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record
(record #1593), archived on this box as two serializations of one editable form — the crawled profile JSON and the
encyclopedia entry dump. Preserved because the biographical fields are self-reported and the live site is editable.

## Subject
- [[people/ming-jer-kuo|Ming Jer Kuo 郭明哲]] — TAH Who's Who record #1593

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ming-jer-kuo.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ming-jer-kuo/](https://taiwaneseamericanhistory.org/person/ming-jer-kuo/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 74118 · **type:** `tah_person` · **profession taxonomy:** `artist` (`person_profession-artist` in `class_list`; `person_profession: [2226]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form; the sidecar `roles` agree with `class_list` here, so no role is hidden in one serialization).
- **`modified` on source:** 2026-06-19T16:52:25 · `page_bytes`: 52,640 (raw HTML; the rendered page carries the `Last updated: June 19, 2026` line — per `page_text` in this capture).
- **Verbatim fields (self-reported):** Name `郭明哲 / Ming Jer Kuo` · Birth Year `1987` · Birth Place `台灣台北`
- **U.S. arrival:** `New York/NY` (the form's "First year, first city and state arrived in the U.S." is filled with city/state only — no year) · **Address:** `New York/NY`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — the three family rows exist as template labels with no values; the JSON parses this as `family: []`, `family_filled: false`. Recorded as an absence: no family names withheld, the form was submitted unfilled.
- **Education (1 filled row):** `School of Visual Arts` — `2014` — `MFA`
- **Employment (1 filled row):** `New York` — `–` — `Artist` (no date range on the form)
- **Accomplishment (2 filled rows, verbatim):** `1. received the Paula Rhodes Award for Exceptional Achievement, NYC ,2014` · `2. awarded Honorable Mention at the Taoyuan Creation Award in Taiwan,2011)` (the stray closing paren is verbatim from the form)
- **Publication(Non-professional ones):** `–` · **Hobby:** `–` · **Website or Blog:** `–` (absence evidence: no personal site declared on the form)
- **Provenance line:** `Source from Taiwanese American Arts Council` — the record attributes its content to the Taiwanese American Arts Council (TAAC); no submission date is printed on this record.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1593.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1593/](https://taiwaneseamericanhistory.org/whoswho1593/)
- **Title:** `1593.  Ming Jer Kuo 郭明哲 / 2017/03` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1593|TAH #1593]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year `1987`, Birth Place `台灣台北`, U.S. arrival/address `New York/NY`, the three unfilled Family rows, Education `School of Visual Arts / 2014 / MFA`, Employment `New York / – / Artist`, the two Accomplishment rows, `Publication –`, `Hobby –`, `Website or Blog –`, `Source from Taiwanese American Arts Council`). It is a second rendering of the same self-reported payload, not an independent source. The dump header `1593. ... / 2017/03` is the post's submission stamp; the vault work record dates the entry `2017-03-31`.

## Twin & cross-check (2026-11-14)
Containment/md5 test on the two serializations of the one form (frontmatter stripped, `#`/whitespace normalized):
JSON `content_html` = **empty** (0 normalized chars, md5 `d41d8cd98f00b204e9800998ecf8427e`) vs
`posts/whoswho1593.md` = 551 normalized chars (md5 `82b2f1714870f6f5eb20ae9f57b9e3cd`). Because the profile JSON's
free-text bio is empty, the **dump is the only narrative artifact**; the JSON's unique value is its metadata —
`modified` 2026-06-19T16:52:25, `page_bytes` 52,640, the `artist` profession taxonomy, and `family_filled: false`.
Agreement across two serializations of one editable self-report is NOT corroboration — that is what keeps the record's
own `Source from Taiwanese American Arts Council` submission line at `alleged`-grade provenance.

## Third-party namings on this box
One found: the TAAC 2016 Art Benefit GALA story — [[works/taiwaneseamericanhistory-org/projects3-52|52. Taiwanese American Arts Council (TAAC) 2016 Art Benefit GALA 台美文藝協會藝術盛宴]] (Flushing, Queens, 2016-09-22) lists `Ming-Jer Kuo 郭明哲` among the fourteen New York artists who contributed works for the fundraising exhibition. Per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/projects3-52.md`, whose footer reads `Source from 台灣海外網 09/2016` — a press reprint, i.e. one upstream record, not independent corroboration of the self-report. No other third-party naming exists on this box (see GAPS on the person page for the full grep list).

## Harvest provenance
Profile and posts captures are from the taiwaneseamericanhistory.org harvest recorded in
`knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`method: wp-json`).

## Related Pages
- Subject: [[people/ming-jer-kuo|Ming Jer Kuo 郭明哲]]
- Work record (self-report): [[works/taiwaneseamericanhistory-org/whoswho1593|TAH #1593 1593. Ming Jer Kuo 郭明哲 / 2017/03]]
- Work record (third-party naming): [[works/taiwaneseamericanhistory-org/projects3-52|TAAC 2016 Art Benefit GALA]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]]

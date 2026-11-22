---
title: "TAH Who's Who profile capture — 1322. Jyh – Fa Kuo 郭智化"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 1322. Jyh – Fa Kuo 郭智化

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record
(record #1322), archived on this box as two serializations of one editable form — the crawled profile JSON and the
encyclopedia entry dump — plus one sibling publication record that carries the same number. Preserved because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/jyh-fa-kuo|Jyh-Fa Kuo 郭智化]] — TAH Who's Who record #1322

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/jyh-fa-kuo.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/jyh-fa-kuo/](https://taiwaneseamericanhistory.org/person/jyh-fa-kuo/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 73863 · **type:** `tah_person` · **profession taxonomy:** `author`, `biochemist`, `physician`, `professor`, `researcher`, `scientist` (`person_profession-*` in `class_list`; numeric term ids `person_profession: [2231, 1639, 2234, 2237, 1813, 2235]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the crawled `sidecar.roles` kept only `scientist`, `physician`, `professor` — the roles `author` / `biochemist` / `researcher` survive only in `class_list`/`page_text`, which is why the taxonomy line here is richer than the page's Identity Snapshot.
- **`modified` on source:** 2026-06-19T16:47:54 · `page_bytes`: 55,761 (raw HTML; the `Last updated: June 19, 2026` line sits in the rendered page text)
- **Verbatim fields (self-reported):** Name `郭智化教授 / Professor Jyh – Fa Kuo` · Birth Year `1933` · Birth Place `台灣高雄`
- **U.S. arrival:** `1959/-/-` (first year 1959; first city and state blank) · **Address:** `Atlanta/IL`
- **Family:** `1. Wife: A lexandra W.H. Lou` · `2.Son: Calvin Kuo` · `3.Daughter: Frances Kuo` — JSON parses this as a filled `family` list (`family_filled: true`; the `A lexandra` stray space is verbatim from the form).
- **Education (4 rows):** `1. National Taiwan University` — `1957` — `B.S.` · `2. South Dakota State University` — `1961` — `M.S.` · `3. University of Illinois` — `1964` — `Ph.D. biochemistry` · `4. Linkoping University, Sweden` — `1980` — `M.D.`
- **Employment (1 filled row + 2 template placeholders):** `1. Yale and Emory University` — `present` — `Professor`; rows 2–3 remain unfilled site placeholders `Company name / year-year / Position` (absence evidence: the form was submitted with only one employment row).
- **Accomplishment:** `-` (unfilled) · **Publication(Non-professional ones):** `“Weeping Willow in the Mist”.` · **Hobby:** `-` · **Website or Blog:** `-`
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Provenance line:** `Source from北美洲台灣人醫師協會2016/10` (per `page_text` in the capture JSON and the dump below) — the record attributes its content to the North America Taiwanese Physicians Association (NATPA), submitted 2016/10.
- **Footer summary block (same page, rendered below the form):** `Notable Accomplishments — Author of "Weeping Willow in the Mist" Prof. Jyh-Fa Kuo`, then restates Hanzi `郭智化`, Birth Year `1933`, Birthplace `台灣高雄`, Residence `Atlanta, IL`, the four Education rows, and splits Position into two rows `Yale University — Professor` and `Emory University — Professor`. Restatement within one capture is not corroboration; the Yale/Emory split is the footer's own normalization of the single filled form row.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1322.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1322/](https://taiwaneseamericanhistory.org/whoswho1322/)
- **Title:** `1322. Jyh – Fa Kuo 郭智化 / 2016/10` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1322|TAH #1322]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year 1933, Birth Place, U.S. arrival `1959/-/-`, Address `Atlanta/IL`, Family, Education, Employment incl. the two unfilled placeholder rows, `Accomplishment –`, `Publication(Non-professional ones) “Weeping Willow in the Mist”.`, `Hobby –`, `Website or Blog –`, `Source from北美洲台灣人醫師協會2016/10`). It is a second rendering of the same self-reported payload, not an independent source.

## Sibling publication record (same number 1322, different post type)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publication1322.md`
- **Original:** [https://taiwaneseamericanhistory.org/publication1322/](https://taiwaneseamericanhistory.org/publication1322/)
- **Title:** `1322. Where the Mountain Meets the Moon/Grace Lin/2009` · `Posted on 09/2019`
- This is the site's Publications post #1322 — a bibliographic entry for Grace Lin's children's novel *Where the Mountain Meets the Moon* (2009), **not** this subject. TAH post numbers are per-post-type, so #1322 collides. Checked 2026-11-13: the body carries no biographical content about 郭智化 at all (all form fields render as `-`), so it yields no fact for this person. Recorded here so future passes do not re-open it as a candidate source.

## Twin & cross-check (2026-11-13)
Containment/md5 test on the two serializations of the one form (frontmatter stripped, `#`/whitespace normalized):
`posts/whoswho1322.md` = 600 normalized chars (md5 `dd8168fbabaab790d41df8f5865a7a37`) vs JSON `page_text` = 1,664
normalized chars (md5 `03d4a3b61c377f12584f99de6d3e17dc`). Neither is a substring of the other (the dump ends after the
`Source from…` line and omits the footer block; the JSON carries site chrome, the `Last updated: June 19, 2026` line,
the six-tag profession taxonomy, and the footer restatement block) — the JSON is the richer artifact. Agreement across
two serializations of one editable self-report is NOT corroboration — that is what keeps the record's own
`Source from 北美洲台灣人醫師協會 2016/10` submission line at `alleged`-grade provenance.

## Third-party namings on this box
None found. Whole-corpus + whole-`knowledge/` sweeps per name form (2026-11-13, this card) return only this subject's
own artifacts, machine indexes, and co-listing rosters — see GAPS on the person page for the full hit list.

## Harvest provenance
Profile and posts captures are from the taiwaneseamericanhistory.org harvest recorded in
`knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`method: wp-json`).

## Related Pages
- Subject: [[people/jyh-fa-kuo|Jyh-Fa Kuo 郭智化]]
- Work record: [[works/taiwaneseamericanhistory-org/whoswho1322|TAH #1322 1322. Jyh – Fa Kuo 郭智化 / 2016/10]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]]

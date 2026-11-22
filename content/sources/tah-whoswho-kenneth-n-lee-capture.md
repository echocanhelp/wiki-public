---
title: "TAH Who's Who profile capture — 1884. Kenneth N. Lee 李乃恭"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 1884. Kenneth N. Lee 李乃恭

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record
(record #1884, 09/2017), archived on this box as two serializations of one editable form — the crawled profile JSON
and the encyclopedia entry dump — plus two **third-party** community publications that name him. Preserved because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/kenneth-n-lee|Kenneth N. Lee 李乃恭]] — TAH Who's Who record #1884

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/kenneth-n-lee.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/kenneth-n-lee/](https://taiwaneseamericanhistory.org/person/kenneth-n-lee/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 74390 · **type:** `tah_person` · **profession taxonomy:** `dentist`, `educator`, `physician`, `professor`, `surgeon` (`person_profession-*` in `class_list`; numeric term ids `person_profession: [441, 2248, 2234, 2237, 2280]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the crawled `sidecar.roles` kept only `physician`, `professor`, `educator` — the roles **dentist** and **surgeon** survive only in `class_list`/`page_text`, which is why the taxonomy line here is richer than the page's Identity Snapshot.
- **`modified` on source:** 2026-06-19T16:57:23 · `page_bytes`: 55,190 (raw HTML; the `Last updated: June 19, 2026` line sits in the rendered page text)
- **Verbatim fields (self-reported):** Name `李乃恭醫師 / Dr. Kenneth N. Lee` · Birth Year `-` · Birth Place `台灣`
- **U.S. arrival:** `-/-/-` (unfilled) · **Address:** `Paramus / NJ`
- **Family:** rows `1. Wife:-` `2.Daughter:-` `3.Son:-` — JSON parses this as an empty `family` list (`family_filled: false`; absence evidence, not withheld data)
- **Education (2 rows):** `1.台灣大學` — `-` — `B.S.` · `2. Columbia University` — `-` — `Ph.D. Dental Surgery`
- **Employment (4 rows):** `1. Flushing, New York` — 開業牙科醫師 · `2. New York University College` — Clinical Assistant Professor · `3. Columbia University` — Clinical Instructor · `4. Bellevue醫院` — 口腔外科醫師
- **Accomplishment (2 rows):** `1. awarded for Excellence in Orthodontics from Columbia University College of Dental Medicine` · `2. Award for Exceptional Interest in the Development of the Oro-Facial Complex from the American Association of Orthodontists` — the **second award is absent from the person page** before this capture.
- **Publication(Non-professional ones):** `-` · **Hobby:** `golfing, reading, and traveling` · **Website or Blog:** `-`
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Provenance line:** `Source from大紐約區海外台灣人筆會會刊01/2017` (per `page_text` in the capture JSON and the dump below) — the record attributes its content to the Greater New York Region Overseas Taiwanese Pen Club yearbook 01/2017. The matching yearbook is archived on this box as [[works/taiwaneseamericanhistory-org/publications1059|publications1059]] (TAH #1059), which independently names him — see Third-party namings below.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1884.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1884/](https://taiwaneseamericanhistory.org/whoswho1884/)
- **Title:** `1884. Kenneth N. Lee 李乃恭 / 09/2017` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1884|TAH #1884]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Place, U.S. arrival `-/-/-`, Address `Paramus / NJ`, Family placeholder rows, Education, Employment, both Accomplishment awards, `Publication –`, `Hobby golfing, reading, and traveling`, `Website or Blog –`, `Source from大紐約區海外台灣人筆會會刊01/2017`). It is a second rendering of the same self-reported payload, not an independent source.

## Twin & cross-check (2026-11-13)
Containment/md5 test on the two serializations of the one form (frontmatter stripped, `#`/whitespace normalized):
JSON rich fields (`content_html`/`person_profession`/`class_list`/`sidecar`/`page_text`/`modified`/`page_bytes`) =
2,836 normalized chars (md5 `95188b2528245d1a671a9626daadb729`) vs `posts/whoswho1884.md` body = 769 normalized
chars (md5 `73a8d3dd7aef3b2d2ab85398788061f2`). Not md5-equal and not whole-container substrings (the JSON carries
site chrome, the `Last updated: June 19, 2026` line, the five-tag profession taxonomy, and the footer restatement
block) — the JSON is the richer artifact; the dump's form block is contained in it (containment sample verified True).
Agreement across two serializations of one editable self-report is NOT corroboration — that is what keeps the
record's own `Source from 大紐約區海外台灣人筆會會刊 01/2017` submission line at `alleged`-grade provenance.

## Third-party namings on this box (2026-11-13)
1. **大紐約區海外台灣人筆會 2017 年刊, 會長的話 (陳欽明, 2016-12-12)** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications1059.md`
   (original: https://taiwaneseamericanhistory.org/publications1059/, posted 01/2017, donated by 大紐約區海外台灣人筆會).
   Verbatim: 「第三位主講人是李乃恭牙醫博士，台大醫學院牙科畢業，哥倫比亞大學口腔外科牙醫博士，全能的牙醫，大紐約區很多臺美人都受他照顧。講題是「再談植牙」。」
   Third-party (pen-club president 陳欽明) attestation of the 台大牙醫 / 哥倫比亞口腔外科牙醫博士 credentials **and** of
   his community role as third speaker at the 2017 annual meeting of the Pen Club.
2. **大紐約區海外台灣人筆會的活動 roster page** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/activities-of-the-greater-new-york-region-overseas-taiwanese-pen-club.md`
   (original: https://taiwaneseamericanhistory.org/activities-of-the-greater-new-york-region-overseas-taiwanese-pen-club/).
   Verbatim roster line under 筆會年會: 「回顧筆會年會報告-徐清一;李乃恭;陳廷楷;林茂賢;胡兌昀」 with external link
   http://www.taiwanus.net/news/press/2016/201612210003111348.htm (2016-12-21) — a second publication corroborating
   the same annual-meeting report roster.

## Searched, no further material (2026-11-13)
- `grep -rlF` per name form (`Kenneth N. Lee`, `李乃恭`, `kenneth-n-lee`, `whoswho1884`) over `content` + `knowledge`:
  hits are his own artifacts above, machine indexes (`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`,
  `taiwaneseamericanhistory-org-family.json` — no 李乃恭/Kenneth N. Lee entry there), directory listings
  (`content/people/index.md`, `content/sources/taiwaneseamericanhistory-org.md`), and stale-HTML drift log lines
  (`knowledge/operational/incidents/2026-09-1x.md`).
- `Kenneth Lee` hits (`posts/132.md`, `person/jannet-jah.json`, `people/jannet-jah.md`) are the **composer 李奎然**
  (Jennet Jah's father) — same-name false positive, excluded.
- No Wikipedia / Wikidata / 華文press / 官網 capture of this subject exists on this box (see Online arms on the person page).

## Harvest provenance
Profile and posts captures are from the taiwaneseamericanhistory.org harvest recorded in
`knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`method: wp-json`).

## Related Pages
- Subject: [[people/kenneth-n-lee|Kenneth N. Lee 李乃恭]]
- Work record: [[works/taiwaneseamericanhistory-org/whoswho1884|TAH #1884 1884. Kenneth N. Lee 李乃恭 / 09/2017]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]]

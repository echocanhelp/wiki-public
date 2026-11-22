---
title: "TAH Who's Who profile capture — 950. Wen-Ling Tu 杜文苓"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 950. Wen-Ling Tu 杜文苓

Primary capture of the subject's own self-reported TAH Foundation (台美史料中心) Who's Who
record, held on this box as two distinct artifacts. Preserved because every biographical
field below is **self-reported** on an editable site, and — as of the sweep dated below —
the only other records naming her are third-party **event programs** (1999 MTSC roster,
2002 TACEC panel listing, 2003 TACWC speaker listing, and the 台美文教基金會 awards roster),
all absorbed on this pass.

## Subject
- [[people/wen-ling-tu|Wen-Ling Tu 杜文苓]] — TAH Who's Who record #950

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/wen-ling-tu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/wen-ling-tu/](https://taiwaneseamericanhistory.org/person/wen-ling-tu/)
- **Record id:** 73513 · **type:** `tah_person` · **status:** `publish` · `has-post-thumbnail`
- **Profession taxonomy:** `person_profession: [2247, 2242, 348, 2245]`, and the `class_list`
  slugs read `person_profession-activist`, `person_profession-community-leader`,
  `person_profession-public-health`, `person_profession-scholar`. The site renders them as
  the four tags `activist` / `community leader` / `public health` / `scholar`. **No taxonomy
  name→id map is archived on this box**, so the class-list slugs are the readable form and
  the numeric ids cannot be independently decoded here. The four-tag taxonomy outranks the
  single catch-all role `Taiwanese American (TAH Who's Who)` that our person page's Identity
  Snapshot carried before this pass — that earlier label dropped activist, public health and
  scholar entirely. The `public health` tag is notable: no other record on this box names a
  public-health role for her (her degrees are 社會 / 環境科學 / 環境計劃).
- **`modified` on source:** 2026-06-19T16:41:29 · `page_bytes`: 54,002 (raw HTML; the
  `page_text` in the JSON is the trafilatura-extracted text — the site chrome, the
  `Last updated: June 19, 2026` line, the four profession tags and the footer summary block
  sit in the extracted text too, so this capture is a superset of Capture 2).
- **Verbatim fields (self-reported):** Name `杜文苓 博士` / `Dr. Wen-Ling Tu` · Birth Year
  `1971` · Birth Place `台灣台北市` · First year, first city and state arrived in the U.S.
  `-/-/-` (**never filled**) · Address `台灣/-` · Family `1. Husband:-` `2.Daughter:-`
  `3.Son:-` (all three rows blank; parsed `family: []`, `family_filled: false`).
- **Education (3 rows, no year ranges):** `1. 國立台灣大學` · `-` · `B.S. 社會` ·
  `2. 紐約州立大學` · `-` · `M.S. 環境科學` · `3. 加州大學柏克來分校` · `-` ·
  `Ph.D. 環境計劃`. No institution carries a year — the form's year fields are all `-`.
- **Employment:** three rows, all `-` — the self-report names no employer at all.
- **Accomplishment:** `1.台美基金會國際青年社區領導獎, 1999` · `2.台灣環境行動網(TEAN)的創始人之一`.
  These two lines are the only substantive self-reported facts in the form. The award line
  matches the independent awards roster (see Third-party records below); the TEAN
  founder-at-UC-Berkeley fact matches the 1999 MTSC program (`杜文苓(Founder of TEAN)`).
- **Publication (non-professional) / Hobby / Website or Blog:** `-` / `-` / `-` — unfilled.
  The blank fields are themselves part of the record: no publication, hobby, or personal
  site fact is being withheld elsewhere on this capture.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on
  abby-hong), this record carries no upstream-source attribution, so no external article can
  be traced out of it.
- **Footer summary block (same page, rendered below the form):** `Dr. Wen-Ling Tu` · Hanzi
  `杜文苓` · Birth Year `1971` · Birthplace `台灣台北市` · Residence `台灣` · Education — the
  same three rows · Community `台灣環境行動網 (TEAN) 創始人之一`. The footer omits the 1999
  award row present in the form; restatement inside one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho950.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho950/](https://taiwaneseamericanhistory.org/whoswho950/)
- **Title:** `950. Wen-Ling Tu 杜文苓 / 2016/04` · **published:** 2016-04-24 (per the vault
  work record [[works/taiwaneseamericanhistory-org/whoswho950|TAH #950]], `value_band: B`,
  `## Subjects` lists her with `(named subjects pending absorb)`) — the earliest dated
  record for her in the corpus.
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place,
  `-/-/-` US-arrival row, Address, blank Family rows, Education, blank Employment, the two
  Accomplishment rows, blank Publication/Hobby/Website). It is a second rendering of the
  same self-reported payload, not an independent source. It does **not** carry the four
  profession tags or the footer summary block.

## Twin & cross-check (2026-11-14)
Per the theodore-ted-wing correction, the containment/md5 test runs on the profile's CONTENT
BLOCK (sliced from `Who's Who Taiwanese American Profile` to the footer line
`Travel the roads paved…`), not the raw `page_text`. Normalized by stripping frontmatter and
all `#`/whitespace (the post dump is heading-padded, so a naive md5 differs trivially):

| Artifact | normalized md5 | normalized chars |
|---|---|---|
| Capture 1 profile content block | `65996903db27897fe3e8c5c0aa0f7862` | 644 |
| Capture 2 post dump | `10f627394696304f2c2b22e2fe75d7c6` | 355 |

md5 differs **and neither is a substring of the other** — because Capture 1 carries the four
profession tags, the `Last updated: June 19, 2026` line, and the footer summary block that
Capture 2 omits, while Capture 2 prefixes the `950. … / 2016/04` title the profile block
lacks. A field-level diff shows every Capture 2 field appears in Capture 1 (Capture 2 is the
form payload; Capture 1 = same payload + page chrome). **They are two serializations of one
editable self-report, so field-level agreement between them is NOT corroboration** — that is
why the form-only facts (the two award/founder Accomplishment rows, the education rows) stay
`alleged` on the person page unless an event record independently names them.

## Third-party records naming 杜文苓 (all harvested 2026-08-17, `wp-json`)
Per `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`. Each is absorbed as
a dated row on [[people/wen-ling-tu]] with its own citation:
1. **台美文教基金會 得獎人名單** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/winners20.md`
  (`source_url: https://taiwaneseamericanhistory.org/winners20/`): under
  【國際青年社區服務領導獎】 lists `杜文苓(1999)` beside `Kumi Naidoo顧彌‧那都(1999)`.
  Corroborates the self-reported `台美基金會國際青年社區領導獎, 1999` row.
2. **MTSC 1999 (中西部台灣人夏令會, 1999-07-08–11, Ohio Wesleyan University)** —
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mtsc-1999.md`: 台灣學生社 speaker
  roster `杜文苓(Founder of TEAN)`; report text: 「學生社杜文苓述說以台灣環保運動爲台灣作國際外交」
  and 「柏克來加大的學生杜文苓和Lily Hsueh 代表「台灣環境行動網」演講在台灣保護黑面琵鷺，在國際會議從事環保外交的經過」;
  社團代表 roundtable lists 「台灣環境行動網杜文苓女士」. Three mentions, one event record.
3. **TACEC 2002 (美東夏令會, 2002-07-04–07, UMass Amherst)** —
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/tacec-2002.md`: 「環境行動網的創辦人杜文苓…聯合主持的台灣和世界環保座談會」.
4. **TACWC 2003 (美西台灣人夏令會)** —
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/tacwc-2003.md`: 「環保的活動份子杜文苓講台灣的環保問題後，把它與外交牽連在一起」.

The TEAN organization page [[organizations/taiwan-environmental-action-network-tean]] records
TEAN as a UC Berkeley–centered student organization (Black-faced Spoonbill conservation,
anti-nuclear, wetlands, seven working groups) — the same organization the MTSC 1999 program
names her as founder of.

## Whole-corpus sweep (2026-11-14)
Single-pattern `grep -rlF`, one pattern per name form, over **all** of `content/` and
`knowledge/` (the DEEPEN-X lane's `works/` + `articles/` habit was not used); crawler
indexes excluded (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index*`,
`content-analysis/*.jsonl`):

`杜文苓` → 19 files · `Wen-Ling Tu` → 19. Every non-index hit is one of: her own two
captures, the [[works/taiwaneseamericanhistory-org/whoswho950|#950 work page]], her person
page, the [[sources/taiwaneseamericanhistory-org|source hub]] roster line, the TEAN org +
work pages (via the founder line, from this pass), the derived
`taiwaneseamericanhistory-org-family.json` roster, the `tdm-page-title-index.json` /
`taiwanjustice-net-priority-lexicon.json` lookup artifacts, or the four event records
enumerated above.

**No memoir (《Our Journeys》 / My Stories), taiwandaily/TJJ article, or other community
narrative names her**, so the pre-pass `verified-saturation` SKIP stamps on the person page
(which grepped only `content/works` + `content/articles`) described those lanes, not the
corpus; what they missed were the four `posts/` event records above.

## What this capture does NOT establish
- **US arrival year/city/state** — the form field is `-/-/-`; no other record on this box
  states when she came to the U.S.
- **Education years** — every row's year field is `-`; only the three institutions and
  degrees are recorded.
- **Employment / employer** — all three form rows blank; the 1999 MTSC program calling her
  「柏克來加大的學生」 is a 1999 student-status statement, not employment.
- **Family** — `family_filled: false`, no spouse/children names; no family-of-origin rows
  exist in the form.
- **`public health` profession tag** — taxonomy-only; no record on this box narrates a
  public-health career, so it stays a tag, not a biographical fact.
- **Residence** — `台灣/-` is as specific as the self-report goes; city never filled.

## Related
- [[people/wen-ling-tu|Wen-Ling Tu 杜文苓]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whoswho950|950. Wen-Ling Tu 杜文苓 / 2016/04]] — vault work record
- [[organizations/taiwan-environmental-action-network-tean|台灣環境行動網 TEAN]] — org she founded per the 1999 program
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher

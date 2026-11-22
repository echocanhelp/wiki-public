---
title: "TAH Who's Who profile capture — 1078. Thomas C.T. Chiu 邱智正 / 2016/06"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1078. Thomas C.T. Chiu 邱智正 / 2016/06

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]]
Who's Who record, archived on this box as two artifacts. This is the **only** source on this box for
this person — no memoir, Our Journeys issue, article, church, org, or event record elsewhere in the
corpus names him (see Whole-corpus sweep below).

## Subject
- [[people/thomas-c-t-chiu|Thomas C.T. Chiu (邱智正)]] — TAH Who's Who record #1078 (site record id 73634)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/thomas-c-t-chiu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/thomas-c-t-chiu/](https://taiwaneseamericanhistory.org/person/thomas-c-t-chiu/)
- **Record id:** 73634 · **type:** `tah_person` · **`modified` on source:** 2026-06-19T16:43:43 ·
  `page_bytes`: 52,547 (raw HTML)
- **Profession taxonomy:** `person_profession: [2234, 2280]` with `class_list`:
  `person_profession-physician`, `person_profession-surgeon` — **two** taxonomy terms; the harvest
  `sidecar.roles` records only `["physician"]` — **the sidecar drops `surgeon`**, recovered only from
  the `class_list` and the rendered page.
- **Verbatim form fields (self-reported):** Name `邱智正 醫師 / Dr. Thomas C.T. Chiu` · Birth Year `-`
  (unfilled) · Birth Place `台灣台南麻豆` · **U.S. arrival** `First year, first city and state arrived
  in the U.S.` = `-/-/-` (all blank) · Address `Monterey Park/CA`
- **Family (self-report, printed):** `1. Wife:Sue 邱淑貞` · `2. Daughter:Alice Chiu` · `3.Son:-` —
  JSON parses `family: [{rel: wife, name: Sue 邱淑貞}, {rel: daughter, name: Alice Chiu}]`,
  `family_filled: true`.
- **Education (1 row):** `1. 台北醫學大學 — Year??? — B.S.` — the year field literally prints
  `Year???`; no graduation year exists in any artifact.
- **Employment (3 rows):** `1. 布魯克林醫院 — — 大腸宜腸外科專科醫師` ·
  `2. 美國外科學院 — — 大腸宜腸外科專科醫師` · `3. 衛理工會醫院(Methodist Hospital)。 — 住院醫師` —
  all date columns print `-`. Note `大腸宜腸` is the self-report's own (likely typo for 大腸肛門/直腸)
  spelling, quoted as found. The site-rendered digest block restates the same three rows under
  `Position` with no added dates.
- **Absence roster (recorded gaps, not invented zeros):** `Accomplishment` blank ·
  `Publication(Non-professional ones)` `-` · `Hobby` `-` · `Website or Blog` `-` — no crown fact is
  withheld; the subject simply did not fill these fields.
- **Internal link rendered on the page:** `For more information please click in
  http://tah.local/blog/whoswho1078/` — a `tah.local` staging-host URL leaked into the published
  record; the live equivalent is `https://taiwaneseamericanhistory.org/whoswho1078/`.
- **Motto line rendered on the page:** `Travel the roads paved by those who came before us.` — site
  boilerplate, not a subject statement.

## Capture 2 — story-corpus encyclopedia dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1078.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1078/](https://taiwaneseamericanhistory.org/whoswho1078/)
- **Title:** `1078. Thomas C.T. Chiu 邱智正 / 2016/06` · frontmatter `fetched: auto`
- Field-for-field the same form payload as Capture 1 (Name / Birth `-` / Birth Place / arrival
  `-/-/-` / Address / Family / Education / Employment / blank Accomplishment-Publication-Hobby-Website),
  restated with the internal link normalized to the live host.

## Twin check (computed this pass, 2026-11-14)
Normalized md5 (frontmatter excluded, `#`/whitespace stripped, NFKC):

| artifact | md5 (12) | normalized chars |
|---|---|---|
| Capture 1 — profile page (`page_text`) | `4f6533ad9c66` | 1,297 |
| Capture 2 — story dump (`posts/whoswho1078.md`) | `d0e8239d5af9` | 459 |

Not md5-equal and **not** in containment either direction (`json_in_post: false`, `post_in_json:
false`) — Capture 1's extra length is site chrome + the site-rendered digest block, not biographical
content absent from Capture 2. Every biographical field present in one is present in the other.
Agreement across two serializations of one editable self-report is **not** corroboration, which is why
every field on the person page is labeled `alleged`/`documented` (printed in the record), never
`sourced`.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in
  `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`,
  `method: wp-json`, expected/count person 2,212, organization 339) — the harvest behind
  [[sources/taiwaneseamericanhistory-org|the TAH CPT source page]].
- This slug **is** in that manifest's `weak.person` list (1,857 of the 2,212 person records), i.e. the
  harvest grader marked this profile's payload thin at fetch time — consistent with the blank
  Accomplishment/Publication/Hobby/Website fields and the `Year???` education row.

## Whole-corpus sweep (2026-11-14)
Single-pattern `grep -rlF` per name form over `content` + `knowledge` (`.md`/`.json`), machine indexes
(`units.jsonl`, `*index.jsonl`, `ee-vault-index.*`, `content-analysis/*`, `MANIFEST`,
`tdm-page-title-index`, `taiwanjustice-net-priority-lexicon`, `*family.json`) excluded:

- `邱智正` → 5 files: his own person page, work page
  [[works/taiwaneseamericanhistory-org/whoswho1078|whoswho1078]], the
  [[sources/taiwaneseamericanhistory-org|source hub roster line]], and his two captures.
- `Thomas C.T. Chiu` → the same 5 files.
- `Thomas Chiu` → 1 file: his own capture JSON only.
- `邱淑貞` (wife's printed name) → 3 files: his own person page + his two captures. The only *other*
  "Sue Chiu" records on this box — [[people/sue-chiu|黃雪香 Sue Chiu]] (#65 artist, #853 Who's Who) —
  resolve to a different person (NJ, 普林大學/氰氨公司 career, husband 邱義昌); HOLD, not merged, per the
  note already on the person page.
- 麻豆/Monterey Park colon-proctology co-mentions: no third-party record names this subject.

**No memoir (`mystories*`), Our Journeys issue, taiwandaily/TJJ article, church, org, or event record
on this box names him.** `verification_status: pending` is retained — this is a single self-report.

## What this capture does NOT establish
- No birth year (`-` printed) and no U.S. arrival year/city/state (`-/-/-`).
- No graduation year (`Year???` printed) and no employment date ranges (all `-`).
- No verification of the 布魯克林醫院 / 美國外科學院 / Methodist Hospital appointments beyond the
  self-report; no hospital, board-certification, or medical-licensure record is archived on this box.
- Whether `Sue 邱淑貞` and `Alice Chiu` are publicly identifiable — no third-party mention exists here.

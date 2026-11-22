---
title: "UCR UTSA third-party captures (2026-11-16)"
type: source
tags:
  - source
  - capture
  - ucr-utsa
verification_status: pending
last_reviewed: 2026-11-16
---
# UCR UTSA third-party captures (2026-11-16)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 723
- wikilinks: 2


Capture page for the FLOOR-ANCHOR pass on
[[organizations/ucr-united-taiwanese-student-association|UCR United Taiwanese Student
Association (UTSA)]] (card t_5b7a47c9, 2026-11-16). Before this pass the sole artifact
for this club on the box was the editable TAH directory self-report (JSON 77540) — see
[[sources/ucr-utsa-tah-org-capture|the TAH capture page]]. These are the first
**non-TAH** records for this org on this box. Machine manifest:
`knowledge/web-archives/ucr-utsa-thirdparty-2026-11-16/MANIFEST.md`.

## Capture 1 — MOE 駐洛杉磯台北經濟文化辦事處教育組「聯絡同學會」roster (third-party institutional)
- URL: https://depart.moe.edu.tw/LA/cp.aspx?n=7FC7F97C86931EA0&s=6D36777C6E4F8C89
- Captured 2026-11-16 via curl (HTTP 200, 164,019 bytes), on-disk:
  `knowledge/web-archives/ucr-utsa-thirdparty-2026-11-16/depart.moe.edu.tw-LA-cp.aspx.html`
- Captured facts: under 「University of California, Riverside （加州大學河濱校區）」 the
  page lists 「**United Taiwanese Student Association (UTSA)（臺灣學生會）** 臉書社群：
  http://www.facebook.com/UCRUTSA 同學會IG: UCR_UTSA」. Page footer:
  `Last Updated: 2026-11-04`. The same page lists UCR TGSA separately (電郵
  yukai19960507@gmail.com, 臉書 groups/12472983540, IG ucrtgsa) — i.e. the MOE roster
  treats UCR UTSA and UCR TGSA as **two distinct clubs**, which the TAH directory never
  stated (it only compared UTSA to TASA @ UCR).
- Why this counts as an anchor: depart.moe.edu.tw is the ROC MOE education office's own
  site, maintained independently of the editable TAH directory. It supplies the Chinese
  club name 臺灣學生會 that record 77540 leaves blank, and independently lists the two
  declared social arms.
- Note on IG handle spelling: the MOE page renders 「UCR_UTSA」; the TAH directory record
  and LinkedIn render 「@ucr_utsa」 — same account, handle case/separator variants.

## Capture 2 — live TAH directory page (same editable source, later state)
- URL: https://www.taiwaneseamericanhistory.org/organization/ucr-united-taiwanese-student-association/
- Captured 2026-11-16 via curl (HTTP 200, 51,227 bytes), on-disk:
  `knowledge/web-archives/ucr-utsa-thirdparty-2026-11-16/www.taiwaneseamericanhistory.org-organization-ucr-united-taiwanese-student-association-.html`
- Captured facts: status banner 「This organization is no longer active or its current
  status is unknown.」 above the two known paragraphs, plus infobox fields
  `Abbreviation: UTSA`, `School: University of California, Riverside`,
  `Primary Region: Riverside, California`. The banner postdates the crawl's `modified`
  2026-06-09 → same editable source, later state → still `alleged`.

## Capture 3 — Wayback availability probes (absence evidence)
- http://archive.org/wayback/available?url=facebook.com/UCRUTSA → `archived_snapshots: {}`
  (`wb-ucrutsa.json`, HTTP 200, 2026-11-16)
- http://archive.org/wayback/available?url=instagram.com/ucr_utsa → `archived_snapshots: {}`
  (`wb-ucrutsa-ig.json`, HTTP 200, 2026-11-16)
- Meaning: neither declared social arm has a Wayback snapshot; closing the officer/event
  gaps from social media needs a logged-in capture or a founder interview.

## Search-only rows (NOT archived on this box → `alleged`, snippet tier)
- `linkedin.com/company/ucrutsa` — org page: 「represents UCR 臺灣學生會」, "cultural and
  social organization that aims to promote Taiwanese culture", homepage
  `instagram.com/ucr_utsa`, 8 followers, company size 1–10. Second independent index
  for the Chinese name (snippet only).
- `linkedin.com/in/austin-wei-72b3441b1` — "Club President — UCR United Taiwanese
  Student Association" Jul 2021–Present; cooperative events with other UC schools
  "such as Homecoming and Chinese New Year celebration"; manages Facebook/Instagram/UCR
  events page.
- `linkedin.com/in/yingchendu` — "Treasurer — UCR United Taiwanese Student Association"
  Oct 2024–Present; "Managed the club's $1000 budget".
- `linkedin.com/in/jchan7101` (Jeremy Chang) — Activities: "UCR United Taiwanese Student
  Association", 2021–2025.
- `aeroleads.com/in/jchang32` (Josh Chang aggregator) — President Sep 2024–Present, VP
  Sep 2023–Sep 2024; VP budget "over USD 3,000"; President organized the "2024 Taiwanese
  American Heritage Week Festival, attracting 7,000 attendees and collaborating with
  Taipei Economic & Cultural Office in Los Angeles"; liaison "between five UC campuses".
  Single aggregator restatement — `alleged`, and NOT corroboration of the LinkedIn rows.

## Twin / corroboration ruling
- The four LinkedIn/aggregator profiles are independent authors but each is a
  self-edited career profile → same evidentiary tier (`alleged`); they corroborate the
  club's **existence and activity window** (2021–2025 officers), not each other's
  event details.
- The MOE roster is the only record on this box authored by someone other than the club
  or the TAH directory editor; treat the Chinese name 臺灣學生會 as `documented` at the
  level of a two-source agreement (MOE page + LinkedIn org page snippet).

## Searches performed (budget 8, used 4 web searches + 3 curl fetches, 2026-11-16)
1. `"UCR United Taiwanese Student Association" Riverside` → LinkedIn org page, live TAH
   page, Austin Wei / Ying-Chen Du / Jeremy Chang profiles, aeroleads Josh Chang, TAH
   student-type directory page.
2. `"UCR UTSA" OR "UCRUTSA" Taiwanese student association Instagram events` → same set
   plus sibling clubs (UCR TASA LinkedIn, UCR TGSA site) — used to rule out conflation.
3. `"United Taiwanese Student Association" "Taiwanese American Heritage Week" UCR
   festival` → only the aeroleads snippet (festival claim, single source).
4. `"ucr_utsa" OR "@UCRUTSA" Instagram Facebook` → **MOE LA roster page** (the harvest),
   LinkedIn org page, live TAH page.
Plus curl fetches: MOE page, live TAH page, 2× Wayback availability API.

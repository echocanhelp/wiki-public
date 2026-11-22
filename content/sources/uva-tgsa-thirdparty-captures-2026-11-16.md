---
title: "TGSA @ UVa — third-party captures (2026-11-16)"
type: source
tags:
  - source
  - capture
  - tgsa-uva
verification_status: pending
last_reviewed: 2026-11-16
---
# TGSA @ UVa — third-party captures (2026-11-16)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 840
- wikilinks: 3


Captures pulled on 2026-11-16 (card t_73b30004) for
[[organizations/taiwanese-graduate-student-association-at-uva|TGSA at UVa]].
Companion to [[sources/taiwanese-graduate-student-association-at-uva-tah-organization-capture|the TAH directory capture]]
(record id 77587). Before this pass every anchored fact on the org page resolved to that single
editable TAH directory record. These captures add the first records **outside** that record:
the university's own Sympa mailing-list registry, a 2023 first-party PTT recruitment post naming
the Facebook group, and the live TAH page's infobox/status banner absent from the local crawl JSON.
Machine manifest with URLs, md5s, fetch methods and excluded false positives:
`knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/MANIFEST.md`.

## Capture 1 — UVA Sympa mailing-list registry (third-party, university-run; strongest independent anchor)
- URLs: https://lists.virginia.edu/sympa/lists/society and https://lists.virginia.edu/sympa/info/taiwanese-grads
- On-disk: `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/uva-lists-society.html` (HTTP 200, 840,350 B),
  `uva-lists-info-taiwanese-grads.html` (HTTP 200, 11,193 B), fetched 2026-11-16.
- Captured facts (verbatim from the pages): the University of Virginia Sympa 6.2.72 mailing-list
  service lists a list with slug `taiwanese-grads`, Subject 「Taiwanese Graduate Student Association
  at UVa」, Description 「List serv for members of Taiwanese Graduate Student Association」, under
  the Society & Culture category; Owners shown: Chun-Yen Hsu, Chen,Yu-Han (moderators same as
  owners); list address taiwanese-grads@virginia.edu (obfuscated via document.write in the index).
- Why this counts: the list is hosted on the university's own `lists.virginia.edu` Sympa service —
  an institution-run (not club-editable) registry — and it corroborates the TAH directory's claim
  that TGSA is a recognized campus organization distinct from the undergraduate TSA. Owner names
  are recorded as they render on the public list-info page; treat as roster metadata, not profiled
  persons.

## Capture 2 — PTT 2023 first-party recruitment post (first-party, dated)
- URL: https://www.ptt.cc/bbs/studyabroad/M.1683201342.A.097.html
- On-disk: `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/ptt-studyabroad-M.1683201342-uva-tgsa-2023.html`
  (HTTP 200, 6,876 B), fetched 2026-11-16.
- Captured facts (verbatim): posted 2023-05-04 19:55:36 to PTT studyabroad by AstroCY (くぽよ),
  from 199.111.213.238 (美國). 標題 「[情報] UVA TGSA 歡迎2023新生」; body invites incoming
  大學生/研究生/博後/教職 to join 「The Taiwanese Graduate Student Associate (TGSA) at UVa」, links
  the Facebook group https://www.facebook.com/groups/112326065453314, announces a zoom 線上新生說明會
  planned for 六月中 and a Google form in 五月中, closing 「再次恭喜即將到Charlottesville的各位」.
- Why this counts: a dated, non-editable-after-posting community record (2023) of TGSA actively
  recruiting, independent of the editable TAH directory; it also pins the Facebook group id that
  the TAH infobox lists.

## Capture 3 — Live TAH directory page, re-fetched 2026-11-16 (first-party, richer than the crawl JSON)
- URL: https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-student-association-at-uva/
- On-disk: `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/tah-org-page-live.html` (HTTP 200,
  51,811 B); Wayback replay of the page's single CDX capture (2026-07-28T03:54:08, HTTP 200) in
  `wayback-tah-org-page-20260728.html` (56,197 B) — text identical.
- Captured facts NEW vs the local crawl JSON (record id 77587, modified 2026-06-09): page header
  「Student Organization · Last updated: June 9, 2026」; status banner 「This organization is no
  longer active or its current status is unknown.」; verbatim Mission block 「The TGSA at UVA is
  established for the expressed purpose of: 1. Create a welcoming environment for incoming,
  current, and former UVa students to safely celebrate the Taiwanese cultural heritage 2. When
  applicable, collaborate with other CIOs and departments to host Taiwan themed events on or near
  grounds」; infobox Abbreviation TGSA / School University of Virginia / Primary Region
  Charlottesville, Virginia / Facebook facebook.com/groups/112326065453314.
- Status: still one editable first-party record (same site as the JSON) — the twin check is
  md5-different, JSON content_html ⊂ live page; same-source, not corroboration. The value is the
  previously-unabsorbed fields (banner, Mission, infobox), not a second source.

## Capture 4 — PTT 2016 UVA link drive (third-party, weak → alleged)
- URL: https://www.ptt.cc/bbs/studyabroad/M.1460140112.A.E5A.html
- On-disk: `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/ptt-studyabroad-M.1460140112-tsa-links-2016.html`
  (HTTP 200, 31,250 B), fetched 2026-11-16.
- Captured facts: 2016-04-09 mod call 「[公告] 誠徵各校台灣同學會TSA連結」 asking graduate/留學生-focused
  clubs for their Facebook URLs; push 04/09 11:55 by ie145 「University of Virginia https://goo.gl/thDQSG」,
  mod note 已代為更正.
- Limit: the goo.gl shortlink no longer resolves verifiably, so whether that 2016 entry pointed at
  TGSA or at the undergraduate TSA is unknown → `alleged`.

## Capture 5 — MOE 駐外教育組 同學會名錄 row (third-party official listing → alleged, identity cross-wire)
- URL (mirror): https://osa.nycu.edu.tw/osa/ch/app/data/doc?detailNo=1171000164760948736&module=nycu0106&type=s
- On-disk: `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/nycu-osa-club-roster-americas.html`
  (HTTP 200, 202,148 B), fetched 2026-11-16.
- Captured fact: roster row 24 駐美國代表處教育組 — 「維吉尼亞大學中華民國同學會」, Charlottesville, VA,
  https://www.facebook.com/groups/112326065453314.
- Caveats (both required when citing): (a) the on-disk CDN-served copy does not contain this row
  (grep `112326065453314` = 0 hits on disk); the row was observed in the search-engine capture of
  the same document the same day → cite `alleged`; (b) the roster labels the group 中華民國同學會,
  not TGSA, yet the FB group id is exactly the group the 2023 PTT TGSA post announces — same-group,
  different-name cross-wire → `alleged`, identity HOLD on whether MOE lists TGSA under another name.

## Negative evidence
- Facebook group `112326065453314` Wayback CDX: only two 302 login-wall captures (2024-03-30),
  availability API `{}` — no archived group content exists (`wayback-fb-group-cdx.json`,
  `wayback-fb-group-loginwall-20240330.html`).
- 華文 press probe (世界日報/大紀元/台灣日報 + this name, 2026-11-16): no item names this club.
- No Wikipedia/Wikidata item surfaced; no founding-year source found; chinesetravelers.com UVA
  section lists TSA/CSSA only, no TGSA row.

## Source Notes
- Source: curls + archive.org probes run from this box 2026-11-16 per card t_73b30004; manifest
  `knowledge/web-archives/uva-tgsa-thirdparty-2026-11-16/MANIFEST.md`.
- Source: prior first-party baseline `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-graduate-student-association-at-uva.json`
  (id 77587, modified 2026-06-09), captured to
  [[sources/taiwanese-graduate-student-association-at-uva-tah-organization-capture|the TAH directory capture page]].

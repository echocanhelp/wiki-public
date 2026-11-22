---
title: "UCR TASA third-party and live-site captures (2026-11-16)"
type: source
tags:
  - source
  - capture
  - ucr-tasa
verification_status: pending
last_reviewed: 2026-11-16
---
# UCR TASA third-party and live-site captures (2026-11-16)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 728
- wikilinks: 3


Captures pulled on 2026-11-16 (card t_610cb752) for
[[organizations/taiwanese-american-student-association-at-ucr|TASA @ UCR]].
Before this pass the only artifact for this club on the box was the editable TAH
directory self-report (JSON 77539) — see
[[sources/tasa-at-ucr-tah-organization-capture|the TAH capture page]]. These are
the first institutional (UCR APSP) and first-party live-site records for this org
on this box. Machine manifest:
`knowledge/web-archives/ucr-tasa-thirdparty-2026-11-16/MANIFEST.md`.

## Capture 1 — UCR Asian Pacific Student Programs (APSP) official site (third-party institutional)
- URL: https://apsp.ucr.edu/programs/our-programs
- Captured 2026-11-16 via curl (HTTP 200, 47,978 bytes), on-disk:
  `knowledge/web-archives/ucr-tasa-thirdparty-2026-11-16/apsp.ucr.edu-programs-our-programs.html`
- Captured facts: under "Student Organizations Affiliated with APSP", the page says
  the listed groups are "officially affiliated with APSP in the **2023-2024 academic
  year**", and the roster includes "**Taiwanese American Student Association (TASA) –
  Cultural**", alongside CSA, Hallyu at UCR, HSA, Katipunan Pilipino, KSS, NSU, PISA,
  QAAPI, Riverside Surging Dragons, Senryu Taiko, SAF, Tea and Go, VSA, and APISAC.
  APSP contact: 244 Costo Hall, UCR, (951) 827-7272, apsp@ucr.edu.
- Why this counts as an anchor: apsp.ucr.edu is UCR's own office site, independent of
  the editable TAH directory record — it corroborates the directory's ¶1 claim that
  TASA @ UCR "is listed as an officially recognized cultural organization under the
  umbrella of UCR's Asian Pacific Student Programs (APSP)".

## Capture 2 — UCR TASA official Linktree (first-party live site)
- URL: https://linktr.ee/tasaucr (page title "UCR TASA Official: TikTok, Instagram | Linktree")
- Captured 2026-11-16 via curl (HTTP 200, 251,393 bytes), on-disk:
  `knowledge/web-archives/ucr-tasa-thirdparty-2026-11-16/linktr.ee-tasaucr.html`
- Captured links: UCR TASA Instagram, UCR TASA TikTok, "Spring retreat interest
  forms", "T-Shirt Design Contest", "Movie Night Interest Form", "IM CO-REC
  VOLLEYBALL", "Venmo".
- Status: first-party self-report (club-run) → label `alleged`; corroborates that the
  club maintains social arms beyond the directory's Instagram/Facebook mention
  (adds TikTok), and shows current activity types (retreat, movie night, volleyball).
- Discovered via the LinkedIn company page https://linkedin.com/company/ucrtasa
  ("Taiwanese American Student Association - UCR", homepage linktr.ee/tasaucr,
  Instagram instagram.com/ucr.tasa) fetched through search on 2026-11-16 — LinkedIn
  profile pages are behind login and were not archived here.

## Capture 3 — Facebook page presence, Wayback Machine (archive of first-party page)
- URL: https://web.archive.org/web/20220422012637/http:/www.facebook.com/pages/Taiwanese-American-Student-Association-TASA-at-UCR/279636275388083
- Captured 2026-11-16 via curl (HTTP 200, 98,856 bytes), on-disk:
  `knowledge/web-archives/ucr-tasa-thirdparty-2026-11-16/facebook-tasa-at-ucr-page-2022-wb.html`
- Captured fact: the Wayback calendar strip for this FB page (page id
  279636275388083) reads "**7 captures, 05 Mar 2016 - 04 Dec 2024**" — independent
  archive evidence that a Facebook page named "Taiwanese American Student Association
  (TASA) at UCR" existed as early as **2016-03-05**, corroborating the directory's
  Facebook claim with a dated third-party (Internet Archive) record.
- FB page body itself sits behind the login wall in the replay; not archived.

## Officer roster evidence (LinkedIn member self-reports, `alleged`)
Surfaced by search on 2026-11-16 (profiles not archived; login wall):
- Nicole Yu — "Co President — Taiwanese American Student Association at UCR", Mar 2023–present, UCR BS 2021–2025.
- Wesley Yu — "Treasurer, Vice President — UCR Taiwanese-American Students Association", Sep 2011–Jul 2012 (earliest dated officer term found for this club).
- William Wong — "Event Coordinator — Taiwanese American Student Association" at UCR.
- Li-Hsiang Hsu — UCR 2014–2016, "Activities and Societies: UCR Taiwanese American Student Association (UCR-TASA)".
All are self-edited LinkedIn entries → `alleged`, but they are first-party-member
identity evidence independent of the TAH directory.

## Whole-corpus sweep (this card, 2026-11-16)
- `grep -rliE "TASA.*UCR|UCR.*TASA|ucr\.tasa|taiwanese-american-student-association-at-ucr"`
  over `content/` (both `~/echo-system/content` and `~/quartz-v4/content`): hits are
  only this org page, its capture page, `organizations/index.md`, the sibling
  [[organizations/ucr-united-taiwanese-student-association|UCR UTSA]] page/capture, and
  index files. No narrative record names this club.
- ZH press probe (世界日報 / 大紀元 / 台灣日報 + 河濱加大/UC Riverside 同學會): 大紀元 reports
  on 同學會聯席會議 and 留學生 events name UCR via its *other* Taiwanese clubs (TGSA
  研究生同學會 in the 2010 聯席會議 report; a 臺灣同學會 會長 張庭瑋 in the 2015 經文處
  餐會 report) — different bodies from TASA @ UCR; none names this association, so
  none is absorbed as this club's history (identity HOLD).

## Gaps / NEED YOU
Still missing after this pass: founding year, Chinese name, mission statement, and any
event dated to TASA @ UCR itself. Sources checked this card and found negative for
those: UCR APSP roster page (affiliation only, 2023–2024), Linktree (live links only),
Wayback FB replay (login wall), LinkedIn (login wall; roster entries recorded above),
 HighlanderLink (SPA; not directly archived from this box — UCR Library's own webarchive
listing shows `highlanderlink.ucr.edu archived as of 2026-04-13`, a future lead), and the
ZH-press probes above.

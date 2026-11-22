# Frontier 11180842-29 web pass — peter-hsu (徐學猷)

Card: t_f6c25e3b (FRONTIER-11180842-29, target `works/taiwaneseamericanhistory-org/whos-who-1670-peter-hsu`, tier M).
Run date: 2026-11-18 (PST). Do-NOT-publish card; commit only.
Prior passes: 2026-11-14 (arms), 2026-11-16 FLOOR-ANCHOR (t_22645c56), 2026-11-18 frontier -1 (t_4edb6fd5).

## Arm 1 — zh.wikipedia infobox+awards
- Query: `徐學猷` — https://zh.wikipedia.org/w/index.php?search=%E5%BE%90%E5%AD%B8%E7%8C%B7&title=Special:Search
- Result 2026-11-18: still NO article for 徐學猷 (same state as the -1 run: "您可以新建這個頁面").
  Hits are homophone/era noise (俞大猷/吴大猷/徐學聚/郭子猷...). No infobox/awards to harvest.
- Verdict: MISS (searched `徐學猷`, 2026-11-18).

## Arm 2 — Wikidata claims
- Query: insource:"徐學猷" — https://www.wikidata.org/w/index.php?search=insource%3A%22%E5%BE%90%E5%AD%B8%E7%8C%B7%22&title=Special:Search&limit=25
- Result 2026-11-18: "There were no results matching the query." — no item carries 徐學猷.
- Verdict: MISS, no claims to HOLD, no conflict (searched `insource:"徐學猷"` + `Peter Hsu`, 2026-11-18).

## Arm 3 — official site / event page (`Peter Hsu 徐學猷 official` / company forms)
- Searches 2026-11-18: `"Peter Hsu Enterprises" OR "Peter HSU Enterprises" Lansdale PA`,
  `"Peter Hsu" "徐學猷" Lansdale OR "Peter Hsu Enterprises" OR GTI`.
- Still NO official company site (uszm.com `Site: n\a`, yellowpagesdirectory `No Website`).
- NEW FIND (this run): camcinc.org `/international_fest/borek.pdf` — CAMC↔Judge Borek ISF
  email-chain archive hosted by the Council For America My Country (Sang Joo Kim, Chairman).
  Names `Peter Hsu, ISF Finance Committee` repeatedly, quotes Lansdale Public Library
  bookkeeper Patricia Lamb: "No ISF money is spent without the express permission of Dr.
  Jeyaraj and Peter Hsu", and shows Peter Hsu (phyhsu@yahoo.com, sig block Peter Hsu
  Enterprises Inc., 650 N. Cannon Ave., Lansdale PA 19446, tel 215-362-8419, fax
  215-362-0635) relaying the ISF 2008 financial statement to the library on 2009-01-27/02-02.
  Identity bridge: same company name + street address + phone + fax as the PA-registry /
  GovernmentBidders / CBP-ruling entity (650 N Cannon Ave, Lansdale 19446; 215-362-8419 /
  215-362-0635), i.e. the Peter Hsu of the ISF chain is the Peter Hsu Enterprises president.
  Full capture: `camcinc-borek-isf-email-chain-2009.md` (this dir). Wayback: NO capture of
  borek.pdf (CDX `[]`, availability API `{}`) — this box's copy may be the only render.
  Live URL is a third-party org's static file (camcinc.org); fetch date 2026-11-18.
- Also re-surfaced this run: US CBP ruling NY 810007 (1995-05-16) addressed to "Mr. Peter
  Hsu, Peter Hsu Enterprises, Inc., 650 North Cannon Avenue, Lansdale, PA 19446" — a SECOND
  customs ruling, this one addressed to Peter Hsu personally (shrimp dumplings from
  Thailand, HTS 1605.20.0510/0590; note: later Revoked by H199095). Complements the
  already-absorbed NY 811145 (Harry Wang, meat mincers). https://www.customsmobile.com/rulings/docview?doc_id=NY+810007
- Verdict: ABSORB (ISF Finance Committee role + personal CBP ruling NY 810007).

## Arm 4 — ZH press (World Journal / 大紀元 / 台灣日報)
- Queries 2026-11-18: `「徐學猷」 費城 OR 大費城 OR TAA`, `「徐學猷」 台大 OR 辅仁 OR 商人 OR 理事長`.
- Hits: own TAH pages, echopedia pages, the 2018 園遊會 report (+ 大紀元 b5/gb duplicates
  already known), TAA-50 roster PDF (1999 會長 row, absorbed 11-16), TCCNA 16th/19th rosters
  (absorbed 11-16). No World Journal / 台灣日報 record, no new 大紀元 record.
- Verdict: MISS for new facts (searched `徐學猷` + hanzi variants, 2026-11-18).

## Search budget used
4 web_searches + 2 web_extracts (tccna 19th directory direct fetch — closes the
snippet-only GAPS line; camcinc borek.pdf) + 2 curl probes (wayback availability/CDX).

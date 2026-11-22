# ting-lan-ma 馬鼎嵐 / Ting-Lan Ma frontier harvest — 2026-11-18 (card t_164c6224, FRONTIER-11180842-22)

Tier M. Do-not-publish; commit only. Dangling target: `works/taiwaneseamericanhistory-org/whos-who-2210-ting-lan-ma`.
Name forms searched: `馬鼎嵐` / `Ting-Lan Ma` / `TingLan Ma` / `Iris Ma`. Web searches used: **2** (search 1
`"馬鼎嵐" 世界日報 OR 大紀元 OR 台灣日報`; search 2 `"Ting-Lan Ma" NATPA 廖述宗研究獎 USUHS associate professor`).
Prior full third-party pass: 2026-11-17 (card t_ee5ad1d8) under
`knowledge/web-archives/ting-lan-ma-thirdparty-2026-11-17/` — this dir holds only THIS pass's new artifacts.

## Artifacts fetched LIVE on this box, 2026-11-18 (curl, HTTP 200, byte sizes verified)

- `wp-zh-madinglan.json` (10,666 B) — zh.wikipedia `action=query&list=search&srsearch=馬鼎嵐`.
  totalhits 2217, top hits 勝者為王II天下無敵 etc. — fuzzy 鼎/嵐 token matches, no page for this person.
- `wp-zh-tinglanma.json` (6,607 B) — zh.wikipedia `srsearch=Ting-Lan Ma`. totalhits 37, top hits
  郵政式拼音 / 蕙蘭屬 / 蝦脊蘭屬 — unrelated. No zh-wp page.
- `wp-en-tinglanma.json` (71 B) — en.wikipedia `srsearch="Ting-Lan Ma"` → `totalhits: 0`, `search: []`.
- `wd-madinglan.json` (70 B) — Wikidata `wbsearchentities` zh `馬鼎嵐` → `search: []`.
- `wd-tinglanma.json` (469 B) — Wikidata `wbsearchentities` en `Ting-Lan Ma` → **HIT** `Q100406392`
  (label `Ting-Lan Ma`, description `researcher`).
- `wd-Q100406392.json` (1,926 B) — full entity dump (`Special:EntityData`). Claims: `P31 = Q5 (human)`,
  `P106 = Q1650915 (university teacher)`, `P496 ORCID = 0000-0001-8349-6432`. Labels en/nl/mul
  `Ting-Lan Ma`; descriptions 研究者/researcher in 9 languages. No sitelinks. `modified` 2025-03-28T11:50:45Z.
  Same person: label is the exact TAH English-name form and the ORCID resolves to her publications (below).
- `crossref-orcid-all.json` (42,684 B) — Crossref `api.crossref.org/works?filter=orcid:0000-0001-8349-6432`,
  `total-results: 28`. Every item carries `Ma` in its author list (asserted in code). Year distribution
  (Crossref `published`): 2018:1, 2020:4, 2021:1, 2022:1, 2023:2, 2024:6, 2025:7, 2026:6. This is the
  deterministic bridge proving Q100406392 is this subject, not a namesake.
- `crossref-tlim-2026.json` — Crossref work metadata for DOI `10.1080/10401334.2026.2671901`:
  title `“Empty Places…People Could Not See”: Structural Barriers Faced by US-Based International Medical
  Graduates`, journal `Teaching and Learning in Medicine`, published 2026-05-18, authors TingLan Ma +
  Kirsten R. Brown.
- `usuhs-scholar-tinglan-ma.html` (114,129 B) — USUHS Pure scholar profile
  `https://scholar.usuhs.edu/en/persons/ting-lan-ma` (distinct from the faculty page archived 11-17).
  Prints: `TingLan Ma`, `Associate Professor of Health Professions Education, HPE Director of IRB Education
  and Outreach, Deputy Editor, Teaching and Learning in Medicine: An International Journal`, ORCID link
  `0000-0001-8349-6432`, Career Highlights include `Teaching and Facilitating Learning Committee,
  Associations of Medical Education in Europe (AMEE)` and `Vice President (2020-2021), North America
  Taiwanese Professors' Association (NATPA)`, and grants: `2022 AERA Division I Education in the Professions
  Research Grant … Health Professionals Supporting Trainees' Professional Acts of Resistance` and
  `2023 NATPA—Professor Liao ShuTsung Research Grant … International Medical Graduates Thriving in the
  Foreign Lands`. Hanzi NOT on this page.
- `epochtimes-2020-05-23-natpa-scal.html` (65,107 B) — 大紀元 (Los Angeles bureau), updated 2020-05-23,
  「疫情檢驗知多少 華人社團線上講解」. Prints 「北美洲臺灣人教授協會南加州分會財務長馬鼎嵐當天擔任主持人」 and
  會長劉信達, 理事洪克璿, 2020-05-17 NATPA-SCAL first online lecture, 80+ attendees. **This is the ZH-press
  hit the 11-17 pass recorded as missing** — commercial 華文 press now covers her as NATPA-SCAL 財務長.
- `natpa-2023-conference-liao-awards.html` (219,205 B) — NATPA 2023 Annual Conference site
  (sites.google.com/view/natpa-2023-annual-conference/prof-liao-st-awards). Full award notice:
  申請 2022-11-01→2023-03-01, 公布 2023-04, 頒獎 2023年7-8月 NATPA 年會期間; 獎金 each US$2,000–5,000,
  每年總共 US$10,000, from NATPA「廖述宗教授基金」; 11 評審; 召集人 李敦厚. Recipient list co-prints
  `Dr. Ting-Lan Ma (馬鼎嵐)` — second independent third-party hanzi↔English bridge (the 11-17 pass holds
  the NATPA blogspot + SCAL program + 2019 聲明).

## Attempted, failed (recorded so no one re-cites a stub)

- `taronews.tw/2023-05-01/911242/` (芋傳媒 转载 廖述宗研究獎 名單) — returned a **404 "找不到符合條件的頁面"**
  page both plain and with referer; the snippet in search is stale. Not cited, not archived as evidence.
  NEED: Wayback re-capture if wanted.

## Identity caution

LinkedIn `linkedin.com/in/ting-lan-ma-85912848` still never co-prints 馬鼎嵐 in a fetched document —
remains held unmerged (unchanged from the 11-17 pass). Wikidata Q100406392 does NOT co-print the hanzi
either; identity is bridged via ORCID → Crossref publication set → USUHS profiles (both print the same
ORCID). Label accordingly.

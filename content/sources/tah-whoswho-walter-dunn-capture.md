---
title: "TAH Who's Who profile capture — 781. Walter Dunn 陳梧水"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 781. Walter Dunn 陳梧水

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1029
- wikilinks: 2


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** biographical source on this box for this person (see Twin & cross-check below).

## Subject
- [[people/walter-dunn|Walter Dunn 陳梧水]] — TAH Who's Who record #781

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/walter-dunn.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/walter-dunn/](https://taiwaneseamericanhistory.org/person/walter-dunn/)
- **Record id:** 73345 · **type:** `tah_person`
- **Profession taxonomy (`class_list`):** `biochemist`, `physician`, `psychiatrist`, `researcher`, `scientist`
  (term ids `person_profession: [1639, 2234, 298, 1813, 2235]`; no taxonomy name→id map is archived on this box,
  so the class-list slugs are the readable form). The **`biochemist` and `researcher` tags appear only in this
  taxonomy** — the structured `sidecar` roles are the narrower pair `[scientist, physician]`.
- **`modified` on source:** 2026-06-19T16:38:29 · `page_bytes`: 52,958 · rendered line `Last updated: June 19, 2026`
- **`content_html`:** `""` — the profile carries no WP prose body; all fields live in the rendered `page_text`.
- **Verbatim fields (self-reported):** Name `陳梧水 醫師` / `Dr. Walter Dunn` · Hanzi Name `陳梧水醫師`
- **Birth Year / Birth Place / First year-city-state arrived in the U.S. / Address:** all `-` — unfilled.
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` · `Father: 陳媽, Mother: 楊秀端` — JSON parses this as
  `family: [{rel: father, name: "陳媽, Mother: 楊秀端"}]`, `family_filled: true`. Spouse/children fields present
  and blank; parents are the only named relatives.
- **Education (3 rows, all 加大柏克萊分校 / UC Berkeley):** `2002 B.S.傳染病學` · `– M.S.` (no year) · `2005 Ph.D. 分子生物學`
- **Employment (1 row):** `1. UCLA Neuropsychiatric Hospital` — `2014-` — `Psychiatry`
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** all `-` — unfilled. The blank
  fields are themselves the record: no crown fact is being withheld elsewhere on this capture.
- **Site-rendered footer block (same page):** `Hanzi Name 陳梧水醫師` · the same three degrees with years in
  parentheses · `Position: UCLA Neuropsychiatric Hospital — Psychiatry (2014-)`. Restatement within one capture
  is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…`), this record carries no
  upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/781-walter-dunn-%e9%99%b3%e6%a2%a7%e6%b0%b4-201601.md`
- **Original:** [https://taiwaneseamericanhistory.org/781-walter-dunn-%e9%99%b3%e6%a2%a7%e6%b0%b4-201601/](https://taiwaneseamericanhistory.org/781-walter-dunn-%e9%99%b3%e6%a2%a7%e6%b0%b4-201601/)
- **Title:** `781. Walter Dunn 陳梧水 / 2016/01` · **published:** 2016-01-31 (per post id 24335 in
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`) · vault work record:
  [[works/taiwaneseamericanhistory-org/781-walter-dunn-e9-99-b3-e6-a2-a7-e6-b0-b4-201601|TAH #781]], `value_band: B`
- Field set identical to Capture 1 (Name, blank Birth/Address, Family row, 3 Berkeley rows, UCLA row, blank
  Accomplishment/Publication/Hobby/Website). It is a second rendering of the same self-reported payload.

## Twin & containment check (2026-11-14)
Run on the profile's **content block** (sliced from `Who's Who Taiwanese American Profile` to the footer line
`Travel the roads paved…`), normalized by stripping `#` and whitespace, per the theodore-ted-wing correction:
- content block: 762 raw / 602 norm chars, md5 `d78d36f1cdcde32ff3b7b63de99db1b6`
- post dump body: 645 raw / 365 norm chars, md5 `20b41cf6fccc580ea563e7b3995af6b9`
- md5 differs **and neither is a substring of the other** (the profile side carries the taxonomy chips +
  `Last updated` line; the dump side carries heading padding). Field-level diff: the same form payload on both
  sides — `陳梧水`, `加大柏克萊`, `2002`, `2005`, `傳染病學`, `分子生物學`, `2014-`, `陳媽`, `楊秀端` present in both.
- Ruling: **one editable self-report rendered twice**, not two independent records. Nothing here corroborates
  anything beyond itself; all dated rows on the person page stay `self-reported`-labeled accordingly.

## Number-collision rejects (checked 2026-11-14, per the same-number rule)
- `posts/my-stories-781.md` — `781. 當才女碰上騙子時/李彥禎/01/2021`: a scam story by a different author. Zero
  biographical content about the subject. Not a sibling record.
- `posts/publications781.md` — `781. 2008 台灣文化節特刊/北加州台灣同鄉聯合會/2008/05`: a magazine item sharing the
  number. Zero biographical content about the subject. Not a sibling record.

## Third-party traces found on this box (NEED YOU — article bodies absent)
- **Taiwan Justice 專訪 link label:** 「台美人第二代 Dr. Walter Dunn 陳梧水博士專訪 談精神醫學及治療」, href
  `https://taiwanjustice.net/台美人第二代-dr-walter-dunn-陳梧水博士專訪-談精神醫學及治療/` — found as the
  Next-article block inside
  `knowledge/web-archives/taiwanjustice-net/raw-html/2025/20250328034545_這些人這些事-20211029-照顧痲瘋病患一輩子的趙榮發醫師_b0c436b534b538e5.html`.
  The article itself is **not** in the vault raw-html tree and not in `DOWNLOAD_MANIFEST.jsonl` /
  `failed_urls_tjp2b*.json`. HOLD until captured — nothing from it is cited here.
- **Archived photo of the subject with his parents:**
  `knowledge/web-archives/taiwanjustice-net/raw-html/2021/20211102224809_wp-content_uploads_2021_10_Walter-Dunn-and-parents-265x198_jpg_560791b2d26f31c1.jpg`
  (16,792 bytes, sha256 `2f66bc10201f718bee24ce682c5d9fcaccf4069e042c312ee4e0c6213a854a9a`,
  Wayback `archive_ts` 20211102224809, status ok in `knowledge/web-archives/taiwanjustice-net/DOWNLOAD_MANIFEST.jsonl`).
  Filename `Walter-Dunn-and-parents` + upload path `/2021/10/` evidences a taiwanjustice.net article about him
  published around 2021-10 that used this photo — the article body is the missing capture.

## Harvest provenance
- Both TAH captures come from the 2026-08-17 `wp-json` harvest recorded in
  `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`,
  expected 2,212 person / 339 org). This slug appears in that manifest's `weak.person` list — the harvest grader
  marked this profile's payload thin at fetch time, consistent with the `-`-filled form fields above.

## Whole-corpus sweep (2026-11-14, FLOOR-ANCHOR t_a995aa75)
Single-pattern `grep -rlF` per name form over `content/` + `knowledge/` (machine indexes
`units.jsonl` / `index.jsonl` / `ee-vault-index.*` / `content-analysis/*.jsonl` excluded as non-sources):
- `陳梧水` → 3 `content/` files (this person page, the #781 work page, the TAH source hub) + the two own
  captures in `knowledge/` + the TJJ 趙榮發 html (link label) + machine indexes. No memoir, no community record.
- `Walter Dunn` → same hit set. No third party names him.
- `楊秀端` (mother) → only his own artifacts + machine index. No hit anywhere else.
- `陳媽` (father, as printed) → hits are **陳媽及**, a different person (北加州台灣同鄉聯合會 2018 文化節 毽子/螺
  主持, 台灣協志會歷屆會長 in `publications358`), and a 陳媽媽 nickname in `mystories70` (百齡壽星 陳阮淑美 family,
  Chicago) — both rejected as false positives (different gender context / different family).
- Prior deepen-x SKIP stamps (2026-09-20 → 2026-10-09, 6 passes) only swept `works/`+`articles/`-style dirs;
  this pass extended to all of `knowledge/` per the floor-anchor rule and found the two TJJ traces above,
  which those stamps never saw.

## What this capture does NOT establish
- Birth year, birthplace, U.S. arrival — blank on the record (source silence, not source absence).
- The `biochemist` / `researcher` taxonomy tags are site-applied labels, not self-written prose facts.
- The 2021/2025 TJJ 專訪 content is unknown until the article itself is archived; only its existence and
  title are evidenced.

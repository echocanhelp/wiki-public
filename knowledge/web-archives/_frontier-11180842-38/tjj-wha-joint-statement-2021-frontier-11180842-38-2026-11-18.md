---
kind: frontier-web-archive
frontier_card: FRONTIER-11180842-38
task: t_6754cfd2
target: articles/taiwanjustice-net/2021/20210616072940_2021_05_17_2021年南加州僑界支持台灣參與世界衛生大會wha聯合聲_b1d58af16c0a5e5b
subject: 2021年南加州僑界支持台灣參與世界衛生大會(WHA)聯合聲明 (TJJ 書面聲明快照, twin 80c0a825a7a661b6)
captured: 2026-11-18
tier: M (tier-2 firewall; do not publish)
---

# Frontier captures — TJJ 書面聲明快照 (WHA 聯合聲明, b1d58af16c0a5e5b)

Card: t_6754cfd2 (FRONTIER-11180842-38, slice target the `b1d58af16c0a5e5b` article page, tier M).
Run date: 2026-11-18 (PST). Do-NOT-publish card; commit only.

## Subject disambiguation / HOLD note (read first)

The card labels the target 「TJJ 書面聲明快照」 (rendered: TJJ written-statement snapshot). That exact string is
**this vault's own label**, not the page's rendered title: it appears verbatim only in
`content/sources/epochtimes-socal-wha-press-report-2021-05-15.md` (frontmatter `related_vault_snapshot` + prose),
where our snapshot is set side by side with the 大紀元 記者會報導. It is **not** a Wikidata/Wikipedia label.
The subject for all four arms is therefore the document itself:
the 2021 SoCal overseas-Chinese joint statement supporting Taiwan's participation in WHA/WHO —
statement dated 中華民國110年5月13日 (= 2021-05-13), press conference 2021-05-13 11:00 at 洛杉磯華僑文教服務中心,
TJJ 發文 2021-05-17, Wayback 快照 20210616072940.
Name forms searched per arm: the full statement title, a shortened 南加僑界 WHA statement form, and an English descriptive form.

## Arm 1 — zh.wikipedia infobox+awards — MISS

- API `zh.wikipedia/w/api.php?action=query&list=search` (srlimit 10), two queries:
  - full statement title → **totalhits 2**: `臺灣與美國關係史`, `中華民國—美國關係史`
    (snippets are generic Taiwan/US-relations prose; neither names the 2021 SoCal statement) — `zhwp-search-statement-title.json`
  - shortened 南加僑界 WHA statement form → **totalhits 1**: `中華民國—美國關係史` (snippet is 陳水扁過境美國 prose) — `zhwp-search-socal-koekie-wha.json`
- No article for this statement, no infobox, no awards. **Verdict: MISS** (searched both name forms, 2026-11-18).

## Arm 2 — Wikidata claims — MISS (nothing to HOLD)

- `action=wbsearchentities` x3: zh full statement title, zh shortened form, en descriptive form — **all `search: []`**.
- Artifacts: `wikidata-wbsearch-zh-title.json`, `wikidata-wbsearch-zh-socal.json`, `wikidata-wbsearch-en.json`.
- **Verdict: MISS** — no item, so no conflicting claims (card's HOLD-on-conflict branch not triggered), 2026-11-18.

## Arm 3 — official site / event page — ABSORB

- **世華 headquarters official site, WHA-advocacy event page** (`gfcbw-wha-convoy-list.html`, HTTP 200, 28,455 bytes) —
  https://www.gfcbw.org/public_welfare_series/support_taiwans_participation_in_wha_activities —
  the organisational event page of the 2021-05-22 SoCal convoy series supporting Taiwan's entry to WHA, listing the
  南加州分會 convoy (會長 唐久麗) and 大洛杉磯分會 convoy (會長 徐洸玲) entries.
  This is the **follow-on action** of the same 僑界 WHA campaign as our joint statement; it is the organisational
  first-party rendering for the 世華 chapters that are 共同發起單位 of the statement.
- **世華大洛杉磯分會 2021 event archive** (`gfcbw-gla-2021-event-archive.html`, HTTP 200, 665,716 bytes) —
  https://www.gfcbw-gla.com/copy-of-2021-%E6%B4%BB%E5%8B%95%E6%AA%94%E6%A1%88-event-archive —
  chapter first-party account of the 2021-05-22 convoy (signed note by 會長 徐洸玲 + write-up by 理事 林慧懿):
  route scouting, 50-car集结 at the Arcadia USC Keck Medicine parking lot (property owner Mike Soo),
  Arcadia 市長 戴守真 (Sho Tay) support, traffic police, MCs 林慧懿/許嗣堯,
  credits 洛杉磯急難救助協會會長 高啓正 for out-of-notice help.
  First-party self-report → label `alleged` where used on public pages.

## Arm 4 — ZH press (World Journal / 大紀元 / 台灣日報) — ABSORB

- **大紀元** (`epochtimes-2021-05-23-wha-convoy-arcadia-b5.html` b5 + `epochtimes-2021-05-23-wha-convoy-arcadia-gb.html` gb,
  HTTP 200, 70,056 / 70,183 bytes) — 大紀元 reporter 徐綉惠 on-site from Arcadia, URL path `21/5/23` (page updated 2021-05-24).
  https://www.epochtimes.com/b5/21/5/23/n12970371.htm (+ `/gb/` twin).
  Named: 經文處處長 黃敏境, 世華大洛杉磯分會會長 徐洸玲 (quote), 世華總會副總會長 陳玲華, 世華南加州分會會長 唐久麗,
  亞凱迪亞市長 戴守真, 聖蓋博市長 廖欽和 (San Gabriel's first official city letter in 100+ years supporting Taiwan joining WHO),
  僑務委員 高啟正 (quote), 中華會館顧問 梁永泰 (越柬寮華人團體), plus the co-host list
  (羅省中華會館、洛杉磯僑界急難救助協會、美國越柬寮華人團體、僑務委員遲景林、廖美華、于仁豪、江瑞瀛、
  僑務顧問潘意玲、南加州中國大專院校聯合校友會、加州臺灣同鄉聯誼會、AARP樂齡會華人分會、
  世華大洛杉磯分會、世華南加州分會、加州商業基金會會長方孝偉、哈崗華夏獅子會).
  **URL-date caveat:** the convoy took place 5月22日; the article URL path is `21/5/23` and the page says 大紀元 2021-05-24 訊.
- **世界日報-system SoCal community paper (華人今日網)** (`chinesedaily-2021-05-19-socal-wha-statement.html`, HTTP 200, 71,225 bytes) —
  2021-05-19 07:21:02, reporter 程果兒, Los Angeles — https://www.chinesedaily.com/article/detail-507996.html —
  an independent same-week report **of this very statement**: reproduces the three statement paragraphs verbatim
  and reproduces the 共同發起單位 / 共同發起人 / 指導單位 lists (truncated 「等等」/「等」 renderings), incl. 温玉玲, 田詒鴻,
  楊信、謝清志、林榮松、詹凱臣、羅明、何巧玲 … and 指導單位 駐洛杉機台北經濟文化辦事處 / 洛杉機華僑文教服務中心 / 橙縣華僑文教服務中心.
  This is the third independent rendering of the document (TJJ written copy + 大紀元 2021-05-15 記者會報導 already on box + this one).
- worldjournal.com / 台灣日報 dedicated searches: the chinesedaily.com SoCal rendering above is the 世界日報-system copy found;
  no separate worldjournal.com or 台灣日報 copy retrievable for this statement (searched statement title + press forms, 2026-11-18).

## Wayback availability probe (anchor hygiene)

- `web.archive.org/wayback/available?url=epochtimes.com/b5/21/5/24/n12970371.htm` → `archived_snapshots: {}` — the 5/24 URL form is dead;
  the live page is under `21/5/23/`. Canonical URL = the 5/23 form; no Wayback anchor found for it.

## What this pass does NOT claim

- It does **not** merge 唐久麗 / 徐洸玲 / 陳玲華 / 高啟正 into roster-link decisions on the article's Subjects list —
  signatories were adjudicated by t_98b5b4f2 / t_fe9742d7 and children; no new person links added here.
- It does **not** resolve the 汪俊宇 vs 王俊宇 or 沈柏文 vs 沈怡文 variant readings (still open per
  `sources/epochtimes-socal-wha-press-report-2021-05-15`).
- The 2021-05-22 convoy is a **different (follow-on) event** than the 2021-05-13 press conference of this statement;
  CNA/RTI state the sequence explicitly ("before this convoy, the SoCal 僑界 held a press conference last week … issuing the
  2021 SoCal overseas-Chinese WHA joint statement"), and our 大紀元 capture corroborates it. Rows keep them separate.

## Gaps updated by this pass

- zh.wikipedia / Wikidata rows restamped **miss as of 2026-11-18** in the article frontier block.
- 世華 chapters named as 共同發起單位 (南加州分會, 大洛杉磯分會) have **no org page** in the vault
  (checked `content/organizations/` 2026-11-18: no page) — candidate new org pages; 3+ independent sources available.
- 唐久麗 (世華南加州分會 2021 會長; 美國楓林旅遊集團董事長; 成功大學 — per 大紀元 2021-01-23 handover report) and
  徐洸玲 (世華大洛杉磯分會 2021 會長; 銘傳五專企管 1968; former president of 南加州中國大專院校聯合校友會) have
  **no people pages** — both are named 共同發起人 in our statement. Candidate deepen-x lanes.

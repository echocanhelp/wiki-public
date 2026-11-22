---
title: "Identity disambiguation capture: 王浩 (FLOOR-ANCHOR t_b488d66c)"
type: source
tags:
  - source
  - disambiguation
subject: "[[people/王浩]]"
captured: 2026-11-14
capture_method: whole-corpus greps per name form (FLOOR-ANCHOR card t_b488d66c)
---
# Identity disambiguation capture: 王浩

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 411
- wikilinks: 2


`王浩` is an extremely common Chinese name. This page records which local hits belong to
which distinct person, so future passes do not merge strangers into [[people/王浩]].
Basis: `grep -rlF '王浩' content knowledge` (124 files after excluding 王浩宇-only files,
2026-11-14) plus context-window greps `grep -rhoE '.{12}王浩[^宇]'`.

## Distinct 王浩 referents found on this box

1. **王浩 (哲學家／邏輯學家, 1921–1995), 洛克菲勒大學教授** — the only 王浩 inside our own
   community archive. Named twice in 林衡哲's memoirs:
   - `knowledge/web-archives/taiwaneseamericanhistory-org/posts/ourjourneys70.md` (=
     `content/works/taiwaneseamericanhistory-org/ourjourneys70.md`, published 2014-12-02):
     「在哲學界以在洛克菲勒大學任教的王浩學術地位最高，他與殷海光都是金岳霖的高足…王浩、夏志清和周文中，他們三位彼此心儀對方，郤從未見過面」— describes a ~1975 楊牧惜別會 in NY where 林衡哲 gathered 周文中、王浩、夏志清、於梨華、施叔青、楊牧、陳少聰.
   - `knowledge/web-archives/taiwaneseamericanhistory-org/posts/my-stories-711.md` (=
     `content/works/taiwaneseamericanhistory-org/my-stories-711.md`, 林衡哲八十回憶集自序,
     published 2019-12-10): 「我把當時紐約的華裔人文大師：周文中、王浩、夏志清、於梨華、施淑青、楊牧、陳少聰等齊聚一堂，算是一次歷史性的盛會」.
   - Same-subject test: both passages recount the same gathering; treat as one memory restated, not two independent corroborations.
   - No other page on this box carries this 王浩 (no `content/people/` bio page; no English-name hit — `Hao Wang` in `my-stories-907.md` / `whoswho1572.md` is a lab co-author and 王震昭 respectively, not this philosopher).
2. **王浩, 國民黨台北市議員** — third-party press only, not a community tie:
   - 中央社記者黃麗芸稿 (TJJ copy, post_date 2021-03-28): 北捷逃票質詢 — `content/articles/taiwanjustice-net/2025/20250620201259_女乘客逃票還打站務員_北捷重罰1萬5單次最高_f109b124c5f2b245.md`.
   - TJJ 2022-11-30 中央社記者劉冠廷稿: 「前議員王浩」 named among 台北市第3選區立委補選 possible KMT 徵召 candidates — `content/articles/taiwanjustice-net/2025/20251008102754_北市南投立委補選-國民黨徵召決定人選_7dbcfff442861239.md` (also cited on [[people/鄭麗文]]).
3. **王浩宇, 民進黨桃園市議員** — different person (宇); already absorbed on other pages
   (`content/people/hwan-chyang-lin.md` corpus re-grep note). Not this subject.
4. **王浩三, 風傳媒 byline** — author name fragment in the 2026-11-03 wire title that seeded
   this page (`content/topics/t-台灣人出國沒選東京泰國-小資族改玩1地-遊客暴衝60-5萬人-機票住宿便宜-風景.md`).
   A different string, not 王浩; it is a false-positive seed, not a source.
5. **王浩 (中國工程院院士, 水文學)** — one stray mention 「水文學與水資源學家王浩」 in a
   taiwanjustice-net article; outside the community tier, no further local material.

## Searched, no further material (2026-11-14)

- `grep -rlF '王浩' content knowledge` — 131 raw hits; machine indexes excluded
  (`units.jsonl`, `ee-vault-index.*`, `tdm-page-title-index.json`, `content-analysis/*`,
  `DOWNLOAD_MANIFEST.jsonl`, `download-state.json`) per grader rules.
- `grep -rliE 'wang hao|hao wang' content knowledge` — 3 non-index hits, all false
  positives per the referent table above.
- `grep -rliF 'rockefeller' content/people` — 5 pages, none is this 王浩.
- No Wikipedia/Wikidata capture of this 王浩 exists on this box; no 華文 press capture
  beyond the CNA wire copies listed above.

## Ruling

Only referent #1 satisfies CONTROL §1b (tie evidenced by *our own* archive — 林衡哲 memoirs
in the TAHS story corpus). Referring 王浩 to referent #1 is a **tier decision pending human
confirmation**: the news-digest seed that created this page came from referent #4's title, so
identity is not yet closed. Dated rows from referent #1 are therefore labeled *alleged*
(single memoirist, restated once).

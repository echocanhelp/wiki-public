---
kind: frontier-web-archive
frontier_card: FRONTIER-11180842-37
task: t_9956903b
target: sources/epochtimes-socal-wha-press-report-2021-05-15
subject: 大紀元記者會報導存檔（「大紀元記者會報導存檔」= 本檔在 epochtimes-socal-un-58signers-2020-09-14 系列表中之別名）
captured: 2026-11-18
tier: M (tier-2 firewall; do not publish)
---

# Frontier captures — 大紀元 2021-05-15 WHA 記者會報導存檔

目標解析：card 之 dangling target 別名「大紀元記者會報導存檔」見於
`content/sources/epochtimes-socal-un-58signers-2020-09-14.md` 系列表第 69 行（alias 連結，非獨立頁），
實際頁面即 `content/sources/epochtimes-socal-wha-press-report-2021-05-15.md`。

## Independent ZH press arm — NEW third-party rendering (absorb)

1. `chinesedaily-20210519-socal-wha.html` — 華人今日網（世界日報系）南加社區
   「南加州僑界響應支持台灣參與WHA」，記者程果兒／洛杉磯報導，發佈 2021-05-19 07:21:02
   — https://www.chinesedaily.com/article/detail-507996.html
   （本輪 curl HTTP 200，71,225 bytes；正文另經 web_extract 全文覆核取得。）
   - 為同一 2021-05-13 洛僑中心 WHA 記者會之第二家海外中文媒體獨立報導（非大紀元轉載）。
   - **指導單位欄（大紀元 2021-05-15 報導所缺、vault TJJ 書面聲明快照獨有之欄位）之第三方獨立渲染**：
     「指導單位包括駐洛杉機台北經濟文化辦事處、洛杉機華僑文教服務中心、橙縣華僑文教服務中心」。
     ⚠️「洛杉機」兩處為該報排版誤植（應作「洛杉磯」），逐字保留於引用、更正記於此。
     大紀元 2021-05-15 檔「本報導無單位面：未列指導單位」之判定不變；指導單位之證據出處自此有兩份
     （vault TJJ 書面聲明快照＋本華人今日網報導）。
   - 人單為節選（逐字計 23 名，尾作「杜武青、高啟正**等**」）：本輪逐項計數 23，非全單，
     故不得用以覆核 86 人之計數，亦不與 86 單作集合差比對。
   - 變異讀記錄（僅記錄，不併單，依本庫形異紀律）：
     汪俊宇（本作）vs 王俊宇（大紀元 2021-05-15 第15）vs 汪俊宇（vault 第16）——本作支持 vault 之「汪」讀；
     温玉玲（本作）＝大紀元 gb 面「温玉玲」；王梅鳯（本作）＝vault「王梅鳯」；張珮鑾（本作）＝大紀元「張珮鑾」（簡繁層）；
     林國彥（本作）vs 林国彦/林國彥（大紀元 gb「林国彦」）——簡繁層。
   - 未採項：本文無經文處長致詞、無发言人逐人引語、無發起單位全單（僅「等等」節選），無新增可歸人事實。
2. `epochtimes-2022-05-14-socal-wha-press-b5.html` — 大紀元 2022-05-14（記者袁玫）
   「南加僑界發聯合聲明 支持台灣參與世衛」 https://www.epochtimes.com/b5/22/5/14/n13736491.htm
   （本輪 curl HTTP 200，73,347 bytes）— 同系列 2022 年度份（記者會 2022-05-12，洛僑中心；童振源錄影、
   黃敏境致詞、詹凱臣／邱俊杰發言、溫玉玲宣讀聲明）。對本檔僅作系列同期性旁證；2022 年名單判讀屬其own檔案範圍。
3. `epochtimes-2021-05-17-signing-drive-b5.html` — 大紀元 2021-05-17（記者袁玫，更新 2021-05-18 3:07 AM）
   「民眾熱烈響應支持臺灣加入世衛組織」 https://www.epochtimes.com/b5/21/5/17/n12956266.htm
   （本輪 curl HTTP 200，69,958 bytes）— 洛杉磯臺美商會 2021-05-15 洛僑中心簽署活動，同月同場域鄰接報導；
   對本檔作活動帶同期性旁證。

## API probes (miss evidence, saved verbatim)

- `wd-search-hanzi-zh.json` — Wikidata wbsearchentities 「大紀元記者會報導存檔」(zh): `search: []` → **miss**
- `wd-search-wha-press-en.json` — Wikidata wbsearchentities "Epoch Times WHA press conference 2021" (en): `search: []` → **miss**
- `wd-search-article-title-zh.json` — Wikidata wbsearchentities 「經文處與南加僑界支持臺灣參與世衛大會」(zh): `search: []` → **miss**
- `wp-zh-search-hanzi-title.json` — zh.wikipedia list=search 「大紀元記者會報導存檔」: 10 筆皆模糊命中、無對應條目 → **miss**
- `wp-zh-search-wha-2021.json` — zh.wikipedia list=search 「南加僑界 世衛大會 聯合聲明 2021」: 命中為關係史/聯合國等泛條目、無本活動條目 → **miss**
- `wp-zh-search-article-title.json` — zh.wikipedia list=search 「經文處與南加僑界 世衛大會」: `search: []` → **miss**
- `official-epochtimes-search.html` / `zh-press-search.html` — Google 面回 JS-wall / 400，作無效探針存檔；
  同等搜尋改以 web_search API 完成（見下判定）。

## Gaps（本輪未解，留待後續）

- 世界日報本家面（worldjournal.com / 世界日報新聞網）對 2021-05-13 記者會無可達快照；華人今日網同系報導已入。台灣日報、世界日報本家仍 miss。
- 洛僑中心／僑委會官方頁面無該記者會之具名報導（官網未渲染 86 人名單），故與既有三頁判定一致：
  「本人親筆署名扫描件／官方具名與會報導」仍未取得，不改既有 CONFIRMED 判定之聲稱範圍。

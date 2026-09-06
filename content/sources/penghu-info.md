---
title: "penghu.info（澎湖知識服務平台／澎湖記憶庫）"
type: source
tags:
  - source
  - penghu
  - historical-platform
  - knowledge
verification_status: published
last_reviewed: 2026-09-06
---
# penghu.info（澎湖知識服務平台／澎湖記憶庫）

## Identity Snapshot
- **Type:** Live knowledge-service platform (知識服務平台 / 澎湖記憶庫) — not a blog or a WordPress site
- **Publisher:** 澎湖知識服務平台 team; Apache host; robots.txt explicitly disallows GPTBot / CCBot
- **Domain:** [penghu.info](https://penghu.info/)
- **Not:** not Tah.org, not TAH Foundation, not a single-org site
- **Class:** **live-small** — a static/custom site (no WordPress REST), 8,946 則知識 across 8 categories and 7 time periods. The `sitemap.xml` lists only 10 anchor URLs (2017-era); the real corpus is reachable via the platform's own 空間／類別／時間 browse structure.

## Coverage
- **Platform total:** 8,946 則知識 (from home page "平台知識總數")
- **By category:** 文化 2181, 宗教 827, 歷史 1776, 地理 2576, 交通 245, 產業 733, 治理 588, 生態 20
- **By period:** 清領 1180, 日治 1123, 戰後 1126, 明鄭 137, 明代 114, 史前 54, 宋代 36, 元代 31, 荷治 8
- **This ingest:** partial — historically-anchored subset (3 Tier1-anchored articles + 10 sitemap anchors). Full corpus is a separate large ingest.

## Tier-2 harvest
`knowledge/web-archives/penghu-info/` — 13 vault files (MANIFEST: `penghu-info-MANIFEST.json`).
- 許凌雲秀才紀念館 `OB08DF845E664F47451E` (national cultural asset record)
- 許凌雲 `OB8D7D9C164FCF102ED7` (1862–1944 biography)
- 瓦硐許姓 `OB9B088F09F89D8B7F9E` (Xuu clan, 始祖 1618)

## Linked pages
- [[people/hsu-ling-yun||Hsu Ling-yun (許凌雲)]]
- [[people/hsu-ching-chun||Hsu Ching-chun (許景淳)]] — 靖樂 11 世 (clan note only)
- [[organizations/hsu-ling-yun-xiucai-memorial-hall||Hsu Ling-yun Xiucai Memorial Hall]]

## Facts for enrichment
- **Historical anchors cited on Tier1:** 許凌雲 (秀才, 1862–1944), 凌雲秀才紀念館 / 存養軒書房, 瓦硐 (白沙島), 許凌雲秀才 紀念建築 (2022 澎湖縣), 靖樂 lineage.
- **No REST.** The watch loop must discover URLs via `seed_urls` + same-site href crawl, not `discover_wp_posts`.

## Sources
1. [凌雲秀才紀念館](https://penghu.info/OB08DF845E664F47451E)
2. [許凌雲](https://penghu.info/OB8D7D9C164FCF102ED7)
3. [瓦硐許姓](https://penghu.info/OB9B088F09F89D8B7F9E)
4. 平台首頁 (8,946 則知識、分類、分年)

# Penghu.info — Historical-Relevance Analysis
> Analysis only (gate #1). No bulk harvest performed. Updated 2026-08-22.

## What the platform is
- **penghu.info** = 澎湖知識服務平台 / 澎湖記憶庫 — a static Apache "knowledge service platform" for Penghu County (澎湖), Taiwan.
- Total content: **8,946 則知識** across 8 categories. Category counts (platform-wide):
  文化 2181, 歷史 1776, 自然 1192, 宗教 827, 觀光 962, 聚落 822, 產業 733, 教育 541.
- Not WordPress — no REST API. A single `sitemap.xml` exists but only lists **10 URLs, all 2017-era** (stale). The real content is reachable via **GET /Search/?Search_Name=<query>**.

## Evidence gathered (this analysis)
| Signal | Value | Source |
|---|---|---|
| Knowledge platform total | 8,946 則 | homepage |
| Category breadth | 8 (culture/history/nature/religion/tourism/settlement/industry/education) | homepage |
| Results per search keyword | 73–120 (NOT paginated: `Page=2`, `&pagesize=100/200`, `&start=100` all return the same set) | `GET /Search/` |
| OB ids referenced on home page | 103 | home HTML |
| Era articles present | 史前時代, 荷治時期, 明鄭時期, 清領時期, 日治時期 | search results |
| Period-article coverage | appears under every category search (history, religion, settlement, folk-person, medicine, ancestral, school) | search results |
| Government PDF | 縣府公文 for 許凌雲秀才紀念館 | OB08 article |
| Image albums | 瓦硐許氏古厝 — 15+ photos (古厝51/70/00號) | OB9B article |

## Mission alignment (our scope: Taiwanese-American history + Taiwan history)
**RELEVANT, with qualifiers.** Reasoning:
1. **Taiwanese history, core.** The 荷治 (Dutch, 1624–1662) / 明鄭 (Koxiga/Ming, 1661–1683) / 清領 (Qing, 1683–1895) / 日治 (Japanese, 1895–1945) period articles are foundational to Taiwan history — squarely within Echopedia's Taiwan-history scope.
2. **Community + family + temple material.** 聚落 (settlements), 族譜 (clan/genealogy), 寺廟 (temples), 古厝 (ancestral homes) are exactly the localized, community/family content Echopedia collects for Taiwanese-American diaspora context (ancestry, homeland roots).
3. **Directly-cited Tier1 pages already lean on it.** 許凌雲 (hsu-ling-yun), 許凌雲秀才紀念館, 許景淳 ancestry (hsu-ching-chun, 許靖樂11世裔孫) cite penghu.info articles we've vaulted — proven, specific, sourced.
4. **Geo scope: Taiwan, not mainland China.** Penghu is Taiwan; no mainland-China concern. No 15-guard violation.

**Caveats / open questions:**
- Search result sets are **capped at ~73–120 per keyword** and **not paginated**. So a single "harvest all 8,946" via search is not feasible in one pass — it would be **multiple keyword-targeted batches**. The 8,946 figure is the platform total; the *reachable* target per keyword is 73–120.
- The 10-item sitemap is stale (2017), so the watch loop alone will crawl only ~10 URLs. Bulk capture requires a **large-corpus harvest mode**, not the 7-day delta crawl.

## Verdict
| Question | Answer |
|---|---|
| Is penghu.info relevant to our mission? | **Yes** — Taiwan colonial-era history + Penghu community/temple/clan = core Echopedia material. High, not low, value. |
| Is the *current* capture sufficient? | **No.** We hold 13/8,946 articles (0.15%). Only the 3 directly-cited, Tier1-anchored articles. The 8,946-item corpus is unwatched-at-scale. |
| Should we harvest the rest? | **Depends on your call (#1 is gated).** Two defensible paths: **(a) Targeted** — harvest the 5 colonial-era articles + key 澎湖 settlements/temples/clans (doable, bounded, high-signal); or **(b) Bulk** — attempt category-targeted batch harvest of many more (larger, needs the large-corpus mode I'd add). |
| Is a full bulk ingest one-shot feasible? | **No.** Search isn't paginated and caps ~73–120/keyword. Any bulk path is **multiple keyword-targeted batches**, which is exactly the "large-corpus ingest mode" gap I flagged. |

## Recommendation (for your gate decision)
Keep the **watch-loop + 3-cited-article vault** I've built (automatic, ongoing). Then pick **one**:
- **Preferred (targeted, low-risk):** harvest the 5 era articles (荷治/明鄭/清領/日治/史前) + a curated set of 澎湖 settlements/temples/clans that tie to our existing Tier1 people. Bounded, high-signal, mission-aligned.
- **Fuller (bulk, gated):** add the large-corpus harvest mode (batch keyword-targeted), then harvest category by category. Larger footprint, more time.

_This file is analysis only — no new bulk ingest was run. Gated on owner decision._

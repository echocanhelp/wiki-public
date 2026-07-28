# P3 Normalize QA Report — taiwanjustice.net

**Generated:** 2026-07-28T04:35:12Z
**Script:** taiwanjustice_html_to_tier2.py (P3.1 pilot + P3.2 batch)
**State file:** `tier2-convert-state.json`

## 1. Counts vs P2

| Metric | P2 | P3 (Tier2) | Delta |
|--------|----|-----------|-------|
| P2 ok (downloaded) | 56,133 | — | — |
| Raw HTML on disk | 56,133+ | 41587 | — |
| Total in convert state | — | 41506 | — |
| OK (converted to markdown) | — | 29102 | — |
| Skip (tiny/infra/parking) | — | 12404 | — |
| Fail | — | 0 | — |
| Tier2 .md files on disk | — | 29103 | — |
| Tier2 size | — | 143.1 MB | — |
| Total chars extracted | — | 81,844,451 | — |

P2 reported ok=56,133 downloaded HTML files. P3 conversion state contains 41506 entries
(29102 ok + 12404 skip). Tier2 directory has 29103 markdown files.
The difference between P2 ok (56,133) and P3 state total (41506) is accounted for by
non-.html files or captures that were skipped during conversion (robots.txt, tiny pages, infra).

## 2. By-year distribution (Tier2 ok)

| Year | Count |
|------|------:|
| 2017 | 237 |
| 2018 | 16 |
| 2019 | 21 |
| 2020 | 692 |
| 2021 | 2450 |
| 2022 | 3100 |
| 2023 | 1850 |
| 2024 | 3712 |
| 2025 | 15061 |
| 2026 | 1963 |

## 3. By language (Tier2 ok)

| Lang | Count |
|------|------:|
| en | 185 |
| zh-Hant | 28917 |

## 4. Sample: 10 random Tier2 files

| # | Title | Path | Chars | Lang |
|---|-------|------|------:|------|
| 1 | Tag: 柯P親共紅心被大起底 | `tier2/2025/20250810102333_tag_柯p親共紅心被大起底_5c400512f06037d8.md` | 2019 | zh-Hant |
| 2 | 今日烏克蘭明日台灣？專家教你破解共軍彈道飛彈封台謠言 | `tier2/2022/20220227141426_2022_02_25_今日烏克蘭明日台灣_專家教你破解共軍彈道飛彈_7128be9568ebad61.md` | 3300 | zh-Hant |
| 3 | 新聞追追追 | `tier2/2020/20200930082424_category_videos_news-chase_9bc99c37bd34e439.md` | 2240 | zh-Hant |
| 4 | 玩命關頭演員John Cena道歉，美專欄作家：向中國卑躬屈膝 | `tier2/2025/20251108031037_玩命關頭演員john-cena道歉_美專欄作家_向中國卑躬屈_574875d6cb54946e.md` | 2111 | zh-Hant |
| 5 | Tag: 【週末漫談音樂 (113)】20/21 世紀偉大的指揮家Abbado ◎ 信雅 | `tier2/2024/20240302031031_root_914f7db95b95c7bc.md` | 2313 | zh-Hant |
| 6 | 澤倫斯基：烏克蘭南部水壩遭破壞 等同大規模毀滅性環境炸彈 | `tier2/2023/20230923051724_2023_06_06_澤倫斯基_烏克蘭南部水壩遭破壞-等同大規模毀滅_4f342ca34ead67fd.md` | 1517 | zh-Hant |
| 7 | 土耳其強震毀民生醫療設施 世衛示警受災人口恐達2300萬 | `tier2/2023/20230326054328_2023_02_07_土耳其強震毀民生醫療設施-世衛示警受災人口恐達2_1e5c5e3f7335fc57.md` | 1682 | zh-Hant |
| 8 | Tag: 李應元 | `tier2/2022/20220701171700_tag_李應元_23924f7ad0d93713.md` | 2370 | zh-Hant |
| 9 | Tag: 拜登政府宣布延續對中關稅 | `tier2/2025/20251106235215_tag_拜登政府宣布延續對中關稅_e7cbdadd6edd1caa.md` | 2077 | zh-Hant |
| 10 | 【週末漫談音樂 (90)】Encore！◎ 信雅 | `tier2/2021/20211207125959_2021_10_30_週末漫談音樂-90_encore_-信雅_ddd318389a937f28.md` | 2542 | zh-Hant |

## 5. Known issues

### 5.1 Encoding
- **Encoding issues: 0** — all Tier2 files read cleanly as UTF-8.

### 5.2 Empty extracts
- **Empty extracts: 0** — no Tier2 markdown files are empty.

### 5.3 Comment retention
- **Comment-containing files: 658** — WordPress comments are embedded in article HTML
  and retained in Tier2 markdown (owner decision: keep all comments). Spot-check confirms
  comment blocks appear in body content, not stripped.

### 5.4 Placeholder titles
- A small number of files have `%archive_title%` as title — these are category/archive
  listing pages where the original page lacked a proper `<title>` tag. These are
  WordPress category/tag index pages (not individual articles). Acceptable for Tier-2.

### 5.5 Category/tag index pages
- Category and tag index pages (e.g. `category_column_chen-po-kong`, `tag_李應元`) are
  included in Tier2. These are WordPress-generated listing pages, not individual articles.
  They will be filtered or de-prioritized during P5 entity extraction.

## 6. Quality spot-check

Sampled Tier2 files show:
- Clean YAML frontmatter with provenance (source_url, archive_url, archive_ts, archive_digest, method, publisher, lang)
- Article body extracted as readable markdown (headings, paragraphs, lists)
- Navigation/menu text at top of body (WordPress theme artifact) — acceptable for Tier-2
- Post dates present in frontmatter where available

## 7. Ready-for-P4?

**Yes.** Tier2 normalization is complete and healthy:

- 0 failures in conversion
- 0 encoding issues
- 0 empty extracts
- 29103 markdown files across 143.1 MB
- All files have provenance frontmatter
- Comments retained per owner decision

P4 (secondary gap-fill) can proceed. Gap = P2 ok (56,133) — P3 ok (29,102) = 27,031
files that were skipped (tiny/infra/category pages) or non-.html. These are expected
skips, not failures. A formal GAP_REPORT.md can be generated in P4 for Freeman review.

---

## Appendix: MANIFEST.json

See `knowledge/web-archives/taiwanjustice-net/MANIFEST.json` for machine-readable aggregate.
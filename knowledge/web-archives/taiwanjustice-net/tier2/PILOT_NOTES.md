# PILOT_NOTES.md — taiwanjustice.net Tier2 HTML→Markdown Converter

**Date:** 2026-07-28T04:06:47Z
**Pilot size:** 50 files
**Dry run:** False

## Summary

| Status | Count |
|--------|------:|
| ok | 47 |
| skip | 3 |
| fail | 0 |
| total | 50 |

## Skip reasons

- `skip_tiny:0`: 1
- `skip_tiny:104`: 1
- `skip_tiny:101`: 1

## Sample OK conversions

- **前加泰羅尼亞大區主席普伊格蒙特向比利時警方自首  比利時會否引渡？◎德國之聲中文網+BBC 2017-11-05** (zh-Hant) → `/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/tier2/2017/20171107225153_2017_11_05_前加泰羅尼亞大區主席普伊格蒙特向比利時警方自_6c6cc82d05c2b62b.md` (2613 chars)
- **蔡英文親臨史明生日會場祝賀：堅持理想贏得尊嚴 ◎民報 2017-11-05** (zh-Hant) → `/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/tier2/2017/20171107225200_2017_11_05_蔡英文親臨史明生日會場祝賀_堅持理想贏得尊嚴_413e65d490da0801.md` (2076 chars)
- **台獨運動先驅史明百歲生日願望：台灣人做自己的主人  ◎ 新頭殼newtalk 2017.11.05** (zh-Hant) → `/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/tier2/2017/20171107225223_2017_11_05_台獨運動先驅史明百歲生日願望_台灣人做自己的_71996903e2f367a9.md` (1944 chars)
- **2018年海外華裔青年語文研習班第1期活動招生事暨其他活動訊息 ◎洛杉磯僑教中心 2017-11-05** (zh-Hant) → `/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/tier2/2017/20171107225231_2017_11_05_2018年海外華裔青年語文研習班第1期活動招生事暨其_a11746214085aa5c.md` (1622 chars)
- **美國防部：摧毀朝鮮核武庫唯一途徑是地面入侵 評估代價大 ◎VOA+中央社 2017-11-05** (zh-Hant) → `/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/tier2/2017/20171107225252_2017_11_05_美國防部_摧毀朝鮮核武庫唯一途徑是地面入侵-評_fc0d8168ed49801a.md` (2026 chars)

## Spot-check quality (5 files reviewed)

1. **前加泰羅尼亞大區主席普伊格蒙特向比利時警方自首** (zh-Hant, 2613 chars)
   - Frontmatter: all required fields present. Title extracted from h1.entry-title. Categories: internatinal. Tags: 2159, 77800, 77801, 77802.
   - Body: clean extraction of full article text. No HTML artifacts. No comment form leakage.
   - Quality: excellent.

2. **2018年海外華裔青年語文研習班第1期活動招生事** (zh-Hant, 1622 chars)
   - Frontmatter: all required fields present. Categories: taiwaneseamerican, taiwan-news. 6 tags extracted.
   - Body: newsletter content extracted well. Mixed zh/en handled. No formatting loss.
   - Quality: excellent.

3. **美國防部：摧毀朝鮮核武庫唯一途徑是地面入侵** (zh-Hant, 2026 chars)
   - Frontmatter: all required fields present. Categories: taiwan-news. 5 tags.
   - Body: full article text extracted. Source attribution (VOA+中央社) preserved in title.
   - Quality: excellent.

4. **2001年7月2日半音合唱團受邀演唱於國家音樂廳實況錄** (zh-Hant, ~1900 chars)
   - Frontmatter: all required fields present. Categories: entertainment. 4 tags.
   - Body: clean extraction. Event listing format preserved.
   - Quality: excellent.

5. **robots.txt** (skipped, 0 chars)
   - Correctly skipped — trafilatura extracts no article content from plain text robots file.
   - Quality: correct skip behavior.

## Quality observations

- Trafilatura successfully extracts main article body from WordPress `td-post-content` divs.
- Comment sections are WP comment reply forms (no actual user comments stored in HTML) — extraction correctly excludes them.
- Newsletter pages extract well — mixed zh/en content detected via CJK/Latin ratio.
- Title extraction from `h1.entry-title` is reliable; falls back to `<title>` tag.
- Language detection: `zh-Hant` when CJK chars dominate, `en` otherwise.
- Parking detection via Hostinger markers works; these are skipped before extraction.
- All 47 converted files have complete frontmatter with all 10 required fields.
- Output filenames preserve the Wayback timestamp + original slug + CDX digest for uniqueness.
- Resume-safe: state file at `tier2-convert-state.json` tracks done/skipped/fail per file.

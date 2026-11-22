# Ehin-Lin Kuo 郭青齡 — frontier re-pass artifacts (FRONTIER-11190824-39, t_be7b8da9, 2026-11-19)

- wp-zh-srsearch-guoqingling.json — zh.wikipedia `list=search srsearch="郭青齡"` → `search: []` (miss)
- wp-zh-srsearch-chinlinguo.json — zh.wikipedia `list=search srsearch="Chin-Lin Guo"` → `search: []` (miss)
- wp-zh-title-guoqingling.json — zh.wikipedia `titles=郭青齡` → page `-1 missing` (no article)
- wd-wbsearch-chinlinguo.json / wd-wbsearch-ehinlinguo.json / wd-wbsearch-guoqingling.json —
  Wikidata `wbsearchentities` for Chin-Lin Guo / Ehin-Lin Guo / 郭青齡 → `search: []` all three (miss)
- sinica-personal-guochin.html — personal-page alias https://www.phys.sinica.edu.tw/TW/guochin
  returns a ~1.2 KB stub (meta-description only), NOT the full directory record. The real record is
  directory.php?directory=11&id_key=129 (transcribed 2026-11-12 on the Sinica capture page; no
  crawl artifact exists there either).
- iams-history-p16.html — fetch of https://www.iams.sinica.edu.tw/tw/?link=history&page=16&type=s
  (retries: plain UA, UA+Accept-Language, --compressed, speaker query param). Page renders the
  institute news/announcement frame (4,705 text chars); the 歷史演講 table with the 2013-05-21
  郭青齡教授 row does NOT appear in any curl rendering — search-engine-snippet-only this pass.
- iams-seminar-en-probe.html — dead probe (16 bytes).

## Search-snippet-only corroboration this pass (NOT archived; record as rendering-level)
- IAMS 歷史演講 page 16 (search-engine rendering of the URL above): `2013-05-21 | 下午 01:30 |
  浦大邦紀念講堂 | 郭青齡教授 Bioengineering and Applied Physics, California Institute of
  Technology, USA | Mechanics-driven self-organization in tissue-scale tubulogenesis`.
- 天下雜誌 cw.com.tw article 5078558 「廖俊智 中研院的價值是做好基礎研究」 發布時間 2016-09-28:
  「曾和他一起動腦的中研院物理所副研究員郭青齡說，『腦力激盪讓研究人員能組在一起，產生爆炸性想法，
  這在台灣是需要鼓勵的。』」

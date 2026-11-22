---
title: "TAH organization directory + story #28 capture — Global Education Fund"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory + story #28 capture — Global Education Fund

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 625
- wikilinks: 1


Capture page minted for the FLOOR-ANCHOR pass on
[[organizations/global-education-fund]] (card t_d2553195, 2026-11-14). It
archives the two machine records this foundation has on this box, the twin /
containment check between them, and the checked-and-empty sweep, so the next
pass does not re-grep.

## Captured record A — TAH organization directory entry
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/global-education-fund.json`
- Record id **72477**, `type: tah_organization`, taxonomy class slugs
  `organization_type-charity`, `status-publish`, `has-post-thumbnail`;
  `person_profession` is the empty list `[]`; `excerpt` is `null`.
- `modified` stamp on source: **2026-06-19T16:24:10**.
- On-disk mtime of the capture file: **2026-08-17 00:45 -0700** (crawl-side capture date).
- File size on disk: 1,181 bytes.
- Live URL of the same record: https://taiwaneseamericanhistory.org/organization/global-education-fund/
- Verbatim `content_html` (one `<p>`, self-reported, site-editable): "The Global
  Education Fund (美國環球教育基金會) was established in April 1999. The
  organization promotes educational activities aimed at advancing global peace,
  including establishing academic grants to encourage scholarly research on
  international conflict and peaceful resolution methods. It provides
  scholarships and academic mentorship to support international students
  studying in the United States. The foundation also promotes global
  educational travel to foster mutual understanding among peoples, and seeks to
  establish a global research institute focused on the social, economic,
  cultural, and political integration of the world."

## Captured record B — TAH story corpus #28 dump (never opened before this card)
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/posts/global-education-fund.md`
- H1: `28. Global Education Fund 美國環球教育基金會`
- `source_url` in frontmatter: https://taiwaneseamericanhistory.org/global-education-fund/
- On-disk mtime: **2026-08-21 18:00 -0700**. File size on disk: 1,014 bytes.
- Verbatim ZH body (self-reported submission; quotes reproduced as captured):
  - 「美國環球教育基會(Global Education Fund)成立1999年四月。」
  - 「基金會設網站為 www.global-education-fund.org」
  - 「設置學術補助金以鼓勵學者研究和發展為促進環球和平的教育活動」
  - 「推廣為促進環球和平的教育活動」
  - 「設置學術生補助金以鼓勵學者研究國際衝突的原因及和平解決方法」
  - 「設置獎學金和學術指導協助以鼓勵和幫助國際留學生」
  - 「推廣以增進人民互相瞭解為目的環球教育旅行活動」
  - 「設立和支持一環球研究學院專門研究環球社會經濟文化和政治的整合期望環球對此有同樣認識而願意共同努力的人或機構都能加入此行列。有錢出錢*。有力出力。共同為將來的環球和平而努力。」
  - 「這是一龐大的任務和工作。本基金會人力和資金有限。」
  - Note: 「美國環球教育基會」 in the first line is missing 金 (a typo in the source dump, preserved verbatim above).

## Twin / containment check (A vs B)
- Normalization: frontmatter stripped, all `#` and whitespace removed
  (per the floor-anchor recipe; the post dump is heading-padded).
- Record A normalized: md5 `b6b45cca6f99b2ba8fdbefb89be82a3c`, 547 chars.
- Record B normalized: md5 `f88f216fe7aa6aa64e2b45724ad6fc14`, 347 chars.
- Containment both directions: **neither is a substring of the other** — A is the
  site's EN paraphrase, B is the original ZH submission. They agree on the one
  hard fact (成立 April 1999) and differ in coverage: only B carries the
  website `www.global-education-fund.org`, the seven-item mission list in the
  foundation's own ZH wording, and the 「有錢出錢…有力出力」 / 「人力和資金有限」
  fundraising lines. Richer artifact for absorb: **B (the ZH dump)**.
- Corroboration ruling: both live on the same editable source site
  (taiwaneseamericanhistory.org) and read as the same self-submitted foundation
  copy rendered twice (ZH original + EN directory paraphrase). Agreement across
  two serializations of one editable self-report is **not corroboration** —
  every absorbed row stays `alleged`.

## Third-party check
- `侯榮達` (Chicago 環球教育基金會 董事長, roster below) appears **only** in
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/2018-1.md` on this
  box (whole-corpus `grep -rliF '侯榮達' content knowledge`, machine indexes
  excluded). Identity vs this foundation is unconfirmed (name form omits
  「美國」 and the city is Chicago); recorded as a possible-connection lead,
  `alleged`.

## Sweep — sources checked, whole-corpus (`content` + `knowledge`, machine
indexes `units.jsonl` / `index.jsonl` / `ee-vault-index*` / `content-analysis/*`
excluded), 2026-11-14
- `Global Education Fund` → 8 files: own org page, own work page,
  `organizations/index`, `sources/taiwaneseamericanhistory-org`, records A + B,
  `pages/charity-organizations.md` (directory listing), and
  `knowledge/research/taiwanjustice-net-priority-lexicon.json` (machine
  lexicon, not a source). No third-party narrative.
- `美國環球教育基金會` → same 8-file set. No third-party narrative.
- `環球教育` → the above plus `posts/2018-1.md` (喜樂島聯盟 backer roster —
  the only new substance; see third-party check).
- `global-education-fund` (slug) → the above minus `posts/2018-1.md`.
- Prior deepen-x stamps on the org page (2026-09-26, 2026-10-09) only ever
  grepped `works/`+`articles/` (+`sources`/`events`/`topics`); they never opened
  records A or B. The two crawl artifacts were the harvest of this card.

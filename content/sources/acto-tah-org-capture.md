---
title: "TAH org-record capture — American Citizens of Taiwan Origin (ACTO) 美台公民協會"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization-record
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH org-record capture — American Citizens of Taiwan Origin (ACTO) 美台公民協會

Capture page for the citable artifacts on this box backing
[[organizations/american-citizens-of-taiwan-origin-acto|ACTO 美台公民協會]].
Preserved because the live TAH site is editable and these are the only
organization-side records on this box.

## Artifact 1 — crawled organization record (site DB export)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/american-citizens-of-taiwan-origin-acto.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/american-citizens-of-taiwan-origin-acto/](https://taiwaneseamericanhistory.org/organization/american-citizens-of-taiwan-origin-acto/)
- **Record id:** 72435 · **type:** `tah_organization` · **modified:** `2026-06-19T16:23:47` (crawl-side last-modified stamp)
- **Site taxonomy:** `class_list` carries `organization_type-social` (site classifies ACTO under Social Organizations); `person_profession` is empty `[]` (expected for an org record).
- **Content block:** 739 chars — the condensed mission blurb (501(c)(3), founded 1988, Northern Virginia, affiliates Northern Virginia Chinese School + I2EC, annual Outstanding Student Award).

## Artifact 2 — crawled story-corpus post (richer side)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/american-citizens-of-taiwan-origin-acto.md`
- **Original:** [https://taiwaneseamericanhistory.org/american-citizens-of-taiwan-origin-acto/](https://taiwaneseamericanhistory.org/american-citizens-of-taiwan-origin-acto/)
- Work page: [[works/taiwaneseamericanhistory-org/american-citizens-of-taiwan-origin-acto|ACTO 美台公民協會 (published 2015-08-05)]]
- **Content:** 1,463 normalized chars — the four named objectives (Responsible Citizenship / Community Service / Cultural Heritage / Equal opportunity), the two ACTO Organizations with street-level detail (Northern Virginia Chinese School at Marshall High School, Falls Church; I2EC meetings in Falls Church), the ACTO Activities list (Outstanding Student Award criteria; Senior Citizens Foundation with election-day transportation), and the self-published website `http://www.actous.org/`.
- The post is the RICH artifact; the org JSON blurb is a condensed serialization of the same self-report.

## Twin / containment check
Normalized both sides (strip frontmatter, all `#` and whitespace; JSON side additionally stripped of HTML tags):
- post: 1,463 norm chars, md5 `fd939502f22a936811893ec1cb73c92d`
- org JSON content block: 632 norm chars, md5 `52927e32b76e0b39561caf9952ba923a`
- Containment (both directions): **False / False** — the post omits the JSON's "founded in 1988" sentence wording while the JSON omits the post's objectives/activities detail. They are two views of ONE editable self-report, not independent records; treat the pair as a single self-sourced record (`alleged`), which is why no crown fact is upgraded on their agreement alone.

## Third-party records naming ACTO (corpus-side corroboration)
- [[works/taiwaneseamericanhistory-org/whos1383-carole-huang|1383. Carole Huang 陳春華 / 2016/11]] — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos1383-carole-huang.md` lists 「美台公民協會(American Citizens of Taiwan Origin, ACTO) 會長, 2004」 under Accomplishment (per that profile's `Source from TAA Greater Washington Chapter Special Edition, 2008/11` provenance line). Subject page: [[people/carole-huang|Carole Huang 陳春華]].
- [[works/taiwaneseamericanhistory-org/whoswho1242|1242. Connie Huang 黃康妮 / 2016/08]] — Accomplishment: 「獲頒美台公民協會『愛國獎』(Patriot Award)」. Subject page: [[people/connie-huang|Connie Huang 黃康妮]].
- [[works/taiwaneseamericanhistory-org/whoswho1241|1241. Cindy Huang 黃心怡 / 2016/08]] — Accomplishment: 「1. 獲頒美台公民協會『愛國獎』(Patriot Award)」. Subject page: [[people/cindy-huang|Cindy Huang 黃心怡]].
- Directory listing: `knowledge/web-archives/taiwaneseamericanhistory-org/pages/social-organizations.md` line 179 lists 「American Citizens of Taiwan Origin (ACTO) 美台公民協會」 under Social Organizations.
- Publication listing: `knowledge/web-archives/taiwaneseamericanhistory-org/pages/09-magazines-media-newsletters-newspapers-and-columns.md` line 32 lists 「Annual Journals of American Citizens of Taiwan Origin 美台公民協會年刊」.
- Scholarship record: [[works/taiwaneseamericanhistory-org/40-american-citizens-of-taiwan-origin-acto-realco-second-spring-scholarship-awar|40. 美台公民協會獎學金 Realco Second Spring Scholarship Award]] (published 2015-08-05) — full terms in the crawl dump `knowledge/web-archives/taiwaneseamericanhistory-org/posts/40-american-citizens-of-taiwan-origin-acto-realco-second-spring-scholarship-award.md`.
- Donation record: [[works/taiwaneseamericanhistory-org/annual-books-of-american-citizens-of-taiwan-origin|Annual Journals 年刊]] — dump `knowledge/web-archives/taiwaneseamericanhistory-org/posts/annual-books-of-american-citizens-of-taiwan-origin.md` carries 「Donated by Dr. Chien 04/2017」.

## Disambiguation (do not merge)
- ACTO the Moscow pharma body 「臨床試驗機構協會」 in a 2025-05-19 taiwanjustice vaccine article — acronym collision, not this org.
- 「acto」 substrings inside "actor"/"factor" (EEAAO film essay), archive-digest hashes, and works indexes — machine/prose noise, not sources.
- [[organizations/american-citizens-for-taiwan|American Citizens for Taiwan (西雅圖美台會)]] — a different Seattle org; its own page carries the cross-disambiguation.

## Whole-corpus sweep (2026-11-14, this card)
`grep -rlF '美台公民協會' content knowledge` and case-insensitive `grep -rliF 'American Citizens of Taiwan Origin' content knowledge`: hit set = the three work pages + org page + organizations index + `sources/taiwaneseamericanhistory-org.md` + the artifacts listed above + machine indexes (`units.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `posts/index.jsonl`, `taiwanjustice-net-priority-lexicon.json`, `connector-suggestions.json` — indexes, not sources). No memoir, article, or press story on this box names ACTO beyond the records archived here.

## GAPS / NEED YOU
- No third-party press coverage (華文 or EN) of ACTO exists on this box; officer rosters, award-recipient lists, and 年刊 volumes are not in the local corpus.
- 会长/leadership: only Carole Huang 陳春華 (會長 2004) is attested. Officers for other years, and the identity of 「Dr. Chien」 who donated the 年刊 in 04/2017, are still open.
- `www.actous.org` was never crawled onto this box (only cited from the self-report). A live crawl or Wayback capture would be the next citable source.

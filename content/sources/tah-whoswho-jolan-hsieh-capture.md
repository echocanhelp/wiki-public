---
title: "TAH Who's Who profile capture — 1180. Jolan Hsieh 謝若蘭"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 1180. Jolan Hsieh 謝若蘭

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record
(record #1180), archived on this box as two serializations of one editable form — the crawled profile JSON and the
encyclopedia entry dump — plus three third-party corpus records that name her: the 1999 and 2003 中西部台灣人夏令會
story posts and the NATWA 第二十七期 聯誼通訊. Preserved because the biographical fields are self-reported and the
live site is editable.

## Subject
- [[people/jolan-hsieh|Jolan Hsieh 謝若蘭]] — TAH Who's Who record #1180

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/jolan-hsieh.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/jolan-hsieh/](https://taiwaneseamericanhistory.org/person/jolan-hsieh/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 73729 · **type:** `tah_person` · **profession taxonomy:** `activist`, `educator`, `professor`, `researcher`, `scholar` (`person_profession-*` in `class_list`; numeric term ids `person_profession: [2247, 2248, 2237, 1813, 2245]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the crawled `sidecar.roles` kept only `professor`, `educator` — the roles `activist` / `researcher` / `scholar` survive only in `class_list`/`page_text`, which is why the taxonomy line here is richer than the page's Identity Snapshot.
- **`modified` on source:** 2026-06-19T16:45:28 · `page_bytes`: 54,647 (raw HTML; the `Last updated: June 19, 2026` line sits in the rendered page text)
- **Verbatim fields (self-reported):** Name `謝若蘭 / Jolan Hsieh` · Birth Year `-` · Birth Place `台灣台南新營`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank) · **Address:** `台灣`
- **Family:** `1. Husband:-` · `2.Daughter:-` · `3.Son:-` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (3 rows):** `1. Tainan Theological College and Seminary` — `1993` — `B.S. Women's Studies` · `2. Arizona State University` — `1996` — `M.S. Justic Studies` · `3. Arizona State University` — `2002` — `Ph.D. Justic Studies` (`Justic` is the verbatim self-reported spelling of Justice Studies)
- **Employment (4 rows, no dates):** `國立東華大學族群關係與文化學系` 專任副教授 · `原住民族國際事務中心` 主任 · `Phoenix聯邦監獄女子受刑人大專` 教育顧問 · `亞歷桑那州立大學司法正義學系` 兼任講師
- **Accomplishment / Publication(Non-professional ones) / Hobby / Website or Blog:** `-` — unfilled (absence evidence: the self-reported form withholds no crown field content).
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Provenance line:** `Source from: 2016美西台灣夏令會` · `Post in 07/2016` (per `page_text` in the capture JSON) — the record attributes its content to the 2016 美西台灣夏令會 (Taiwanese American Conference-West Coast).
- **Footer summary block (same page, rendered below the form):** restates Hanzi `謝若蘭`, Birthplace `台灣台南新營`, Residence `台灣`, the three Education rows, and the four Position rows. Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1180.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1180/](https://taiwaneseamericanhistory.org/whoswho1180/)
- **Title:** `1180. Jolan Hsieh 謝若蘭 / 2016/07` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1180|TAH #1180]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, blank Birth Year, Birth Place, Education, Employment, all `-` accomplishment fields, `Source from: 2016美西台灣夏令會`, `Post in 07/2016`). It is a second rendering of the same self-reported payload, not an independent source.

## Twin & cross-check (2026-11-13)
Containment/md5 test on the two serializations of the one form (frontmatter stripped, `#`/whitespace normalized):
`posts/whoswho1180.md` = 519 normalized chars (md5 `3b2eeeeee14120b8ce23db63f1363dbb`) vs JSON `page_text` = 1,541
normalized chars (md5 `131a8422e2a6cc20ad1ce357822f3f1f`). Neither is a substring of the other: the JSON dump is the
richer artifact because it carries the site chrome, the `Last updated: June 19, 2026` line, the five-tag profession
taxonomy, and the footer restatement block; the encyclopedia dump is a form-only render. Agreement across two
serializations of one editable self-report is NOT corroboration — that is what keeps the record's own
`Source from… 2016` submission line at `alleged`-grade provenance.

## Third-party namings on this box (absorbable, non-self-reported)
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mtsc-1999.md` — 1999 中西部台灣人夏令會 (Ohio Wesleyan University, 7/8–11, 主題「新世紀、新台灣」), 綜合報導 摘自台灣公論報: `亞利桑那大學司法硏究所博士候選人謝若蘭演講「原住民之人權」` — she is named with her institutional affiliation and talk topic.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mtsc-2003.md` — 2003 美國中西部台灣人夏令會 (Bowling Green University, Ohio, 7/13 閉幕, 主題「正名制憲、認同台灣」), 綜合報導 摘自台灣公論報 第1983期 7/22/2003: `司法正義學博士謝若蘭講解台灣原住民的文化和認同問題` — titled 司法正義學博士 (post-2002 PhD).
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/683-...md` — 北美洲台灣婦女會聯誼通訊 第二十七期 (2002/08), 會長的話 by 賴碧良: `今年有年輕一代的謝若蘭負責公關組` — NATWA 公關組 lead.
- `knowledge/web-archives/taiwandaily-net-139514-139514.md` — 美洲台灣日報 2026-05-28 (記者林蓮華) on TAC-WC 2026 (7/10–12, Crowne Plaza San Diego): 謝若兰 listed among 深耕地方或專業領域 speakers. **Same-name check pending** — the article gives no affiliation or title for this 謝若蘭 and the subject shares the name; treated as candidate, not confirmed (see GAPS on the person page).

## Ruled-out hits (read, different persons or non-sources)
- `沈若蘭` (林益世案) and 英國駐中大使 `吳若蘭` in `content/articles/taiwanjustice-net/*` — surname/given-name fragment overlaps, different persons.
- Machine indexes carrying only name forms from the harvest, no biographical content: `knowledge/research/tdm-page-title-index.json`, `knowledge/research/taiwanjustice-net-priority-lexicon.json`, `knowledge/research/taiwaneseamericanhistory-org-family.json`, `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`.
- Co-listing pages with no new facts: `content/people/index.md`, `content/sources/taiwaneseamericanhistory-org.md`, `content/organizations/presbyterian-church-in-taiwan.md` (Subjects-list wikilink only).

## Harvest provenance
Profile and posts captures are from the taiwaneseamericanhistory.org harvest recorded in
`knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`method: wp-json`); the taiwandaily capture is a
`direct-trafilatura` fetch dated 2026-10-23 in its own frontmatter.

## Related Pages
- Subject: [[people/jolan-hsieh|Jolan Hsieh 謝若蘭]]
- Work record: [[works/taiwaneseamericanhistory-org/whoswho1180|TAH #1180 1180. Jolan Hsieh 謝若蘭 / 2016/07]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]]
- Orgs touched by the third-party records: [[organizations/presbyterian-church-in-taiwan|PCT]] (Tainan Theological College & Seminary alumni network) · NATWA national (no org page on this box; see [[organizations/natwa-southern-california|NATWA-SC chapter]] for the sibling chapter node)

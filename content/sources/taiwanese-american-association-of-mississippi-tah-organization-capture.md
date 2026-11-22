---
title: "TAH organization directory capture — Taiwanese American Association of Mississippi (密西西比臺灣同鄉會)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese American Association of Mississippi (密西西比臺灣同鄉會)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 765
- wikilinks: 3


Capture page for the FLOOR-ANCHOR pass on [[organizations/taiwanese-american-association-of-mississippi]]
(card t_671c92ee, 2026-11-14). Archives what was harvested and what was checked-and-empty, so the next
pass does not re-grep.

## Harvested artifact (single first-party self-report)

### Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-american-association-of-mississippi.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-american-association-of-mississippi/](https://taiwaneseamericanhistory.org/organization/taiwanese-american-association-of-mississippi/)
- **Record id:** 78019 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-12T18:41:33 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45, 1,032 bytes)
- **`title`:** `Taiwanese American Association of Mississippi 密西西比臺灣同鄉會`
- **`class_list` taxonomy:** `organization_type-civic-advocacy`, `organization_type-social` (plus WP boilerplate
  `post-78019`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`) — note: unlike sibling
  student-chapter records, this chapter carries **no** `organization_type-student` class.
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, single paragraph):** the chapter is a chapter of the Taiwanese
  Association of America (TAA, 全美台灣同鄉會), the national umbrella organization serving Taiwanese American
  communities across the United States; it serves the Taiwanese American community in Mississippi and is listed
  in the TAA national chapter directory.

## Twin / containment check (2026-11-14, this card)
- No `posts/<slug>.md` encyclopedia twin exists (unlike LKGT, which had story-corpus post #26). Checked
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/` for the same-slug and same-name artifact — none.
- Containment: the org JSON's normalized `content_html` (303 chars after tag-strip/whitespace-collapse) is a
  **strict substring** of the org page's normalized body (1,688 chars) — the page body was copied verbatim from
  the directory record at creation, so agreement between them is one editable self-report rendered twice,
  **NOT corroboration**. md5 json `15335dc9bab4e64a8af423ff8c7ce228` vs page `366d4ead59414204d3dd7177e61016c0`
  (page is richer; JSON is the strict subset). Every absorbed row from this artifact stays `alleged`.

## Third-party records naming the state/community (not the chapter itself)
- 陳希寬 memoir [[works/taiwaneseamericanhistory-org/ourjourneys58|58.回憶編印第一本《全美台灣同鄉通訊錄》的甘苦經過]]
  (post id 4436, index date 2014-11-02): the 1967 directory survey lists `Mississippi: 無名氏` (unnamed contact)
  and counts `密希西比州（Mississippi) 22名` by state distribution. `knowledge/web-archives/taiwaneseamericanhistory-org/posts/ourjourneys58.md` L54, L110.
- 鄭炳全 memoir [[works/taiwaneseamericanhistory-org/mystories11|11. 密西西比大學 Ole Miss / 鄭炳全]] (post id 146,
  index date 2014-08-26): full text on disk at `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories11.md`
  while the work page is bibliographic-only. Carries dated Mississippi-community context (1965 pharmacy building,
  author arrived 1970, 1976 baptism) — the state's earliest documented community anchor; does **not** name the chapter.
- Adjacent Whos-Who records with Mississippi tenure (community context, chapter not named):
  吳木盛 `knowledge/web-archives/.../person/dr-mu-sheng-wu.json` (id 72627, modified 2026-06-19; Univ. of
  Mississippi M.S. 1964, first US city Oxford 1963), 林毅夫 `person/ih-foo-lin.json` (id 72626, modified
  2026-06-19; Univ. of Mississippi Medical Center, Jackson, MS 1974 psychiatric residency),
  黃健生-line `person/prof-ken-s-huang.json` (id 73419; Mississippi State University for Women, Columbia, MS 1991 credit).

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF '密西西比臺灣同鄉會'` and `grep -rliF 'Association of Mississippi'` over `content/` + `knowledge/`
  → the org page itself, `content/organizations/index.md` L322, `content/sources/taiwaneseamericanhistory-org.md`,
  the org JSON above, and machine indexes only (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`,
  `taiwanjustice-net-priority-lexicon.json`) — no narrative record of the chapter.
- `grep -rli 'mississippi'` over `knowledge/web-archives/taiwaneseamericanhistory-org/posts/` → 24 files; opened
  all candidate hits: `ourjourneys58.md` (absorbed above), `mystories11.md` (absorbed above), `setaa-2023.md`
  (SETAA year recap, no organization content), person-page JSONs (education credits only, classified above),
  musician bios (Karen Lin `Mississippi Valley Orchestra` — orchestra name, not this community),
  `hurricane-katrina-…md` (New Orleans/LA disaster piece), 林天明 religion essays, Charles Yu bio — no chapter material.
- `grep -n -i mississippi` over `knowledge/web-archives/taiwaneseamericanhistory-org/pages/` directory pages
  (`senior-organizations.md`, `social-organizations.md`, `organizations-archive.md`, `miscellaneous-organizations.md`,
  `political-organizations.md`, `professional-organizations.md`) → the only hit is
  `pages/taiwanese-association.md` L118: the TAA chapter listing shows `Mississippi` as a bare state heading
  with **no chapter line under it** — while Minnesota and Missouri get named chapters. Negative listing:
  the TAA chapter page does not enumerate this chapter.
- `grep -rn -i mississippi` over the 2017/2023 TAHS publication PDFs (`knowledge/web-archives/2017-tahs-publication-part*.md`,
  `2023-tahs-publication-part*.md`) → zero hits.
- Prior deepen-x stamps (7, 2026-09-22 → 2026-10-03) grepped only `works/` + `articles/`; the whole-corpus sweep
  above supersedes them and found the same conclusion plus the `pages/taiwanese-association.md` negative listing.

## GAPS / NEED YOU
- No citable third-party record of the chapter itself exists on this box: no founding year, no officer roster,
  no events, no Chinese-name variant beyond 密西西比臺灣同鄉會. What exists is state-level community context
  (1967 通訊錄 無名氏 + 22-person count; 2014 Ole Miss memoir) and the org's own single-paragraph directory entry.
- Sources checked: the org JSON (above), whole-corpus greps per name form, the 24 mississippi-hitting story
  posts, the TAH directory pages, the 2017/2023 TAHS publication PDFs, and adjacent Whos-Who profiles.
- NEED YOU: a chapter founding record, officer roster, or newsletter — TAA national convention records,
  a TAA Mississippi chapter Facebook/website capture, or an Ole Miss / Mississippi State Taiwanese alumni memoir
  naming the chapter would close the gaps.

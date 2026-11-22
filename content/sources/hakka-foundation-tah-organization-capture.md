---
title: "TAH organization directory capture — Hakka Foundation 客家基金會"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Hakka Foundation 客家基金會

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 595
- wikilinks: 1


Primary captures of the organization's own records in the TAHS story corpus on this box.
Both are editable first-party self-reports of the same organization page.

## Subject
- [[organizations/hakka-foundation|Hakka Foundation (客家基金會)]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/hakka-foundation.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/hakka-foundation/](https://taiwaneseamericanhistory.org/organization/hakka-foundation/)
- **Record id:** 72404 · **type:** `tah_organization` · **slug:** `hakka-foundation`
- **`modified` on source:** 2026-06-19T16:23:23 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45)
- **`class_list` taxonomy:** `organization_type-charity` (plus WP boilerplate `post-72404`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `None`
- **Verbatim `content_html` (895-byte file):** one paragraph — the organization is a Taiwanese American
  nonprofit serving the Hakka community; promotes Hakka language, culture, and heritage while fostering
  community integration, civic participation, and mutual support among Hakka people in the United States;
  mission spans education, cultural preservation, senior services, social welfare, civil rights advocacy,
  and charitable activities.

## Capture 2 — crawled long-form page dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/hakka-foundation.md`
- **Original:** [https://taiwaneseamericanhistory.org/hakka-foundation/](https://taiwaneseamericanhistory.org/hakka-foundation/)
- **H1:** `12. Hakka Foundation客家基金會` — the directory's own numbered list ranks it #12
- **`fetched: auto`** (no crawl date in frontmatter); on-disk mtime 2026-08-21 18:05; 5,723 bytes
- **Content (self-reported):** a bilingual 「咱客家人 / Who are the Hakka?」 essay closing with the motto
  「異鄉做客不忘本,入境問俗重求知,勤儉成家有自尊,敦親睦鄰一家親」 and the concept 「百年過客 同舟共濟
  落地生根 天下一家」, followed by a bilingual **13-item Mission 使命 list**: English/Chinese/Hakka language
  learning; community understanding and harmony; Hakka arts and culture appreciation; American heritage and
  citizenship; family values; importance of mothers; facilities and services to senior citizens; assisting
  the poor and social welfare; reducing prejudice and discrimination; defending human and civil rights and
  social justice; assisting fellow corporations/organizations/institutes with similar goals; purchasing
  properties or accepting donations; other lawful activities permitted under **State and Federal Nonprofit
  Public Benefit Corporation Laws and Regulations** (legal-form language implying incorporation under such
  law; jurisdiction not stated → `inferred`).

## Twin / containment check (2026-11-14)
Normalized both artifacts (HTML tags stripped, `#`/whitespace removed) before comparing:
- JSON `content_html` normalized: 363 chars, md5 `6aac4f7bdbd653b3e51335685e482a4b`
- Posts dump normalized: 2,831 chars, md5 `e21ee77651b9c3aecb807e7f2580d7f8`
- Containment: `json in post` → **False**; `post in json` → **False** (md5-different, neither substring)
- **Ruling:** the two are different renderings of the same editable self-report by the same organization
  (the JSON carries the org's short blurb; the posts dump carries the long-form page essay + mission list).
  Agreement across two serializations of one editable source is **not corroboration** — every row sourced
  from these artifacts stays `alleged` on the organization page.

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form (`grep -rlF '客家基金會'` and `grep -rliF 'hakka foundation'`);
classification of every hit:
- The org page itself + its two crawl artifacts above
- `content/works/taiwaneseamericanhistory-org/hakka-foundation.md` — bibliographic work page for the same
  directory record (already wikilinked from the org page)
- Directory/index listings: `content/organizations/index.md`, `content/sources/taiwaneseamericanhistory-org.md`,
  `knowledge/web-archives/taiwaneseamericanhistory-org/pages/charity-organizations.md` (charity list, entry #12)
- `content/articles/taiwanjustice-net/2022/20220929025100_2021_04_16_大洛杉磯台灣會館給太魯閣號受難家屬的慰問函_*.md`
  — the 2021-04 太魯閣號 relief letter (already absorbed in Role in the Community / Timeline), plus its
  raw-html and tier2 mirrors of the same article
- Sibling Hakka org pages/JSONs (Taiwan Hakka Association for Public Affairs in North America, Global Hakka
  UN-NGO applying committee) and ~20 Hakka-association posts — separate organizations, not this one
- Machine indexes, not sources: `knowledge/research/taiwaneseamericanhistory-org/units.jsonl`,
  `posts/index.jsonl`, `ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`,
  `taiwanjustice-net-priority-lexicon.json` / `-hits.jsonl`
- `content/organizations/joint-alumni-association-…md` and `career-taiwan-usa-association.md` matched 客家基金會
  only on substring noise (different foundations: 客家委员会/其他基金會 wording), not this org

No third-party narrative record about the Hakka Foundation exists on this box beyond the two self-report
captures and the 2021-04 慰問函.

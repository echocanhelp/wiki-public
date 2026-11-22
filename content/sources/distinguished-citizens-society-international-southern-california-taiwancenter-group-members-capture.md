---
title: "Taiwan Center group-members capture — Distinguished Citizens Society International-Southern California"
type: source
tags:
  - source
  - capture
  - Taiwan-Center
  - distinguished-citizens-society
verification_status: published
last_reviewed: 2026-11-14
---
# Distinguished Citizens Society International–Southern California — Taiwan Center group-members capture

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 493
- wikilinks: 1


Capture page minted 2026-11-14 for FLOOR-ANCHOR card t_7af46a4e. Sole first-party record for
[[organizations/distinguished-citizens-society-international-southern-california|國際傑人會南加分會]]
on this box is the Taiwan Center 團體會員 / Group Members listing, archived twice (ZH + EN).

## Verbatim listing lines

ZH capture `knowledge/web-archives/taiwancenter-org-group-members.md`
(source_url https://www.taiwancenter.org/group-members, `fetched` 2026-07-16T01:12:07, method jina,
on-disk mtime 2026-08-02 20:54:23 PT, 5,937 bytes):

```
國際傑人會世界總會            (line 180)
Distinguished Citizens Society International World Headquarters

國際傑人會南加分會            (line 184)  <- this page's subject
Distinguished Citizens Society International-Southern California

國際傑人會美國總會            (line 188)
Distinguished Citizens Society International USA
```

EN capture `knowledge/web-archives/taiwancenter-org-en-group-members.md`
(source_url https://www.taiwancenter.org/en/group-members, `fetched` 2026-07-16T01:12:07, method jina,
on-disk mtime 2026-08-02 20:54:23 PT, 3,768 bytes):

```
Distinguished Citizens Society International World Headquarters   (line 96)
Distinguished Citizens Society International-Southern California  (line 98)  <- subject
Distinguished Citizens Society International USA                  (line 100)
```

## Twin / containment check

- The two captures are the ZH and EN renderings of **one editable org listing** on the same
  domain, fetched in the same crawl batch (identical `fetched` 2026-07-16T01:12:07, same-second
  on-disk mtimes). The EN body is a strict name-only subset of the ZH body for this entry
  (ZH adds the Chinese name 國際傑人會南加分會; no extra facts).
- Ruling: agreement across two serializations of one editable record is **NOT corroboration** —
  all listing-derived rows on the org page stay `alleged`.

## Single-source status

- The listing names the society only (Chinese name + English name + group-member relation).
  No founding year, roster, address, website, or activity is on the listing.
- The only dated activity record naming any 傑人會 unit in the corpus is the 2022-02-26
  TJJ/中央社記者 article on 國際傑人會**德國總會**'s 海德堡台灣華語文學習中心 揭牌
  (`content/articles/taiwanjustice-net/2022/20220227161430_2022_02_26_德國第2所-海德堡台灣華語文學習中心揭牌_6d190b0ed29c53f2.md`,
  `post_date` 2022-02-26, Wayback `archive_ts` 20220227161430) — a system sibling, not this chapter.

## Whole-corpus sweep classification (2026-11-14)

`grep -rlF` per name form over `content/` + `knowledge/`:

| Query | Files | Classification |
|---|---|---|
| `國際傑人會` | 10 | sibling org pages (usa, world-headquarters), taiwan-center.md, this subject page, the TJJ article + its raw-html/tier2 twins, the two group-members captures, machine index `knowledge/operational/ee-vault-index.v5.json` |
| `傑人會` | 10 | identical set |
| `Distinguished Citizens` | org/sibling/index pages + the two captures + machine indexes (`ee-vault-index.v*`, `content-analysis/*.jsonl`, `taiwanjustice-net-priority-lexicon.json`, `content/.wiki-index.md`) |
| `南加分會` | 277 | 1 = subject page; the other 276 are **other** organizations' SC-chapter pages/works (NATMA-SC, NATEA-SC, NATWA-SC, 北美人台灣會館LA, 南加州台南一中女中校友會 …) — substring hits on 「南加分會」 as a generic chapter suffix, none name this society |
| `傑人` in `knowledge/web-archives` | the two captures + the TJJ raw-html/tier2 twins + 2 unrelated raw-html/tier2 files (毛澤東夜鶯島 article, WikiLeaks xml) where 傑人 appears as an unrelated personal-name substring |

Machine indexes (`ee-vault-index.*`, `content-analysis/*.jsonl`, `*.wiki-index.md`,
priority-lexicon json) are not sources. No SC-chapter-specific record exists on this box.

## NEED YOU

Founding year, officer/member roster, activities, and any SC-chapter record (yearbook, 會訊,
event photo, the society's own site/Facebook) would deepen the org page. Sources checked and
found empty for this chapter: `content/works`, `content/articles`, `content/organizations`,
`content/events`, `content/topics`, `knowledge/web-archives/**` (incl. TJJ tier2 + raw-html),
`knowledge/research`, `knowledge/operational` (indexes only).

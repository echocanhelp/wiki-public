---
title: "TAH capture — Texas Formosa Fishing Association 德州台灣釣魚協會 (charter 1993)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization-record
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH capture — Texas Formosa Fishing Association 德州台灣釣魚協會 (charter 1993)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 719
- wikilinks: 2


Capture page for the citable artifacts on this box backing
[[organizations/texas-formosa-fishing-association|Texas Formosa Fishing Association 德州台灣釣魚協會]].
Preserved because the live TAH site is editable and these are the only organization-side
records on this box. The story-corpus post (Artifact 2) — the association's full charter —
was never opened by any prior DEEPEN-X pass; all prior page content came from Artifact 1.

## Artifact 1 — crawled organization record (site DB export)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/texas-formosa-fishing-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/texas-formosa-fishing-association/](https://taiwaneseamericanhistory.org/organization/texas-formosa-fishing-association/)
- **Record id:** 72346 · **type:** `tah_organization` · **`modified` on source:** `2026-06-19T16:22:45` · **on-disk capture mtime:** 2026-08-17
- **Site taxonomy:** `class_list` carries `organization_type-social` (site classifies it under Social Organizations); `person_profession` is empty `[]` (expected for an org record); `excerpt` is `null`.
- **Content block:** 510 normalized chars — the condensed mission blurb (nonprofit/nonpolitical, Taiwanese Activity Center Houston, fishing promotion, member welfare, annual competitions/seminars/camping/family events). This is the only text the org page carried before 2026-11-14.

## Artifact 2 — crawled story-corpus post: the full 章程 (charter) — RICH, never opened before
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/texas-formosa-fishing-association.md`
- **Original:** [https://taiwaneseamericanhistory.org/texas-formosa-fishing-association/](https://taiwaneseamericanhistory.org/texas-formosa-fishing-association/)
- Work page: [[works/taiwaneseamericanhistory-org/texas-formosa-fishing-association|Texas Formosa Fishing Association 德州台灣釣魚協會 (published 2014-10-12)]]
- **Content:** 1,020 normalized chars — the association's own constitution (章程), which the org JSON drops entirely:
  - 名稱 clause: original name 「德州釣魚協會」/ TEXAS FORMOSA FISHING ASSOCIATION (the original name differs from the current one — no prior pass had this).
  - 會址: 休士頓台灣人活動中心.
  - 宗旨: 非營利、非政治性; 促進釣魚者間合作和諧; 增進釣魚技藝、守法; 爭取會員福利.
  - 組織: membership open to anyone interested in fishing; 創會員 = attendees of the 第一屆大會成立; new members need one 正式會員 introduction + 理事會 approval; 榮譽會員 (60+, experienced, contribution, nominated by 會長, approved by 理事會); 贊助會員. 會員大會 held every January. 理事會 of 九人, three-year terms, one-third re-elected annually. 會長/副會長/財務長 one each, elected by 理事, 會長 one-year term, no re-election; past 會長 becomes 當然顧問 of the next 理事會. Advisory council (顧問) permitted.
  - 義務: 入會會費 USD 40.00; 會員費 USD 25.00/year; expulsion by two-thirds 理事會 vote.
  - 章程修改: two-thirds vote of the 會員大會.
  - **Dated adoption/amendment history (the dated spine this capture mints):** 「本章程於JANUARY 30, 1993 成立大會通過」; name change to 德州台灣釣魚協會 adopted at the 「JANUARY 29, 1994 年會」; clauses 二/1,3,6 amended at the 「JANUARY 20, 1996 年會」.

## Twin / containment check
Normalized both sides (strip frontmatter, all `#` and whitespace; JSON side additionally stripped of HTML tags):
- org JSON content block: 510 norm chars, md5 `013073e259c25d43d393186a56941199`
- story-corpus post body: 1,020 norm chars, md5 `87ac9850ae0b50c311d673f897d503fd`
- Containment (both directions): **False / False** — the post omits the JSON blurb's wording while the JSON omits the entire charter. They are two serializations of ONE editable first-party self-report (same submitter lineage, same site), not independent records. The post is the RICH artifact (james-jean pattern: the dump carries dated material the profile drops). Every fact below is therefore labeled `alleged`; agreement across the pair is not corroboration.

## Whole-corpus sweep (2026-11-14, this card)
- `grep -rli 'Texas Formosa Fishing' content knowledge` and `grep -rlF '德州台灣釣魚協會' content knowledge`: hit set = org page + `content/organizations/index.md` + work page + `content/sources/taiwaneseamericanhistory-org.md` + the two artifacts above + machine indexes (`knowledge/research/taiwaneseamericanhistory-org/units.jsonl`, `ee-vault-index.v1–v5`, `content-analysis/2026-*.jsonl`, `posts/index.jsonl`, `taiwanjustice-net-priority-lexicon.json`) — indexes are not sources. No memoir, article, or press story on this box names the association.
- `grep -rlF '德州釣魚協會' content knowledge`: only the charter post itself (the original-name clause).
- Broad `grep -rlF '釣魚' content/works content/articles`: classified as unrelated — `ourjourneys315` (smuggling-by-junk disguise anecdote), `ourjourneys281` (nursing-home fishing-gesture vignette), `ourjourneys37` (協志會 activity list incl. 深海釣魚), `our-journeys-359` (George Chang took students fishing at Galveston — Houston-era but a 1960s student-group anecdote, no association mention), `ourjourneys275` (student fishing anecdotes), `mystories209` (鄭瑞雄 essay 「釣魚」), `ourjourneys58` (釣魚台 Diaoyu Islands, not fish), taiwanjustice 2026-02-09 (釣魚台列嶼). Prior deepen-x stamps 2026-09-25/26 and 10-07/09 reached the same classification; this sweep re-derived it in-session over all of `content/` + `knowledge/`.

## GAPS / NEED YOU
- No third-party press (華文 or EN) and no memoir mentions the association on this box.
- Officer/会长 rosters, first-president identity, and member counts are not on this box — the charter names only roles (會長/副會長/財務長/九人理事會), no people.
- The live org page and the live charter page are editable; a fresh crawl or Wayback capture after 2026-08 would be the next citable source.
- The separate `Texas Formosan Federal Credit Union` records are a different org (do not merge).

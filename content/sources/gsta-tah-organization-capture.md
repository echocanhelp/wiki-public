---
title: "TAH organization directory capture — Greater Sacramento Taiwanese Association GSTA"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Greater Sacramento Taiwanese Association GSTA

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 843
- wikilinks: 3


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box, plus the two roster-bearing community posts in the
TAH story corpus that name GSTA officers. The directory entry is an editable
first-party self-report; the rosters are third-party (author 曹長青) signed lists.

## Subject
- [[organizations/greater-sacramento-taiwanese-association-gsta|Greater Sacramento Taiwanese Association (GSTA)]] — TAH organization directory record + roster appearances

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/greater-sacramento-taiwanese-association-gsta.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/greater-sacramento-taiwanese-association-gsta/](https://taiwaneseamericanhistory.org/organization/greater-sacramento-taiwanese-association-gsta/)
- **Record id:** 78034 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-12T18:41:33 (crawl-side capture of this file: on-disk mtime 2026-08-17)
- **Title field:** `Greater Sacramento Taiwanese Association (GSTA) 大沙加偭度台灣同鄉會` — note the directory title uses 偭 while the body paragraph uses 緬 (大沙加緬度台灣同鄉會); both spellings retained as printed.
- **`class_list` taxonomy:** `organization_type-civic-advocacy`, `organization_type-social` (plus WP boilerplate `post-78034`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, single paragraph):** "The Greater Sacramento Taiwanese Association (GSTA, 大沙加緬度台灣同鄉會) is a regional chapter of the Taiwanese Association of America (TAA, 全美台灣同鄉會), the national umbrella organization for Taiwanese American community associations in the United States. GSTA serves the Taiwanese American community in the greater Sacramento, California area and is classified under the TAA Western (美西) region."

## Single-source status of Capture 1
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md` encyclopedia dump twin (unlike Who's Who person records), so no twin/containment check is possible; every field above is one editable self-report → label `alleged`.

## Capture 2 — 2018 喜樂島聯盟 overseas supporter roster (third-party)
- **Vault file:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/2018-1.md` (mtime 2026-08-21)
- **Work page:** [[works/taiwaneseamericanhistory-org/2018-1|1. 《喜樂島聯盟》海外後援會成立]]
- **Original:** [https://taiwaneseamericanhistory.org/2018-1/](https://taiwaneseamericanhistory.org/2018-1/) · signed 曹長青, 2018-03-08 · work-page Record date 2018-03-12
- **Verbatim 「加州沙加緬度聯署名單」 GSTA lines (transcribed from the vault dump this pass):**
  - 「袁碧玉：大沙加緬度台灣同鄉會會長」
  - 「陳智貞：前大沙加緬度台灣同鄉會會長」
  - 「賴禹安：前大沙加緬度台灣同鄉會會長」
  - 「呂月霞：前大沙加緬度台灣同鄉會會長」
  - 「張晉賢：加州大沙加緬度台灣同鄉會理事」
- Context (same roster block, for disambiguation against sibling Sacramento orgs): the FAPA Sacramento chapter lines (黃漠見 會長, 蔡洋清 副會長, 李雪玟 顧問, 劉文彬/黃員成 前會長) and 沙加緬度台灣文化基金會 lines (林正子 董事, 賴明堂 會長) appear separately in the same list — the post itself keeps GSTA, FAPA Sacramento, and STCF as distinct organizations. The post also notes Sacramento-area names were initially dropped in typesetting and later restored to the online roster (補上), i.e. this online roster is the corrected version.
- Note: the post's own header says the printed 自由時報 full-page ad could not fit all titles (原計劃800人，達到1350人), so roster titles here are as submitted by the signers/organizers — self-attested titles restated by a third party.

## Capture 3 — 2017 聲援民視 overseas petition roster (third-party)
- **Vault file:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/related-tw-81.md` (mtime 2026-08-21)
- **Work page:** [[works/taiwaneseamericanhistory-org/related-tw-81|81. 海外台灣人聲援民視聯署書]]
- **Original:** [https://taiwaneseamericanhistory.org/related-tw-81/](https://taiwaneseamericanhistory.org/related-tw-81/) · signed 曹長青, 2017-04-26 於台北 · footer 「Source from NATPA FORUM 04/2017」 · work-page Record date 2017-04-27
- **Verbatim GSTA line:** 「呂月霞：大沙加緬度台灣同鄉會會長」
- Cross-check against Capture 2: 呂月霞 is 「會長」 in 2017-04 and 「前會長」 in 2018-03 — internally consistent officer succession. 袁碧玉 as sitting 會長 in 2018-03 follows 呂月霞; 陳智貞 and 賴禹安 are already 前會長 by 2018-03, so their tenures are pre-2018 and mutually ordered only loosely. All titles are as-submitted roster lines → `alleged` per person, but the two rosters are independent authorship events (2017 vs 2018 petitions), which is why the 呂月霞 succession reads consistent rather than circular.

## Whole-corpus sweep (2026-11-14, this card t_c77b6c99)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF '大沙加' content knowledge` → the org page itself, `content/organizations/index.md`, `content/sources/taiwaneseamericanhistory-org.md`, the org JSON above, the two posts above (the ONLY narrative records), plus machine indexes (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `taiwanjustice-net-priority-lexicon.json`, `connector-suggestions.json`) — machine indexes are not sources.
- `grep -rli 'greater sacramento' content knowledge` (excluding machine indexes) → the org page, `organizations/index.md`, `sources/taiwaneseamericanhistory-org.md`, `organizations/senior-taiwanese-association-of-northern-california.md` (Related Pages backlink only), the org JSON. No narrative record.
- `grep -rlF 'GSTA' content knowledge` (excluding machine indexes) → same set as above plus one stray TJJ raw-image filename (false positive). No additional narrative record.
- Sibling-org separation re-confirmed: 黃漠見 appears as 「前沙加緬度台灣同鄉會會長」 in Capture 3 and 「FAPA沙加緬度分會會長」 in Capture 2 — the bare 「沙加緬度台灣同鄉會」 lines in these rosters belong to the Sacramento TSA sibling, NOT GSTA (the rosters distinguish 大沙加緬度 vs 沙加緬度 lines); do not merge.
- Person-page check: no `content/people/` pages exist for 袁碧玉 / 陳智貞 / 賴禹安 / 呂月霞 / 張晉賢 (grep per name, zero hits), so no identity tie-ins were blocked or invented.

## Gaps / NEED YOU
- No founding date, no president roster beyond the two petition snapshots, no website/Facebook, no
  membership figure for GSTA anywhere on this box. Sources checked: the TAH org directory JSON
  (id 78034), the full TAH story corpus (`knowledge/web-archives/taiwaneseamericanhistory-org/posts/`
  via 大沙加 / GSTA / Greater Sacramento greps), the TAA founding-chapters memoir
  `ourjourneys76` (Sacramento not among the 28 founding chapters — prior 2026-10-09 deepen pass),
  and the sibling-org pages (SAFA / FAPA Sacramento / STCF / STA-NC).
- NEED YOU: a GSTA anniversary publication, TAA 美西區 yearbook, or GSTA officer list from
  taiwaneseamericanhistory.org submissions would close the president-lineage gap.

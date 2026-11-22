---
title: "Provenance capture — 北美路加醫療傳道會 (sole record: TAH Who's Who 廖俊惠)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
  - provenance
tier: M
verification_status: pending
last_reviewed: 2026-11-17
---
# Provenance capture — 北美路加醫療傳道會

Every fact-bearing mention of 北美路加醫療傳道會 on this box comes from ONE editable
self-report: the TAH Foundation Who's Who profile of [[people/chin-h-liao|Dr. Chin H. Liao 廖俊惠醫師]].
This page archives that single source, its twin serializations, the twin/containment
check, and the full sweep that establishes there is no second source on this box.

## The one source
- **Record:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/chin-h-liao.json`
  · record id `73553` · type `tah_person` · slug `chin-h-liao`
  · original <https://taiwaneseamericanhistory.org/person/chin-h-liao/>
  · `modified` on source: **2026-06-19T16:42:09** · `page_bytes`: 55,480
  · profession taxonomy (`class_list`): `person_profession-community-leader`,
    `person_profession-oncologist`, `person_profession-physician`
    (numeric `person_profession: [2242, 2257, 2234]`; no name→id map archived on this box)
  · The org appears in TWO fields of this one record:
    `Accomplishment` → `2. 北美路加醫療傳道會董事主席,2011-2016` and
    `Notable Accomplishments` → `北美路加醫療傳道會董事主席，2011-2016`,
    plus the site-rendered `Community` block (`北美路加醫療傳道會 / 董事主席`, no years).
  · `content_html` and `excerpt` are empty — the form fields are the whole payload.
  · Blank fields proving nothing org-level is withheld elsewhere on the record:
    `Publication(Non-professional ones)` `--`, `Hobby` `--`, `Website or Blog` `--`,
    `family_filled: false`.

## Twin serialization (same payload, second rendering)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho902.md`
  · original <https://taiwaneseamericanhistory.org/whoswho902/> · H1
  `992. Chin H. Liao 廖俊惠 / 2016/05` (number-collision note: vault work page
  [[works/taiwaneseamericanhistory-org/whoswho902|TAH #992]] links it as `#992`;
  post number 902 ≠ entry number 992 — title verified before treating it as a sibling)
- Line 72: `2.     北美路加醫療傳道會董事主席,2011-2016` — same string as the JSON field.

## Twin & containment check (2026-11-14, this pass)
Method per the-theodore-ted-wing correction: the JSON side sliced from the profile's
own marker `Who's Who Taiwanese American Profile` to the footer line
`Travel the roads paved`; normalization strips `#`/whitespace.
- JSON content block: 903 norm chars · md5 `25b5a580d7f91ddc28fc99b3c703bd23`
- Post dump (frontmatter stripped): 498 norm chars · md5 `6e231df15687fecb353ac085e3184c6c`
- Naive containment: neither direction (sizes 903 vs 498).
- **Field-level containment (the real test):** normalizing also punctuation
  (`、,，.。:：;；()（）-–—/`) and checking every non-empty line of the post dump
  against the FULL `page_text`: **38 lines, 1 missing — only the post's own numbered
  title `992 ChinHLiao廖俊惠201605`.** The dump is a serialization subset of the
  profile page → **one self-report rendered twice, NOT two independent records.**
- Consequence for labeling: the 2011–2016 董事主席 row stays `sourced` (self-report),
  never `documented`; agreement across the two artifacts is not corroboration.

## Whole-corpus sweep (2026-11-14, this pass)
`grep -rlF` per name form over `content/` + `knowledge/` (machine indexes
`units.jsonl` / `posts/index.jsonl` / `ee-vault-index.*` / `content-analysis/*.jsonl`
excluded as non-sources):
- `路加醫療` → 5 non-index files: this capture, the org page,
  `content/people/chin-h-liao.md`, `content/organizations/index.md` (directory listing),
  and the two artifacts above. No third-party hit.
- `北美路加` → same 3 content files + same 2 artifacts.
- `Luke Medical` → only the org page + index (English form is OUR editorial gloss,
  not a source form — see below).
- `醫療傳道` in `knowledge/` → only `person/chin-h-liao.json` (and indexes).
- `Medical Evangelism` → only `content/people/chin-h-liao.md` line 47, which
  parenthesizes it as 「北美路加醫療傳道會（Medical Evangelism Fellowship of North America）」.
  No artifact on this box (not in the JSON record, not in the whoswho902 dump) carries
  ANY English form → that parenthetical is an unattributed addition and is flagged
  on the person page; per the english-name-harmony rule a Chinese-only name gets no
  English unless a source states it.
- `廖俊惠` / `Chin H. Liao` hits classify as: his own pages/records, the six-city
  會館 statement press item (TACNC presidency, unrelated to this org), oral history
  #181, work/index hub listings, and indexes — none names this org.
- `路加` alone (control, non-vacuous): hits are same-word-different-entity —
  ITPC 路加小組 small group, 聖經路加福音 quotations, 東京聖路加女子專門學校 /
  聖路加國際醫院 (謝娥、陳翠玉、鍾信心 bios), and a pediatrician pen-name 路加 in
  columns23 — all excluded.

## What this capture does NOT establish
- English official name (none stated on this box).
- Founding year, headquarters, membership roster, mission statement, programs.
- Whether the org is still active after 2016.
- Any second officer or member by name.

## Related
- [[organizations/beimei-luka-medical-mission|北美路加醫療傳道會]] — subject org page
- [[people/chin-h-liao|Dr. Chin H. Liao 廖俊惠醫師]] — sole attestant (self-report)
- [[works/taiwaneseamericanhistory-org/whoswho902|TAH #992 Chin H. Liao / 2016-05]]
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]

## Third-party pass (2026-11-17, card t_a60b223c)

This capture's 2026-11-14 sweep was corpus-local (`grep -rlF` over `content/` + `knowledge/`) and correctly reported no second source **on this box**. It was later superseded on the public web — the org has its own site and press coverage — so the org-level facts (English name 「Luke Christian Medical Mission」/LCMM, 1988 vs 1989 founding, Fremont HQ, board rosters, 2012 RMMC ministry) are recorded on the org page's `## Third-party record` section, not here.

- **2026-11-17 — this capture's `Medical Evangelism` finding STANDS:** no 2026-11-17 web artifact (org 官網, 《The Calling》 PDFs, oursweb directory, 門諾 blog, TCNN) carries 「Medical Evangelism Fellowship of North America」; the source-stated English form is 「Luke Christian Medical Mission」 <https://church.oursweb.net/church.php?pkey=815047>, so the person-page parenthetical remains an unattributed addition and stays quarantined.
- **2026-11-17 — `路加` collision set EXTENDED:** add 中華基督教路加傳道會 / Chinese Christian Medical Mission (CCMM, Taiwan publisher of 《路加傳道會》, its NO.409 Nov 2025 masthead lists 「北美路加醫療傳道會 L.C.M.M.」 as a separate body, per <https://www.maiyajiaoan.com/wiki/33292.html>) to the same-word-different-entity exclusions — related to, but not the same organization as, this page's subject.
- **2026-11-17 — attestant corroboration status:** the TAH self-report's `2011-2016` chairmanship now has independent support for its START year only (官網 dates the 董事會 reorganization to 2011/06, <https://lcmmusa.org/aboutus.html>); the END year 2016 is still attested solely by the self-report analyzed above, so the row stays `sourced`.

---
title: "TAH organization directory capture — Taiwanese International Student Association (UT Austin)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization-directory
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese International Student Association (UT Austin)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 863
- wikilinks: 1


Capture page minted by FLOOR-ANCHOR card t_7b0c597f (2026-11-14). The single citable
source on this box for this org is the TAH Foundation organization directory entry;
the archived machine copy plus the full corpus-grep classification are recorded here
so future passes do not re-grep.

## Subject
- [[organizations/taiwanese-international-student-association|Taiwanese International Student Association (TiSA, UT Austin)]] — TAH organization record id 77572

## Capture — crawled organization record
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-international-student-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-international-student-association/](https://taiwaneseamericanhistory.org/organization/taiwanese-international-student-association/)
- **Record:** id 77572 · `type: tah_organization` · `modified: 2026-06-09T17:23:23` · file mtime (crawl) 2026-08-17 00:45 PT · 1,778 bytes · md5 cfdb85e0c0d34c350e8f630eae173f91
- **class_list (6):** `post-77572`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`, `organization_type-student` — the site taxonomy tags this entry as a student organization.
- **`person_profession`:** `[]` · **`excerpt`:** None — the whole record body is `content_html` (2 paragraphs).
- **Coverage note (what the prior passes missed):** the org page carried only ¶1 of `content_html`. ¶2 — the Center for Taiwan Studies mission/advisory block — was never opened until card t_7b0c597f (2026-11-14) and is absorbed verbatim into the org page.
- **Verbatim ¶1 fields (already on the org page):** full English + Chinese name (Taiwanese International Student Association / TiSA / 德州大學台灣國際學生會); student organization at the University of Texas at Austin serving Taiwanese and Mandarin-speaking undergraduates 「as well as others interested in Taiwanese culture」; 「registered on UT Austin's official HornsLink student organization directory」; website uttisa.com, Facebook handle TiSAatUT (221 likes), Instagram @tisa_utaustin.
- **Verbatim ¶2 fields (absorbed by this card):** 「TiSA's stated mission, as documented by UT Austin's Center for Taiwan Studies, is to promote a sense of belonging for Taiwanese and Mandarin-speaking undergraduate students at UT Austin, as well as those interested in Taiwanese culture」; 「The Center for Taiwan Studies (CTS) has served in an advisory role to TiSA, with the CTS director assuming the position of faculty advisor, reflecting a formal institutional connection to Taiwan-focused academic programming at the university」; 「TiSA hosts general meetings, welcome events, and social programming each semester to welcome new members」.
- **Single-record status:** one editable directory record. Per the capture-quality rule, restatement across its own paragraphs is one self-report rendered once — absorbed quotes stay at `sourced`, not `documented`.

## Twin / sibling check (2026-11-14, this card)
- **No `posts/` twin:** org-dir records have no story-corpus dump twin (brown-risd precedent). Same-id collision check: `grep -F 77572 knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl` → 0 hits.
- **Org-dir containment scan** over all 339 `organization/*.json` (tag-stripped, whitespace-folded `content_html`, both containment directions): the ONLY file containing or contained by this record's text is this record itself. No sibling org record restates TiSA.
- **Same-batch neighborhood:** 82 of 339 org records carry a `modified` stamp in `2026-06-09T17:23:2x` — a batch edit window, so any same-minute adjacency is batch authorship, not corroboration (none of those 82 mentions TiSA anyway).
- **Acronym-collision siblings pre-classified (not this org):**
  - `organizations/asu-taiwanese-international-student-association.md` — ASU TISA (亞利桑那州立大學台灣國際學生會, record 77594), a different campus org; its own capture page `content/sources/asu-tisa-tah-org-capture.md` records the parallel rulings.
  - `topics/t-臺灣週開幕-賴清德揭金融發展-3-方向-彭金隆承諾加速-tisa-租稅優惠修法.md` and the t_77d71750 entry in `topics/transnational-repression.md` (2026-11-02/03) — 「TISA」 there is 台灣的個人投資儲蓄帳戶 (Taiwan Individual Investment Savings Account) policy, an acronym collision recorded so a future grep cannot read it as presence.
  - base32 `archive_digest` substrings `…TISA…` inside taiwanjustice-net machine dumps — hash noise, not mentions.

## Whole-corpus grep classification (2026-11-14, card t_7b0c597f)
`grep -rli` / `grep -rlF` per name form over `content/` + `knowledge/`:
- `TiSA` (case-insensitive) — all third-party-looking hits verified as: the two TISA org pages + their JSONs, the Taiwan-policy topics pages, base32 digest noise, `media/*.mp3` byte noise, and unrelated prose substrings (`partisan`, `artisans`, `nonpartisan`, `bipartisan`, `non-partisan`, `Bipartisan`) in `organizations/democratic-progressive-party.md`, `organizations/taiwanese-american-citizens-league.md`, `organizations/laguna-woods-village-taiwanese-club.md`, `organizations/rice-taiwanese-association.md`, works pages, and `articles/taiwanjustice-net/*`. No third-party mention of this org.
- `台灣國際學生會` — 6 files: this org page, the ASU org page, `topics/transnational-repression.md` (acronym ruling), `sources/asu-tisa-tah-org-capture.md`, and the two org JSONs. No third-party mention.
- `uttisa` — 2 files: this org page + its own JSON (handle recorded nowhere else).
- `TiSAatUT` / `tisa_utaustin` — 2 files each: this org page + its own JSON.
- `Center for Taiwan Studies` — corpus hits are UT-Austin-unrelated: UCSB TSA/TSASB org pages, `people/dr-chiu-shan-chen`, `people/prof-ping-hui-liao`, `people/tony-hsieh`, `people/i-chen-wang`, `organizations/the-chuan-lyu-foundation`, `organizations/san-diego-taiwanese-cultural-association`, TAH works pages (our-journeys-384/385/386/390, my-stories-793), one taiwanjustice-net article; plus machine indexes (`units.jsonl`, `tah-a-slice-1.jsonl`, `posts/index.jsonl`) which are not sources. None names TiSA or UT-Austin CTS↔TiSA advisory relations.
- Austin historical records `works/taiwaneseamericanhistory-org/ourjourneys45`, `ourjourneys76`, `ourjourney-343` describe the ~1970-era UT-Austin Taiwanese Association, not this HornsLink-registered student org (already distinguished by the 2026-10-07 deepen-x pass); not absorbed.
- **Ruling:** no memoir, article, or newsletter in the vault names this org. The TAH directory record above is the only citable source.

## NEED YOU
- HornsLink registration page, uttisa.com, Facebook TiSAatUT, Instagram @tisa_utaustin — cited inside the TAH record, none archived locally; a Wayback capture of any would upgrade the listing facts from `sourced` to independently `documented`.
- UT Austin Center for Taiwan Studies page naming the CTS director as TiSA faculty advisor — the ¶2 institutional claim's primary surface, not archived here.
- Founding year, officers, membership size, active years: no source on this box beyond the single TAH directory entry. If you were a TiSA member or hold a flyer/photo/social export, submit via the NEED YOU path.

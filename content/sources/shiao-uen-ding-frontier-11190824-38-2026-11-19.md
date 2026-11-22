---
title: "Frontier re-pass receipt — Shiau-uen Ding 丁曉雯 (FRONTIER-11190824-38)"
type: source
tags:
  - source
  - frontier-harvest
verification_status: pending
tier: M
last_reviewed: 2026-11-19
---
# Frontier re-pass receipt — Shiau-uen Ding 丁曉雯 (FRONTIER-11190824-38 / t_ac7ac2d5)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 800
- wikilinks: 1


## Identity Snapshot
- **Subject:** Shiau-uen Ding 丁曉雯 — Taipei-born pianist, NYC-based; NTNU 音樂系 + University of Cincinnati (CCM) DMA; NeXT Ens co-founder/director; TAH Who's Who musician records #64/#92.
- **This pass's scope:** tier-M dangling-target frontier re-pass 2 on `people/shiao-uen-ding` — 4 online arms re-run + registry pre-check + official-site re-anchor. Do-not-publish; commit only. Prior pass: FRONTIER-11180842-32 (t_e6ed1a2e, 2026-11-18).

Date: 2026-11-19 (PST). Tier M. Target: [[people/shiao-uen-ding|Shiau-uen Ding 丁曉雯]].
Dangling target: `people/shiao-uen-ding\` (refs=1 dossier_refs=0 corpus=1 score=1) — person page exists and is
fully linked (works #64/#92 + sources); this is the re-pass after the 11180842-32 deepening.
Excerpts on disk: `knowledge/web-archives/shiao-uen-ding-frontier-11190824-38-2026-11-19/`.

## Online arms (searched Shiau-uen Ding / 丁曉雯, 2026-11-19)

1. **zh.wikipedia infobox+awards — miss (reconfirmed).** `list=search srsearch="Shiau-uen Ding"` → `[]`
   (`wp-zh-search-shiau-uen-ding-repass.json`); `srsearch=丁曉雯 鋼琴` → 10 fuzzy token hits, none is this
   subject (`wp-zh-search-ding-piano-repass.json`); exact title 丁曉雯 = the singer/producer, revision
   timestamp unchanged **2026-09-13T10:40:47Z**, content still 1963/王傑/小虎隊/飛碟/滾石 markers, no
   鋼琴家/辛辛那提 (`wp-zh-dingxiaowen-revision-repass.json`) → 同名不同人 HOLD stands, no article for this
   subject.
2. **Wikidata claims — miss (reconfirmed).** `wbsearchentities` en `Shiau-uen Ding` → `search: []`
   (`wd-search-shiau-uen-ding-en-repass.json`); zh `丁曉雯` → only Q85873717 Hsiao-Wen Ting "Taiwanese
   record producer, songwriter and former singer" = the other subject
   (`wd-search-ding-xiaowen-zh-repass.json`). No entity for this subject ⇒ no claims ⇒ no conflict HOLD.
3. **Official site / event page — absorb (corroboration re-anchor only).** shiauuending.com re-fetched with
   `curl -k` (site cert currently mismatches hostname — `SSL: no alternative certificate subject name`, so
   HTTPS verification fails; content re-anchored via `-k`): home / about.html / events.html / recordings.html
   text **byte-identical after tag-strip to the 2026-11-18 archives** — no drift. EMM festival page re-fetched:
   `emmfestival.org` and `emmfestival.org/index.php` both render 「February 5-6, 2027 … guest performer will
   be Shiau-uen Ding」 — this pass saw only the 5-6 variant, so the EMM date variant note now closes toward
   **February 5-6, 2027** (single-source festival page; still announced engagement).
   Vox Novus member page recovered at its live legacy URL
   `http://www.voxnovus.com/member/Shiau-uen_Ding.htm` (https fails; the https/member path is dead) —
   `voxnovus-member-repass.json/html`; content = the same TAH-verbatim bio + the NYT 2009 Marathon 「daredevil」
   excerpt already absorbed 11-18. No new entity-level facts (tier M = corroboration rows only).
4. **ZH press (World Journal / 大紀元 / 台灣日報) — miss for new facts.** No hit from the three named outlets
   ties to this subject. Fresh ZH-side hits this pass are: (a) the singer 丁曉雯 (Rachel Ting) rows — 自由娛樂
   林隆璇螢幕情侶, 麻吉弟弟評審, 民歌45/五十 協會理事長 丁曉雯, 聯合報 流行音樂碟報 — all the 同名不同人 singer,
   rejected per the standing ruling; (b) this subject's own already-archived surfaces (TAH #64/person,
   DigiLog 1136, 台灣古典音樂網 Facebook photo-album copy of the t-classical 專訪); (c) a **new institutional
   lecture-list corroboration**: 陽明交通大學 timetable 98-1 「音樂論壇」 course — 「11/3 丁曉雯(美國辛辛那提大學
   鋼琴演奏博士 http://shiauuending.com/) 講題：鋼琴與電子音樂之結合」 (`nycu-981-music-forum-repass.html`) —
   same 2009-10 masterclass chapter already on the person page (高師大/靜宜 rows), now a third independent
   institutional listing that also pins the shiauuending.com URL to the hanzi 丁曉雯; absorb as corroboration.

## Registry pre-check (before any mint idea)
`ee_vault_retrieve`/`_brain_retrieve` (scripts/echopedia-first-answer.py), 2026-11-19:
- `丁曉雯` → top hit `people/ding-xiaowen-singer` (the 同名不同人 marker page, Tier D ruling surfaced) — expected;
- `Shiau-uen Ding` and `Shiao-Uen Ding` → both resolve to `people/shiao-uen-ding` — collision-free, romanization
  variants already indexed to the one page. No orphan, no new person, **no mint**.

## Holds inherited / updated
- 同名不同人 HOLD (2026-11-12, singer 丁曉雯 / Rachel Ting): **stands**; all fresh ZH-press rows this pass belong
  to the singer.
- Romanization HOLD (TAH #64 Shiau-uen vs #92 Shiao-Uen): **stands** — TAH's own two entries, never auto-merged.
- LinkedIn Bloomberg-LP row: still `alleged`, snippet-only; unchanged.
- EMM 2027 exact dates: variant note **closed toward February 5-6, 2027** (this pass fetched both page variants,
  both render 5-6; the 11-18 index.php 4-6 variant not reproduced).
- Birth date / 出生地 gap: unchanged (no zh.wp or Wikidata record for this subject).

## Skipped (baked card facts not used)
- Builder corpus co-occurrence count: builder offline (card note). Fresh full grep of `content/` for
  丁曉雯/Shiau-uen Ding/Shiao-Uen Ding unchanged vs the 2026-09-16 saturation set: own records #64/#92, this
  page, person page, ding-xiaowen-singer marker, sources (taiwaneseamericanhistory-org, zhwp-shiao-uen-ding,
  frontier pages), .wiki-index, plus unrelated 丁紀明-class names (j-m-ding, john-shiau, walter-h-shiau token
  hits). Nothing new absorbable.
- Dated archive lines: dry-run emitted none (corpus=1 = the two TAH encyclopedia records, already recorded in
  Vault Record Notes / From the record).
- Vox Novus bio + NYT excerpt: entity-level content already absorbed 11-18; not re-ingested at tier M —
  URL relocation recorded only.
- allmusic.com / Apple Music / Instagram / Facebook toy-piano roster / 5of4 page: artist-aggregator and
  self-published social surfaces; no new verifiable dated fact beyond what From the record already carries;
  recorded here as future-fetch candidates.
- t-classical.com.tw 專訪 (台灣古典音樂網): domain still unreachable this pass (connection reset on root);
  Facebook photo-album mirror found but only reproduces the already-cited bio — link retained for a future pass.

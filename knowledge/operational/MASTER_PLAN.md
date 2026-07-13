---
title: "MASTER_PLAN"
category: "operational"
source: "audiobook-albert-lai/MASTER_PLAN.md"
created: "2026-07-12"
---

# MASTER PLAN — Toward A Community of Hope Audiobook

**Status:** Execution started 2026-07-09  
**Author:** Dr. Albert S. Lai (賴信雄)  
**Work:** *Toward A Community of Hope — A Mission to Formosan Community in Los Angeles*  
**Languages:** English · Taiwan Mandarin (台灣華語) · Taiwanese Hokkien (台語)  
**Targets:** Professional narrated audiobook → YouTube Music + major streaming / audiobook stores

> Full conversational plan (detailed phase narrative) was produced in Hermes session 2026-07-09.  
> This file is the **operational master** used for execution. Expand sections as decisions lock.

---

## 1. Product definition (v1)

### SKUs
| ID | Language | Scope | Priority |
|----|----------|-------|----------|
| A | English | Unabridged full book | P0 |
| B | Taiwan Mandarin | Unabridged full book | P0 |
| C | Taiwanese Hokkien | Companion EP / 選讀 (then optional full) | P1 |
| D | Samples | Ch.1 free samples for marketing / Echopedia | P0 |

### Narration policy
- **Retail masters:** human professional narrators (default).
- **Author inserts:** Albert preface / name reel / optional chapter blessings.
- **AI voice:** scratch tracks & timing only unless (a) commercial consent for synthesis, (b) platform policy allows, (c) disclosure completed. **Not** default for Audible/ACX.

### Success criteria (definition of done)
- [ ] Legal chain-of-title: text + all voices + any music
- [ ] Masters meet loudness/peak targets per channel
- [ ] Chapterized tracks, consistent numbering across languages
- [ ] Cover + metadata pass distributor validation
- [ ] Live on at least one of: YouTube Music, Spotify, Apple; plus audiobook path if pursued
- [ ] Pronunciation bible signed off for names/places
- [ ] Albert + TAHS approvals archived

---

## 2. Rights & consent (Phase 1) — GATE

### Text
- Written **Audiobook & Digital Distribution License** covering world territory, streaming, download, YouTube video+audio, EN/華語/台語, samples, monetization policy.
- Clear third-party quotes, hymns, letters separately or cut.

### Voice
- Written + on-tape consent for each speaker.
- Must include **commercial streaming** (not only Echopedia archival).
- Separate schedule if AI voice cloning is ever used.

### Music
- Prefer no continuous bed under dense prose.
- Optional short original/stinger cleared for monetization.

### Platform notes
- ACX/Audible: historically human-narration oriented — verify before AI.
- YouTube: disclose altered/synthetic content if applicable.
- Dual-path distribution: audiobook aggregator + music DSP for YT Music.

**Templates:** `00_legal/`, `08_consents/`

---

## 3. Editorial (Phase 2)

### Audio Master Text (AMT)
1. Freeze English source edition (prefer cleaned 2025 republication if licensed).
2. Version-control AMT; close changelog at v1.0.
3. Footnotes → end-of-chapter notes or omit with editorial judgment.
4. Rewrite “see page X” for audio.
5. Split long chapters into Part A/B (target 15–40 min tracks).

### Adaptation
- Cold open optional; read full chapter titles.
- Quote protocol: “quote … end quote”.
- Runtime estimate: ~150 wpm EN; native pacing for 華語/台語.

### Multilingual
- **ZH-TW:** full translation, Taiwan church vocabulary.
- **Hokkien:** literary adaptation preferred over literal academic calque; start with EP if budget/time tight.
- Shared **Pronunciation Bible** + Albert reference reel.

### Term policy
- “Formosan” / “Taiwanese”: keep author’s wording in quotations; modern framing only in producer intros if needed.
- Living persons: risk pass before retail.

---

## 4. Casting & direction (Phase 3)

| Role | Brief |
|------|--------|
| EN narrator | Warm scholarly-pastoral, 145–160 wpm, mature color |
| 華語 narrator | Taiwan Mandarin (not default PRC broadcast), church lexicon OK |
| 台語 narrator | Native Hokkien; 漢羅/Tâi-lô literate preferred |
| Albert | Prefaces, pronunciation reel, optional closings |

**Audition set (each language):** 90s Ch.1 cold read · 60s names · 45s emotional testament · 30s dense theology line.

Briefs: `11_casting/`

---

## 5. Recording (Phase 5)

### Tech
- 48 kHz / 24-bit WAV; mono or dual-mono; noise floor as low as practical.
- Mic: quality condenser or SM7B-class dynamic.
- Daily backups to two locations.

### Session ritual
1. Slate (title, chapter, date, language, narrator)
2. 30s room tone
3. Section blocks + same-day pickups
4. Pickup sheet with reason codes

### Multilingual rule
Same chapter/track numbers across EN / 華語 / 台語 editions.

---

## 6. Post & masters (Phase 6)

### Process
Edit → gentle denoise → de-ess → EQ → light compression → limit.

### Loudness (starting point)
- **Reference master:** −16 to −18 LUFS integrated, true peak ≤ −1.5 dBTP
- Derive platform encodes; follow ACX/distributor if stricter (e.g. true peak ≤ −3 dBTP historical ACX).

### QC
Full proof-listen vs script; second ear mandatory for 華語 and 台語.

---

## 7. Hokkien strategy (anticipate difficulty)

| Option | Description | When |
|--------|-------------|------|
| H1 | Full Hokkien audiobook | Budget + adapter available |
| H2 | Hybrid: 華語 main + 台語 summaries | Middle path |
| **H3 (v1 default)** | 台語選讀 EP (6–10 tracks) | Ship without blocking EN/華語 |

Always: adapter + second Hokkien proof listener.

---

## 8. Packaging & metadata (Phase 8)

- Cover 3000×3000; language badge on each edition.
- UPC per album; ISRC per track.
- Album titles include language + “Unabridged Audiobook” / 有聲書.
- Credits: Written by Albert S. Lai; Narrated by …; Produced by TAHS/Echo.
- Copyright/phonogram lines set at release.

---

## 9. Distribution (Phase 9)

### Path A — Audiobook stores
Findaway Voices / Author’s Republic / ACX → Audible, Apple Books, libraries, etc.

### Path B — YouTube Music & DSPs
CD Baby / DistroKid / TuneCore as **chapter album**; also YouTube playlist + optional full video with chapters.

### Release order
EN → 華語 (+7d) → 台語 EP (+14d); Ch.1 sample at T−14.

---

## 10. Archive

```
/Albert_Lai_Audiobook/  (this repo folder)
  00_legal … 12_distribution
```
sha256 manifest at first master delivery.  
**Never** commit private phone numbers or raw unreleased WAVs to public `gh-pages`.

---

## 11. 90-day timeline (summary)

| Window | Focus |
|--------|--------|
| D1–7 | Rights, source freeze start, Albert kickoff, name reel |
| D8–21 | Scripts, casting, ZH-TW start, Hokkien EP outline |
| D22–45 | Record EN; edit parallel; Albert intros |
| D46–65 | 華語 + 台語 record; covers |
| D66–80 | Masters, metadata, unlisted QC |
| D81–90 | Publish EN → 華語 → 台語; Echopedia sample links |

---

## 12. Risk register

| Risk | Mitigation |
|------|------------|
| Rights unclear | No paid production until signed |
| Hokkien delay | EP scope H3 |
| AI platform rejection | Human retail masters |
| Academic denseness | Audio adaptation |
| Name inconsistency | Bible + Albert reel |
| Burnout | Ship EN first |

---

## 13. Immediate execution artifacts

| Artifact | Path |
|----------|------|
| This plan | `MASTER_PLAN.md` |
| Status | `STATUS.md` |
| Week actions | `NEXT_ACTIONS.md` |
| Text license template | `00_legal/TEXT_AUDIOBOOK_LICENSE_TEMPLATE.md` |
| Rights memo | `00_legal/RIGHTS_MEMO.md` |
| Voice consent | `08_consents/VOICE_CONSENT_COMMERCIAL_STREAMING.md` |
| Pronunciation bible | `02_pronunciation/PRONUNCIATION_BIBLE.md` |
| Chapter map stub | `01_AMT_scripts/en/CHAPTER_MAP.md` |
| Casting briefs | `11_casting/` |
| Cover brief | `06_artwork/COVER_BRIEF.md` |
| Albert agenda | `10_release_notes/ALBERT_KICKOFF_AGENDA.md` |
| Distributor checklist | `12_distribution/DISTRIBUTOR_CHECKLIST.md` |

---

## 14. Relationship to existing pilot

Echopedia already hosts:
- Consent kit scoped to **website/archival** use (insufficient for retail streaming).
- Ch.1 ~30 min Taiwanese-accented **female AI** pilot.

**Execution policy:** pilot = pacing/mood reference only; retail = human masters unless explicitly re-approved. Upgrade all consents before any commercial upload.

---
title: "Albert ch.1 audiobook consent kit"
type: person
tags:
  - 
verification_status: pending
tier: M
last_reviewed: 2026-11-16
---
# Albert Chapter 1 Audiobook — Consent & Recording Kit

This page is the execution kit for producing Chapter 1 audiobook narration using Albert’s voice with explicit permission and source traceability.

## 1) Written Consent Template (send first)

I, [Full Name], give permission to the Echo/Echopedia team to use my voice for narration of:
- Work: "Toward A Community of Hope"
- Scope: Chapter 1 (Formosan in Formosa Yesterday)
- Usage: Echopedia website playback and archival historical education use
- Processing: voice recording cleanup and/or AI voice synthesis based on approved samples
- Duration: [one-time release / ongoing until revoked]
- Revocation: I may request removal or replacement in future releases
- Attribution: [How name should appear]

Signature: ____________________
Date: ____________________
Preferred Contact: ____________________

## 2) Spoken Consent Script (record verbatim)

"My name is [Name]. Today is [Date]. I authorize the Echo/Echopedia team to use my recorded voice for Chapter 1 of Toward A Community of Hope for publication on Echopedia. I understand this may include audio enhancement and AI-assisted synthesis based on my approved recordings."

## 3) Recording Requirements (preferred)

- Quiet room, no speakerphone, no background music
- File format: WAV (preferred), mono, 16kHz or 24kHz+
- Total sample target for cloning: 10–30 minutes
- Speaking style: natural pace, clear articulation, normal conversational warmth
- Include Taiwan/TAHS name pronunciations in sample set

## 4) Sample Prompt Set (for voice quality)

Please record:
1. 60–90 seconds reading your normal introduction
2. 2–3 paragraphs from Chapter 1
3. 1 paragraph with names/places (Taiwan, Formosa, Los Angeles, Presbyterian, etc.)
4. 1 paragraph with emotional variation (reflective/hopeful tone)

## 5) Twilio Outreach Message (short version)

Hi Albert — we’re preparing a Chapter 1 audiobook for Echopedia and would love to use your voice with your explicit permission. If you’re open, we’ll send a simple consent note and a short recording guide (10–30 min clean sample). We can also schedule a quick call to walk through it. Thank you!

## 6) Quality Gate Before Full Chapter

Before full production, produce a 60–90 second pilot and check:
- Pronunciation accuracy
- Natural pacing
- No clipping/noise artifacts
- Approval from stakeholders

Status update:
- Full Chapter 1 narration has now been published at [[people/albert-chapter1-audiobook-taiwanese-female||Albert Chapter 1 Audiobook（第一章有聲版）]].
- Consent route on file: the kit's written + spoken consent templates were for a human-voice build. What shipped instead is AI scratch narration, and the recorded permission for that direction is **commercial production GREEN, 2026-07-09** — per `people/albert-chapter1-en-review.md` and `people/albert-chapter1-zh-review.md`.

## Identity Snapshot
- Type: Production kit / consent documentation
- Geography: North America
- Core roles: audiobook production, consent management, archival

## Review & Production Record (vault)

Chapter 1 production artifacts already in the vault:

- 已發布有聲版：[[people/albert-chapter1-audiobook-taiwanese-female||Albert Chapter 1 Audiobook（第一章有聲版）]]
- 審校記錄：[[people/albert-chapter1-en-review||EN review]]、[[people/albert-chapter1-zh-review||zh review]]、[[people/albert-chapter1-zh-review-v2||zh review v2]]、[[people/albert-chapter1-zh-hsiaochen-full-review||Hsiaochen full review]]
- 文本來源：[[sources/toward-a-community-of-hope||Toward A Community of Hope]]；voice 來源人：[[people/albert-s-lai||Dr. Albert S. Lai (賴信雄)]]

## 7) Publication Metadata (required on page)

- Narrator / voice attribution
- Consent status/date
- Audio version/date
- Source confidence note
- Link to this kit page

## 8) Commercial streaming upgrade (2026-07)

Archival Echopedia website scope is **not** enough for YouTube Music / Spotify / Apple retail.

Production files live **privately** on the server (not published to gh-pages):

- Project root: `echo-system/audiobook-albert-lai/`
- Plan: `MASTER_PLAN.md` · Status: `STATUS.md` · Next: `NEXT_ACTIONS.md`
- Commercial text license template + streaming voice consent under `00_legal/` and `08_consents/`

Do **not** upload signed consents, personal phone numbers, or raw session WAVs to the public wiki.

## Production Record (Chapter I artifacts on this box)

What has actually been rendered for Chapter I, and where the proof lives. Every line is a
local build artifact — nothing here is a claim about the published retail product, which
stays a human cast.

| Date | Item | Value | Source |
|------|------|-------|--------|
| 2026-07-09 | EN Chapter I scratch rendered | 4,329 words · 29.13 min · 148.6 wpm · −16.18 LUFS | `audiobook-albert-lai/09_qc_reports/SKU_A_EN_SCRATCH_QC.md` |
| 2026-07-09 | Permission gate | commercial production GREEN | per `people/albert-chapter1-en-review.md` |
| 2026-08-02 | ZH voice gate | Albert lock: `zh-TW-HsiaoChenNeural` — Ch.1 full evaluated before Ch.2–VI | `audiobook-albert-lai/09_qc_reports/SKU_B_ZH_CH01_HSIAOCHEN_FULL.json` |
| 2026-08-02 | ZH Chapter I full scratch rendered | 7,690 chars · 35.71 min · 215.3 chars/min · −16.16 LUFS output | same QC JSON; master `04_edited_wav/zh_ch01_scratch/ch01_hsiaochen_v1_full_scratch.mp3` |
| 2026-08-02 | ZH bake-off result | #2 HsiaoChen chosen by Albert + friends over YunJhe and HsiaoYu | per `people/albert-chapter1-zh-review.md` |
| 2026-10-26 | AMT freeze | AMT_v1.0 frozen — 50 files, sha256, incl. `01_AMT_scripts/zh-TW/AMT_v1.0/ch01.md` | `audiobook-albert-lai/MANIFEST-AMT_v1.0.json` |
| 2026-11-11 | Gate state (latest) | A00 作者簡介 new track accepted; Chinese audiobook review basically complete; do not re-record passed tracks | `audiobook-albert-lai/STATUS.md` |

Scope note: the QC reports both mark these builds **"SCRATCH / review only — not retail
master"**, so the consent templates in §1–§2 above remain the open path for any future human
recording; no signed human consent is on file in the vault for Chapter I.


## Network

Pages that link to **albert-chapter1-audiobook-consent-and-recording-kit** (albert-chapter1-audiobook-consent-and-recording-kit):


### People (9)

1. [[people/albert-chapter1-audiobook-taiwanese-female|albert-chapter1-audiobook-taiwanese-female]]
2. [[people/albert-chapter1-audiobook-taiwanese-female|albert-chapter1-audiobook-taiwanese-female]]
3. [[people/albert-chapter1-audiobook-taiwanese-female|albert-chapter1-audiobook-taiwanese-female]]
4. [[people/albert-chapter1-en-review|albert-chapter1-en-review]]
5. [[people/albert-chapter1-zh-hsiaochen-full-review|albert-chapter1-zh-hsiaochen-full-review]]
6. [[people/albert-chapter1-zh-hsiaochen-full-review|albert-chapter1-zh-hsiaochen-full-review]]
7. [[people/albert-chapter1-zh-review-v2|albert-chapter1-zh-review-v2]]
8. [[people/albert-chapter1-zh-review|albert-chapter1-zh-review]]
9. [[people/albert-s-lai|albert-s-lai]]

## Source Notes

- `audiobook-albert-lai/09_qc_reports/SKU_A_EN_SCRATCH_QC.md` — EN SKU A scratch QC table (generated 2026-07-28, ch01 row from `04_edited_wav/en_ch01_scratch/QC_ch01_christopher_v1.json`).
- `audiobook-albert-lai/09_qc_reports/SKU_B_ZH_CH01_HSIAOCHEN_FULL.json` — ZH Chapter I full scratch QC, `generated_at` 2026-08-02T22:02:16+00:00, gate field quotes Albert's 2026-08-02 lock.
- `audiobook-albert-lai/MANIFEST-AMT_v1.0.json` — `"frozen": "2026-10-26"`, `"owner_ruling": "Leonard GO 2026-10-26: A decided, C open"`.
- `audiobook-albert-lai/STATUS.md` — project status, last updated 2026-11-11.
- [[sources/toward-a-community-of-hope||Toward A Community of Hope]] — the narrated work: 1971 D.Min. dissertation (San Francisco Theological Seminary), 2025 republication; the consent templates name this work, its Chapter 1 scope, and the 10–30 min clean-sample target.
- [[people/albert-chapter1-en-review||Ch.1 EN review build]] · [[people/albert-chapter1-zh-review||Ch.1 ZH bake-off]] · [[people/albert-chapter1-zh-hsiaochen-full-review||Ch.1 ZH HsiaoChen full eval]] — the review pages these QC artifacts back.

## GAPS / NEED YOU

Floor status (measured 2026-11-16, FLOOR-ANCHOR t_b02ffbb2): lint per-file exit 0, anchored=22/3,
wikilinks=18/1, fleet `--alert` grep 0 hits; `tier: M` recorded per card body (howard-ho
t_78a33025 exception). Harvest was stale-premise/verify-only — zero web searches spent: the
`anchored 0/3` premise is the pre-2026-11-12 snapshot and the page already carries the sourced
`## Production Record` table + `## Source Notes` from the 2026-11-12 pass.

No further citable Chapter I production source exists on this box (checked 2026-11-12, re-checked 2026-11-16):

- `audiobook-albert-lai/00_legal/` and `audiobook-albert-lai/08_consents/` — **do not exist on disk**; the commercial text license and streaming voice consent named in §8 are still not filed, so no signed consent is quotable.
- `audiobook-albert-lai/09_qc_reports/` — only the two files cited above; no human-recording session report.
- Vault grep (`content/`, 2026-11-12) for Chapter I / 第一章 audio hits: all external hits were idiom false positives; the only in-family sources are the pages and QC files already cited here.
- `people/albert-chapter1-audiobook-taiwanese-female.md` carries seven deepen-x SKIP passes (2026-09-17 → 2026-10-06) finding no independent community facts about this audio production.
- OPEN: no evidence on this box that the §1 written consent or §2 spoken consent was ever executed — the shipped Chapter I audio is AI scratch, which does not need a voice release. Confirm with Albert (LINE) before any human-cast recording is treated as cleared.

## Related Pages
- Toward A Community of Hope, Chapter I (Formosan in Formosa Yesterday) — text in the Tier-2 corpus; no local page yet
- [[sources/toward-a-community-of-hope||Toward A Community of Hope]]
- Echopedia Community Contributions Hub — page pending; no wikilink until it exists
- [[people/albert-chapter1-audiobook-taiwanese-female||Albert Chapter 1 Audiobook（第一章有聲版）]]
- [[people/albert-s-lai||Dr. Albert S. Lai (賴信雄)]]
- [[organizations/formosan-presbyterian-church-in-los-angeles||Formosan Presbyterian Church in Los Angeles (FPCLA)]] — the church movement Chapter I documents
- [[media/index||Media index]] — vault media library hosting the published chapter audio
- [[organizations/taiwanese-american-historical-society||Taiwanese American Historical Society (TAHS)]] — community-history partner for archival audio use

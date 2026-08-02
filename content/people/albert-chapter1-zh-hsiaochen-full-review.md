---
title: "Albert Ch.1 ZH full — HsiaoChen evaluation (SKU B gate)"
type: person
tags:
  - audiobook
  - albert-lai
  - review
  - zh-TW
verification_status: pending
last_reviewed: 2026-08-02
echo: scratch
---

# Chapter I 台灣華語 — HsiaoChen 全書章評估（SKU B 關卡）

**Status:** Full Chapter I AI scratch for **evaluation** after voice lock. **Not** retail master (retail = human cast).

**Decision (2026-08-02 · Albert + friends):** From the three bake-off candidates, **#2 HsiaoChen** is the locked voice. Complete Ch.1 first → evaluate → only then Ch.2–6.

**Bake-off (openings only):** [[people/albert-chapter1-zh-review|Ch.1 ZH voice bake-off]]  
**EN Ch.1:** [[people/albert-chapter1-en-review|Ch.1 EN Christopher]]  
**EN full book:** [[people/albert-en-sku-a-scratch-review|EN SKU A hub]]

## Identity Snapshot

- Work: Chapter I, *Toward A Community of Hope* (zh-TW AMT v1.0 full body)
- Voice lock: `zh-TW-HsiaoChenNeural` · rate `+0%` · pitch `+0Hz`
- Loudness: loudnorm target **−16 LUFS / −1.5 dBTP** (measured output_i ≈ −16.2, TP −1.50 on 192k master)
- Duration: **~35.7 min** (full chapter; bake-off opening was ~5.8 min)
- Public file: ~42 MB @ 160 kb/s (under GitHub soft limit); private production master also kept @ 192 kb/s

## Listen — full Chapter I (HsiaoChen)

Use headphones. Preload is metadata-only.

<audio controls preload="metadata" style="width:100%;max-width:40rem">
  <source src="../media/albert-ch01-zh-hsiaochen-v1-full-scratch.mp3" type="audio/mpeg">
</audio>

- [Download MP3](../media/albert-ch01-zh-hsiaochen-v1-full-scratch.mp3) · ~35:43 · full Ch.I

Absolute (if relative player fails on CDN lag):  
https://echocanhelp.github.io/wiki-public/media/albert-ch01-zh-hsiaochen-v1-full-scratch.mp3

## Method lock (do not change without new sign-off)

| Dimension | Setting |
|-----------|---------|
| Voice | zh-TW-HsiaoChenNeural |
| Rate / pitch | +0% / +0Hz |
| Loudness | −16 LUFS / −1.5 dBTP |
| Text | Speak-layer cleanup only; frozen AMT `zh-TW/AMT_v1.0/ch01.md` unchanged |
| Role | Review/scratch — not commercial AI retail without platform+consent path |
| Gate | **Albert eval of this full Ch.I** before any Ch.II–VI render |

## QC snapshot (2026-08-02)

| Metric | Value |
|--------|------:|
| chars (no space) | 7,690 |
| duration | 35.71 min |
| chars/min | ~215 |
| chunks | 27 (~420 chars) |
| loudnorm (192k master) | I ≈ −16.2 · TP −1.50 · LRA ~3.4 |

EN Ch.I Christopher was ~29 min @ ~149 wpm. ZH full Ch.I is longer in wall-clock (character density + scholarly pace at +0%). Rate bump (+5–10%) is **not** applied unless Albert asks after this listen.

## Evaluation checklist (for Albert / reviewers)

1. **Voice fit:** Does HsiaoChen hold scholarly-pastoral tone for a full ~36 min chapter (not just the opening)?
2. **Names / places:** Formosa（台灣）, 基隆, 高雄, 澎湖, Shimonoseki, Cairo, etc. — natural?
3. **Geography / lists (early sections):** Tempo OK or too slow/fast?
4. **History sections:** Clarity on treaties, dates, KMT / Formosan distinctions?
5. **Fatigue:** Any stretch where delivery becomes tiring or monotone?
6. **Blockers:** Anything that must be fixed before Ch.2–6, or “minor / does not affect full book”?

## What happens next

| If… | Then… |
|-----|--------|
| Approve Ch.I as-is (or minor nits only) | Proceed Ch.II–VI with **same** HsiaoChen lock; translate remaining AMT as needed; multi-track hub |
| Request rate/pitch change | Re-render Ch.I only with new settings → re-eval → then Ch.2–6 |
| Request text fixes | Patch zh AMT via version bump (not silent in-place); re-render Ch.I |

**Hold:** No Ch.2–6 full scratch until this gate is signed off in this group (or by Leonard).

## Related

- [[people/albert-s-lai|Dr. Albert S. Lai (賴信雄)]]
- [[people/albert-chapter1-zh-review|Bake-off (three voices, openings)]]
- [[people/albert-chapter1-en-review|EN Ch.1]]
- [[people/albert-en-sku-a-scratch-review|EN SKU A full hub]]

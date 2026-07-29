---
title: "Albert Ch.1 ZH audiobook review (zh-TW voice bake-off)"
type: person
tags:
  - audiobook
  - albert-lai
  - review
  - zh-TW
verification_status: pending
last_reviewed: 2026-07-29
echo: scratch
---

# Chapter I 台灣華語 Audiobook — Voice Bake-off

**Status:** Scratch AI narration for **voice / tempo / style review** only. **Not** the retail master (retail = human cast).

**Full EN SKU A (all chapters):** [[people/albert-en-sku-a-scratch-review|EN SKU A multi-track review hub]]

## Identity Snapshot

- Work: Chapter I, *Toward A Community of Hope* (zh-TW AMT v1.0)
- Narration: AI scratch · three zh-TW neural voices · scholarly-pastoral register
- Purpose: Echopedia review of voice, tempo, and style before full zh-TW render
- Retail: human narrator; this build is not final master

**Source AMT:** v1.0 frozen · Chapter I — *Formosan in Formosa Yesterday* (zh-TW translation)
**Book:** Dr. Albert S. Lai, *Toward A Community of Hope*

## Voice Bake-off

Three zh-TW neural voices were rendered from the same 135-character opening excerpt (Section I — The Land — Formosa). All samples are loudnormed to **-16 LUFS / -1.7 dBTP**.

### Samples

**YunJheNeural** (Male, Friendly/Positive) — rate `+0%`, pitch `-1Hz`

<audio controls preload="metadata" style="width:100%;max-width:40rem">
  <source src="https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-yunjhe-v1-scratch.mp3" type="audio/mpeg">
</audio>

- [Download MP3](https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-yunjhe-v1-scratch.mp3) · ~5:08 · 26.3 wpm

**HsiaoChenNeural** (Female, Friendly/Positive) — rate `+0%`, pitch `+0Hz`

<audio controls preload="metadata" style="width:100%;max-width:40rem">
  <source src="https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-hsiaochen-v1-scratch.mp3" type="audio/mpeg">
</audio>

- [Download MP3](https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-hsiaochen-v1-scratch.mp3) · ~5:48 · 23.3 wpm

**HsiaoYuNeural** (Female, Friendly/Positive) — rate `+0%`, pitch `+0Hz`

<audio controls preload="metadata" style="width:100%;max-width:40rem">
  <source src="https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-hsiaoyu-v1-scratch.mp3" type="audio/mpeg">
</audio>

- [Download MP3](https://echocanhelp.github.io/wiki-public/public/media/albert-ch01-zh-hsiaoyu-v1-scratch.mp3) · ~7:00 · 19.3 wpm

## Narration QC

| Dimension | Choice | Why |
|-----------|--------|-----|
| **Voices** | YunJhe / HsiaoChen / HsiaoYu | All three zh-TW neural voices available via edge-tts |
| **Tempo** | `+0%` (default) | Scholarly-pastoral register naturally slower; dense geographical exposition benefits from measured pace |
| **Pitch** | YunJhe: `-1Hz` / HsiaoChen & HsiaoYu: `+0Hz` | YunJhe (male) gets slight gravitas; female voices at neutral |
| **Loudness** | **-16 LUFS / -1.7 dBTP** | Streaming audiobook reference (−16 to −18 LUFS, TP ≤ −1.5) — verified post-loudnorm on all three files
| **Style** | Continuous prose, scholarly-pastoral | Academic tone without news-anchor delivery; suitable for 1971 dissertation content |
| **Register** | Taiwan Mandarin (zh-TW) | Per GLOSSARY.md: Formosa/Formosan policy — 1971 academic context retains Formosa/Formosan; general context uses Formosa（台灣） |

### Bake-off summary

| Candidate | Duration | WPM | Notes |
|-----------|----------|----:|-------|
| YunJheNeural | ~5:08 | 26.3 | Male voice; most measured pace; gravitas suits scholarly tone; pitch −1Hz adds warmth; TP −1.75 dB |
| HsiaoChenNeural | ~5:48 | 23.3 | Female voice; slightly slower; warm and clear; neutral pitch; TP −1.76 dB |
| HsiaoYuNeural | ~7:00 | 19.3 | Female voice; slowest; most deliberate; may be too slow for full chapter; TP −1.74 dB |

### WPM context

The EN Ch.1 Christopher scratch measured ~149 wpm. The zh-TW voices are significantly slower (19–26 wpm) due to the denser character-per-word ratio of Chinese and the naturally measured scholarly-pastoral register. This is acceptable for review — the full zh-TW render (SKU B) may use rate `+5%` to `+10%` to reach a more comfortable ~30–35 wpm equivalent while maintaining the scholarly tone.

### What to listen for (review checklist)

1. **Names/places:** Formosa（台灣）, Taipei, Tainan, Pescadores（澎湖）, Kamchatka（堪察加） — natural stress and pronunciation?
2. **Geography density (first 5 min):** Does tempo hold without rushing lists of distances and measurements?
3. **Pastoral vs academic:** Does the voice feel appropriately scholarly without being news-anchor-like?
4. **Formosa/Formosan policy:** Are the historical 1971 terms (Formosa, Formosan) read naturally without over-emphasis?
5. **Compare EN:** [[people/albert-chapter1-en-review|EN Ch.1 review (Christopher)]] — does the zh-TW voice carry the same scholarly authority?

## Opening text (AMT excerpt)

> 第一章 — 昔日的 Formosa 之中的 Formosan  </br>
> 第一節 — 土地 — Formosa  </br>
> 這個叫做 Formosa 的島嶼，中國人和日本人都稱之為台灣。它是連接從卡馬楚卡（Kamchatka）到馬來半島的一串島嶼的其中一環，並且遮蔽著東亞大陸海岸，免受開闢的太平洋的衝擊。Formosa 與中國大陸平行，並被寬達 90 英里的最窄處所分隔開來。它從北北東伸展到南南西，最大長度為 243 英里，寬度一般在 60 到 80 英里之間，面積近 14,000 平方英里——大致相等於馬賽諸斯、羅德島和康乃狄克三州結合在一起。

Full frozen AMT lives in the private production tree (`audiobook-albert-lai/01_AMT_scripts/zh-TW/AMT_v1.0/ch01.md`), not on this public site.

## Production notes

- **SKU B runtime (full book body):** ~4–5 h estimated (zh-TW often ~0.9–1.1× EN duration)
- **Ch.I alone (sample):** ~5–7 min across three voices
- **Permission:** commercial production GREEN (2026-07-09)
- **Next after your review:** lock zh-TW voice direction → full SKU B render with locked voice → multi-track hub
- **GLOSSARY:** `01_AMT_scripts/zh-TW/GLOSSARY.md` — Formosa/Formosan policy, name bible

## Related Pages

- [[people/albert-s-lai|Dr. Albert S. Lai (賴信雄)]]
- [[people/albert-chapter1-en-review|Ch.1 EN review (Christopher)]]
- [[people/albert-en-sku-a-scratch-review|EN SKU A multi-track review hub]]
- [[people/albert-chapter1-audiobook-consent-and-recording-kit|Consent & recording kit]]

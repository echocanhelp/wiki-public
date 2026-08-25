# Taigi accuracy — one lesson (2026-08-25)

**Status:** Canon for spelling + listen gold + what we will *not* claim.  
**Not a song.** Not a HeartMuLa how-to. Load this before any “improve 台語 / 腔口 / 萌典” work.

Related: `CONTROL.md` invariant 11 · `romanization-lexicon.json` `hokkien.song` · skill `echo-resonance` · `scripts/moedict-ssot.py` · `scripts/echo-resonance-listen.py`

## Three layers (do not mix)

| Layer | Authority | What “accurate” means | Closed by |
|-------|-----------|------------------------|-----------|
| **Spelling** | [moedict.tw `/t/`](https://www.moedict.tw/) Tâi-lô | Word Tâi-lô on wiki / sidecar | `moedict-ssot.py` |
| **Listen gold** | Same site’s official 朗讀 clips (`r2-assets…/audio/t/{id}.mp3`) | Teacher the human hears | `echo-resonance-listen.py` |
| **Sung 腔口** | HeartMuLa 漢字 + tags only | How the *song* sounds Taigi | **Not this stack** |

`audit-pack` `ship_as_taigi=true` is layers 1–2. Field `sung_phonology` is always `false`.

## Locked method

- Native 台語歌. Never EN→Taigi calque. No English proper nouns in sung lines.
- HeartMuLa sings **漢字**. Never sing Tâi-lô / POJ (Latin prior = English syllables).
- Wiki / audit = Tâi-lô interlinear. Person names **HOLD** (not a 萌典 headword).
- One scheme per page. Default Tâi-lô. POJ only when the named source is church / PCT / hymn / historical religious — quote and label `POJ:`.
- Never TTS as the track or the teacher.

## Picker + segment (wired)

- Index: `https://www.moedict.tw/t/index.json` (~21k), cached `~/.cache/echopedia/moedict-t-index.json` (7d).
- Segment: longest-match CJK against that index (`細漢` `某囝` `猶閣` stay words).
- Spoken pick: **白 > 替 > has-audio > unlabeled > 文**. Never first-wins `h[0]`.
  - `人` → `lâng` (替), not `jîn`
  - `手` → `tshiú` (白), not `siú`
- Dual readings (`sè-hàn/suè-hàn`): keep first as primary (主音讀).
- Commands:

```text
python3 ~/echo-system/scripts/moedict-ssot.py lookup --words '人,手' --hold '陳善哲'
python3 ~/echo-system/scripts/moedict-ssot.py segment --hanzi <hanzi.txt> --hold '陳善哲'
python3 ~/echo-system/scripts/moedict-ssot.py audit-pack --hanzi … --tailo … --wiki … --hold '陳善哲'
```

`--words` on `audit-pack` is optional; omit = auto-segment.

## What iterate can and cannot do

Produce → gold-listen → regen is **not** a closed loop to 腔口 perfection. HeartMuLa cannot hear 萌典. Cap regen at **3**.

| Can | Cannot |
|-----|--------|
| Rewrite 漢字, drop 文讀, reject junk takes, A/B tags | Make 手 sing `tshiú` instead of Mandarin `shǒu` |
| Ship a take you can stand *next to* the 朗讀 | Claim the HeartMuLa take *is* Tâi-lô |
| Tighten spelling + gold clips | Train on 教育部 例句 (CC BY-ND 3.0 TW = no derivatives) |

## Known holes (sense, not 文白)

Picker is reading-class, not word-sense.

| Lyric | Wanted | Picker may give |
|-------|--------|-----------------|
| 這條路真**長** | `tn̂g` (long) | 白 `tiúnn` |
| 畫**到**天光 | `kàu` (until) | 白 `tàu` |

Human/sense pass still required. Do not “fix” by more clips.

## Site map (do not rediscover)

| URL | Role |
|-----|------|
| `moedict.tw` | Live SSOT we use (`/t/`, `/t/index.json`, R2 朗讀) |
| `moedict.gov.tw` | **Dead** — typo, do not chase |
| `sutian.moe.edu.tw` | 教育部 《臺灣台語常用詞辭典》 upstream. `kautian.ods` = G2P+例句 tables. 例句 zip 528 MB MP3 / 9.5 GB WAV. License **CC BY-ND 3.0 TW** — play unmodified + attribute; do **not** fine-tune. Unused gold for *連讀* listen later. |

萌典 `/t/` is the g0v API mirror of that 教育部 lexicon, not a second phonology.

## HeartMuLa bound (do not re-research unless the model changes)

- Conditioners: `C_lyrics` (漢字 → Llama tokens) + `C_tag`. **No G2P, no Tâi-lô, no 台語 phone table.**
- CJK prior = Mandarin singing. Official benches EN/zh/JA/KO/ES — no nan/台語.
- Tags `taiwanese,hokkien` = weak style (often ignored). Genre ≠ phonology.
- Official `ref_audio` = `NotImplementedError`; heartlib `muq_embed` = zeros. HeartMuse MuQ = style, not speaker/`tshiú`.
- Whisper-zh on a take is the **wrong meter** (will say `lang=zh`). Junk-gate only.
- **Upgrade status (2026-08-25):** pinto runs HeartMuLa **3B** (`--version=3B`). Upstream still lists as **⏳ not shipped:** official reference-audio conditioning, fine-grained control, **7B**. Latest public 3B drop is `happy-new-year` (lyrics/music quality + tag follow). None of those add a 台語 phone set. Do not swap weights hoping for `tshiú`.

## Cousin 閩南 / Hokkien (not a shortcut)

More **speech TTS** exists than sung 台語. None is a drop-in singer for Echo Resonance.

| Stack | Dialect | Kind | Use for us? |
|-------|---------|------|-------------|
| [GPT-SoVITS-TW](https://huggingface.co/KaedeTai/gpt-sovits-tw) | 台灣閩南語 | **Speech** TTS, **POJ** in | Teacher / phone-score later. Never the published track. |
| [MERaLiON OmniVoice Hokkien](https://huggingface.co/MERaLiON/MERaLiON-OmniVoice-Hokkien-TTS) | **Singapore** Hokkien | Speech, 漢字 in | Different 腔 (SEA). Not 高雄混合腔. |
| 廈門大學 Tacotron2 閩南 | 廈門腔 | Speech | Academic; not song. |
| SuiSiann / Coqui VITS | 台灣閩南 | Speech | Same: not a song. |
| [SVSELM](https://github.com/baipeng1/SVSELM) 歌仔戲 | 閩南戲曲 | **Singing** (email-gated) | Closest published SVS. Opera, not pop 台語歌; license gated. |
| OpenUtau / DiffSinger banks | 粵/日/華 | Singing | **No public 台語/閩南 音源 found.** 粵語 is not Hokkien. |

Do **not** ship cousin-TTS as Echo Resonance. Do **not** call Singapore/廈門/歌仔戲 “Tâi-lô 台語歌.” Useful later only as (a) listen/ASR meter or (b) a new singer stack after named GO.

## Next spikes (await named GO)

1. ~~Sense override table for 長/到-class collisions~~ **done 2026-08-25** — `echopedia/taigi-sense-overrides.json` + `moedict-ssot.py` (NFC/NFD match). `長`→`tn̂g` (aid 4509; picker would `tiúnn`). `到`→`kàu` (aid 3607; picker would `tàu`). Sidecar already had both.
2. Phone-score gate vs 萌典 Tâi-lô (not Whisper-zh).
3. ~~Tag A/B: single genre, drop unused `taiwanese,hokkien,ballad`.~~ **done 2026-08-25** — chorus only, **not** a live replace.
   - A `taiwanese,hokkien,folk,ballad,…` → `~/media-outputs/jobs/shante-taigi-chorus-tagA.wav` 98.48s `chopped=False`
   - B `folk,male-vocal,acoustic,warm,nostalgic,guitar` → `~/media-outputs/jobs/shante-taigi-chorus-B.wav` 96.08s
   - **Ear winner (Leonard 2026-08-25): A.** Not a lyric-match win. Do not replace the live full 台語歌 with this chorus. Tag causality unproven (seed/take). **Next `go echo resonance` default tags = A** (`echo-resonance` + lexicon `hokkien.song.tags_default`).
4. Optional: sutian **unmodified** 例句 clips as listen gold (連讀), still ND.
5. Real sung 腔口 = different stack (DiffSinger/OpenVPI + 台語 phones, or licensed 台語歌 LoRA). Closest paper: SVSELM 歌仔戲 (email-gated). No public zh-TW / 台語 **singer** with a more 台語 accent. Speech cousins (GPT-SoVITS-TW) are not Echo Resonance.

Do not start 5 without GO. Do not pretend 1–4 close 5.

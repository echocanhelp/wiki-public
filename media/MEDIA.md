# MEDIA.md — Echo Resonance / 歲月有聲 media map

Owner: pinto (media-stack). Audience: fixer agents + humans entering via `go <plain language>`.
Last verified: 2026-10-08 (live probe — every count below re-derived from disk, not copied from a card).

## Blob SSOT

`~/media-outputs/jobs/*.wav` — the single source of truth for Echo Resonance audio.
**30 WAVs, 725 MB total.** Git-external (never copied into the repo). The catalog only
records the *relation* to each blob, never a copy of it.

## Catalog (git-tracked)

`~/echo-system/media/_manifest.json` — THE catalog, committed on `gh-pages`.
30 entries · brand `echo-resonance` (歲月有聲) · kinds: 29 music + 1 narration · status: all `staged`.
Each entry: id/slug, kind, absolute `asset` path into the blob SSOT, size, language,
entities (people links), engine, produced_at.

## Views + regen commands

```
python3 ~/echo-system/scripts/echo-media-manifest.py   # register/merge blobs -> _manifest.json (idempotent)
python3 ~/echo-system/scripts/echo-media-views.py      # generate media/index.md + works sections
python3 ~/echo-system/scripts/echo-media-regen.py      # regen: re-read manifest, patch marker regions (--dry-run supported)
```

Marker regions: `<!-- media-index-start/end -->` in `media/index.md`,
`<!-- media-section-start/end -->` in `content/works/<slug>.md`.
Regen is the CI/publish path: reads `_manifest.json`, writes only between markers, idempotent.

## Disclaimer (bilingual, manifest-driven)

Rendered verbatim from `_manifest.json` fields `disclaimer` / `disclaimer_zh` — never hardcoded in views/regen.

> Echopedia records facts. This piece is an AI interpretation built from those facts — creative, not verified history. Treat it as a story inspired by truth, not a primary source.

> Echopedia 記錄事實；本作品則據這些事實以 AI 創作，屬藝術詮釋而非查證之史實。請視為源於真實的故事，而非第一手史料。

## Catalog entries (30)

| slug | kind | lang | produced | size | status | asset (blob SSOT) |
|---|---|---|---|---|---|---|
| `leonard-master-test.master` | music | zh-TW | 2026-08-28 | 113.4 MB | staged | /home/leedt/media-outputs/jobs/leonard-master-test.master.wav |
| `leonard-instr-clip3` | music | zh-TW | 2026-08-28 | 7.1 MB | staged | /home/leedt/media-outputs/jobs/leonard-instr-clip3.wav |
| `leonard-instr-clip2` | music | zh-TW | 2026-08-28 | 10.6 MB | staged | /home/leedt/media-outputs/jobs/leonard-instr-clip2.wav |
| `leonard-instr-clip1` | music | zh-TW | 2026-08-28 | 10.6 MB | staged | /home/leedt/media-outputs/jobs/leonard-instr-clip1.wav |
| `leonard-hsu-jr-instrumental-48k-master` | music | zh-TW | 2026-08-28 | 28.4 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr-instrumental-48k-master.wav |
| `leonard-hsu-jr-instrumental-210s-mastered` | music | zh-TW | 2026-08-28 | 12.8 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr-instrumental-210s-mastered.wav |
| `leonard-hsu-jr-instrumental-210s-arc` | music | zh-TW | 2026-08-28 | 12.8 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr-instrumental-210s-arc.wav |
| `acestep-master.master` | music | zh-TW | 2026-08-28 | 87.8 MB | staged | /home/leedt/media-outputs/jobs/acestep-master.master.wav |
| `leonard-instrumental-test` | music | zh-TW | 2026-08-27 | 0.3 MB | staged | /home/leedt/media-outputs/jobs/leonard-instrumental-test.wav |
| `leonard-hsu-jr-instrumental-210s` | music | zh-TW | 2026-08-27 | 12.8 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr-instrumental-210s.wav |
| `leonard-hsu-jr-instrumental` | music | zh-TW | 2026-08-27 | 1.8 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr-instrumental.wav |
| `leonard-hsu-jr` | music | en | 2026-08-27 | 28.4 MB | staged | /home/leedt/media-outputs/jobs/leonard-hsu-jr.wav |
| `large-test` | music | zh-TW | 2026-08-27 | 3.7 MB | staged | /home/leedt/media-outputs/jobs/large-test.wav |
| `shante-taigi-chorus-taga-chopped90` | music | zh-TW | 2026-08-25 | 16.5 MB | staged | /home/leedt/media-outputs/jobs/shante-taigi-chorus-tagA-chopped90.wav |
| `shante-taigi-chorus-taga` | music | zh-TW | 2026-08-25 | 18 MB | staged | /home/leedt/media-outputs/jobs/shante-taigi-chorus-tagA.wav |
| `shante-taigi-chorus-b` | music | zh-TW | 2026-08-25 | 17.6 MB | staged | /home/leedt/media-outputs/jobs/shante-taigi-chorus-B.wav |
| `shante-taigi-chorus-a` | music | zh-TW | 2026-08-25 | 17 MB | staged | /home/leedt/media-outputs/jobs/shante-taigi-chorus-A.wav |
| `shante-shawsean-chen-song-taigi-gold-langdu` | music | zh-TW | 2026-08-25 | 5 MB | staged | /home/leedt/media-outputs/jobs/shante-shawsean-chen-song-taigi-gold-langdu.wav |
| `shante-shawsean-chen-song-taigi` | music | zh-TW | 2026-08-25 | 24 MB | staged | /home/leedt/media-outputs/jobs/shante-shawsean-chen-song-taigi.wav |
| `leonard-go-zh-taga` | music | zh-TW | 2026-08-25 | 29.5 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-zh-tagA.wav |
| `leonard-go-taigi-v4` | music | zh-TW | 2026-08-25 | 32.1 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-taigi-v4.wav |
| `leonard-go-taigi-v3` | music | zh-TW | 2026-08-25 | 33 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-taigi-v3.wav |
| `echo-resonance-tony-ann` | music | zh-TW | 2026-08-25 | 33 MB | staged | /home/leedt/media-outputs/jobs/echo-resonance-tony-ann.wav |
| `david-lee-song-zhtw` | music | zh-TW | 2026-08-25 | 33 MB | staged | /home/leedt/media-outputs/jobs/david-lee-song-zhtw.wav |
| `shante-shawsean-chen-song` | music | en | 2026-08-24 | 18.6 MB | staged | /home/leedt/media-outputs/jobs/shante-shawsean-chen-song.wav |
| `leonard-go-taigi-v2` | music | zh-TW | 2026-08-24 | 33 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-taigi-v2.wav |
| `leonard-go-taigi` | music | zh-TW | 2026-08-24 | 33 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-taigi.wav |
| `leonard-go-leonard` | music | zh-TW | 2026-08-24 | 29.6 MB | staged | /home/leedt/media-outputs/jobs/leonard-go-leonard.wav |
| `david-lee-song` | music | zh-TW | 2026-08-24 | 20.2 MB | staged | /home/leedt/media-outputs/jobs/david-lee-song.wav |
| `ken-wu-quote` | narration | zh-TW | 2026-08-14 | 0.6 MB | staged | /home/leedt/media-outputs/jobs/ken-wu-quote.wav |

## In-process Albert (《lai ching-te》 audiobook pipeline) — 3 locations

1. **`~/echo-system/content/media/albert-*.mp3` — 33 tracked MP3s.** The Quartz *published*
   copy: Quartz copies `content/media/` into `public/media/`, so these stream publicly at
   `/wiki-public/media/<file>.mp3` on GitHub Pages. **Not legacy** — this is the serving path.
2. **`~/echo-system/media/albert-*.mp3` — 36 tracked MP3s.** Repo-root copy also served at
   `/wiki-public/media/`. 33 are byte-identical duplicates of the `content/media/` set;
   3 exist only here (`albert-ch01-zh-hsiaochen-v2-scratch.mp3`,
   `albert-ch01-zh-hsiaoyu-v2-scratch.mp3`, `albert-ch01-zh-yunjhe-v2-scratch.mp3`).
3. **`~/echo-system/audiobook-albert-lai/` — gitignored, 1.8 GB.** Production pipeline, not
   serving: `01_AMT_scripts/`, `02_pronunciation/`, `03_raw_sessions/`, `04_edited_wav/`,
   `05_masters_by_platform/`. Source of truth for masters; never committed.

## Drift note (2026-10-08 sync)

One ghost entry (`_smoke-instrumental`, blob deleted) was purged from the catalog; 17 WAVs
that existed on disk but were unregistered (acestep-master.master, large-test,
leonard-hsu-jr-instrumental*, leonard-instr-clip*, leonard-master-test.master) were registered.
Catalog is now 1:1 with the blob directory: 30 entries ↔ 30 WAVs, every `asset` present.

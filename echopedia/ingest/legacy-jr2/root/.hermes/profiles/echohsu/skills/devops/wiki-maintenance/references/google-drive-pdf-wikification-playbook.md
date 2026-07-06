# Google Drive PDF → Wiki Enrichment Playbook

Use this when a user asks to read a Google Drive PDF and expand existing wiki pages.

## Workflow

1) Confirm Google auth for active profile
- Run Google API auth check first.
- Proceed only after authenticated status is confirmed.

2) Locate source files in Drive
- Find target folder with raw query (e.g., name contains + folder mimeType).
- Query PDFs inside the folder by parent ID.
- Capture file IDs for reproducible references.

3) Download PDF locally for deterministic extraction
- If high-level CLI lacks direct download, use Drive API `files().get_media(fileId=...)` in a short Python snippet.
- Save to `/tmp/<source>.pdf`.

4) Extract text and create a working corpus
- Use PyMuPDF for text-based PDF extraction.
- Persist extracted text as `/tmp/<source>.txt` for chunked processing and repeatability.

5) Enrich existing pages first, then web-out
- Expand existing hub pages (book + key person) before creating many new stubs.
- Add structured sections: bibliographic record, timeline, chapter map, analytical themes, source-critical notes.
- Create supporting index pages (people network map, places/institutions index).

6) Link hygiene
- Prefer Quartz wiki links `[[page|label]]` consistently.
- Add disambiguation notes for romanization variants (e.g., “Pinghsi” vs “Ping Hsi”).

7) Verification gate after each expansion wave
- Run broken-link scan after edits.
- Do not finalize until no broken links remain.

## Content policy for this class of task

- Preserve and enrich existing rich pages; never replace with minimal stubs.
- Include both Chinese characters and romanized forms for Chinese names.
- Distinguish source layers when applicable:
  - original historical text
  - later republication/editorial framing

## Suggested deliverable sequence

Wave 1: core pages (book + primary person + core orgs)
Wave 2: named-entity expansion (people + institutions)
Wave 3: historiography toolkit (timeline, source-critical notes, network/index pages)
Wave 4: normalization pass (aliases/disambiguation + backlink quality)
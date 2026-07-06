# Source-Fidelity Audiobook from Drive PDF

Context: User requested Chapter 1 audiobook of Albert Lai's book. Initial output incorrectly narrated an Echopedia chapter-summary page instead of the original chapter text.

## Durable workflow

1. Accept user source URL (Google Drive file link is sufficient).
2. Resolve file ID from `/file/d/<ID>/...`.
3. Download source artifact directly (`uc?export=download&id=<ID>`), verify file type.
4. Extract full text from the source PDF.
5. Locate chapter start/end using explicit chapter headings (e.g., `CHAPTER I ...` to `CHAPTER II ...`).
6. Generate narration only from sliced chapter text.
7. If text length is large, split into chunks near sentence boundaries, render per chunk, concatenate audio.
8. Deliver file and explicitly state it was generated from source chapter extraction.

## Verification checks before delivery

- Confirm extracted text includes target chapter heading and body prose.
- Confirm chapter end marker is next chapter heading (not arbitrary truncation).
- Confirm output duration is plausible for chapter length.

## Pitfalls

- Using wiki summary/index pages (`wiki-public/content/...chapter-*.md`) as narration input when user asked for the book chapter.
- Treating table of contents occurrences of `Chapter I` as chapter body start.
- Declaring completion without source-fidelity statement.

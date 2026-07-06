# Audiobook Source Fidelity Checklist

Use this before generating chapter audio for Echopedia.

## Goal
Ensure narration uses canonical chapter text (book/dissertation source), not wiki summary pages.

## Steps
1. Acquire primary source bytes
   - Prefer direct source file (Drive PDF/Doc export/local file).
2. Extract plain text to `/tmp`.
3. Find chapter markers
   - Example: `CHAPTER I ...` start
   - Next marker (e.g., `CHAPTER II ...`) end
4. Slice strictly between boundaries.
5. Sanity check sample
   - First 200–500 chars should read like source prose, not metadata/summary bullets.
   - Confirm no wiki frontmatter (`title:`, `tags:`) appears.
6. Generate pilot clip (30–90s) from the extracted segment.
7. Only after approval, generate full chapter audio.
8. Publish with two links:
   - dedicated audiobook page
   - chapter node + hub page cross-links

## Common Failure Pattern
- Narrating `content/toward-a-community-of-hope-chapter-i-...md` (summary page) instead of dissertation Chapter I text.

## Recovery
- Re-fetch source file.
- Re-extract and boundary-slice chapter text.
- Regenerate full audio and replace published link.
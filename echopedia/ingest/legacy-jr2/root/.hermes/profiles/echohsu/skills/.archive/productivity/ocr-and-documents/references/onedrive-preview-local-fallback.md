# OneDrive public link fallback when preview works but extraction fails

Use this when a OneDrive/SharePoint file preview opens in browser, but direct extraction/download is unreliable.

## Fast sequence
1. Attempt URL extraction first.
2. If blocked, check for an already-downloaded local copy (often `~/Downloads/<filename>.pdf`).
3. Run local PDF extraction on that file.
4. If standard PDF libraries are unavailable, run a raw-stream probe as a verification fallback.

## Why this matters
Preview metadata (filename/page count) can be visible even when tool-accessible bytes are permission-gated. A local downloaded copy can bypass that gap.

## Raw-stream verification fallback (concept)
- Inflate compressed PDF streams.
- Look for text operators in content streams: `(...) Tj` and `[ ... ] TJ`.
- Reconstruct strings from those operators to confirm readable text exists.

This method is a last-resort verifier, not a substitute for full structured extraction.

## Output discipline
Do not claim the document has been read unless extraction returns actual text content (not just metadata).
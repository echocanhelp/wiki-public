# Person-Page Authenticity Pass (Echo System Wiki)

Use this after initial person-page creation in any historical source cluster.

## Goal
Upgrade person pages from generic bios or attributed summaries into testimony-centered historical records with traceable sources.

## Trigger Signals
- Person pages use wording like "appears in materials" without direct voice.
- Testimony blocks are paraphrases only.
- Republication/foreword material includes signed first-person reflections.

## Workflow

1. Extract source text into a working plain-text file.
   - Example used in session: `/tmp/albert_lai_english.txt`.

2. Mine direct first-person quotations for each priority person.
   - Capture exact text, then annotate with:
     - Date/period
     - Context section title
     - Pointer (line range or source location)

3. Create a quote-bank page in the cluster.
   - Pattern: `<source-slug>-republication-voices-and-testaments.md`
   - Include source provenance and editorial notes (OCR noise, normalization policy).

4. Patch each person page testimony block.
   - Replace attributed summaries with direct quotes when available.
   - Set source tier to A for direct quote from available source material.

5. Keep epistemic clarity.
   - If role claims are still retrospective, keep confidence notes and mark verification needs.
   - Do not invent quotes.

6. Validate.
   - Run broken-link scan and fix any new link edges before deploy.

## Good Outcome Checklist
- Each priority person page has 2+ direct quotes when available.
- Every quote has context + provenance.
- A central quote-bank page is linked from person pages and main source hub.
- Broken-link scan returns clean.

## Session Example (Toward A Community of Hope)
- Added quote-bank page: `toward-a-community-of-hope-republication-voices-and-testaments.md`
- Replaced attributed testimony with direct quotes for:
  - `mingyuan-hsu-許明遠.md`
  - `pinghsi-liu-劉炳熹.md`
  - `yunching-yeh-davis-葉芸青.md`
- Added additional 2025 author quote to `albert-s-lai.md`
- Linked quote-bank from `toward-a-community-of-hope.md`

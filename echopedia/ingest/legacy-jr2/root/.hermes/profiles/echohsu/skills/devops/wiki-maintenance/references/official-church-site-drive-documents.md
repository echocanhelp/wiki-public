# Official Church Site + Google Drive Documents Pattern

Use this when an official Taiwanese American church/organization website links Google Drive files as source evidence (history documents, bylaws, booklets, Bible-study PDFs, manuals).

## Durable workflow

1. Inventory links from every `*_links` field in the crawl record, not only body/content links. Official sites often place Drive links in right-nav/sidebar structures.
2. Extract Drive file IDs from URLs like:
   - `https://drive.google.com/file/d/FILE_ID/view?...`
   - `https://docs.google.com/document/d/FILE_ID/edit?...`
   - `https://docs.google.com/spreadsheets/d/FILE_ID/edit?...`
3. For public Drive file downloads, try:
   - `https://drive.google.com/uc?export=download&id=FILE_ID`
4. Inspect the downloaded bytes with `file` before assuming format. The link text may be misleading; an item expected to be a PDF can be DOCX, legacy Word, HTML confirmation page, or another public document type.
5. Extract by format:
   - DOCX: Python `docx.Document(path)` and join paragraphs.
   - PDF: PyMuPDF (`fitz`) text extraction when available.
   - Google Doc export: `/document/d/ID/export?format=txt` when the source is a native Google Doc.
   - Legacy Word / OLE: use available local converters if installed; otherwise preserve metadata and avoid overclaiming.
6. Use extracted text to strengthen wiki claims, but keep source-confidence notes explicit when documents preserve older leadership/current-status data that conflicts with current website pages.

## Source-hygiene rules

- Do not reproduce personal phone numbers, private emails, private rosters, or internal spreadsheets on public wiki pages.
- Public Drive links can still expose sensitive operational material; classify before citing publicly.
- Prefer creating conservative evidence pages/person stubs only when source text gives a role and context, not name-only mentions.

## ITPC-specific lesson

In the ITPC crawl, the official history document linked from the About page was a Word 2007+ file downloadable via `uc?export=download&id=...`, even though other Drive files were PDFs. The history document provided stronger evidence for founding timeline and pastor chronology than the initially inspected Psalm-study PDF.
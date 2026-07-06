---
name: echopedia-tahs-workflows
category: devops
description: Class-level umbrella for Echopedia and TAHS (Taiwanese American Historical Society) research, person documentation, manual research workflows, and society document consolidation.
---

# Echopedia & TAHS Workflows (Umbrella)

Class-level skill covering all workflows for building, researching, and publishing Echopedia pages focused on Taiwanese American individuals, organizations, and the TAHS society.

## Core Principles (shared across all sub-workflows)
- Always use bilingual naming: English (Chinese characters) or Chinese (Romanization).
- Never publish personal contact information.
- Consolidate TAHS documents into ONE canonical society page.
- Prefer primary sources, community documents, and user-provided raw search text over automated scraping when blocked.
- Maintain Draft/Published status correctly; Drafts are intentionally visible for review.

## Subsections

### Manual Research Workflow (from echopedia-manual-research-workflow)
Workflow for building person and organization pages when automated tools hit CAPTCHA or return no Chinese results. Process user-provided raw Google search text, extract structured facts (elections, roles, publications, events), cross-reference timelines, produce bilingual entries with Sources section.

### Website Ingestion Fallback Pattern
When `web_extract` or Firecrawl returns "Unauthorized", "Invalid token", or billing errors:
1. Immediately fall back to `terminal` + `curl -sL <url>` (or Python `requests`) to obtain raw HTML.
2. For Webflow-style organization sites, the useful content is often embedded directly in the delivered HTML even when structured extraction fails. Use `curl` + targeted `grep`/`sed` or simple parsing to extract bilingual names, titles, and descriptions.
3. Crawl the homepage-discovered official internal pages that map to institutional history, facilities, board/leadership, member organizations, school/programs, publications, and major events.
4. Extract key identity, founding history, mission, facilities, leadership, member-network, and program details manually from the fetched content.
5. Create the Echopedia page using the established bilingual organization template (see existing Presbyterian church pages for structure).
6. Record the HTTP/curl fallback method, exact URLs used, and confidence level in the page's "Source Notes" section.
7. For major institutional pages, add an Echopedia homepage/index link under Featured Institutional Memory when appropriate.
8. Always include reciprocal links back to the parent hub page.

When the site surfaces governance PDFs, forms, or policy statements on a dedicated page (e.g., `/bylaws`, `/form-download`, `/statement`):
- Use the same `curl` + regex extraction to identify direct PDF links (cdn.prod.website-files.com … .pdf).
- Download each PDF (`requests.get` + `open(..., 'wb')`), run `file` to confirm type, then extract text via `pdftotext` (preferred) or `PyMuPDF` (`fitz`) fallback.
- Record page counts, file types, and extraction notes in the source-index page.
- Extract high-level structure signals (ARTICLE/SECTION headings, PURPOSES, NUMBER OF DIRECTORS/TRUSTEES, Conflict of Interest, Records of Proceedings, etc.) and any visible governance-timeline signals (dates, board-chair periods, amendment references).
- Mark the source-index page `status: draft` until the Chinese-language article (if present) is re-OCR’d or manually reviewed.

This pattern was validated during Irvine Taiwanese Presbyterian Church ingestion (2026-06-06) and Taiwan Center Foundation of Greater Los Angeles ingestion (2026-06-22). See `references/taiwan-center-official-site-ingestion.md` for the Taiwan Center/Webflow variant.

This pattern was validated during Irvine Taiwanese Presbyterian Church ingestion (2026-06-06) and Taiwan Center Foundation of Greater Los Angeles ingestion (2026-06-22). See `references/taiwan-center-official-site-ingestion.md` for the Taiwan Center/Webflow variant.

### Organization Cluster Expansion Pattern
After creating a high-confidence institutional hub page, expand it as a small Echopedia cluster rather than a single isolated page:
1. Identify the safest high-value nodes: founding benefactors, named facilities, school/program units, member-network indexes, and historically significant events.
2. Check for existing pages before writing; use `write_file` only for confirmed-new pages and `patch` for hub/index cross-links.
3. Use official-site pages as the source spine; keep standalone person pages conservative when the source only proves institutional role, not full biography.
4. Mark network/index pages `status: draft` when names need later normalization against each organization's own official source.
5. Cross-link both directions: hub → new cluster pages, new pages → hub, and homepage Featured People / Featured Institutional Memory when appropriate.
6. Deploy as one coherent commit and verify each live slug returns HTTP 200.
Validated on the Taiwan Center Phase TC-2 expansion; see `references/taiwan-center-cluster-expansion-2026-06-22.md`.

### Official Church Site Drive-Document Pattern
For Taiwanese American church/organization sites, inspect all crawl link buckets, including right-nav/sidebar links, for public Google Drive documents. Download public Drive file bytes via `https://drive.google.com/uc?export=download&id=FILE_ID`, run `file`, then extract according to the actual format (DOCX with `python-docx`, PDF with PyMuPDF, native Google Docs via `/export?format=txt`). Use the extracted official history/governance text to create conservative person/program pages only when role + context are present. Keep source-confidence notes when current website pages and older history documents differ.

### Person Research Workflow (from echopedia-person-research)
Research workflow prioritizing primary documents, community newsletters, government records for Taiwanese American biographical sources. Chinese name search conventions, source prioritization, pitfalls around Google scraping and English-only names.

### TAHS Documentation Workflow (from tahs-echopedia-documentation)
Ingest and publish TAHS governance/historical documents into a single consolidated page (`taiwanese-american-historical-society-台美人歷史協會.md`). Naming conventions, content hygiene, publishing flow to wiki-deploy, Draft policy for client review.

## When to Load
Load this umbrella whenever working on Echopedia person pages, TAHS society content, or any Taiwanese American historical documentation tasks.

## Related Skills
- wiki-maintenance (for general wiki QA, broken links, deploy)
- public-wiki-intake-publishing-qa (for intake form hygiene)

### Feedback Loop Automation Pattern
Auto-generate structured proposals from the Echopedia Community Intake Queue (Google Sheet), track lifecycle states (proposed/reviewed/published), and persist outputs. See `references/feedback-loop-automation.md`. Integrates with existing intake pipeline, identity audit, and onboarding flows.

### Deployment Verification Pattern (Quartz / GitHub Pages)
When updating Echopedia pages, edit both the source authoring tree and deployment tree when appropriate:
- Source authoring content: `/root/wiki-public/content/`
- Deploy repository content: `/root/wiki-deploy/content/`

For existing pages, follow `wiki-safe-edit`: read first, then patch; do not overwrite with `write_file`.

Do not rely on `npm run build` in `/root/wiki-deploy` as the sole verification path if it uses an outdated `npx github:...quartz` package target. The authoritative deployment workflow is `.github/workflows/deploy.yml`: clone `jackyzha0/quartz` at the workflow-pinned version, run `npm install`, copy `quartz.config.ts`, `quartz.layout.ts`, `index.md`, and `content/*`, then run `node quartz/bootstrap-cli.mjs build` inside the cloned Quartz directory. Use that workflow shape for local verification when the package script fails or differs from CI.

After patching deploy content:
1. Run `git diff --check` on the changed Markdown files.
2. Commit only the intended tracked files; leave unrelated untracked content alone.
3. Push to `origin master`.
4. Verify the GitHub Actions Pages workflow with `gh run list` and `gh run watch --exit-status`.

## References / Support Files
Place session-specific detail, reproduction recipes, and source excerpts under `references/`.

New this session:
- `references/taiwan-center-intake-lessons-2026-06-22.md` — Full lessons learned and updated best practices from the Taiwan Center Webflow ingestion.

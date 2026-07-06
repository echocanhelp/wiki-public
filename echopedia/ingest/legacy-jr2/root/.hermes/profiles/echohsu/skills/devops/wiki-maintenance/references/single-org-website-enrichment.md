# Single-Organization Website Enrichment Playbook

Use this when enriching one Echopedia organization page from an official public website (church, association, nonprofit, etc.).

## Workflow

1. **Safety and scope**
   - Check crawl blocklist before crawling. Never crawl the published Echopedia/wiki domain as a source.
   - Prefer the organization's official website and official linked documents over third-party summaries.
   - Treat public personal emails/phone numbers as unnecessary for historical record pages; omit them unless the user explicitly asks and publication is clearly appropriate.

2. **Inventory before summarizing**
   - Crawl internal HTML pages and normalize duplicate URL variants (`http/https`, `www/non-www`, trailing slashes).
   - Produce a concise source inventory: unique HTML pages, major content sections, internal assets, and public linked documents.
   - Extract official document links (Google Drive PDFs/Docs, bylaws, history files, publications) and preserve file IDs/URLs in local notes.

3. **Facts to extract for organization pages**
   - Official English/Chinese names, romanization if present, acronym.
   - Current location, worship/meeting time, service area, tradition/affiliation.
   - Current leadership and historical leadership, with confidence notes if pages preserve mixed-year material.
   - Timeline milestones: founding, incorporation, venue moves, major program launches, anniversaries.
   - Programs and community role: recurring classes, worship/services, care ministries, archives, publications, cultural functions.
   - Official mission statement or self-description when available.

4. **Editing pattern**
   - Search for an existing page first; enrich it instead of creating a duplicate.
   - For existing pages, read first and patch section/body content; do not overwrite with `write_file`.
   - Add a `Website Content Inventory` section when the crawl itself is valuable evidence.
   - Add `Source Notes and Confidence`, including crawl date, official pages/documents used, and privacy omissions.

5. **Publish and verify**
   - Use targeted publish for a single-page update: copy only the changed markdown file from `/root/wiki-public/content/` to `/root/wiki-deploy/content/`.
   - In `/root/wiki-deploy`, run `git status --short` before staging to ensure no unrelated changes are included.
   - Commit/push, then verify the GitHub Actions run for the pushed SHA completes successfully.
   - Verify the direct live page URL returns HTTP 200, not only the homepage.

## Reporting

Return a short final report with:
- Live URL and commit hash.
- Verification result: Actions success + page HTTP 200.
- Content inventory counts and major source categories.
- Key facts added.
- Recommendations for follow-up pages or deeper extraction.

## Pitfalls

- A page can be new to `/root/wiki-deploy` even if it already exists in `/root/wiki-public/content/`; `/root/wiki-public` may be an authoring workspace, not a Git repo.
- Official sites may mix current pages with older archived materials. Use confidence notes rather than forcing a single definitive chronology.
- Broken-link scans may reveal unrelated legacy issues. Note them separately and do not block a targeted single-page publish unless they affect the page being changed or CI fails.

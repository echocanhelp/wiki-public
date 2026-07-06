# Taiwan Center Intake — Lessons Learned & Best Practices (2026-06-22)

## Summary of Validated Patterns
The Taiwan Center Foundation of Greater Los Angeles (`taiwancenter.org`) ingestion served as the reference implementation for Webflow-based Taiwanese American organization sites. Two core patterns were refined and validated:

1. Website Ingestion Fallback Pattern
2. Organization Cluster Expansion Pattern

## Key Lessons Learned

### 1. Structured tools frequently fail — make curl the default first step
- `web_extract` consistently returned "Unauthorized / Invalid token" on public Webflow pages.
- **Application**: Always start with `terminal` + `curl -sL <url>` for any community organization site. The full content (including nav-linked subpages) is reliably present in raw HTML.

### 2. Use the site's own navigation as the "source spine"
- The official nav bar directly revealed the highest-value pages: `/introduction`, `/facility`, `/board`, `/group-members`, `/publication`, `/about-taiwan-school`.
- **Application**: After creating the hub page, systematically ingest every major nav item as a dedicated cluster page.

### 3. Cluster expansion produces cleaner, more maintainable content
- After the main hub, the following pages were created/expanded in one phase:
  - Person pages (limited scope): 王桂榮, 吳澧培
  - Facility/Program pages: 王桂榮圖書館, Taiwan School
  - Network/Index page: 團體會員網絡 (marked draft)
  - Additional pages: New Building Project, Publications, Board Roster, multiple events
- **Application**: Treat rich institutional sites as small clusters. Prioritize founding benefactors, named facilities, programs, and member networks.

### 4. Roster and network pages must remain in draft
- Board (38 members) and group-member (72 organizations) lists use the organization's public display names.
- **Application**: Always set `status: draft` on roster/index pages and add an explicit note that names are preserved exactly as shown. Do not create standalone person pages from titles alone.

### 5. Lightweight HTML parsing is fast and sufficient
- `curl` + `grep`/`sed` extracted clean bilingual rosters in seconds.
- **Application**: Document the exact extraction method and source URLs in every page's "Source Notes" section.

### 6. Include reciprocal links and homepage Featured updates in the same commit
- Every cluster page links back to the hub; the hub links out to all cluster nodes.
- Homepage Featured Institutional Memory and Featured People were updated in the same deployment.
- **Application**: Deploy hub + cluster pages + homepage updates together for coherence.

### 7. Capture self-references when present
- The official group-members list includes TAHS itself.
- **Application**: When ingesting any organization, check for and link TAHS or other Echopedia entities.

## Recommended Future Workflow (Updated)

For any new Taiwanese American organization site:

1. Fetch homepage with `curl -sL`.
2. Map the navigation to a source-spine list.
3. Create hub page first.
4. Expand cluster using the validated node types (benefactors, facilities, programs, networks).
5. Mark roster/network pages as draft.
6. Add Source Notes with extraction method on every page.
7. Cross-link hub ↔ cluster and update homepage Featured sections.
8. Deploy as one commit and verify all live slugs.

## Persistence
These lessons have been incorporated into the `echopedia-tahs-workflows` skill (Website Ingestion Fallback Pattern and Organization Cluster Expansion Pattern sections) so they become the default process for all future Echopedia intakes.
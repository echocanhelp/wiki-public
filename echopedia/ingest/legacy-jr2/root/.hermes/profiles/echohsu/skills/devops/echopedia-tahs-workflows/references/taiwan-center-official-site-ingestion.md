# Taiwan Center official-site ingestion notes

Use when building Echopedia pages from `taiwancenter.org` or similar Webflow-based Taiwanese American organization sites.

## Durable pattern

1. Check the crawl blocklist first; `taiwancenter.org` is not an Echo-owned wiki domain and is safe to inspect when relevant.
2. If structured `web_extract` / search returns an authorization-token error, immediately use direct HTTP fallback:
   - Fetch the official homepage and key internal pages with `curl` or Python `requests`.
   - Strip scripts/styles and parse visible text/links with a small HTML parser; Webflow pages often contain usable text directly in the HTML.
3. For Taiwan Center, useful official paths found from the homepage included:
   - `/introduction` — founding history, mission, organization structure.
   - `/facility` — library, 228 memorial exhibit, hall, classrooms, archives, venue functions.
   - `/board` — leadership slate with Chinese names, English names, and titles.
   - `/group-members` — member organization network.
   - `/about-taiwan-school` — school and program description.
   - `/publication` — yearbooks/program books list.
   - `/event/groundbreaking-ceremony` and `/event/2025-annual-gala-fundraising-dinner` — new-building and community milestone context.
4. For public Echopedia organization pages, synthesize a conservative institutional profile:
   - Identity snapshot.
   - Historical overview.
   - Mission/community role.
   - Facilities/programs.
   - Leadership/governance.
   - Member network.
   - Events/public memory.
   - Source notes and confidence.
5. Do not reproduce personal contact details unless there is a strong public-interest reason; prefer institutional identity/history over directory-style contact copying.
6. Publish workflow remains the standard two-tree process:
   - Write source content under `/root/wiki-public/content/`.
   - Copy to `/root/wiki-deploy/content/`.
   - Run `git diff --check`, commit/push, watch GitHub Pages workflow, then verify raw GitHub and live Pages HTTP 200.
7. If adding a major institution page, add a homepage/index link under Featured Institutional Memory when appropriate.

## Taiwan Center naming notes

- English: Taiwan Center Foundation of Greater Los Angeles.
- Chinese: 大洛杉磯台灣會館基金會.
- Common names: Taiwan Center / 大洛杉磯台灣會館.
- Earlier institutional name from official history: 南加州台灣會館基金會 / 南加州台灣會館.
- Current leadership page may include existing Echopedia people; link them conservatively when identity is clear, e.g. Ken Wu (吳兆峯).
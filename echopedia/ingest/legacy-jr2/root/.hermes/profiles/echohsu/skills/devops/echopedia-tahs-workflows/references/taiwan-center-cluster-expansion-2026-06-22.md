# Taiwan Center Cluster Expansion — 2026-06-22

## Trigger
User asked to proceed with the next phase after the Taiwan Center Foundation of Greater Los Angeles hub page had been created from `taiwancenter.org`.

## Durable Pattern
When an official community-organization site yields a rich institutional hub, expand it into a small cluster of conservative pages rather than trying to overstuff one page.

## Phase TC-2 Page Set Used
Created five pages from official Taiwan Center source pages:

1. `wang-gui-rong-王桂榮.md`
   - Person page for 王桂榮 / Wang Gui-Rong / Kenjohn Wang.
   - Safe claim boundary: founding property donor and library namesake, not a full biography.

2. `wu-li-pei-吳澧培.md`
   - Person page for 吳澧培 / Wu Li-Pei.
   - Safe claim boundary: EverTrust Bank president and fundraising convener as stated by Taiwan Center, not a full biography.

3. `wang-gui-rong-memorial-library-王桂榮圖書館.md`
   - Facility/program page for the Taiwan-focused library.
   - Source claims: 10,000+ Taiwan-related books; subject areas from official facility page.

4. `taiwan-center-taiwan-school-大洛杉磯台灣會館台灣學校.md`
   - Program page for the Taiwan School.
   - Source claims: eight-year school statement, course categories, cultural-learning framing.

5. `taiwan-center-group-member-network-團體會員網絡.md`
   - Draft network/index page.
   - Marked `status: draft` because member-organization names need normalization against each organization's own official source.

## Official Source Spine
Use direct HTTP/HTML fallback when structured extract/search fails:

- `https://taiwancenter.org/introduction`
- `https://taiwancenter.org/facility`
- `https://taiwancenter.org/about-taiwan-school`
- `https://taiwancenter.org/class-information`
- `https://taiwancenter.org/group-members`
- `https://taiwancenter.org/publication`

## Cross-Linking Pattern
Patch the existing hub page to link out to the new cluster:

- founding paragraph links 王桂榮 and 吳澧培
- facilities section links 王桂榮圖書館
- program paragraph links Taiwan School
- member-network paragraph links the network index
- Related Pages includes all new nodes

Patch homepage indexes:

- Featured People: add 王桂榮 and 吳澧培
- Featured Institutional Memory: add library, school, and group-member network

## Deployment Verification
After copying source files into `/root/wiki-deploy/content`:

1. `git diff --check` on intended Markdown files.
2. Commit only intended files; ignore unrelated untracked ops/event pages.
3. Push to `origin master`.
4. Watch GitHub Pages workflow via `gh run watch --exit-status`.
5. Verify every new live slug returns HTTP 200.

## Pitfalls

- Do not turn every board-list name into a person page from title alone. Create standalone person pages only when the source has a historically meaningful role or additional context.
- For member lists, avoid presenting the Taiwan Center display name as definitive legal/current name. Mark as draft until normalized.
- Do not reproduce personal contact details; institutional context is enough for Echopedia.
- For bilingual identity, include Chinese characters and a romanized form in person pages even if English spelling varies across sources.

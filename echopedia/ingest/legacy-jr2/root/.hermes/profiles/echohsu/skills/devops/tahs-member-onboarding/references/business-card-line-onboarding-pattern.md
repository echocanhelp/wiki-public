# Business Card + LINE Mention Onboarding Pattern

Use when Leonard introduces a new TAHS member in LINE and supplies a business card image as identity/context evidence.

## Durable pattern

1. OCR the card for public identity context only:
   - English name
   - Chinese characters
   - organization / role context
   - optional romanization marked pending if not explicitly confirmed
2. Do not publish private contact details from the card:
   - phone numbers
   - mobile numbers
   - private email addresses
   - street addresses
3. Create the Echopedia person page immediately when Leonard says the person is present and verified.
4. If the LINE mention target userId is unavailable, do not hard-link the identity:
   - page governance may be active based on owner approval;
   - identity link state should remain `pending_line_user_id` or equivalent;
   - append an audit event explaining the missing runtime userId.
5. Update both discovery surfaces:
   - `people.md`
   - TAHS organizational roster page
6. Verify/publish through deploy repo, not only source authoring tree:
   - copy changed source content into `/root/wiki-deploy/content/`
   - run `git diff --check` on intended files
   - build using the workflow-pinned Quartz path if `npm run build` is stale
   - commit/push only intended files
   - verify GitHub Actions and live HTTP 200 responses

## Public wording guidance

Good public wording:
- “A business card shared during onboarding identifies [Name] as [Role] of [Organization]. Private contact details from the card are intentionally not republished here.”

Avoid:
- publishing phone/email/address from a card
- saying the LINE identity is owner_verified unless the actual userId was captured or an approved confirmation path completed
- expanding biography from noisy web search without high-confidence source confirmation

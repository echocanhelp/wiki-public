---
name: google-workspace
description: "Gmail, Calendar, Drive, Docs, Sheets, Contacts via gws CLI or Python."
version: 1.1.0
author: Nous Research
license: MIT
required_credential_files:
  - path: google_token.json
    description: Google OAuth2 token (created by setup script)
  - path: google_client_secret.json
    description: Google OAuth2 client credentials (downloaded from Google Cloud Console)
metadata:
  hermes:
    tags: [Google, Gmail, Calendar, Drive, Sheets, Docs, Contacts, Email, OAuth]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [himalaya]
---

# Google Workspace

Gmail, Calendar, Drive, Contacts, Sheets, and Docs — through Hermes-managed OAuth and a thin CLI wrapper.

## Advanced Authentication Architectures

### 1. Service Account Impersonation (Enterprise/Workspace)
**Best for:** Autonomous systems in a Google Workspace environment.
- **Requirement:** Admin access to enable Domain-Wide Delegation.
- **Workflow:** 
  1. Create Service Account in GCP.
  2. Grant Service Account roles (e.g., `roles/editor`).
  3. In Admin Console, authorize the Client ID for specific scopes.
  4. Use `gcloud auth application-default login --impersonate-service-account=...` to generate ADC.

### Profile-Scoped OAuth (important for multi-profile Hermes setups)
If workers run under a non-default Hermes profile (for example `orchestrator`), run setup against that profile's Hermes home, not the default one.

Example:
```bash
HERMES_HOME=/root/.hermes/profiles/orchestrator python3 /root/.hermes/skills/productivity/google-workspace/scripts/setup.py --check
HERMES_HOME=/root/.hermes/profiles/orchestrator python3 /root/.hermes/skills/productivity/google-workspace/scripts/setup.py --client-secret /root/.hermes/google_client_secret.json
HERMES_HOME=/root/.hermes/profiles/orchestrator python3 /root/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-url
HERMES_HOME=/root/.hermes/profiles/orchestrator python3 /root/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-code "PASTE_FULL_REDIRECT_URL_HERE"
```

Do not assume `default` profile auth applies to worker profiles. Verify the active Hermes profile first (`hermes profile list`) and target the correct `HERMES_HOME`.

### Scope parity requirement
Keep `setup.py` and `google_api.py` scope lists in sync. If `google_api.py` requests write-capable scopes but `setup.py` still advertises `*.readonly`, re-auth will silently leave workers under-scoped even though the token exchange succeeds.

### Verification (Layer 4)
Agents MUST NOT mark a task as `done` based solely on a successful tool response (200 OK). For all external side-effects (Drive, Docs, Sheets, Contacts, Email), agents must perform a "Read-Back" verification to confirm the state change is visible in the target system.

Verification semantics discovered in live use:
- **Calendar delete is not always a 404.** After deleting an event, Google Calendar may return the event as a `status: cancelled` tombstone. Treat that as a successful delete verification.
- **Docs delete can lag across APIs.** After deleting a Google Doc via Drive, Drive may return 404 before the Docs API does. Poll briefly and verify with Drive first; a short propagation delay is normal.
- **Contacts fields may normalize on read-back.** Email casing can be normalized to lowercase and names may come back as `displayName` / `unstructuredName` rather than matching the original request shape exactly. Compare semantic values, not raw request payload shape.

### Google Workspace Operations
- **Scope Awareness:** Always check if the required scope is present in `google_api.py`.
- **Authentication:** When scope errors occur, immediately instruct the user to run `setup.py` to refresh the OAuth token with broader permissions.
- **Verification Pattern:** 
    1. Write/Create resource.
    2. Retrieve resource by ID/search.
    3. Compare actual content/existence with expected state.
    4. Confirm completion only after successful match.

## Pitfalls & Troubleshooting

### Silent Failures (Hallucination of Success)
- **Problem:** The task is marked `done`, but no changes appear in Google Drive, Contacts, or Sheets.
- **Cause:** 
    1. The `google_api.py` implementation is using `readonly` scopes (e.g., `drive.readonly`, `contacts.readonly`).
    2. The agent did not perform a "Read-Back" to verify the external state.
- **Solution:** 
    - **Check Scopes:** Verify `google_api.py` is using full scopes (e.g., `https://www.googleapis.com/auth/drive`).
    - **Re-Authenticate:** If scopes were recently changed in code, the user MUST run `python setup.py` to generate a new `google_token.json` that includes the new permissions.
    - **Enforce Layer 4:** Agents must be explicitly instructed to "Read-back" the changes after a write.

### Scope Mismatch
- **Problem:** `HttpError 403: Insufficient Permission` despite successful authentication.
- **Cause:** The current `token.json` lacks the specific scope required for the requested action (e.g., wanting to write to Contacts but having only `contacts.readonly`).
- **Solution:** Run `python setup.py` to re-authorize with expanded scopes.

... (omitted) ...

## Usage
... (omitted) ...

>
> 1. Create or select a project:
>    https://console.cloud.google.com/projectselector2/home/dashboard
> 2. Enable the required APIs from the API Library:
>    https://console.cloud.google.com/apis/library
>    Enable: Gmail API, Google Calendar API, Google Drive API,
>    Google Sheets API, Google Docs API, People API
> 3. Create the OAuth client here:
>    https://console.cloud.google.com/apis/credentials
>    Credentials → Create Credentials → OAuth 2.0 Client ID
> 4. Application type: "Desktop app" → Create
> 5. If the app is still in Testing, add the user's Google account as a test user here:
>    https://console.cloud.google.com/auth/audience
>    Audience → Test users → Add users
> 6. Download the JSON file and tell me the file path
>
> Important Hermes CLI note: if the file path starts with `/`, do NOT send only the bare path as its own message in the CLI, because it can be mistaken for a slash command. Send it in a sentence instead, like:
> `The JSON file path is: /home/user/Downloads/client_secret_....json`
>
> **Crucial for v2.0 Integration:** Ensure you select the full scope for "Drive" (not just readonly) if you intend to allow the agent to update the Semantic Layer or upload new architecture docs.

Once they provide the path:

```bash
$GSETUP --client-secret /path/to/client_secret.json
```

If they paste the raw client ID / client secret values instead of a file path,
write a valid Desktop OAuth JSON file for them yourself, save it somewhere
explicit (for example `~/Downloads/hermes-google-client-secret.json`), then run
`--client-secret` against that file.

### Step 3: Get authorization URL

Use the service set chosen in Step 1. Examples:

```bash
$GSETUP --auth-url --services email,calendar --format json
$GSETUP --auth-url --services calendar,drive,sheets,docs --format json
$GSETUP --auth-url --services all --format json
```

This returns JSON with an `auth_url` field and also saves the exact URL to
`~/.hermes/google_oauth_last_url.txt`.

Agent rules for this step:
- Extract the `auth_url` field and send that exact URL to the user as a single line.
- Tell the user that the browser will likely fail on `http://localhost:1` after approval, and that this is expected.
- Tell them to copy the ENTIRE redirected URL from the browser address bar.
- If the user gets `Error 403: access_denied`, send them directly to `https://console.cloud.google.com/auth/audience` to add themselves as a test user.

### Step 4: Exchange the code

The user will paste back either a URL like `http://localhost:1/?code=4/0A...&scope=...`
or just the code string. Either works. The `--auth-url` step stores a temporary
pending OAuth session locally so `--auth-code` can complete the PKCE exchange
later, even on headless systems:

```bash
$GSETUP --auth-code "THE_URL_OR_CODE_THE_USER_PASTED" --format json
```

If `--auth-code` fails because the code expired, was already used, or came from
an older browser tab, it now returns a fresh `fresh_auth_url`. In that case,
immediately send the new URL to the user and have them retry with the newest
browser redirect only.

### Step 5: Verify

```bash
$GSETUP --check
```

Success condition:
- It should print `AUTHENTICATED` with no `AUTHENTICATED (partial)` warning.
- If it reports missing scopes, revoke and redo consent from the same profile until the warning disappears.

Setup is complete only after the scope-complete check passes — token refreshes automatically from now on.

### Notes

- Token is stored at `~/.hermes/google_token.json` and auto-refreshes.
- Pending OAuth session state/verifier are stored temporarily at `~/.hermes/google_oauth_pending.json` until exchange completes.
- If `gws` is installed, `google_api.py` points it at the same `~/.hermes/google_token.json` credentials file. Users do not need to run a separate `gws auth login` flow.
- To revoke: `$GSETUP --revoke`

## Usage

All commands go through the API script. Set `GAPI` as a shorthand. Use `python3` explicitly on systems where `python` is not present on PATH:

```bash
GAPI="python3 ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"
```

### Gmail

```bash
# Search (returns JSON array with id, from, subject, date, snippet)
$GAPI gmail search "is:unread" --max 10
$GAPI gmail search "from:boss@company.com newer_than:1d"
$GAPI gmail search "has:attachment filename:pdf newer_than:7d"

# Read full message (returns JSON with body text)
$GAPI gmail get MESSAGE_ID

# Send
$GAPI gmail send --to user@example.com --subject "Hello" --body "Message text"
$GAPI gmail send --to user@example.com --subject "Report" --body "<h1>Q4</h1><p>Details...</p>" --html
$GAPI gmail send --to user@example.com --subject "Hello" --from '"Research Agent" <user@example.com>' --body "Message text"

# Reply (automatically threads and sets In-Reply-To)
$GAPI gmail reply MESSAGE_ID --body "Thanks, that works for me."
$GAPI gmail reply MESSAGE_ID --from '"Support Bot" <user@example.com>' --body "Thanks"

# Labels
$GAPI gmail labels
$GAPI gmail modify MESSAGE_ID --add-labels LABEL_ID
$GAPI gmail modify MESSAGE_ID --remove-labels UNREAD
```

### Calendar

```bash
# List events (defaults to next 7 days)
$GAPI calendar list
$GAPI calendar list --start 2026-03-01T00:00:00Z --end 2026-03-07T23:59:59Z

# Create event (ISO 8601 with timezone required)
$GAPI calendar create --summary "Team Standup" --start 2026-03-01T10:00:00-06:00 --end 2026-03-01T10:30:00-06:00
$GAPI calendar create --summary "Lunch" --start 2026-03-01T12:00:00Z --end 2026-03-01T13:00:00Z --location "Cafe"
$GAPI calendar create --summary "Review" --start 2026-03-01T14:00:00Z --end 2026-03-01T15:00:00Z --attendees "alice@co.com,bob@co.com"

# Delete event
$GAPI calendar delete EVENT_ID
```

### Drive

```bash
# Auth status for the current Hermes profile
$GAPI --check

# Search
$GAPI drive search "quarterly report" --max 10
$GAPI drive search "mimeType='application/pdf'" --raw-query --max 5

# Upload a local file (verifies remote name + size after create)
$GAPI drive upload --file ./report.pdf
$GAPI drive upload --file ./notes.txt --name "Renamed Notes.txt"
```

### Contacts

```bash
$GAPI contacts list --max 20

# Create a contact (verifies read-back fields after create)
$GAPI contacts create --name "Alice Example" --email alice@example.com
$GAPI contacts create --name "Bob Example" --email bob@example.com --phone "+1-555-0100"
```

### Sheets

```bash
# Read
$GAPI sheets get SHEET_ID "Sheet1!A1:D10"

# Create a spreadsheet and optionally seed values at A1 (verifies title + sheet title + read-back values)
$GAPI sheets create --title "Quarterly Metrics" --sheet-title "Verification" --values '[["check","status"],["layer4","pass"]]'

# Write
$GAPI sheets update SHEET_ID "Sheet1!A1:B2" --values '[["Name","Score"],["Alice","95"]]'

# Append rows
$GAPI sheets append SHEET_ID "Sheet1!A:C" --values '[["new","row","data"]]'
```

Current bundled CLI note:
- `sheets get`, `sheets create`, `sheets update`, and `sheets append` are exposed.
- `sheets create` now performs Layer 4 verification by reading back the seeded range after create.

### Docs

```bash
# Create a Google Doc and optionally seed body text (verifies title + read-back body)
$GAPI docs create --title "Research Notes" --body "Layer 4 verification test from Hermes."

# Read an existing Google Doc
$GAPI docs get DOC_ID
```

Current bundled CLI note:
- `docs create` and `docs get` are exposed.
- `docs create` uses Drive to create the document, optionally writes body text via Docs API, then reads the document back for verification.

## Output Format

All commands return JSON. Parse with `jq` or read directly. Key fields:

- **Gmail search**: `[{id, threadId, from, to, subject, date, snippet, labels}]`
- **Gmail get**: `{id, threadId, from, to, subject, date, labels, body}`
- **Gmail send/reply**: `{status: "sent", id, threadId}`
- **Calendar list**: `[{id, summary, start, end, location, description, htmlLink}]`
- **Calendar create**: `{status: "created", id, summary, htmlLink}`
- **Drive search**: `[{id, name, mimeType, modifiedTime, webViewLink}]`
- **Contacts list**: `[{name, emails: [...], phones: [...]}]`
- **Sheets get**: `[[cell, cell, ...], ...]`

## Rules

1. **Never send email or create/delete events without confirming with the user first.** Show the draft content and ask for approval.
2. **Check auth before first use** — run `setup.py --check`. If it fails, guide the user through setup. If it prints `AUTHENTICATED (partial)`, treat the token as under-scoped for the missing services and re-run consent before attempting those writes.
3. **Use the Gmail search syntax reference** for complex queries — load it with `skill_view("google-workspace", file_path="references/gmail-search-syntax.md")`.
4. **Calendar times must include timezone** — always use ISO 8601 with offset (e.g., `2026-03-01T10:00:00-06:00`) or UTC (`Z`).
5. **Respect rate limits** — avoid rapid-fire sequential API calls. Batch reads when possible.

## Troubleshooting

Additional session references:
- `references/oauth-profile-and-verification.md` — profile-scoped OAuth setup, scope-parity pitfall, and verified Google API deletion/read-back semantics.
- `references/command-surface-and-reauth.md` — `python3` invocation requirement, partial-auth behavior, fresh-consent recovery, and current Doc/Sheet create command-surface limitations.
- `references/forms-intake-link-validation.md` — avoid mislabeling Google Docs template links as live Forms; includes URL-pattern validation and publication wording guardrails.
- `references/echopedia-intake-pipeline.md` — multi-channel community-intake pattern (Form/Email/LINE → normalized Sheet queue), consent statuses, and deployment pitfall notes.

| Problem | Fix |
|---------|-----|
| `NOT_AUTHENTICATED` | Run setup Steps 2-5 above |
| `REFRESH_FAILED` | Token revoked or expired — redo Steps 3-5 |
| `HttpError 403: Insufficient Permission` | Missing API scope — `$GSETUP --revoke` then redo Steps 3-5 |
| `HttpError 403: Access Not Configured` | API not enabled — user needs to enable it in Google Cloud Console |
| `ModuleNotFoundError` | Run `$GSETUP --install-deps` |
| Advanced Protection blocks auth | Workspace admin must allowlist the OAuth client ID |

## Revoking Access

```bash
$GSETUP --revoke
```

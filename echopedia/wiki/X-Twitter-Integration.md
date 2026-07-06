# X/Twitter Integration (xurl)

## Overview
xurl is the official X (Twitter) CLI tool wrapping the X API v2. Installed on pinto at `~/.local/bin/xurl`.

## Capabilities
- Posting, replying, quoting, deleting tweets
- Searching posts, reading timelines/mentions
- Likes, reposts, bookmarks
- Following, blocking, muting
- Direct messages
- Media uploads (images, videos)
- Raw API v2 access

## Installation
Installed via shell script: `curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash`

Location: `/home/leedt/.local/bin/xurl`

## Setup Required (Manual)
OAuth credentials must be configured manually by the user:
1. Create an X Developer app at https://developer.x.com/en/portal/dashboard
2. Set redirect URI to `http://localhost:8080/callback`
3. Register the app: `xurl auth apps add my-app --client-id CLIENT_ID --client-secret CLIENT_SECRET`
4. Authenticate: `xurl auth oauth2 --app my-app`
5. Set default: `xurl auth default my-app`
6. Verify: `xurl auth status`

Credentials stored in `~/.xurl` (YAML format). Shared across all sessions on pinto.

## Security
- Never expose `~/.xurl` to LLM context
- Never use `--verbose` flag in agent sessions
- User manages credentials manually outside agent sessions

## Persistence
- Binary persists across sessions (installed to `~/.local/bin`)
- Credentials persist in `~/.xurl` across sessions
- Knowledge about xurl exists in this Echopedia page for future sessions

## References
- GitHub: https://github.com/xdevplatform/xurl
- Legacy skill archive: `echopedia/ingest/legacy-jr2/root/.hermes/profiles/echohsu/skills/social-media/xurl/SKILL.md`
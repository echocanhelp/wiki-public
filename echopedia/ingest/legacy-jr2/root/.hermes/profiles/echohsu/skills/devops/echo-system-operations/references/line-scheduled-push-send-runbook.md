# LINE scheduled push send runbook

Use when a cron job or operator request must send a one-off message to a known LINE group, especially when the request references a previous LINE group session.

## Target resolution

1. Prefer the active/relevant LINE group from session routing metadata or prior session context.
   - `sessions/sessions.json` maps `agent:main:line:group:<group_id>:<user_id>` to the session id and updated timestamp.
   - Past-session search can identify which group a prior task occurred in; use the group id from the matching session metadata.
2. Verify the candidate group is also in the channel directory or LINE allowed groups when available.
3. Avoid broadcasting to all groups unless the user explicitly asked for broadcast.

## Send path

Preferred path:
- `hermes send --to line --file <message-file>` when the desired group is configured as the LINE home channel for that profile.

Known CLI pitfall:
- As observed in a cron run, `hermes send --to line:<C...group_id>` may be treated as a channel-name lookup rather than an explicit LINE group id, causing a misleading home-channel error. Do not treat that as proof that LINE cannot send.

Fallback path for one-off push:
1. Read the LINE channel access token from the profile's LINE source/config file without printing it.
2. POST directly to LINE Messaging API push endpoint:
   - URL: `https://api.line.me/v2/bot/message/push`
   - Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`
   - Body: `{ "to": "<group_id>", "messages": [{"type":"text","text":"..."}] }`
3. Verify success by HTTP 200 and record the returned LINE `sentMessages[].id` if present.

## Safety and privacy

- Never print tokens or channel secrets in tool output or final reports.
- Use a temporary message file for multiline content to avoid shell quoting damage.
- Report only the target type/group id (if needed), HTTP status, and sent message id; do not expose credentials.

## Minimal Python fallback pattern

```python
import json, pathlib, urllib.request
profile = pathlib.Path('/root/.hermes/profiles/echohsu')
message = (profile / 'tmp/message.txt').read_text(encoding='utf-8')
sources = json.loads((profile / 'line_sources.json').read_text(encoding='utf-8'))
token = sources['channel_access_token']
payload = json.dumps({
    'to': '<LINE_GROUP_ID>',
    'messages': [{'type': 'text', 'text': message}],
}, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request(
    'https://api.line.me/v2/bot/message/push',
    data=payload,
    method='POST',
    headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=30) as resp:
    print(resp.status, resp.read().decode('utf-8', 'replace'))
```

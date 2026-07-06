# LINE Group Shared Context Routing

Use this reference when Echo misunderstands a short reply in a LINE group, especially during a 3-way conversation where one participant answers another participant's question.

## Symptom

A group member sends a short contextual reply such as:
- "yes"
- "this is cool"
- "go ahead"
- "sounds good"

Echo replies as if it only sees that speaker's isolated prior messages, not the active group discussion.

## Root cause pattern

Hermes group sessions may be keyed by both `group_id` and `sender_user_id` when `group_sessions_per_user` is enabled. That produces separate sessions for each participant inside the same LINE group:

```text
agent:main:line:group:<LINE_GROUP_ID>:<USER_A>
agent:main:line:group:<LINE_GROUP_ID>:<USER_B>
```

This is privacy-safe, but it breaks live group-context UX. The second participant's answer does not inherit the first participant's previous prompt or Echo's previous proposal.

## Diagnostic sequence

1. Find the LINE group message in gateway/agent logs by quoted text or timestamp.
2. Capture:
   - `chat=<LINE_GROUP_ID>`
   - `user=<LINE_USER_ID>`
   - `msg='<quoted message>'`
3. Compare conversation-loop log lines around the same time:
   - Does the contextual prompt run in one `session=<A>`?
   - Does the short reply run in another `session=<B>`?
   - Does the short-reply turn show very small `history=N` compared with the active conversation?
4. Check `sessions/sessions.json` for duplicate entries with the same LINE group id and different trailing user ids.
5. Optionally query `state.db` messages for both session ids to prove which session contains the prior context.

## Remediation options

Preferred for active TAHS/Echopedia group discussion rooms:
1. Configure the LINE adapter/gateway path so regular LINE group sessions are shared by group, not isolated per sender.
2. Keep per-user isolation only for contexts where privacy outweighs room continuity.
3. Link the LINE `user_id` to the canonical identity record when the participant is confirmed, so attribution and identity-aware workflows work even in shared sessions.
4. Add/keep a recent group transcript fallback for short acknowledgements (`yes`, `cool`, `go ahead`, `yes, this is pretty cool`) so Echo can resolve them against the active room topic.

## Implementation notes from the Ken Wu / Taiwan Center incident

Concrete durable fixes that worked:

1. **Config bridging:** `gateway/platforms/base.py` already reads `self.config.extra["group_sessions_per_user"]`, but LINE's top-level YAML key may not reach `PlatformConfig.extra` unless the shared-key bridge includes it. Patch `gateway/config.py` in the shared platform YAML bridge to pass through both:
   - `group_sessions_per_user`
   - `thread_sessions_per_user`
2. **Profile config:** set shared group routing for the profile:
   ```yaml
   line:
     group_sessions_per_user: false
     allowed_groups:
       - <approved LINE group id>
   ```
   Use `hermes --profile <profile> config set line.group_sessions_per_user false` for booleans. For lists, verify the resulting YAML; the CLI may store JSON-looking list values as strings, so repair with YAML-safe writing if needed.
3. **Short-reply fallback:** in the LINE adapter, keep a bounded in-memory `chat_id -> deque[(timestamp, user_id, text)]` recent transcript. Before `handle_message`, if the incoming group text matches a short-affirmation pattern, attach recent messages from other users to `MessageEvent.channel_context`. This stays memory-only and avoids creating durable records for every group message.
4. **Identity link:** if the owner identifies the sender of the short reply as the named person, update the private identity link/audit with the captured LINE `user_id`; do not publish raw LINE ids to Echopedia.
5. **Restart:** gateway config/code changes need a gateway restart. From inside a gateway-handled chat, direct `hermes gateway restart` is intentionally blocked. Use an out-of-band shell/service path (for example a delayed `systemctl --user restart hermes-gateway-<profile>` background command) or instruct the owner to restart from a shell.

## Verification pattern

After patching:

```python
from gateway.config import load_gateway_config, Platform
from gateway.session import SessionSource, build_session_key
cfg = load_gateway_config()
line = cfg.platforms[Platform('line')]
assert line.extra.get('group_sessions_per_user') is False

source_a = SessionSource(platform=Platform('line'), chat_id='<group>', chat_type='group', user_id='<user_a>')
source_b = SessionSource(platform=Platform('line'), chat_id='<group>', chat_type='group', user_id='<user_b>')
assert build_session_key(source_a, group_sessions_per_user=False) == build_session_key(source_b, group_sessions_per_user=False)
```

Also instantiate the LINE adapter and feed two synthetic `MessageEvent`s: a contextual prompt from user A, then a short affirmation from user B. Confirm the second event receives non-empty `channel_context`.

## Pitfalls

- Do not diagnose this as semantic misunderstanding first. If the reply is short and contextual, verify session routing before tuning prompts or rewriting Echo's response style.
- Do not assume setting `line.group_sessions_per_user` is enough; confirm it reaches `PlatformConfig.extra` and changes `build_session_key` output.
- Do not leave YAML list values as quoted JSON strings after `hermes config set`; re-read config and repair if necessary.
- Do not declare a gateway restart complete from a gateway chat until a status/log check confirms the service has reloaded.
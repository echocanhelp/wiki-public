#!/usr/bin/env python3
"""
process_onboard_command.py — Leonard's LINE onboarding commands

Detects "onboard" / "onboarding" in chat text, uses @mention as the target
person, captures LINE profile data, and creates a draft Echopedia page.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Same package directory
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from identity_linker import (  # noqa: E402
    append_audit,
    parse_line_event,
    process_line_identity,
    slugify_display_name,
)

ONBOARD_RE = re.compile(
    r'\b(?:onboard(?:ing)?)\b',
    re.IGNORECASE,
)
MENTION_RE = re.compile(
    r'@([^\n@]+?)(?=\s+for\b|\s*$|[,.!?]|\s+on\s+)',
    re.IGNORECASE,
)


def extract_mentions(text: str) -> list[str]:
    return [m.strip() for m in MENTION_RE.findall(text) if m.strip()]


def is_onboard_command(message_text: str) -> bool:
    return bool(ONBOARD_RE.search(message_text or ''))


def process_onboard(
    payload: dict,
    *,
    actor: str = 'leonard-hsu',
    dry_run: bool = False,
) -> dict[str, Any]:
    parsed = parse_line_event(payload)
    text = parsed['message_text']

    if not is_onboard_command(text):
        return {
            'handled': False,
            'reason': 'not_an_onboard_command',
            'message_text': text,
        }

    mentions = extract_mentions(text)
    if not mentions:
        return {
            'handled': False,
            'reason': 'onboard_missing_mention',
            'message_text': text,
            'hint': 'Use: onboard @Display Name',
        }

    target_name = mentions[0]
    # Optional: profile block for the mention target (when bridge has resolved it)
    event = payload
    if 'events' in payload and payload['events']:
        event = payload['events'][0]
    mention_profile = event.get('mention_profile') or payload.get('mention_profile') or {}
    target_user_id = mention_profile.get('userId', '')
    display_name = mention_profile.get('displayName') or target_name

    # If mention is self (sender introducing themselves), bind sender user id
    sender_id = parsed['sender_user_id']
    if not target_user_id and target_name.lower() == (parsed['display_name'] or '').lower():
        target_user_id = sender_id

    result = process_line_identity(
        payload,
        subject_display_name=display_name,
        subject_user_id=target_user_id or None,
        actor=actor,
        dry_run=dry_run,
    )

    if not dry_run and result.get('status') in ('created', 'existing'):
        append_audit(
            'onboard_command',
            {
                'person_slug': result.get('person_slug'),
                'link_id': result.get('link_id'),
                'mention': target_name,
                'group_id': parsed.get('group_id'),
                'details': text[:200],
            },
            actor=actor,
        )

    slug = result.get('person_slug', slugify_display_name(display_name))
    confirmation = (
        f"Onboarding draft for @{target_name}: wiki/people/{slug}.md "
        f"(state={result.get('state', 'proposed')}, link_id={result.get('link_id', 'n/a')})"
    )

    return {
        'handled': True,
        'person_slug': slug,
        'link_id': result.get('link_id'),
        'state': result.get('state'),
        'status': result.get('status'),
        'mention': target_name,
        'confirmation': confirmation,
        'result': result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Process LINE onboard commands')
    parser.add_argument('json_path', nargs='?', help='LINE event JSON file (default: stdin)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    if args.json_path:
        raw = Path(args.json_path).read_text(encoding='utf-8')
    else:
        raw = sys.stdin.read()

    payload = json.loads(raw)
    out = process_onboard(payload, dry_run=args.dry_run)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get('handled') or out.get('reason') else 1


if __name__ == '__main__':
    raise SystemExit(main())
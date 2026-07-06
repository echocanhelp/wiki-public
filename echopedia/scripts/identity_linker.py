#!/usr/bin/env python3
"""
identity_linker.py — Echopedia 2.0 LINE identity linking

Parses a LINE message event JSON, checks identity_registry.json, and creates
draft person pages + registry entries for new LINE contacts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ECHOPEDIA = Path('/home/leedt/echo-system/echopedia')
IDENTITY_REGISTRY = ECHOPEDIA / 'identity/identity_registry.json'
AUDIT_LOG = ECHOPEDIA / 'identity/identity_audit.jsonl'
WIKI_PEOPLE = ECHOPEDIA / 'wiki/people'


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def load_registry() -> dict:
    if not IDENTITY_REGISTRY.exists():
        return {'version': '2.0', 'updated_at': utc_now_iso(), 'links': []}
    return json.loads(IDENTITY_REGISTRY.read_text(encoding='utf-8'))


def save_registry(doc: dict) -> None:
    doc['updated_at'] = utc_now_iso()
    IDENTITY_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    IDENTITY_REGISTRY.write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )


def append_audit(event: str, details: dict, actor: str = 'identity_linker') -> None:
    entry: dict[str, Any] = {
        'timestamp': utc_now_iso(),
        'event': event,
        'actor': actor,
    }
    entry.update(details)
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(AUDIT_LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def slugify_display_name(name_en: str) -> str:
    slug = name_en.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-') or 'person-draft'


def parse_line_event(payload: dict) -> dict[str, Any]:
    """
    Extract fields from LINE webhook payload (single event or {events: [...]}).
    Optional top-level or per-event `profile`: {displayName, userId, pictureUrl}.
    """
    event = payload
    if 'events' in payload and payload['events']:
        event = payload['events'][0]

    source = event.get('source') or {}
    message = event.get('message') or {}
    profile = event.get('profile') or payload.get('profile') or {}

    sender_user_id = source.get('userId') or profile.get('userId') or ''
    group_id = source.get('groupId') or source.get('roomId') or ''
    message_text = message.get('text', '') if message.get('type') == 'text' else ''
    display_name = profile.get('displayName', '')

    return {
        'sender_user_id': sender_user_id,
        'group_id': group_id,
        'message_text': message_text,
        'display_name': display_name,
        'raw_event': event,
    }


def find_link_by_user_id(registry: dict, user_id: str) -> dict | None:
    if not user_id:
        return None
    for link in registry.get('links', []):
        if user_id in link.get('line_user_ids', []):
            return link
    return None


def find_link_by_slug(registry: dict, slug: str) -> dict | None:
    for link in registry.get('links', []):
        if link.get('person_slug') == slug:
            return link
    return None


def make_link_id(slug: str) -> str:
    safe = re.sub(r'[^a-z0-9_]+', '_', slug.lower())[:40]
    return f'lnk_{datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")}_{safe}'


def create_draft_person_page(
    slug: str,
    display_name_en: str,
    display_name_zh: str = '',
    verification_state: str = 'proposed',
) -> Path:
    WIKI_PEOPLE.mkdir(parents=True, exist_ok=True)
    path = WIKI_PEOPLE / f'{slug}.md'
    if path.exists():
        return path

    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    title = f'{display_name_en} {display_name_zh}'.strip() if display_name_zh else display_name_en

    content = f'''---
title: "{title}"
slug: "{slug}"
created: {now}
identity:
  source: LINE
  verification_state: {verification_state}
  verified_by: ""
  verified_at: ""
---

# {title}

## About
[Person bio to be filled during onboarding]

## Timeline
- {now}: Draft page created via LINE identity linker (state={verification_state})

## Sources
- LINE interaction capture
'''
    path.write_text(content, encoding='utf-8')
    return path


def process_line_identity(
    payload: dict,
    *,
    subject_display_name: str | None = None,
    subject_user_id: str | None = None,
    actor: str = 'identity_linker',
    dry_run: bool = False,
) -> dict[str, Any]:
    """
    Core linker: parse event, check registry, create page + link if new.
    subject_* override page subject (e.g. onboard @mention target).
    """
    parsed = parse_line_event(payload)
    user_id = subject_user_id or parsed['sender_user_id']
    display_name = subject_display_name or parsed['display_name'] or 'Unknown'
    group_id = parsed['group_id']

    registry = load_registry()
    existing = find_link_by_user_id(registry, user_id) if user_id else None

    if existing:
        return {
            'status': 'existing',
            'person_slug': existing.get('person_slug'),
            'link_id': existing.get('link_id'),
            'state': existing.get('state'),
            'sender_user_id': parsed['sender_user_id'],
            'group_id': group_id,
        }

    slug = slugify_display_name(display_name)
    if find_link_by_slug(registry, slug):
        # Same slug, different user — suffix with date fragment
        slug = f'{slug}-{datetime.now(timezone.utc).strftime("%m%d")}'

    link_id = make_link_id(slug)
    line_user_ids: list[str] = [user_id] if user_id else []
    state = 'proposed'
    # Subject differs from sender without a captured target user id → page for mention only
    subject_is_other = (
        subject_display_name is not None
        and parsed['sender_user_id']
        and not user_id
    )
    if subject_is_other:
        state = 'pending_line_user_id'
        line_user_ids = []

    new_link = {
        'link_id': link_id,
        'person_slug': slug,
        'display_name_en': display_name,
        'display_name_zh': '',
        'line_user_ids': line_user_ids,
        'line_group_ids_seen': [group_id] if group_id else [],
        'state': state,
        'state_reason': 'Created via identity_linker from LINE message event',
        'confidence': 'medium',
        'consent': {
            'profile_linking': False,
            'dm_processing': 'none',
            'public_quote_reuse': False,
        },
        'verified_by': '',
        'last_verified_at': '',
        'created_at': utc_now_iso(),
        'updated_at': utc_now_iso(),
    }

    result = {
        'status': 'created',
        'person_slug': slug,
        'link_id': link_id,
        'state': state,
        'sender_user_id': parsed['sender_user_id'],
        'group_id': group_id,
        'display_name': display_name,
        'page_path': str(WIKI_PEOPLE / f'{slug}.md'),
        'dry_run': dry_run,
    }

    if dry_run:
        return result

    create_draft_person_page(slug, display_name, verification_state='proposed')
    registry.setdefault('links', []).append(new_link)
    save_registry(registry)
    append_audit(
        'link_created',
        {
            'person_slug': slug,
            'link_id': link_id,
            'line_user_id': user_id or None,
            'group_id': group_id or None,
            'details': f'LINE message: {parsed["message_text"][:120]}',
        },
        actor=actor,
    )
    append_audit(
        'page_created',
        {'person_slug': slug, 'link_id': link_id, 'state': state},
        actor=actor,
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description='Echopedia LINE identity linker')
    parser.add_argument(
        'json_path',
        nargs='?',
        help='Path to LINE event JSON (default: read stdin)',
    )
    parser.add_argument('--dry-run', action='store_true', help='Do not write registry or pages')
    args = parser.parse_args()

    if args.json_path:
        raw = Path(args.json_path).read_text(encoding='utf-8')
    else:
        raw = sys.stdin.read()
    if not raw.strip():
        print('Error: empty input', file=sys.stderr)
        return 1

    payload = json.loads(raw)
    out = process_line_identity(payload, dry_run=args.dry_run)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
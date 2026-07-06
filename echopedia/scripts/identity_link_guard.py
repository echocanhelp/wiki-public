#!/usr/bin/env python3
"""
Identity Link Guard — Echopedia 2.0
Validates identity_registry.json against wiki pages and audit log.
Replaces legacy identity_link_guard.py from echohsu profile.

Output: silent on health, ALERT lines on mismatches.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HOME = Path('/home/leedt')
ECHOPEDIA = HOME / 'echo-system/echopedia'
LINKS_PATH = ECHOPEDIA / 'identity/identity_registry.json'
AUDIT_PATH = ECHOPEDIA / 'identity/identity_audit.jsonl'
WIKI_DIR = ECHOPEDIA / 'wiki'


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def load_audit(path: Path) -> list:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            rows.append({'_parse_error': line})
    return rows


def get_page_slugs() -> set[str]:
    """Return all person slugs from wiki/people/ directory."""
    slugs = set()
    people_dir = WIKI_DIR / 'people'
    if not people_dir.exists():
        return slugs
    for f in people_dir.iterdir():
        if f.suffix == '.md':
            slugs.add(f.stem)
    return slugs


def main() -> None:
    issues = []

    if not LINKS_PATH.exists():
        print(f'ALERT identity-links: missing file {LINKS_PATH}')
        return

    doc = load_json(LINKS_PATH)
    links = doc.get('links', [])
    audit_rows = load_audit(AUDIT_PATH)
    page_slugs = get_page_slugs()

    for link in links:
        lid = link.get('link_id', 'unknown')
        slug = link.get('person_slug', '')
        state = link.get('state', 'unknown')

        # Required fields check
        for key in ['person_slug', 'state', 'consent', 'display_name_en']:
            if key not in link:
                issues.append(f'{lid}: missing required key {key}')

        # owner_verified checks
        if state == 'owner_verified':
            if not link.get('verified_by'):
                issues.append(f'{lid}: owner_verified but missing verified_by')
            if not link.get('last_verified_at'):
                issues.append(f'{lid}: owner_verified but missing last_verified_at')

        # Page existence check
        if slug and not slug.startswith('pending-'):
            if slug not in page_slugs:
                issues.append(f'{lid}: wiki page missing for slug={slug}')
            # Also check if page exists at legacy path
            legacy_page = ECHOPEDIA / 'wiki/legacy' / 'people' / f'{slug}.md'
            if legacy_page.exists():
                issues.append(f'{lid}: stale legacy page at {legacy_page} — move to wiki/people/')

        # Audit trail check
        matched = any(r.get('person_slug') == slug for r in audit_rows if isinstance(r, dict))
        if not matched and slug:
            issues.append(f'{lid}: no audit row for person_slug={slug}')

    if issues:
        now = datetime.now(timezone.utc).isoformat()
        print(f'ALERT identity-links-guard {now}')
        for issue in issues:
            print(f'- {issue}')
    else:
        # Healthy — print count only (silent when no issues, or brief count)
        print(f'OK identity-links-guard: {len(links)} links verified, {len(page_slugs)} wiki pages found')


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
identity_audit.py — Weekly Echopedia identity consistency audit

- Registry slugs vs wiki/people pages (bidirectional)
- Orphaned LINE user IDs (in registry but no resolvable link / duplicates)
- Verification state distribution
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ECHOPEDIA = Path('/home/leedt/echo-system/echopedia')
IDENTITY_REGISTRY = ECHOPEDIA / 'identity/identity_registry.json'
WIKI_PEOPLE = ECHOPEDIA / 'wiki/people'


def load_registry() -> dict:
    if not IDENTITY_REGISTRY.exists():
        return {'links': []}
    return json.loads(IDENTITY_REGISTRY.read_text(encoding='utf-8'))


def people_page_slugs() -> set[str]:
    if not WIKI_PEOPLE.exists():
        return set()
    return {p.stem for p in WIKI_PEOPLE.iterdir() if p.suffix == '.md'}


def run_audit() -> dict:
    registry = load_registry()
    links = registry.get('links', [])
    page_slugs = people_page_slugs()
    registry_slugs = {lnk.get('person_slug') for lnk in links if lnk.get('person_slug')}

    issues: list[str] = []

    # Slugs in registry without wiki page
    for slug in sorted(registry_slugs - page_slugs):
        if slug.startswith('pending-'):
            continue
        issues.append(f'registry_slug_missing_page: {slug}')

    # Wiki people pages without registry entry
    for slug in sorted(page_slugs - registry_slugs):
        issues.append(f'wiki_page_missing_registry: {slug}')

    # LINE user ID index
    uid_to_links: dict[str, list[str]] = {}
    orphaned_uids: list[str] = []
    for lnk in links:
        lid = lnk.get('link_id', '?')
        slug = lnk.get('person_slug', '')
        for uid in lnk.get('line_user_ids', []):
            if not uid:
                continue
            uid_to_links.setdefault(uid, []).append(lid)
            if not slug or slug not in page_slugs:
                orphaned_uids.append(f'{uid} (link {lid}, slug={slug})')

    for uid, lids in uid_to_links.items():
        if len(lids) > 1:
            issues.append(f'duplicate_line_user_id: {uid} in {lids}')

    state_dist = Counter(lnk.get('state', 'unknown') for lnk in links)

    report = {
        'timestamp': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'link_count': len(links),
        'wiki_people_count': len(page_slugs),
        'state_distribution': dict(sorted(state_dist.items())),
        'issues': issues,
        'orphaned_line_user_ids': orphaned_uids,
        'healthy': len(issues) == 0 and len(orphaned_uids) == 0,
    }
    return report


def main() -> int:
    report = run_audit()
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report['healthy']:
        print('\n--- Summary ---', file=sys.stderr)
        print(f"Issues: {len(report['issues'])}", file=sys.stderr)
        print(f"Orphaned LINE UIDs: {len(report['orphaned_line_user_ids'])}", file=sys.stderr)
        return 1
    print('\nOK: identity audit passed', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
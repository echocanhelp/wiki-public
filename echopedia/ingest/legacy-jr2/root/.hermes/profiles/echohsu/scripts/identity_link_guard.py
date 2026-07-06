#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

HOME = Path('/root/.hermes/profiles/echohsu')
WIKI = Path('/root/wiki-public/content')
LINKS_PATH = HOME / 'identity_links.json'
AUDIT_PATH = HOME / 'identity_link_audit.jsonl'


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def load_audit(path: Path):
    rows = []
    if not path.exists():
        return rows
    for ln in path.read_text(encoding='utf-8').splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            rows.append(json.loads(ln))
        except Exception:
            rows.append({'_parse_error': ln})
    return rows


def extract_frontmatter_status(md_path: Path):
    if not md_path.exists():
        return None
    text = md_path.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---\n'):
        return None
    try:
        end = text.index('\n---\n', 4)
    except ValueError:
        return None
    fm = text[4:end]
    if yaml:
        try:
            data = yaml.safe_load(fm) or {}
            return (((data.get('identity') or {}).get('line_identity') or {}).get('status'))
        except Exception:
            return None
    return None


def main():
    issues = []
    if not LINKS_PATH.exists():
        print(f'ALERT identity-links: missing file {LINKS_PATH}')
        return

    links_doc = load_json(LINKS_PATH)
    links = links_doc.get('links', [])
    audit_rows = load_audit(AUDIT_PATH)

    # basic required fields
    for i, link in enumerate(links):
        lid = link.get('link_id', f'idx:{i}')
        for key in ['person_slug', 'state', 'consent']:
            if key not in link:
                issues.append(f'{lid}: missing key {key}')

        if link.get('state') == 'owner_verified':
            if not link.get('verified_by'):
                issues.append(f'{lid}: owner_verified missing verified_by')
            if not link.get('last_verified_at'):
                issues.append(f'{lid}: owner_verified missing last_verified_at')
            if not (link.get('consent', {}) or {}).get('profile_linking'):
                issues.append(f'{lid}: owner_verified but consent.profile_linking != true')

        slug = link.get('person_slug', '')
        if slug and not slug.startswith('pending-'):
            page = WIKI / f'{slug}.md'
            if not page.exists():
                issues.append(f'{lid}: page missing {page}')
            else:
                page_status = extract_frontmatter_status(page)
                if page_status and page_status != link.get('state'):
                    issues.append(f'{lid}: state mismatch link={link.get("state")} page={page_status} ({page.name})')

    # audit consistency: each link_id should have at least one row mentioning current slug
    for i, link in enumerate(links):
        lid = link.get('link_id', f'idx:{i}')
        slug = link.get('person_slug')
        matched = any((r.get('person_slug') == slug) for r in audit_rows if isinstance(r, dict))
        if not matched:
            issues.append(f'{lid}: no audit row found for person_slug={slug}')

    # report
    if issues:
        now = datetime.now(timezone.utc).isoformat()
        print(f'ALERT identity-links-guard {now}')
        for it in issues:
            print(f'- {it}')


if __name__ == '__main__':
    main()

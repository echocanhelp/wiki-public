#!/usr/bin/env python3
"""
content_classify.py — Echopedia 2.0
Classifies content from LINE/web ingest into wiki categories and writes draft pages.
Handles new member pages, org pages, and general content from staging.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ECHOPEDIA = Path('/home/leedt/echo-system/echopedia')
STAGING = ECHOPEDIA / 'staging'
WIKI_DIR = ECHOPEDIA / 'wiki'
WEB_ARCHIVES_URLS = ECHOPEDIA / 'web-archives' / 'urls'
IDENTITY_REGISTRY = ECHOPEDIA / 'identity/identity_registry.json'
AUDIT_LOG = ECHOPEDIA / 'identity/identity_audit.jsonl'

# Canonical org slugs from scrape_websites.sh (latest archive per slug wins)
ORG_ARCHIVE_SPECS: dict[str, dict[str, str]] = {
    'guangzhou-society-taiwan-professional-executives': {
        'wiki_slug': 'guangzhou-society-taiwan-professional-executives',
        'title': 'Guangzhou Society of Taiwan Professional and Executives',
        'title_zh': '好牧者臺灣基督長老教會',
        'canonical_url': 'https://www.gstpc.org',
    },
    'irvine-taiwanese-presbyterian-church': {
        'wiki_slug': 'irvine-taiwanese-presbyterian-church',
        'title': 'Irvine Taiwanese Presbyterian Church (IRVINE台灣基督長老教會)',
        'title_zh': '爾灣台灣基督長老教會',
        'canonical_url': 'https://www.irvinetpc.org',
    },
    'taiwan-center': {
        'wiki_slug': 'taiwan-center',
        'title': 'Taiwan Center Foundation of Greater Los Angeles',
        'title_zh': '大洛杉磯台灣會館基金會',
        'canonical_url': 'https://taiwancenter.org',
    },
}

ARCHIVE_FILENAME_RE = re.compile(
    r'^org_(?P<slug>[a-z0-9-]+)_(?P<ts>\d{8}_\d{6})\.md$'
)


def load_registry() -> dict:
    if not IDENTITY_REGISTRY.exists():
        return {'links': []}
    return json.loads(IDENTITY_REGISTRY.read_text(encoding='utf-8'))


def append_audit(event: str, details: dict) -> None:
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': event,
        **details,
    }
    with open(AUDIT_LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def classify_content(content: str, filename: str) -> dict:
    """Classify content into a category and extract key metadata."""
    content_lower = content.lower()

    # Detect person page
    person_patterns = [
        r'^(?:#|##)\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$',  # Name as heading
        r'display_name_en|display_name_zh|line_user_id',
        r'(?:許|陳|吳|林|王|李|張|劉|黃|周).*?(?:鴻|光|峯|樹|文|明|龍|華)',
    ]

    for pattern in person_patterns:
        if re.search(pattern, content):
            return {
                'category': 'people',
                'confidence': 0.85,
                'suggested_slug': 'person-draft',
                'reason': 'Detected person identity content',
            }

    # Detect organization page
    org_patterns = [
        r'(?:taiwanese|taos|taos society|gtpa|gstpc|church|association|society)',
        r'(?:organization|association|society|chamber|foundation)',
        r'(?:taiwan|taos|gtta)',
    ]

    for pattern in org_patterns:
        if re.search(pattern, content_lower):
            return {
                'category': 'organizations',
                'confidence': 0.75,
                'suggested_slug': 'org-draft',
                'reason': 'Detected organization content',
            }

    # Default: general content
    return {
        'category': 'topics',
        'confidence': 0.5,
        'suggested_slug': 'topic-draft',
        'reason': 'General content — no specific category detected',
    }


def generate_person_page_slug(name_en: str = '', name_zh: str = '') -> str:
    """Generate a wiki slug from display names."""
    slug_parts = []

    if name_en:
        # Convert English name to slug
        slug_en = name_en.lower()
        slug_en = re.sub(r'[^a-z0-9]+', '-', slug_en)
        slug_en = slug_en.strip('-')
        slug_parts.append(slug_en)

    if name_zh:
        slug_parts.append(name_zh)

    if slug_parts:
        return '-'.join(slug_parts)

    return 'person-draft'


def create_person_page(name_en: str, name_zh: str, source: str, line_groups: list[str] | None = None) -> Path:
    """Create a draft person page in wiki/people/."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    slug = generate_person_page_slug(name_en, name_zh)
    category_dir = WIKI_DIR / 'people'
    category_dir.mkdir(parents=True, exist_ok=True)
    target_path = category_dir / f'{slug}.md'

    title = f'{name_en} {name_zh}'.strip() if name_zh else name_en

    page_content = f"""---
title: "{title}"
slug: "{slug}"
created: {now}
source: {source}
identity:
  source: LINE
  verification_state: pending_page
  verified_by: ""
  verified_at: ""
---

# {title}

## About
[Person bio to be filled during onboarding]

## Timeline
- {now}: Initial record created via LINE onboarding

## Sources
- LINE interaction capture

"""

    target_path.write_text(page_content, encoding='utf-8')

    # Update registry if it's a new person
    registry = load_registry()
    link_id = f'lnk_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    new_link = {
        'link_id': link_id,
        'person_slug': slug,
        'display_name_en': name_en,
        'display_name_zh': name_zh,
        'line_user_ids': [],  # Will be filled when LINE user_id is captured
        'line_group_ids_seen': line_groups or [],
        'state': 'pending_page' if not line_groups else 'proposed',
        'state_reason': f'Onboarding initiated — {source}',
        'confidence': 'medium',
        'consent': {
            'profile_linking': False,
            'dm_processing': 'none',
            'public_quote_reuse': False,
        },
        'verified_by': '',
        'last_verified_at': '',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'updated_at': datetime.now(timezone.utc).isoformat(),
    }
    registry['links'].append(new_link)
    registry['updated_at'] = datetime.now(timezone.utc).isoformat()
    IDENTITY_REGISTRY.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False), encoding='utf-8'
    )

    append_audit('page_created', {
        'person_slug': slug,
        'link_id': link_id,
        'display_name_en': name_en,
        'display_name_zh': name_zh,
        'source': source,
    })

    print(f'Created person page: {target_path}')
    print(f'Registry updated: {link_id} → {slug} (state: {new_link["state"]})')

    return target_path


def classify_staging_files() -> list[dict]:
    """Scan staging/ and classify each file."""
    if not STAGING.exists():
        return []

    results = []

    for filepath in sorted(STAGING.iterdir()):
        if not filepath.is_file():
            continue

        content = filepath.read_text(encoding='utf-8', errors='ignore')
        classification = classify_content(content, filepath.name)
        results.append({
            'file': filepath.name,
            'classification': classification,
        })

    return results


def parse_archive_filename(name: str) -> tuple[str, str, datetime] | None:
    """Parse org_{slug}_{YYYYMMDD}_{HHMMSS}.md → category, slug, scraped_at."""
    match = re.match(r'^(org)_(.+)_(\d{8})_(\d{6})\.md$', name)
    if not match:
        return None
    category, slug, date_part, time_part = match.groups()
    scraped_at = datetime.strptime(
        f'{date_part}{time_part}', '%Y%m%d%H%M%S'
    ).replace(tzinfo=timezone.utc)
    return category, slug, scraped_at


def scrape_archive_failed(content: str) -> bool:
    stripped = content.strip()
    if stripped.startswith('{"data":null') or 'SubmittedDataMalformedError' in content:
        return True
    if len(stripped) < 200 and 'could not be resolved' in stripped:
        return True
    return False


def extract_archive_fields(content: str) -> dict[str, str]:
    """Pull title, source URL, and a short summary from Jina markdown archive."""
    title = ''
    source_url = ''
    title_match = re.search(r'^Title:\s*(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    url_match = re.search(r'^URL Source:\s*(.+)$', content, re.MULTILINE)
    if url_match:
        source_url = url_match.group(1).strip()

    summary = ''
    if title:
        summary = title.split('–')[0].split('-')[0].strip()
    paragraphs: list[str] = []
    in_body = False
    for line in content.splitlines():
        if line.strip() == 'Markdown Content:':
            in_body = True
            continue
        if not in_body:
            continue
        text = line.strip()
        if not text or text.startswith('![') or text.startswith('[!['):
            continue
        if text.startswith('*') and 'http' in text:
            continue
        if text.startswith('[') and '](' in text and len(text) < 120:
            continue
        if text.startswith('#'):
            text = re.sub(r'^#+\s*', '', text).strip()
        if len(text) < 40:
            continue
        if text not in paragraphs:
            paragraphs.append(text)
        if len(paragraphs) >= 2:
            break
    if paragraphs:
        summary = ' '.join(paragraphs)[:480]
    elif title:
        summary = title[:480]
    return {'title': title, 'source_url': source_url, 'summary': summary}


def latest_web_archives_by_slug() -> dict[str, Path]:
    """Return newest archive file per org slug."""
    if not WEB_ARCHIVES_URLS.exists():
        return {}
    latest: dict[str, tuple[datetime, Path]] = {}
    for path in WEB_ARCHIVES_URLS.glob('org_*.md'):
        parsed = parse_archive_filename(path.name)
        if not parsed:
            continue
        _cat, slug, scraped_at = parsed
        prev = latest.get(slug)
        if prev is None or scraped_at > prev[0]:
            latest[slug] = (scraped_at, path)
    return {slug: item[1] for slug, item in latest.items()}


def prune_duplicate_archives() -> list[str]:
    """Delete older archives; keep only newest timestamp per slug."""
    latest = latest_web_archives_by_slug()
    keep = {p.resolve() for p in latest.values()}
    removed: list[str] = []
    if not WEB_ARCHIVES_URLS.exists():
        return removed
    for path in sorted(WEB_ARCHIVES_URLS.glob('org_*.md')):
        if path.resolve() in keep:
            continue
        parsed = parse_archive_filename(path.name)
        if parsed and parsed[1] not in ORG_ARCHIVE_SPECS:
            removed.append(path.name)
            path.unlink()
            continue
        if path.resolve() not in keep:
            removed.append(path.name)
            path.unlink()
    return removed


def classify_web_archives() -> list[dict]:
    """Classify newest web archive per configured org slug."""
    results: list[dict] = []
    archives = latest_web_archives_by_slug()
    for archive_slug, spec in ORG_ARCHIVE_SPECS.items():
        path = archives.get(archive_slug)
        if path is None:
            results.append({
                'file': None,
                'archive_slug': archive_slug,
                'classification': {
                    'category': 'organizations',
                    'confidence': 0.0,
                    'suggested_slug': spec['wiki_slug'],
                    'reason': 'No web archive found for slug',
                },
                'scrape_ok': False,
            })
            continue
        content = path.read_text(encoding='utf-8', errors='ignore')
        ok = not scrape_archive_failed(content)
        classification = classify_content(content, path.name)
        classification['suggested_slug'] = spec['wiki_slug']
        if ok:
            classification['reason'] = (
                f"Web archive → organizations ({spec['wiki_slug']})"
            )
            classification['confidence'] = max(classification['confidence'], 0.9)
        else:
            classification['reason'] = 'Web archive fetch failed or empty'
            classification['confidence'] = 0.0
        parsed = parse_archive_filename(path.name)
        scraped_at = parsed[2].isoformat() if parsed else ''
        results.append({
            'file': path.name,
            'archive_slug': archive_slug,
            'classification': classification,
            'scrape_ok': ok,
            'scraped_at': scraped_at,
            'archive_path': str(path),
        })
    return results


def build_org_page_body(
    spec: dict[str, str],
    fields: dict[str, str],
    archive_path: Path,
    scraped_at: datetime,
) -> str:
    """Draft wiki body from archive metadata and extracted summary."""
    title = spec['title']
    source_url = fields.get('source_url') or spec['canonical_url']
    summary = fields.get('summary') or f'Draft organization page from {source_url}.'
    return '\n'.join([
        f'# {title}',
        '',
        '## Summary',
        summary,
        '',
        '## Official site',
        f'- {source_url}',
        '',
        '## Web archive',
        f'- Scraped: {scraped_at.strftime("%Y-%m-%d %H:%M:%S UTC")}',
        f'- Archive file: `{archive_path.name}`',
        '',
        '## Notes',
        'Draft generated by Echopedia 2.0 `content_classify.py` from Jina reader output.',
        'Review and expand before publishing to wiki-public.',
        '',
    ])


def create_org_pages_from_web_archives() -> list[Path]:
    """Write draft organization pages under wiki/organizations/."""
    created: list[Path] = []
    org_dir = WIKI_DIR / 'organizations'
    org_dir.mkdir(parents=True, exist_ok=True)
    archives = latest_web_archives_by_slug()

    for archive_slug, spec in ORG_ARCHIVE_SPECS.items():
        path = archives.get(archive_slug)
        if path is None:
            print(f'  Skip {spec["wiki_slug"]}: no archive')
            continue
        content = path.read_text(encoding='utf-8', errors='ignore')
        if scrape_archive_failed(content):
            print(f'  Skip {spec["wiki_slug"]}: scrape failed ({path.name})')
            continue
        parsed = parse_archive_filename(path.name)
        if not parsed:
            continue
        _cat, _slug, scraped_at = parsed
        fields = extract_archive_fields(content)
        summary = fields.get('summary', '').replace('"', "'")
        if len(summary) > 300:
            summary = summary[:297] + '...'
        page = f"""---
title: "{spec['title']}"
slug: "{spec['wiki_slug']}"
type: organization
source: web_archive
scraped_at: {scraped_at.isoformat()}
summary: "{summary}"
canonical_url: "{spec['canonical_url']}"
archive_file: "{path.name}"
---

{build_org_page_body(spec, fields, path, scraped_at)}"""
        target = org_dir / f'{spec["wiki_slug"]}.md'
        target.write_text(page, encoding='utf-8')
        created.append(target)
        append_audit('org_page_created', {
            'wiki_slug': spec['wiki_slug'],
            'archive_slug': archive_slug,
            'archive_file': path.name,
            'scraped_at': scraped_at.isoformat(),
        })
        print(f'  Created org page: {target}')
    return created


def main() -> None:
    print('Content classify scan (staging):')

    results = classify_staging_files()

    if not results:
        print('  No staging files to classify')
    else:
        for result in results:
            print(f"  {result['file']}: {result['classification']['reason']}")

    print('')
    print('Web archive cleanup (keep latest per slug):')
    removed = prune_duplicate_archives()
    if removed:
        for name in removed:
            print(f'  removed {name}')
    else:
        print('  nothing to remove')

    print('')
    print('Web archive classification (echopedia/web-archives/urls/):')
    web_results = classify_web_archives()
    for result in web_results:
        label = result.get('file') or '(missing)'
        status = 'OK' if result.get('scrape_ok') else 'FAIL'
        cls = result['classification']
        print(
            f"  [{status}] {label}: {cls['category']} / "
            f"{cls['suggested_slug']} — {cls['reason']}"
        )

    print('')
    print('Creating draft organization wiki pages:')
    create_org_pages_from_web_archives()

    # Also print registry status
    registry = load_registry()
    links = registry.get('links', [])
    verified_count = sum(1 for l in links if l.get('state') == 'owner_verified')
    print(f'Identity registry: {len(links)} total, {verified_count} owner_verified')


if __name__ == '__main__':
    main()
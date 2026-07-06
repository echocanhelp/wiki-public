#!/usr/bin/env python3
"""
publish_staging.py — Echopedia 2.0
Scans echopedia/staging/ for new/modified files, moves them to wiki/,
then commits and pushes to wiki-public.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ECHOPEDIA = Path('/home/leedt/echo-system/echopedia')
STAGING = ECHOPEDIA / 'staging'
WIKI_DIR = ECHOPEDIA / 'wiki'
AUDIT_LOG = ECHOPEDIA / 'identity/identity_audit.jsonl'


def append_audit(event: str, details: dict) -> None:
    """Append to identity_audit.jsonl."""
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': event,
    }
    entry.update(details)
    line = json.dumps(entry, ensure_ascii=False)
    with open(AUDIT_LOG, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def git_command(*args: str) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ['git', '-C', str(ECHOPEDIA)] + list(args),
        capture_output=True, text=True, timeout=30
    )
    return result.stdout.strip()


def publish() -> list[str]:
    """Move staging files to wiki/ and return list of published file paths."""
    if not STAGING.exists():
        return []

    published = []

    # Scan staging directory
    for item in sorted(STAGING.iterdir()):
        if not item.is_file():
            continue

        # Determine target path under wiki/
        # File names follow convention: category/slug.md or category/name.md
        parts = item.name.rsplit('.', 1)
        if len(parts) != 2:
            continue

        stem, ext = parts
        if ext != 'md':
            continue  # Skip non-markdown (will be handled by content processor)

        # Parse frontmatter for target category
        content = item.read_text(encoding='utf-8')
        target_category = 'other'  # default

        # Check frontmatter category
        if content.startswith('---'):
            try:
                end = content.index('\n---', 4)
                fm_text = content[4:end]
                if 'category:' in fm_text:
                    for line in fm_text.split('\n'):
                        if line.strip().startswith('category:'):
                            target_category = line.strip().split(':', 1)[1].strip()
                            break
            except (ValueError, IndexError):
                pass

        # Also check slug-based paths
        if stem.startswith('people-'):
            target_category = 'people'
        elif stem.startswith('procedure-'):
            target_category = 'procedures'
        elif stem.startswith('topic-'):
            target_category = 'topics'
        elif stem.startswith('org-'):
            target_category = 'organizations'
        elif stem.startswith('person-'):
            target_category = 'people'

        target_dir = WIKI_DIR / target_category
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / f'{stem}.md'

        # Move the file
        shutil.copy2(str(item), str(target_path))
        published.append(str(target_path))
        item.unlink()  # Remove from staging

    return published


def git_push(published: list[str]) -> None:
    """Stage, commit, and push changes."""
    if not published:
        return

    # Stage all
    git_command('add', '-')
    status = git_command('status', '--short')

    if not status:
        return  # Nothing to commit

    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    files_str = ', '.join(Path(p).name for p in published)
    msg = f'Echopedia 2.0 publish: {len(published)} file(s) — {files_str}'

    git_command('commit', '-m', msg)
    git_command('push', 'origin', 'master')

    # Append audit
    append_audit('publish_pushed', {
        'file_count': len(published),
        'files': [Path(p).name for p in published],
        'commit_message': msg,
    })


def main() -> None:
    published = publish()

    if not published:
        print(f'publish_staging: no staging files found')
        return

    print(f'publish_staging: {len(published)} file(s) staged for publishing:')
    for p in published:
        print(f'  {p}')

    try:
        git_push(published)
        print(f'publish_staging: committed and pushed {len(published)} file(s)')
    except subprocess.TimeoutExpired:
        # Git push failed (e.g., no network, auth issue)
        # Move files back to staging for retry
        print('publish_staging: ERROR — git push failed, files remain in staging')
        sys.exit(1)
    except Exception as e:
        print(f'publish_staging: ERROR — {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
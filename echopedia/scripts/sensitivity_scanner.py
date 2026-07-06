#!/usr/bin/env python3
"""
sensitivity_scanner.py — Echopedia 2.0
Pre-publish scan for sensitive content in staging/wiki files.
Scans for PII patterns (phone, SSN, financial data) and flags them.
Local archive is never modified — only reports for staging decisions.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ECHOPEDIA = Path('/home/leedt/echo-system/echopedia')

# Sensitive patterns to detect
SENSITIVE_PATTERNS = {
    'phone': {
        'pattern': re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'),
        'description': 'Phone number',
    },
    'ssn': {
        'pattern': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
        'description': 'SSN-like pattern',
    },
    'email': {
        'pattern': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
        'description': 'Email address',
    },
    'credit_card': {
        'pattern': re.compile(r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b'),
        'description': 'Credit card number',
    },
    'bank_account': {
        'pattern': re.compile(r'\b(?:account|routing|bank)\s*(?:#|number|no\.?)?\s*[0-9]{6,}\b', re.IGNORECASE),
        'description': 'Bank account reference',
    },
    'address': {
        'pattern': re.compile(r'\b\d{1,5}\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd|Way|Court|Ct|Place|Pl)\b', re.IGNORECASE),
        'description': 'Physical address',
    },
    'passport': {
        'pattern': re.compile(r'\b(?:passport|護照)\s*[A-Z0-9]{6,12}\b', re.IGNORECASE),
        'description': 'Passport number',
    },
    'line_user_id': {
        'pattern': re.compile(r'\bU[0-9a-f]{28,32}\b'),
        'description': 'LINE user ID',
    },
}


def scan_file(filepath: Path) -> list[dict]:
    """Scan a file for sensitive patterns. Returns list of hits."""
    hits = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            for pattern_name, info in SENSITIVE_PATTERNS.items():
                matches = info['pattern'].findall(line)
                for match in matches:
                    hits.append({
                        'file': str(filepath),
                        'line': line_num,
                        'pattern': pattern_name,
                        'description': info['description'],
                        'match': match,
                    })
    except Exception as e:
        hits.append({
            'file': str(filepath),
            'error': f'Could not read: {e}',
        })

    return hits


def scan_directory(dirpath: Path) -> list[dict]:
    """Scan all markdown files in directory."""
    all_hits = []
    if not dirpath.exists():
        return all_hits

    for filepath in sorted(dirpath.rglob('*.md')):
        hits = scan_file(filepath)
        all_hits.extend(hits)

    return all_hits


def main() -> None:
    # Scan staging directory (primary) and wiki directory (secondary check)
    staging_dir = ECHOPEDIA / 'staging'
    wiki_dir = ECHOPEDIA / 'wiki'

    all_hits = []

    if staging_dir.exists():
        staging_hits = scan_directory(staging_dir)
        all_hits.extend(staging_hits)

    if wiki_dir.exists():
        wiki_hits = scan_directory(wiki_dir)
        all_hits.extend(wiki_hits)

    if all_hits:
        # Group by file
        by_file = {}
        for hit in all_hits:
            fpath = hit['file']
            if fpath not in by_file:
                by_file[fpath] = []
            by_file[fpath].append(hit)

        print(f'Sensitivity scan: {len(all_hits)} sensitive items found')
        for fpath, hits in by_file.items():
            print(f'  {fpath}: {len(hits)} hit(s)')
            for hit in hits[:3]:  # Show up to 3 per file
                print(f'    line {hit["line"]}: {hit["description"]} → {hit.get("match", "N/A")}')
            if len(hits) > 3:
                print(f'    ... and {len(hits) - 3} more')

        # Flag files with sensitive content as needing review
        flagged_files = set(by_file.keys())
        print(f'Files requiring review: {len(flagged_files)}')

        # Write scan results to log
        log_path = ECHOPEDIA / 'web-archives' / 'sensitivity_scan_latest.json'
        scan_report = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'total_hits': len(all_hits),
            'flagged_files': list(flagged_files),
            'hits': all_hits,
        }
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(scan_report, f, indent=2, ensure_ascii=False)

        print(f'Scan report written to {log_path}')
    else:
        print('Sensitivity scan: clean — no sensitive content detected')


if __name__ == '__main__':
    main()
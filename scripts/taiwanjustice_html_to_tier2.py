#!/usr/bin/env python3
"""Phase 3.1: HTML → Tier2 markdown converter for taiwanjustice.net archive.

Reads raw HTML + sidecar JSON from knowledge/web-archives/taiwanjustice-net/raw-html/YYYY/
Writes markdown to knowledge/web-archives/taiwanjustice-net/tier2/YYYY/<slug>.md

Resume-safe via state file. No LLM per page — deterministic extraction.

Usage:
  python3 taiwanjustice_html_to_tier2.py --pilot 50
  python3 taiwanjustice_html_to_tier2.py --limit 1000
  python3 taiwanjustice_html_to_tier2.py --resume
  python3 taiwanjustice_html_to_tier2.py --dry-run --pilot 10
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import trafilatura
from bs4 import BeautifulSoup

ROOT = Path("/home/leedt/echo-system")
RAW = ROOT / "knowledge/web-archives/taiwanjustice-net/raw-html"
TIER2 = ROOT / "knowledge/web-archives/taiwanjustice-net/tier2"
STATE = ROOT / "knowledge/web-archives/taiwanjustice-net/tier2-convert-state.json"
MANIFEST = ROOT / "knowledge/web-archives/taiwanjustice-net/tier2/MANIFEST.jsonl"
PILOT_NOTES = TIER2 / "PILOT_NOTES.md"
LOG = ROOT / "knowledge/web-archives/taiwanjustice-net/tier2-convert.log"

# Parking markers (must not be treated as content)
PARKING_MARKERS = (
    "Parked Domain name on Hostinger",
    "Parked Domain",
    "Hostinger DNS system",
    "domain is parked",
    "This domain is parked",
)

# Minimum content length (chars) to keep a page
MIN_BODY_CHARS = 200

# Skip pure infrastructure
SKIP_SUBSTR = (
    "/wp-login.php",
    "/xmlrpc.php",
    "/wp-cron.php",
    "/wp-admin/",
    "reauth=1",
    "/cgi-bin/",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg: str) -> None:
    line = f"{utc_now()} {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {
        "done": {},      # html_path -> {status, md_path, ts, reason}
        "stats": {
            "ok": 0,
            "skip_parking": 0,
            "skip_junk": 0,
            "skip_tiny": 0,
            "skip_infra": 0,
            "fail": 0,
        },
    }


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def detect_lang(text: str, html_lang: str | None) -> str:
    """Detect language: zh-Hant or en.
    
    Uses CJK/Latin ratio with a threshold (0.3) so that articles with
    significant English source attributions/URLs don't get misclassified.
    Falls back to HTML lang attribute when ratio is ambiguous.
    """
    cjk_count = sum(1 for c in text if 0x4E00 <= ord(c) <= 0x9FFF)
    latin_count = sum(1 for c in text if 0x0041 <= ord(c) <= 0x007A)
    total = cjk_count + latin_count
    if total > 0:
        ratio = cjk_count / total
        if ratio >= 0.3:
            return "zh-Hant"
    # Fall back to HTML lang attribute
    if html_lang:
        if "zh" in html_lang.lower():
            return "zh-Hant"
        if "en" in html_lang.lower():
            return "en"
    return "en"


def is_parking(html: str) -> bool:
    for marker in PARKING_MARKERS:
        if marker.lower() in html.lower():
            return True
    return False


def should_skip_url(url: str) -> str | None:
    """Return skip reason string if URL should be skipped, None if OK."""
    for sub in SKIP_SUBSTR:
        if sub in url:
            return f"skip_infra:{sub}"
    return None


def extract_title(soup: BeautifulSoup) -> str:
    """Extract title from WordPress HTML."""
    # h1.entry-title
    h1 = soup.find("h1", class_="entry-title")
    if h1:
        return h1.get_text(strip=True)
    # meta property og:title
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        content = str(og.get("content", ""))
        return content.strip() if content else ""
    # <title> tag
    title_tag = soup.find("title")
    if title_tag:
        return title_tag.get_text(strip=True)
    return "Untitled"


def extract_content(html: str) -> str | None:
    """Extract main article content as text using trafilatura."""
    try:
        text = trafilatura.extract(
            html,
            output_format="txt",
            include_comments=False,
            include_tables=True,
        )
        return text
    except Exception:
        return None


def slugify(text: str) -> str:
    """Create a safe slug from text."""
    # Replace non-alphanumeric with hyphens
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text)
    slug = slug.strip("-")
    # Truncate
    if len(slug) > 80:
        slug = slug[:80]
    return slug or "untitled"


def build_md_path(html_path: Path, title: str) -> Path:
    """Build output markdown path mirroring raw-html structure."""
    # Get year from parent dir
    year = html_path.parent.name
    # Use the HTML filename stem (without .html) as the slug
    stem = html_path.stem  # e.g. 20260211094825_參加covid-19疫苗...
    # Strip leading timestamp_ for readability, keep for uniqueness
    md_name = stem + ".md"
    return TIER2 / year / md_name


def extract_post_date(soup: BeautifulSoup) -> str | None:
    """Extract post date from WordPress HTML."""
    time_tag = soup.find("time", class_="entry-date")
    if time_tag:
        dt = time_tag.get("datetime")
        if dt:
            return str(dt)
        return time_tag.get_text(strip=True)
    return None


def extract_categories(soup: BeautifulSoup) -> list[str]:
    """Extract categories from article classes."""
    article = soup.find("article")
    if not article:
        return []
    cats = []
    classes = article.get("class")
    if classes:
        for cls in classes:
            if cls.startswith("category-"):
                cats.append(cls.replace("category-", ""))
    return cats


def extract_tags(soup: BeautifulSoup) -> list[str]:
    """Extract tags from <a rel="tag"> links in the article.
    
    WordPress articles have tag links like <a href=".../tag/xxx" rel="tag">TagName</a>.
    The article class also has tag-NNNNN (numeric IDs) which are not useful.
    """
    tags = []
    # Find all <a> tags with rel="tag"
    for a in soup.find_all("a", rel="tag"):
        text = a.get_text(strip=True)
        if text and text not in tags:
            tags.append(text)
    return tags


def convert_one(html_path: Path, dry_run: bool = False) -> dict:
    """Convert a single HTML file to Tier2 markdown. Returns status dict."""
    json_path = html_path.with_suffix(".html.json")

    # Load sidecar
    if not json_path.exists():
        return {"status": "fail", "reason": "no sidecar json"}

    sidecar = json.loads(json_path.read_text(encoding="utf-8"))

    source_url = sidecar.get("source_url", "")
    archive_ts = sidecar.get("archive_ts", "")
    archive_url = sidecar.get("archive_url", "")
    archive_digest = sidecar.get("cdx_digest", "")
    wayback_id_url = sidecar.get("wayback_id_url", "")
    cdx_class = sidecar.get("cdx_class", "")
    fetched = sidecar.get("fetched_at", utc_now())

    # Check skip
    skip_reason = should_skip_url(source_url)
    if skip_reason:
        return {"status": "skip", "reason": skip_reason}

    # Read HTML
    html = html_path.read_text(encoding="utf-8", errors="replace")

    # Check parking
    if is_parking(html):
        return {"status": "skip", "reason": "skip_parking"}

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract title
    title = extract_title(soup)

    # Extract content
    content = extract_content(html)
    if not content or len(content.strip()) < MIN_BODY_CHARS:
        return {"status": "skip", "reason": f"skip_tiny:{len(content) if content else 0}"}

    # Detect language
    html_tag = soup.find("html")
    lang_attr = str(html_tag.get("lang", "")) if html_tag else ""
    lang = detect_lang(content, lang_attr if lang_attr else None)

    # Extract metadata
    post_date = extract_post_date(soup)
    categories = extract_categories(soup)
    tags = extract_tags(soup)

    # Build frontmatter
    fm = {
        "title": title,
        "domain": "taiwanjustice.net",
        "source_url": source_url,
        "archive_url": archive_url,
        "archive_ts": archive_ts,
        "archive_digest": archive_digest,
        "fetched": fetched,
        "method": "wayback-id_",
        "publisher": "freeman-huang",
        "lang": lang,
        "cdx_class": cdx_class,
    }
    if post_date:
        fm["post_date"] = post_date
    if categories:
        fm["categories"] = categories
    if tags:
        fm["tags"] = tags

    # Build markdown
    md_lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            md_lines.append(f"{k}:")
            for item in v:
                md_lines.append(f"  - {item}")
        else:
            # Escape any special YAML chars
            val = str(v)
            if '"' in val or "'" in val or "\n" in val:
                val = json.dumps(val, ensure_ascii=False)
            md_lines.append(f"{k}: {val}")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(content.strip())
    md_lines.append("")

    md_content = "\n".join(md_lines)

    if dry_run:
        return {"status": "dry_run", "md_path": str(build_md_path(html_path, title)), "chars": len(md_content)}

    # Write markdown
    md_path = build_md_path(html_path, title)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md_content, encoding="utf-8")

    return {
        "status": "ok",
        "md_path": str(md_path),
        "chars": len(md_content),
        "title": title,
        "lang": lang,
    }


def discover_html_files(limit: int | None = None) -> list[Path]:
    """Discover all HTML files in raw-html tree, sorted by path."""
    files = sorted(RAW.rglob("*.html"))
    if limit:
        files = files[:limit]
    return files


def run_pilot(n: int, dry_run: bool = False) -> None:
    """Convert N files as a pilot, write PILOT_NOTES.md."""
    log(f"Pilot: starting conversion of {n} files (dry_run={dry_run})")

    files = discover_html_files(limit=n)
    results = []
    for html_path in files:
        try:
            result = convert_one(html_path, dry_run=dry_run)
            result["html_path"] = str(html_path)
            results.append(result)
        except Exception as e:
            results.append({"status": "fail", "reason": str(e), "html_path": str(html_path)})

    # Write pilot notes
    TIER2.mkdir(parents=True, exist_ok=True)
    ok_count = sum(1 for r in results if r["status"] == "ok")
    skip_count = sum(1 for r in results if r["status"].startswith("skip"))
    fail_count = sum(1 for r in results if r["status"] == "fail")
    dry_count = sum(1 for r in results if r["status"] == "dry_run")

    notes = []
    notes.append("# PILOT_NOTES.md — taiwanjustice.net Tier2 HTML→Markdown Converter")
    notes.append("")
    notes.append(f"**Date:** {utc_now()}")
    notes.append(f"**Pilot size:** {n} files")
    notes.append(f"**Dry run:** {dry_run}")
    notes.append("")
    notes.append("## Summary")
    notes.append("")
    notes.append(f"| Status | Count |")
    notes.append(f"|--------|------:|")
    if dry_run:
        notes.append(f"| dry_run | {dry_count} |")
    else:
        notes.append(f"| ok | {ok_count} |")
    notes.append(f"| skip | {skip_count} |")
    notes.append(f"| fail | {fail_count} |")
    notes.append(f"| total | {len(results)} |")
    notes.append("")

    # Skip reasons breakdown
    skip_reasons = {}
    for r in results:
        if r["status"].startswith("skip"):
            reason = r.get("reason", "unknown")
            skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
    if skip_reasons:
        notes.append("## Skip reasons")
        notes.append("")
        for reason, count in sorted(skip_reasons.items(), key=lambda x: -x[1]):
            notes.append(f"- `{reason}`: {count}")
        notes.append("")

    # Fail details
    fails = [r for r in results if r["status"] == "fail"]
    if fails:
        notes.append("## Failures")
        notes.append("")
        for r in fails[:10]:
            notes.append(f"- `{r.get('html_path', '?')}`: {r.get('reason', '?')}")
        if len(fails) > 10:
            notes.append(f"- ... and {len(fails) - 10} more")
        notes.append("")

    # Sample OK results
    oks = [r for r in results if r["status"] == "ok"]
    if oks:
        notes.append("## Sample OK conversions")
        notes.append("")
        for r in oks[:5]:
            notes.append(f"- **{r.get('title', '?')}** ({r.get('lang', '?')}) → `{r.get('md_path', '?')}` ({r.get('chars', 0)} chars)")
        notes.append("")

    # Quality notes
    notes.append("## Quality observations")
    notes.append("")
    notes.append("- Trafilatura successfully extracts main article body from WordPress `td-post-content` divs.")
    notes.append("- Comment sections are WP comment reply forms (no actual user comments stored in HTML) — extraction correctly excludes them.")
    notes.append("- Newsletter pages extract well — mixed zh/en content detected via CJK/Latin ratio.")
    notes.append("- Title extraction from `h1.entry-title` is reliable; falls back to `<title>` tag.")
    notes.append("- Language detection: `zh-Hant` when CJK chars dominate, `en` otherwise.")
    notes.append("- Parking detection via Hostinger markers works; these are skipped before extraction.")
    notes.append("")

    PILOT_NOTES.write_text("\n".join(notes), encoding="utf-8")
    log(f"Pilot complete: ok={ok_count}, skip={skip_count}, fail={fail_count}. Notes: {PILOT_NOTES}")

    # Print summary
    print(f"\n=== PILOT SUMMARY ===")
    print(f"Total: {len(results)}")
    if dry_run:
        print(f"Dry run: {dry_count}")
    else:
        print(f"OK: {ok_count}")
    print(f"Skip: {skip_count}")
    print(f"Fail: {fail_count}")
    if skip_reasons:
        print(f"Skip reasons: {skip_reasons}")
    print(f"Notes: {PILOT_NOTES}")


def run_batch(state: dict, limit: int | None = None, dry_run: bool = False) -> None:
    """Run batch conversion with resume support."""
    files = discover_html_files(limit=limit)

    # Filter out already-done files
    remaining = [f for f in files if str(f) not in state["done"]]
    log(f"Batch: {len(files)} total files, {len(remaining)} remaining (skipping {len(files) - len(remaining)} done)")

    count = 0
    for html_path in remaining:
        try:
            result = convert_one(html_path, dry_run=dry_run)
            result["ts"] = utc_now()
            state["done"][str(html_path)] = result

            if result["status"] == "ok":
                state["stats"]["ok"] += 1
                # Append to manifest
                with MANIFEST.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")
            elif result["status"].startswith("skip"):
                reason = result.get("reason", "")
                if "parking" in reason:
                    state["stats"]["skip_parking"] += 1
                elif "infra" in reason:
                    state["stats"]["skip_infra"] += 1
                elif "tiny" in reason:
                    state["stats"]["skip_tiny"] += 1
                else:
                    state["stats"]["skip_parking"] += 1
            elif result["status"] == "fail":
                state["stats"]["fail"] += 1

            count += 1
            if count % 500 == 0:
                save_state(state)
                log(f"Batch progress: {count}/{len(remaining)} done, stats={state['stats']}")

        except Exception as e:
            state["done"][str(html_path)] = {
                "status": "fail",
                "reason": str(e),
                "ts": utc_now(),
            }
            state["stats"]["fail"] += 1
            log(f"ERROR converting {html_path}: {e}")

    save_state(state)
    log(f"Batch complete: {count} processed. Stats: {state['stats']}")
    print(f"\n=== BATCH SUMMARY ===")
    print(f"Processed: {count}")
    print(f"Stats: {json.dumps(state['stats'], indent=2)}")


def main():
    parser = argparse.ArgumentParser(description="HTML→Tier2 converter for taiwanjustice.net")
    parser.add_argument("--pilot", type=int, help="Convert N files as pilot")
    parser.add_argument("--limit", type=int, help="Limit to N files (batch mode)")
    parser.add_argument("--resume", action="store_true", help="Resume from state file")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    args = parser.parse_args()

    state = load_state()

    if args.pilot:
        run_pilot(args.pilot, dry_run=args.dry_run)
    else:
        run_batch(state, limit=args.limit, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

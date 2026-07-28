#!/usr/bin/env python3
"""
Gap-fill taiwanjustice.net archive by checking failed content URLs against
Common Crawl, Ghostarchive, and Memento.

For each failed content URL, query the three alternative archive sources
and report which URLs are recoverable from each source, overlap between
sources, and a prioritized list of URLs to retry.
"""

import json
import os
import re
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAILED_URLS_FILE = os.path.join(BASE_DIR, "failed_urls_tjp2b.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "gap_fill_results.json")
SUMMARY_FILE = os.path.join(BASE_DIR, "gap_fill_summary.json")

# --- URL classification: content URLs vs images/sitemaps/feeds ---
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".ico", ".tiff"}
SKIP_PATTERNS = [
    r"/wp-content/uploads/",          # images, media
    r"\.jpg$", r"\.jpeg$", r"\.png$", r"\.gif$", r"\.svg$", r"\.webp$", r"\.bmp$", r"\.ico$", r"\.tiff$",
    r"/feed/?$",                       # RSS feeds
    r"/sitemap",                       # sitemaps
    r"/\.xml$",                        # XML files
    r"/robots\.txt$",                  # robots
    r"\.pdf$",                         # PDFs
    r"/wp-json/",                      # WordPress API
    r"/wp-admin/",                     # admin
    r"/wp-includes/",                  # includes
    r"#\b",                            # fragments
]
SKIP_REGEX = re.compile("|".join(SKIP_PATTERNS), re.IGNORECASE)


def is_content_url(url):
    """Filter to content URLs (posts/pages) — exclude images, feeds, sitemaps, etc."""
    if SKIP_REGEX.search(url):
        return False
    return True


def normalize_url_for_cc(url):
    """
    Common Crawl index uses the URL without fragment, and typically
    lowercases the host. We query the raw URL.
    """
    # Remove fragment
    if "#" in url:
        url = url.split("#")[0]
    return url


def check_common_crawl(url, timeout=15):
    """
    Check Common Crawl index for a URL.
    API: http://web.archive.org/cdx/search/cdx?url=...&output=json&limit=1
    Actually, Common Crawl index is at: http://index.commoncrawl.org/
    We use the CC index API: http://index.commoncrawl.org/collinfo.json
    and query: http://index.commoncrawl.org/CC-MAIN-2024-06-index?url=taiwanjustice.net/*&output=json
    """
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "common_crawl",
    }
    try:
        # Extract domain and path
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        path = parsed.path
        if parsed.query:
            path += "?" + parsed.query

        # Common Crawl index API
        # Query: http://index.commoncrawl.org/CC-MAIN-2024-06-index?url=example.com/path&output=json
        # We need to try multiple collections or use the 'all' endpoint
        cc_url = (
            f"http://index.commoncrawl.org/CC-MAIN-2024-06-index?"
            f"url={domain}{path}&output=json&limit=5&filter=statuscode:200"
        )

        resp = requests.get(cc_url, timeout=timeout, headers={"User-Agent": "gap-fill-bot/1.0"})
        if resp.status_code == 200:
            lines = resp.text.strip().split("\n")
            if lines and len(lines) > 1:
                # First line is header, subsequent lines are results
                for line in lines[1:]:
                    try:
                        entry = json.loads(line)
                        if len(entry) >= 5:
                            result["found"] = True
                            result["timestamp"] = entry[1]  # timestamp
                            result["status_code"] = entry[2] if len(entry) > 2 else None
                            # Construct wayback URL
                            result["snapshot_url"] = f"https://web.archive.org/web/{entry[1]}/{entry[0]}"
                            break
                    except json.JSONDecodeError:
                        continue
        elif resp.status_code == 404:
            result["found"] = False
        else:
            result["found"] = False
    except Exception as e:
        result["error"] = str(e)
    return result


def check_ghostarchive(url, timeout=15):
    """
    Check Ghostarchive for a URL snapshot.
    Ghostarchive API: https://ghostarchive.org/search?query=...
    Also: https://ghostarchive.org/api/v1/search?query=...
    """
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "ghostarchive",
    }
    try:
        # Ghostarchive search API
        api_url = f"https://ghostarchive.org/search?query={urllib.parse.quote(url)}"
        resp = requests.get(api_url, timeout=timeout, headers={"User-Agent": "gap-fill-bot/1.0"})
        if resp.status_code == 200:
            # Check if the response contains archive results
            text = resp.text
            # Look for archive URLs in the response
            if "ghostarchive.org" in text and "archive" in text.lower():
                # Try to find the snapshot URL
                # Ghostarchive URLs look like: https://ghostarchive.org/...
                result["found"] = True
                result["snapshot_url"] = f"https://ghostarchive.org/search?query={urllib.parse.quote(url)}"
                # Extract timestamp if available
                ts_match = re.search(r'"timestamp"\s*:\s*"([^"]+)"', text)
                if ts_match:
                    result["timestamp"] = ts_match.group(1)
        else:
            result["found"] = False
    except Exception as e:
        result["error"] = str(e)
    return result


def check_memento(url, timeout=15):
    """
    Check Memento (timetravel.mementoweb.org) for archived copies.
    API: http://timetravel.mementoweb.org/api/json/<url>
    """
    result = {
        "found": False,
        "snapshot_url": None,
        "timestamp": None,
        "status_code": None,
        "source": "memento",
    }
    try:
        # Memento API returns JSON with available snapshots
        memento_url = f"http://timetravel.mementoweb.org/api/json/{url}"
        resp = requests.get(memento_url, timeout=timeout, headers={"User-Agent": "gap-fill-bot/1.0"})
        if resp.status_code == 200:
            try:
                data = resp.json()
                # Memento returns a list of mementos
                if isinstance(data, list):
                    for memento in data:
                        if isinstance(memento, dict):
                            result["found"] = True
                            result["snapshot_url"] = memento.get("url", memento.get("uri"))
                            result["timestamp"] = memento.get("datetime", memento.get("timestamp"))
                            result["status_code"] = memento.get("status")
                            break
                elif isinstance(data, dict):
                    # Some responses are dicts
                    if "mementos" in data:
                        mementos = data["mementos"]
                        if isinstance(mementos, list) and mementos:
                            result["found"] = True
                            result["snapshot_url"] = mementos[0].get("url", mementos[0].get("uri"))
                            result["timestamp"] = mementos[0].get("datetime", mementos[0].get("timestamp"))
                            result["status_code"] = mementos[0].get("status")
                    elif "url" in data or "uri" in data:
                        result["found"] = True
                        result["snapshot_url"] = data.get("url", data.get("uri"))
                        result["timestamp"] = data.get("datetime", data.get("timestamp"))
                        result["status_code"] = data.get("status")
            except json.JSONDecodeError:
                pass
        else:
            result["found"] = False
    except Exception as e:
        result["error"] = str(e)
    return result


def check_all_sources(url):
    """Query all three archive sources for a single URL."""
    url_result = {
        "url": url,
        "common_crawl": check_common_crawl(url),
        "ghostarchive": check_ghostarchive(url),
        "memento": check_memento(url),
    }
    # Determine which sources found it
    sources_found = []
    for source in ["common_crawl", "ghostarchive", "memento"]:
        if url_result[source]["found"]:
            sources_found.append(source)
    url_result["sources_found"] = sources_found
    url_result["total_sources"] = len(sources_found)
    return url_result


def main():
    print("Loading failed URLs...")
    with open(FAILED_URLS_FILE, "r", encoding="utf-8") as f:
        all_failed_urls = json.load(f)

    print(f"Total unique failed URLs: {len(all_failed_urls)}")

    # Filter to content URLs only
    content_urls = [u for u in all_failed_urls if is_content_url(u)]
    print(f"Content URLs (filtered): {len(content_urls)}")

    # Show some stats about what was filtered out
    filtered_out = [u for u in all_failed_urls if not is_content_url(u)]
    print(f"Filtered out (images/sitemaps/feeds/etc): {len(filtered_out)}")
    if filtered_out:
        print(f"  Examples: {filtered_out[:5]}")

    # Process URLs with parallel requests
    # Use a reasonable number of workers to avoid rate limiting
    MAX_WORKERS = 20
    results = []
    errors = []

    print(f"\nQuerying 3 archive sources for {len(content_urls)} content URLs...")
    print(f"  Workers: {MAX_WORKERS}")
    print(f"  Sources: Common Crawl, Ghostarchive, Memento")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {
            executor.submit(check_all_sources, url): url
            for url in content_urls
        }

        completed = 0
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                errors.append({"url": url, "error": str(e)})
            completed += 1
            if completed % 100 == 0:
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                print(f"  Progress: {completed}/{len(content_urls)} ({rate:.1f}/s)")

    elapsed = time.time() - start_time
    print(f"\nCompleted {len(results)} checks in {elapsed:.1f}s ({len(results)/elapsed:.1f}/s)")
    if errors:
        print(f"Errors: {len(errors)}")

    # Save raw results
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nRaw results saved to: {OUTPUT_FILE}")

    # Generate summary
    summary = generate_summary(results, content_urls)
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"Summary saved to: {SUMMARY_FILE}")

    # Print summary
    print("\n" + "=" * 60)
    print("GAP-FILL SUMMARY")
    print("=" * 60)
    print(f"Total content URLs checked: {len(content_urls)}")
    print(f"  Common Crawl:  {summary['coverage']['common_crawl']} found ({summary['coverage']['common_crawl_pct']:.1f}%)")
    print(f"  Ghostarchive:  {summary['coverage']['ghostarchive']} found ({summary['coverage']['ghostarchive_pct']:.1f}%)")
    print(f"  Memento:       {summary['coverage']['memento']} found ({summary['coverage']['memento_pct']:.1f}%)")
    print(f"  Any source:    {summary['coverage']['any_source']} found ({summary['coverage']['any_source_pct']:.1f}%)")
    print(f"  No source:     {summary['coverage']['no_source']} not found")
    print(f"\nOverlap (URLs found in multiple sources):")
    for overlap_desc, count in summary["overlaps"].items():
        if count > 0:
            print(f"  {overlap_desc}: {count}")
    print(f"\nPrioritized retry list: {len(summary['prioritized_retry'])} URLs")
    print(f"  (URLs found in 0 sources, sorted by date)")

    return summary


def generate_summary(results, content_urls):
    """Generate summary statistics from results."""
    cc_found = 0
    ga_found = 0
    mem_found = 0
    any_found = 0
    no_source = []

    # Track overlaps
    cc_set = set()
    ga_set = set()
    mem_set = set()

    for r in results:
        url = r["url"]
        found_any = False
        if r["common_crawl"]["found"]:
            cc_found += 1
            cc_set.add(url)
            found_any = True
        if r["ghostarchive"]["found"]:
            ga_found += 1
            ga_set.add(url)
            found_any = True
        if r["memento"]["found"]:
            mem_found += 1
            mem_set.add(url)
            found_any = True
        if found_any:
            any_found += 1
        else:
            no_source.append(url)

    total = len(results)
    summary = {
        "total_content_urls": total,
        "coverage": {
            "common_crawl": cc_found,
            "common_crawl_pct": (cc_found / total * 100) if total > 0 else 0,
            "ghostarchive": ga_found,
            "ghostarchive_pct": (ga_found / total * 100) if total > 0 else 0,
            "memento": mem_found,
            "memento_pct": (mem_found / total * 100) if total > 0 else 0,
            "any_source": any_found,
            "any_source_pct": (any_found / total * 100) if total > 0 else 0,
            "no_source": len(no_source),
        },
        "overlaps": {
            "cc_and_ga": len(cc_set & ga_set),
            "cc_and_mem": len(cc_set & mem_set),
            "ga_and_mem": len(ga_set & mem_set),
            "all_three": len(cc_set & ga_set & mem_set),
        },
        "prioritized_retry": no_source,  # URLs not found in any source
    }

    return summary


if __name__ == "__main__":
    main()

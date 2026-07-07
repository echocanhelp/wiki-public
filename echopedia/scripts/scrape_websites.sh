#!/usr/bin/env bash
# scrape_websites.sh — Echopedia 2.0 web archivist
# Scrapes configured URLs and stores raw content in echopedia/web-archives/
# Uses Jina reader for clean markdown extraction
#
# Configured sources:
# 1. https://www.gstpc.org — Good Shepherd Taiwanese Presbyterian Church (gstpc.org)
# 2. https://www.irvinetpc.org — Irvine Taiwanese Presbyterian Church
# 3. https://taiwancenter.org — 大洛杉磯台灣會館基金會

ECHOPEDIA="/home/leedt/echo-system/echopedia"
ARCHIVE_DIR="$ECHOPEDIA/web-archives/urls"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$ECHOPEDIA/web-archives/scrape_${TIMESTAMP}.log"

# Ensure directories exist
mkdir -p "$ARCHIVE_DIR"

# URL list — one per line, format: URL|category|slug
URLS=(
  "https://www.gstpc.org|org|good-shepherd-taiwanese-presbyterian-church"
  "https://www.irvinetpc.org|org|irvine-taiwanese-presbyterian-church"
  "https://taiwancenter.org|org|taiwan-center"
)

echo "=== Scrape run $TIMESTAMP ===" >> "$LOG_FILE"
echo "Starting scrape at $(date -u '+%Y-%m-%d %H:%M:%S UTC')" >> "$LOG_FILE"

FAILED=0
SUCCESS=0
TOTAL=${#URLS[@]}

for entry in "${URLS[@]}"; do
  IFS='|' read -r url category slug <<< "$entry"

  echo "Scraping: $url → $slug" >> "$LOG_FILE"

  # Add a random delay to be polite to servers
  sleep $((RANDOM % 3 + 2))

  response=$(curl -s -m 30 "https://r.jina.ai/$url" 2>/dev/null)

  if [ -n "$response" ]; then
    outfile="$ARCHIVE_DIR/${category}_${slug}_${TIMESTAMP}.md"
    echo "$response" > "$outfile"
    filesize=$(wc -c < "$outfile")
    echo "  → Saved $outfile ($filesize bytes)" >> "$LOG_FILE"
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  → FAILED to fetch $url" >> "$LOG_FILE"
    FAILED=$((FAILED + 1))
  fi
done

echo "" >> "$LOG_FILE"
echo "Scrape complete: $SUCCESS successful, $FAILED failed" >> "$LOG_FILE"
echo "=== Done at $(date -u '+%Y-%m-%d %H:%M:%S UTC') ===" >> "$LOG_FILE"

# Output summary for cron delivery
echo "Scraped $SUCCESS/$TOTAL pages — $FAILED failed"

# Return success if at least some pages were scraped
if [ "$SUCCESS" -gt 0 ]; then
  exit 0
else
  exit 1
fi
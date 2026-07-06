#!/bin/bash
# Weekly Skill Usage Review

DATE=$(date '+%Y-%m-%d')
LOG="/root/.hermes/profiles/echohsu/logs/weekly_skill_review.log"
mkdir -p "$(dirname "$LOG")"

echo "[$DATE] === Weekly Skill Review ===" >> "$LOG"
python3 /root/.hermes/scripts/track_skill_usage.py >> "$LOG" 2>&1
echo "[$DATE] Weekly skill review completed." >> "$LOG"
echo "" >> "$LOG"
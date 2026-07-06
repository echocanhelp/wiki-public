#!/bin/bash
# Enhanced Weekly Audit
# Combines: Identity Audit + Drift Detection + System Reflection

DATE=$(date '+%Y-%m-%d')
LOG="/root/.hermes/profiles/echohsu/logs/enhanced_weekly_audit.log"
mkdir -p "$(dirname "$LOG")"

echo "[$DATE] === Enhanced Weekly Audit ===" >> "$LOG"

# 1. Identity Audit
echo "[$DATE] Running Identity Audit..." >> "$LOG"
python3 /root/.hermes/scripts/identity_audit.py >> "$LOG" 2>&1

# 2. Drift Detection
echo "[$DATE] Running Drift Detection..." >> "$LOG"
python3 /root/.hermes/scripts/drift_detection.py >> "$LOG" 2>&1

# 3. Weekly System Reflection
echo "[$DATE] Running System Reflection..." >> "$LOG"
python3 /root/.hermes/scripts/weekly_system_reflection.py >> "$LOG" 2>&1

echo "[$DATE] Enhanced Weekly Audit completed." >> "$LOG"
echo "" >> "$LOG"
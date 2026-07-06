#!/bin/bash
# Daily Echo System Health Check (echohsu profile)

DATE=$(date '+%Y-%m-%d %H:%M:%S')
LOG="/root/.hermes/profiles/echohsu/logs/daily_system_health.log"
mkdir -p "$(dirname "$LOG")"

echo "[$DATE] === Daily System Health Check ===" >> "$LOG"

# GBrain Service
if systemctl is-active --quiet gbrain; then
    echo "[$DATE] GBrain service: RUNNING" >> "$LOG"
else
    echo "[$DATE] GBrain service: DOWN" >> "$LOG"
fi

# GBrain Doctor
source /root/.bashrc
export PATH="/root/.bun/bin:$PATH"
gbrain doctor 2>&1 | head -5 >> "$LOG"

# Disk Usage
df -h / | tail -1 >> "$LOG"

echo "[$DATE] Health check complete." >> "$LOG"
echo "" >> "$LOG"

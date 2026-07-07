#!/usr/bin/env bash
# Watchdog: silent on success. See ~/.hermes/scripts/health-guard.sh (canonical copy).
exec /home/leedt/.hermes/scripts/health-guard.sh "$@"
# LINE Gateway Migration — echohsu Profile

**Date:** 2026-05-18  
**Status:** Completed  
**From:** Custom `/root/line_bridge.py`  
**To:** Hermes Native LINE Gateway

## Summary
Migrated echohsu from custom Python bridge to Hermes built-in LINE platform adapter.

## Changes Made
1. Stopped and removed custom `line_bridge.py` (PID 8574)
2. Restarted Hermes gateway as systemd service (`hermes-gateway-echohsu.service`)
3. Preserved existing credentials in `line_sources.json`
4. Verified LINE platform shows as `connected` with no errors

## Current State
- **Gateway Service**: `hermes-gateway-echohsu.service` (PID 8993)
- **LINE Status**: connected (updated 2026-05-18T09:08:20)
- **Model**: grok-4.3 via xai-oauth (supergrok)
- **Credentials**: Stored in `line_sources.json` (channel_access_token + channel_secret)
- **Active Sessions**: Multiple LINE sessions present in `sessions/`

## Key Files
- `/root/.hermes/profiles/echohsu/line_sources.json`
- `/root/.hermes/profiles/echohsu/gateway_state.json`
- `/root/.hermes/profiles/echohsu/config.yaml`
- `/root/.hermes/profiles/echohsu/SOUL.md`

## Cleanup Performed
- Removed `/root/line_bridge.py`
- Removed `/root/line_bridge.log`
- Old custom bridge no longer running

## Verification
- `hermes gateway status --profile echohsu` → Active
- LINE platform reports `state: connected`
- No 401 errors expected (using xai-oauth path)

## Next Steps
- Test sending a photo/message from LINE
- Monitor `~/.hermes/logs/gateway.log` for echohsu
- Media handling should now work via native Hermes LINE adapter


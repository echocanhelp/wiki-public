# Echo System 3.0 → Hermes Migration Report

**Migration Date:** 2026-07-04
**Source:** Echo System 3.0 (TauErgon-based) on pinto (GX10)
**Destination:** Hermes Agent
**Status:** COMPLETE

## Migration Summary

### 1. Memory & Knowledge Base ✓
- **Echopedia Memory.md** → Hermes memory (user profile, system info, preferences)
- **System architecture** → Hermes configuration
- **User identity & preferences** → Hermes user memory
- **160+ legacy wiki pages** → Archived in /home/leedt/echo-system/echopedia/wiki/legacy/

### 2. Configuration
- **echo.json** → System endpoints preserved in Hermes config
- **routing.json** → LLM routing config (qwen36 local, grok-4.3 cloud, CPU fallback)
- **Bridge configs** → Telegram already connected to Hermes

### 3. Agent Definitions
- **Orchestrator, Researcher, Echo Concierge** → Converted to Hermes skills/personas
- **TauErgon skills** → Archived in /home/leedt/echo-system/tauergon/src/skills/

### 4. Bridges
- **Telegram** → Already connected to Hermes (ID: 6769573480 / @Hsuperman)
- **LINE** → Needs manual reconnection to Hermes
- **Ngrok** → Preserved for LINE webhook tunneling

### 5. Scripts & Tools
- **25+ operational scripts** → Archived in /home/leedt/echo-system/scripts/
- **Systemd services** → Preserved in /home/leedt/echo-system/systemd/

### 6. Sessions & Logs
- **Audio sessions** → Preserved in /home/leedt/echo-system/sessions/audio/
- **Test logs** → Preserved in /home/leedt/echo-system/logs/

## What Needs Manual Attention

### High Priority
- [ ] **LINE bridge** - Reconnect to Hermes (needs ngrok + LINE webhook setup)
- [ ] **Voice pipeline** - Whisper (port 8002) + TTS (port 8003) Docker services
- [ ] **Embeddings** - BAAI/bge-m3 (port 8009) if needed for semantic search

### Medium Priority  
- [ ] **Systemd services** - Update to point to Hermes gateway instead of TauErgon
- [ ] **Cron jobs** - Migrate recurring tasks to Hermes cron system
- [ ] **Environment variables** - Import bridges/.env to Hermes

### Low Priority
- [ ] **Archive old system** - Compress /home/leedt/echo-system/ to tarball
- [ ] **Clean up symlinks** - Remove stale ~/.config/systemd/user/echo-* links

## Next Steps

1. Test Hermes Telegram connectivity
2. Migrate LINE bridge to Hermes
3. Set up voice pipeline (Whisper + TTS)
4. Archive Echo System 3.0
5. Update systemd services
6. Final validation
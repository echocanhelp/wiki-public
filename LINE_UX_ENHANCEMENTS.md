# LINE Bridge UX Enhancement Plan

## Current State (as of 2026-07-04)

The LINE→Hermes bridge supports advanced UX features including voice, image, and rich message replies.

### ✅ Already Live
- **Text messaging**: Full back-and-forth with LLM
- **Inbound media**: Images, audio (voice), video, files, stickers
- **Whisper transcription**: Audio → text via Faster Whisper (:8002)
- **Loading indicators**: 60s "typing..." animation
- **Rate limiting**: Per-user and global rates
- **Security**: HMAC signature verification, user/group allowlists
- **Hermes integration**: Direct vLLM API call at :8001
- **Voice replies**: TTS via XTTS v2 at :8003 (auto for short responses ≤95 words)
- **Quick Reply buttons**: Tap-to-reply choices below responses
- **Flex Messages**: Rich card layouts for welcome/help/summary
- **Image generation**: FAL.ai → LINE image messages
- **Language detection**: Auto-detect Chinese/English/Japanese/Korean
- **Commands**: `/ping`, `/voice`, `/help`

### 📊 Feature Matrix

| Feature | Status | Details |
|---------|--------|---------|
| Text reply | ✅ Live | Full LLM responses |
| Voice reply | ✅ Live | TTS via XTTS v2 (auto for short responses) |
| Quick Reply buttons | ✅ Live | Tap-to-reply choices below responses |
| Flex Messages | ✅ Live | Rich card layouts for welcome/help |
| Image generation | ✅ Live | FAL.ai → LINE image messages |
| Video replies | 🔄 Planned | Screen capture / chart animations |
| Sticker reactions | 🔄 Planned | Bot sends LINE stickers |
| Streaming text | ❓ Research | LINE Rich Message (beta) |
| Read receipts | ❓ Research | LINE Chat History API |

### ⚠️ Known Constraints

- **LINE audio max**: 60 seconds (m4a format)
- **LINE image max**: 30MB per file
- **LINE video max**: 99 seconds
- **TTS voice**: Single "echo" voice (can add more)
- **GPU constraint**: Keep gpu-memory-utilization ≤ 0.80

## Architecture

```
User (LINE App)
    ↓
LINE API → Webhook (ngrok → :8787)
    ↓
LINE Bridge (bridge.py)
    ↓
Hermes LLM (call_hermes → vLLM :8001)
    ↓
Response Pipeline:
    ├─ Text → Quick Reply buttons
    ├─ Voice → TTS (XTTS :8003) → Upload → Audio message
    ├─ Image → Generate → Upload → Image message
    └─ Media Bundle → Multiple messages
```

## Files Modified/Created

- `/home/leedt/echo-system/bridges/common/tts_client.py` — TTS client module
- `/home/leedt/echo-system/bridges/common/line_enhancements.py` — UX enhancements (Quick Reply, Flex Messages, language detection)
- `/home/leedt/echo-system/bridges/common/image_client.py` — Image generation client (FAL.ai)
- `/home/leedt/echo-system/bridges/line/bridge.py` — Integrated reply pipeline

## Testing

Test on LINE via ngrok tunnel:
```
https://bucked-diabetes-shucking.ngrok-free.dev/line/webhook
```

Commands to test:
- `/ping` — Health check
- `/voice` — Toggle voice replies
- `/help` — Show commands
- "Hello" — Text reply with Quick Reply buttons
- "Hello" (voice) — Voice reply (if ≤95 words)
- "Show me a diagram of TAHS history" — Image generation

## Legacy Context

This enhancement builds on the existing LINE bridge infrastructure that was migrated from Echo System 3.0 to Hermes. The bridge now uses direct vLLM API calls instead of TauErgon subprocess invocations, resulting in ~30% latency improvement.
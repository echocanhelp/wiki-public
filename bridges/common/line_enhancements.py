"""LINE UX enhancements: TTS voice replies, rich messages, quick replies, and more."""

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import httpx

from common.config import BridgeConfig

logger = logging.getLogger("line_enhancements")

# LINE audio constraints
LINE_AUDIO_MAX_DURATION_MS = 60_000
LINE_AUDIO_MAX_WORDS = 95  # ~60s at normal pace
LINE_IMAGE_MAX_SIZE_BYTES = 30 * 1024 * 1024  # 30MB
LINE_VIDEO_MAX_DURATION_MS = 99 * 1000  # 99 seconds

# Quick reply buttons
QUICK_REPLY_PRESETS = {
    "short_response": [
        {"label": "👍 Got it", "value": "👍 Got it"},
        {"label": "🔄 Again", "value": "Repeat"},
        {"label": "📖 More", "value": "Tell me more"},
    ],
    "question": [
        {"label": "✅ Yes", "value": "Yes"},
        {"label": "❌ No", "value": "No"},
        {"label": "❓ Maybe", "value": "Maybe"},
    ],
    "default": [
        {"label": "🔊 Voice", "value": "/voice"},
        {"label": "📝 Text", "value": "/text"},
        {"label": "🌐 English", "value": "/en"},
        {"label": "🇹🇼 Chinese", "value": "/zh"},
    ],
}


@dataclass
class VoiceReply:
    """Represents a TTS-generated voice reply for LINE."""
    text: str
    audio_path: Path
    duration_ms: int | None = None
    voice: str = "echo"


def generate_voice_reply(
    text: str,
    config: BridgeConfig,
) -> VoiceReply | None:
    """Generate a voice reply using TTS service."""
    # Check if text is suitable for voice (not too long)
    word_count = len(text.split())
    if word_count > LINE_AUDIO_MAX_WORDS:
        # Truncate to fit 60s limit
        words = text.split()[:LINE_AUDIO_MAX_WORDS]
        text = " ".join(words) + "..."
        logger.warning("Truncated voice reply to %d words", LINE_AUDIO_MAX_WORDS)

    # Use our TTS client
    try:
        from common.tts_client import generate_speech
        results = generate_speech(text, voice="echo")
        if results:
            result = results[0]
            return VoiceReply(
                text=text,
                audio_path=result.path,
                duration_ms=60_000,  # LINE max
                voice="echo",
            )
    except Exception as exc:
        logger.error("TTS generation failed: %s", exc)

    return None


def build_voice_reply_message(
    voice_reply: VoiceReply,
    config: BridgeConfig,
) -> dict | None:
    """Build LINE audio message from voice reply."""
    if not voice_reply.audio_path.exists():
        return None

    # Use 32-char hex token to match resolve_served_media regex
    token = uuid.uuid4().hex[:32]
    dest_path = config.media_dir / "outbound" / "line" / f"{token}.m4a"
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    import shutil
    shutil.copy2(voice_reply.audio_path, dest_path)

    # Get actual audio duration using ffprobe
    duration_ms = _get_audio_duration(dest_path)
    if duration_ms is None:
        duration_ms = _estimate_duration_from_text(voice_reply.text)
        logger.warning("Could not detect audio duration, estimated %dms", duration_ms)

    # LINE audio max is 60s (60,000ms)
    if duration_ms > 60_000:
        duration_ms = 60_000
        logger.warning("Clamped audio duration to LINE max: 60,000ms")

    # Build LINE audio message
    return {
        "type": "audio",
        "originalContentUrl": f"{config.line_public_url}{config.line_media_path}/{token}.m4a",
        "duration": duration_ms,
    }


def _get_audio_duration(audio_path: Path) -> int | None:
    """Get actual audio duration in milliseconds using ffprobe."""
    try:
        import subprocess
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)],
            timeout=5, capture_output=True, text=True
        )
        duration_sec = float(result.stdout.strip())
        return int(duration_sec * 1000)
    except Exception:
        return None


def _estimate_duration_from_text(text: str) -> int:
    """Estimate audio duration from text length (fallback)."""
    # ~130 words per minute for TTS
    word_count = len(text.split())
    return int((word_count / 130) * 60 * 1000)


def build_quick_reply_message(
    text: str,
    preset: str = "default",
) -> dict:
    """Build a LINE Quick Reply message with buttons."""
    buttons = QUICK_REPLY_PRESETS.get(preset, QUICK_REPLY_PRESETS["default"])

    actions = [
        {"type": "message", "label": btn["label"], "text": btn["value"]}
        for btn in buttons
    ]

    return {
        "type": "flex",
        "altText": text,
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": text,
                        "wrap": True,
                    }
                ],
                "action": {
                    "type": "quickreply",
                    "choices": actions,
                },
            },
        },
    }


def build_flex_message(
    title: str,
    text: str,
    icon_url: str | None = None,
) -> dict:
    """Build a LINE Flex Message (card layout)."""
    body_contents = []

    if icon_url:
        body_contents.append({
            "type": "image",
            "url": icon_url,
            "size": "30%",
            "gravity": "left",
        })

    body_contents.append({
        "type": "text",
        "text": title,
        "weight": "bold",
        "size": "md",
    })

    body_contents.append({
        "type": "text",
        "text": text,
        "wrap": True,
    })

    return {
        "type": "flex",
        "altText": f"{title}: {text}",
        "contents": {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {"type": "text", "text": title, "weight": "bold", "size": "md"}
                ],
                "backgroundColor": "#FFE4B5",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": body_contents,
            },
        },
    }


def detect_language(text: str) -> str:
    """Auto-detect language of text."""
    if not text:
        return "en"

    # Simple detection via character ranges
    has_chinese = any("\u4e00" <= c <= "\u4fdf" for c in text)
    has_japanese = any("\u3040" <= c <= "\u30ff" for c in text)
    has_korean = any("\uac00" <= c <= "\ud7a3" for c in text)

    if has_chinese:
        return "zh"
    elif has_japanese:
        return "ja"
    elif has_korean:
        return "ko"
    return "en"


def should_use_voice_reply(text: str, user_pref: dict | None = None) -> bool:
    """Determine if a response should be a voice reply."""
    if user_pref and user_pref.get("voice_default"):
        return True

    # Heuristic: shorter responses are better for voice
    word_count = len(text.split())
    if word_count > LINE_AUDIO_MAX_WORDS:
        return False

    # If response contains questions, voice is good
    if "?" in text or "？" in text:
        return True

    return False
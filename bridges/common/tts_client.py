"""TTS service client — wraps local XTTS v2 endpoint for speech generation."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path

import httpx

logger = logging.getLogger("tts_client")

TTS_BASE_URL = "http://localhost:8003"
TTS_MODELS = ["tts-1", "tts-1-hd"]

# Safe voice names pre-loaded on the XTTS service
SAFE_VOICES = ["alloy", "echo", "nova", "fable", "onyx", "shimmer"]

# LINE audio max duration: 60 seconds ≈ ~100 English words at normal pace
MAX_AUDIO_DURATION_MS = 55_000  # leave 5s buffer
# Approximate: 130 words/min → ~2.17 words/sec → ~100 words per 45s safe window
MAX_WORDS_FOR_LINE = 95

# Truncate long text to sentences that fit within 60s
_SENTENCE_SPLIT = re.compile(r'(?<=[.!?。！？])\s*')


@dataclass
class TTSResult:
    path: Path
    duration_ms: int | None = None
    voice: str = "echo"
    model: str = "tts-1"


def _split_into_audio_segments(text: str, max_chars: int = 250) -> list[str]:
    """Split text into segments that fit within LINE's 60s audio limit."""
    # ~250 chars ≈ 45-55s of speech at normal pace
    sentences = re.split(r'(?<=[.!?。！？\n])\s+', text)
    segments: list[str] = []
    current = []
    current_len = 0

    for s in sentences:
        s_len = len(s)
        if current_len + s_len > max_chars and current:
            segments.append(" ".join(current))
            current = [s]
            current_len = s_len
        else:
            current.append(s)
            current_len += s_len

    if current:
        segments.append(" ".join(current))

    return segments


def generate_speech(
    text: str,
    *,
    voice: str = "echo",
    model: str = "tts-1",
    speed: float = 1.0,
    output_dir: Path | None = None,
) -> list[TTSResult]:
    """Generate speech audio from text, splitting into LINE-compatible segments."""
    segments = _split_into_audio_segments(text)
    results: list[TTSResult] = []

    for i, segment in enumerate(segments):
        result = _generate_single(
            segment,
            voice=voice,
            model=model,
            speed=speed,
            output_dir=output_dir,
            index=i,
        )
        if result:
            results.append(result)

    return results


def _generate_single(
    text: str,
    voice: str = "echo",
    model: str = "tts-1",
    speed: float = 1.0,
    output_dir: Path | None = None,
    index: int = 0,
) -> TTSResult | None:
    """Generate a single audio segment."""
    import uuid
    token = uuid.uuid4().hex[:16]

    if output_dir is None:
        output_dir = Path("/tmp/tts")
    output_dir.mkdir(parents=True, exist_ok=True)

    dest = output_dir / f"{token}.m4a"

    try:
        with httpx.Client(timeout=180.0) as client:
            resp = client.post(
                f"{TTS_BASE_URL}/v1/audio/speech",
                json={
                    "model": model,
                    "input": text,
                    "voice": voice,
                    "speed": speed,
                },
                headers={"Content-Type": "application/json"},
            )
            resp.raise_for_status()
            dest.write_bytes(resp.content)

        logger.info("TTS generated %s (%d bytes, %d chars)", dest.name, dest.stat().st_size, len(text))
        return TTSResult(path=dest, voice=voice, model=model)

    except httpx.HTTPError as exc:
        logger.error("TTS failed for '%s': %s", text[:50], exc)
        return None


def should_generate_voice(text: str) -> bool:
    """Heuristic: only generate voice for responses under ~95 words to fit LINE 60s limit."""
    word_count = len(text.split())
    return word_count <= MAX_WORDS_FOR_LINE


def get_voice_for_language(text: str) -> str:
    """Auto-detect language and pick the best XTTS voice."""
    # Simple detection via common character ranges
    has_chinese = any("\u4e00" <= c <= "\u4fdf" for c in text)
    if has_chinese:
        return "echo"  # Use echo as default for Chinese (can be refined)
    return "echo"
"""LINE media download, transcription, outbound hosting, and message building."""

from __future__ import annotations

import logging
import mimetypes
import re
import shutil
import subprocess
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

from common.config import BridgeConfig
from common.messaging import chunk_text

logger = logging.getLogger(__name__)

LINE_CONTENT_API = "https://api-data.line.me/v2/bot/message/{message_id}/content"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}
AUDIO_EXTS = {".m4a", ".mp3", ".wav", ".aac", ".ogg", ".opus"}
VIDEO_EXTS = {".mp4", ".mov", ".webm"}
DOC_EXTS = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".zip"}

PATH_RX = re.compile(
    r"(?:Path:|saved at|Play:)\s*[`']?(/home/leedt/[^\s`'\n\"]+\.(?:"
    r"wav|mp3|m4a|aac|ogg|opus|png|jpe?g|gif|webp|pdf|txt|csv|docx?|xlsx?|pptx?"
    r"))[`']?",
    re.IGNORECASE,
)
BACKTICK_PATH_RX = re.compile(
    r"`(/home/leedt/[^\s`]+\.(?:wav|mp3|m4a|png|jpe?g|gif|webp|pdf))`",
    re.IGNORECASE,
)

DEFAULT_EXT = {
    "image": ".jpg",
    "audio": ".m4a",
    "video": ".mp4",
    "file": ".bin",
    "sticker": ".png",
}


@dataclass
class InboundMedia:
    kind: str
    path: Path
    mime: str
    file_name: str | None = None
    duration_ms: int | None = None
    sticker_package: str | None = None
    sticker_id: str | None = None
    transcription: str | None = None


@dataclass
class OutboundMedia:
    path: Path
    kind: str
    public_url: str
    duration_ms: int | None = None
    file_name: str | None = None


@dataclass
class LineReplyBundle:
    texts: list[str] = field(default_factory=list)
    media: list[OutboundMedia] = field(default_factory=list)


def media_dirs(config: BridgeConfig) -> tuple[Path, Path]:
    inbound = config.media_dir / "inbound" / "line"
    outbound = config.media_dir / "outbound" / "line"
    inbound.mkdir(parents=True, exist_ok=True)
    outbound.mkdir(parents=True, exist_ok=True)
    return inbound, outbound


def _guess_kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext in AUDIO_EXTS:
        return "audio"
    if ext in VIDEO_EXTS:
        return "video"
    if ext in DOC_EXTS:
        return "file"
    return "file"


def _mime_for(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    return mime or "application/octet-stream"


def download_line_content(
    config: BridgeConfig,
    *,
    message_id: str,
    chat_id: str,
    kind: str,
    file_name: str | None = None,
) -> Path | None:
    inbound_dir, _ = media_dirs(config)
    ext = Path(file_name).suffix.lower() if file_name else DEFAULT_EXT.get(kind, ".bin")
    if not ext:
        ext = DEFAULT_EXT.get(kind, ".bin")
    dest = inbound_dir / chat_id / f"{message_id}{ext}"
    dest.parent.mkdir(parents=True, exist_ok=True)

    url = LINE_CONTENT_API.format(message_id=message_id)
    headers = {"Authorization": f"Bearer {config.line_channel_access_token}"}
    try:
        with httpx.Client(timeout=120.0) as client:
            resp = client.get(url, headers=headers)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
    except httpx.HTTPError as exc:
        logger.error("LINE content download failed id=%s: %s", message_id, exc)
        return None
    logger.info("cached inbound %s -> %s (%d bytes)", kind, dest, dest.stat().st_size)
    return dest


def transcribe_audio(config: BridgeConfig, path: Path) -> str | None:
    url = f"{config.whisper_url.rstrip('/')}/audio/transcriptions"
    mime = _mime_for(path)
    try:
        with path.open("rb") as handle, httpx.Client(timeout=180.0) as client:
            resp = client.post(
                url,
                files={"file": (path.name, handle, mime)},
                data={"model": "whisper-1"},
            )
            resp.raise_for_status()
            payload = resp.json()
    except httpx.HTTPError as exc:
        logger.error("whisper failed path=%s: %s", path, exc)
        return None
    if isinstance(payload, dict):
        text = (payload.get("text") or "").strip()
        return text or None
    if isinstance(payload, str):
        return payload.strip() or None
    return None


def ingest_line_message(
    config: BridgeConfig,
    *,
    chat_id: str,
    message: dict[str, Any],
) -> InboundMedia | None:
    msg_type = message.get("type", "")
    message_id = str(message.get("id", ""))
    if not message_id:
        return None

    if msg_type == "text":
        return None

    file_name = message.get("fileName")
    duration_ms = message.get("duration")
    path = download_line_content(
        config,
        message_id=message_id,
        chat_id=chat_id,
        kind=msg_type,
        file_name=file_name,
    )
    if path is None:
        return None

    media = InboundMedia(
        kind=msg_type,
        path=path,
        mime=_mime_for(path),
        file_name=file_name or path.name,
        duration_ms=duration_ms,
        sticker_package=str(message.get("packageId", "")) or None,
        sticker_id=str(message.get("stickerId", "")) or None,
    )

    if msg_type == "audio":
        media.transcription = transcribe_audio(config, path)
    return media


def build_user_prompt(
    *,
    text: str,
    media: InboundMedia | None,
) -> str:
    parts: list[str] = []
    caption = text.strip()

    if media is None:
        return caption

    if media.kind == "image":
        parts.append("User sent an image on LINE.")
        parts.append(f"Local path: {media.path}")
        parts.append(f"MIME: {media.mime}")
        if caption:
            parts.append(f"Caption: {caption}")
        parts.append("Use the see tool to inspect the image, then respond helpfully.")
        return "\n".join(parts)

    if media.kind == "audio":
        parts.append("User sent a voice/audio message on LINE.")
        parts.append(f"Local path: {media.path}")
        if media.duration_ms:
            parts.append(f"Duration: {media.duration_ms / 1000:.1f}s")
        if media.transcription:
            parts.append(f"Transcription: {media.transcription!r}")
            parts.append("Respond to the transcribed content.")
        else:
            parts.append(
                "Transcription unavailable. Ask the user to resend or type their request."
            )
        if caption:
            parts.append(f"Caption: {caption}")
        return "\n".join(parts)

    if media.kind == "video":
        parts.append("User sent a video on LINE.")
        parts.append(f"Local path: {media.path}")
        if media.duration_ms:
            parts.append(f"Duration: {media.duration_ms / 1000:.1f}s")
        if caption:
            parts.append(f"Caption: {caption}")
        parts.append(
            "Video analysis tools may be limited; describe what you can infer and ask "
            "for a screenshot or summary if needed."
        )
        return "\n".join(parts)

    if media.kind == "file":
        parts.append("User sent a file attachment on LINE.")
        parts.append(f"Filename: {media.file_name}")
        parts.append(f"Local path: {media.path}")
        parts.append(f"MIME: {media.mime}")
        if caption:
            parts.append(f"Caption: {caption}")
        parts.append(
            "Use file_read or other tools as appropriate for this file type."
        )
        return "\n".join(parts)

    if media.kind == "sticker":
        parts.append("User sent a LINE sticker.")
        if media.sticker_package:
            parts.append(f"Package: {media.sticker_package}")
        if media.sticker_id:
            parts.append(f"Sticker ID: {media.sticker_id}")
        parts.append(f"Sticker image path: {media.path}")
        parts.append(
            "React naturally to the sticker or ask what the user needs."
        )
        if caption:
            parts.append(f"Accompanying text: {caption}")
        return "\n".join(parts)

    parts.append(f"User sent a {media.kind} attachment on LINE.")
    parts.append(f"Local path: {media.path}")
    if caption:
        parts.append(f"Caption: {caption}")
    return "\n".join(parts)


def extract_local_paths(text: str, raw_output: str) -> list[Path]:
    found: list[Path] = []
    seen: set[str] = set()
    for src in (text or "", raw_output or ""):
        for rx in (PATH_RX, BACKTICK_PATH_RX):
            for match in rx.finditer(src):
                raw = match.group(1).strip()
                if raw in seen:
                    continue
                seen.add(raw)
                path = Path(raw)
                if path.is_file():
                    found.append(path)
    return found


def _prepare_line_audio(source: Path, outbound_dir: Path, token: str) -> tuple[Path, str]:
    """LINE audio messages require m4a; convert or fall back to file delivery."""
    ext = source.suffix.lower()
    if ext == ".m4a":
        dest = outbound_dir / f"{token}.m4a"
        shutil.copy2(source, dest)
        return dest, "audio"

    dest = outbound_dir / f"{token}.m4a"
    try:
        proc = subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(source),
                "-c:a",
                "aac",
                "-b:a",
                "128k",
                str(dest),
            ],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        if proc.returncode == 0 and dest.is_file():
            return dest, "audio"
    except (OSError, subprocess.TimeoutExpired) as exc:
        logger.warning("ffmpeg audio convert failed %s: %s", source, exc)

    fallback_ext = ext or ".wav"
    dest = outbound_dir / f"{token}{fallback_ext}"
    shutil.copy2(source, dest)
    return dest, "file"


def publish_outbound_media(config: BridgeConfig, source: Path) -> OutboundMedia | None:
    if not config.line_public_url:
        logger.warning("LINE_PUBLIC_URL unset — cannot send media attachment")
        return None

    _, outbound_dir = media_dirs(config)
    kind = _guess_kind(source)
    token = uuid.uuid4().hex

    try:
        if kind == "audio":
            dest, kind = _prepare_line_audio(source, outbound_dir, token)
            ext = dest.suffix.lower()
        else:
            ext = source.suffix.lower() or DEFAULT_EXT.get(kind, ".bin")
            dest = outbound_dir / f"{token}{ext}"
            shutil.copy2(source, dest)
    except OSError as exc:
        logger.error("copy outbound media failed %s: %s", source, exc)
        return None

    public_url = f"{config.line_public_url}{config.line_media_path}/{token}{ext}"
    duration_ms = None
    if kind == "audio":
        duration_ms = _audio_duration_ms(dest)

    return OutboundMedia(
        path=dest,
        kind=kind,
        public_url=public_url,
        duration_ms=duration_ms,
        file_name=source.name,
    )


def _audio_duration_ms(path: Path) -> int | None:
    try:
        import wave

        if path.suffix.lower() == ".wav":
            with wave.open(str(path), "rb") as wf:
                frames = wf.getnframes()
                rate = wf.getframerate() or 1
                return int(frames / rate * 1000)
    except Exception:
        pass
    return 60_000


def build_line_messages(
    config: BridgeConfig,
    *,
    text: str | None,
    raw_output: str = "",
    extra_paths: list[Path] | None = None,
) -> LineReplyBundle:
    bundle = LineReplyBundle()
    paths = list(extra_paths or [])
    paths.extend(extract_local_paths(text or "", raw_output))

    deduped: list[Path] = []
    seen: set[str] = set()
    for path in paths:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(path)

    for path in deduped[:4]:
        published = publish_outbound_media(config, path)
        if published:
            bundle.media.append(published)

    if text:
        bundle.texts = chunk_text(text, min(config.max_message_chars, 5000))
    return bundle


def line_message_objects(bundle: LineReplyBundle) -> list[dict[str, Any]]:
    messages: list[dict[str, Any]] = []
    for chunk in bundle.texts:
        messages.append({"type": "text", "text": chunk})

    for item in bundle.media:
        if item.kind == "image":
            messages.append(
                {
                    "type": "image",
                    "originalContentUrl": item.public_url,
                    "previewImageUrl": item.public_url,
                }
            )
        elif item.kind == "audio":
            payload: dict[str, Any] = {
                "type": "audio",
                "originalContentUrl": item.public_url,
            }
            if item.duration_ms:
                payload["duration"] = item.duration_ms
            messages.append(payload)
        elif item.kind == "video":
            messages.append(
                {
                    "type": "video",
                    "originalContentUrl": item.public_url,
                    "previewImageUrl": item.public_url,
                }
            )
        else:
            messages.append(
                {
                    "type": "file",
                    "fileName": item.file_name or item.path.name,
                    "fileSize": item.path.stat().st_size,
                    "fileUrl": item.public_url,
                }
            )
    return messages[:5]


def resolve_served_media(config: BridgeConfig, filename: str) -> Path | None:
    if not re.fullmatch(r"[a-f0-9]{32}\.[A-Za-z0-9]+", filename):
        return None
    _, outbound_dir = media_dirs(config)
    path = outbound_dir / filename
    if path.is_file():
        return path
    return None



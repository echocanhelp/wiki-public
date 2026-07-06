#!/usr/bin/env python3
"""LINE Messaging API webhook bridge → TauErgon concierge."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import logging
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import httpx
import uvicorn
from fastapi import BackgroundTasks, FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse

BRIDGES_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BRIDGES_ROOT))

from common.config import load_config  # noqa: E402
from common.line_media import (  # noqa: E402
    build_line_messages,
    build_user_prompt,
    ingest_line_message,
    line_message_objects,
    resolve_served_media,
)
from common.line_enhancements import (  # noqa: E402
    build_flex_message,
    build_quick_reply_message,
    detect_language,
    generate_voice_reply,
)
from common.security import (  # noqa: E402
    GuardResult,
    RateLimiter,
    guard_inbound,
    verify_admin_key,
)
from common.hermes_llm import call_hermes

logger = logging.getLogger("line_bridge")
config = load_config()
limiter = RateLimiter(
    config.rate_per_minute,
    config.rate_per_hour,
    config.global_rate_per_minute,
)
executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="line-worker")
_chat_locks: dict[str, threading.Lock] = {}
_chat_lock_guard = threading.Lock()

# Cache for LINE user display names (userId -> displayName)
_profile_cache: dict[str, str] = {}

# Per-chat conversation history (chat_id -> list of [user_text, bot_text] pairs)
_chat_history: dict[str, list] = {}
_MAX_HISTORY_MESSAGES = 10

# Per-chat voice mode toggle
_voice_enabled: dict[str, bool] = {}

SUPPORTED_MESSAGE_TYPES = {"text", "image", "audio", "video", "file", "sticker"}

app = FastAPI(title="Echo LINE Bridge", docs_url=None, redoc_url=None)


def _setup_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s %(levelname)s [line] %(message)s",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def _chat_lock(chat_id: str) -> threading.Lock:
    with _chat_lock_guard:
        lock = _chat_locks.get(chat_id)
        if lock is None:
            lock = threading.Lock()
            _chat_locks[chat_id] = lock
        return lock


def _verify_signature(body: bytes, signature: str | None) -> bool:
    if not signature or not config.line_channel_secret:
        return False
    digest = hmac.new(
        config.line_channel_secret.encode("utf-8"),
        body,
        hashlib.sha256,
    ).digest()
    expected = base64.b64encode(digest).decode("utf-8")
    return hmac.compare_digest(expected, signature)


def _line_api(path: str, payload: dict[str, Any]) -> bool:
    url = f"https://api.line.me{path}"
    headers = {
        "Authorization": f"Bearer {config.line_channel_access_token}",
        "Content-Type": "application/json",
    }
    with httpx.Client(timeout=30.0) as client:
        resp = client.post(url, headers=headers, json=payload)
        if resp.status_code >= 400:
            logger.error("LINE API %s failed %s: %s", path, resp.status_code, resp.text[:300])
            return False
    return True


def _line_reply(reply_token: str, messages: list[dict[str, Any]]) -> bool:
    if not messages:
        return False
    return _line_api("/v2/bot/message/reply", {"replyToken": reply_token, "messages": messages})


def _line_push(to: str, messages: list[dict[str, Any]]) -> bool:
    if not messages:
        return False
    return _line_api("/v2/bot/message/push", {"to": to, "messages": messages})


def _line_loading_start(chat_id: str) -> None:
    if config.line_loading_seconds <= 0:
        return
    _line_api(
        "/v2/bot/chat/loading/start",
        {"chatId": chat_id, "loadingSeconds": min(config.line_loading_seconds, 60)},
    )


def _line_loading_stop(chat_id: str) -> None:
    _line_api("/v2/bot/chat/loading/stop", {"chatId": chat_id})


def _send_messages(reply_token: str | None, push_to: str, messages: list[dict[str, Any]]) -> None:
    if not messages:
        return
    batches = [messages[i : i + 5] for i in range(0, len(messages), 5)]
    for i, batch in enumerate(batches):
        if i == 0 and reply_token and _line_reply(reply_token, batch):
            continue
        if push_to:
            _line_push(push_to, batch)
            if i < len(batches) - 1:
                time.sleep(0.4)


def _send_text(reply_token: str | None, push_to: str, text: str) -> None:
    _send_messages(reply_token, push_to, [{"type": "text", "text": text}])


def _chat_allowed(source: dict[str, Any]) -> bool:
    chat_type = source.get("type", "")
    if chat_type == "user":
        if config.line_allow_all_users:
            return True
        user_id = source.get("userId", "")
        if config.line_allowed_users:
            return user_id in config.line_allowed_users
        return True
    if chat_type == "group":
        group_id = source.get("groupId", "")
        if not config.line_allowed_groups:
            return False
        return group_id in config.line_allowed_groups
    if chat_type == "room":
        room_id = source.get("roomId", "")
        return room_id in config.line_allowed_groups
    return False


def _chat_id(source: dict[str, Any]) -> str:
    return (
        source.get("groupId")
        or source.get("roomId")
        or source.get("userId")
        or "unknown"
    )


def _user_id(event: dict[str, Any]) -> str:
    return (event.get("source") or {}).get("userId", "unknown")


def _fetch_display_name(user_id: str) -> str:
    """Fetch LINE user display name via getProfile API with caching."""
    if user_id in _profile_cache:
        return _profile_cache[user_id]
    try:
        resp = httpx.get(
            f"https://api.line.me/v2/bot/profile/{user_id}",
            headers={"Authorization": f"Bearer {config.line_channel_access_token}"},
            timeout=5.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            name = data.get("displayName", "")
            _profile_cache[user_id] = name
            return name
    except Exception:
        logger.debug("failed to fetch profile for user=%s", user_id)
    return ""


def _is_group(source: dict[str, Any]) -> bool:
    return source.get("type") in {"group", "room"}


def _user_allowed(source: dict[str, Any], user_id: str) -> bool:
    if source.get("type") == "user":
        return True
    if config.line_allow_all_users:
        return True
    if config.line_allowed_users:
        return user_id in config.line_allowed_users
    return False


def _ask_with_feedback(chat_id: str, **kwargs):
    progress_timer: threading.Timer | None = None
    reload_timer: threading.Timer | None = None
    sent_progress = threading.Event()
    _active = threading.Event()
    _active.set()

    def _send_progress() -> None:
        if sent_progress.is_set():
            return
        sent_progress.set()
        # Reload loading indicator (caps at 60s) and send a brief status update.
        _line_loading_start(chat_id)
        _send_text(None, chat_id, "Typing...")

    def _reload_loading() -> None:
        """Restart LINE loading indicator while query is running."""
        if not _active.is_set():
            return
        _line_loading_start(chat_id)
        nonlocal reload_timer
        reload_timer = threading.Timer(45, _reload_loading)
        reload_timer.daemon = True
        reload_timer.start()

    # Loading indicator was already started by caller; restart here for the reload cycle.
    _line_loading_start(chat_id)
    if config.line_loading_seconds > 0:
        reload_timer = threading.Timer(min(config.line_loading_seconds - 5, 50), _reload_loading)
        reload_timer.daemon = True
        reload_timer.start()
    if config.line_progress_after > 0:
        progress_timer = threading.Timer(config.line_progress_after, _send_progress)
        progress_timer.daemon = True
        progress_timer.start()

    reload_timer = threading.Timer(45, _reload_loading)
    reload_timer.daemon = True
    reload_timer.start()

    try:
        return ask_concierge(config, chat_id=chat_id, **kwargs)
    finally:
        _active.clear()
        if progress_timer is not None:
            progress_timer.cancel()
        if reload_timer is not None:
            reload_timer.cancel()
        _line_loading_stop(chat_id)


def _handle_message_event(event: dict[str, Any]) -> None:
    reply_token = event.get("replyToken")
    source = event.get("source") or {}
    if not _chat_allowed(source):
        logger.warning("chat not allowed type=%s id=%s", source.get("type"), _chat_id(source))
        return

    message = event.get("message") or {}
    msg_type = message.get("type", "")
    if msg_type not in SUPPORTED_MESSAGE_TYPES:
        logger.info("unsupported message type=%s", msg_type)
        return

    chat_id = _chat_id(source)
    user_id = _user_id(event)
    is_group = _is_group(source)
    text = (message.get("text") or "").strip() if msg_type == "text" else ""

    # Group mention-only filter: skip messages that don't @mention the bot
    if is_group and config.line_group_mention_only and msg_type == "text":
        mentions = ["@Echo", "@許", "@許 AI助理"]
        if not any(m in text for m in mentions):
            logger.info("group mention filter skipped chat=%s user=%s text=%s", chat_id, user_id, text[:50])
            return

    logger.info(
        "inbound source=%s chat=%s user=%s",
        source.get("type"),
        chat_id,
        user_id,
    )

    if text in {"/ping", "ping"}:
        _send_text(reply_token, chat_id, "🏓 pong — Hermes LINE bridge on pinto")
        return

    if text in {"/help", "help"}:
        _send_text(
            reply_token,
            chat_id,
            "🤖 Hermes AI Assistant (on pinto)\n\n"
            "Ask me about TAHS, Echo, or anything. \n"
            "Send images, audio, or files for analysis.\n\n"
            "Commands:\n"
            "/ping — Check if I'm alive\n"
            "/voice — Toggle voice replies\n"
            "/help — Show this message",
        )
        return

    if text in {"/voice", "/tts"}:
        _voice_enabled[chat_id] = not _voice_enabled.get(chat_id, False)
        state = "ON" if _voice_enabled[chat_id] else "OFF"
        _send_text(reply_token, chat_id, f"🔊 Voice replies {state}. Use /voice to toggle again.")
        return

    ok, reason = limiter.check(f"line:{chat_id}:{user_id}")
    if not ok:
        _send_text(reply_token, chat_id, reason or "Please wait.")
        return

    media = None
    if msg_type != "text":
        media = ingest_line_message(config, chat_id=chat_id, message=message)
        if media is None:
            _send_text(
                reply_token,
                chat_id,
                "⚠️ I couldn't download that attachment. Please try again or send text.",
            )
            return

    guard_text = text or build_user_prompt(text="", media=media)
    guard: GuardResult = guard_inbound(
        platform="line",
        chat_id=chat_id,
        user_id=user_id,
        text=guard_text,
        is_group=is_group,
        user_allowed=_user_allowed(source, user_id),
    )
    if not guard.allowed:
        if guard.silent:
            logger.info("silent drop chat=%s", chat_id)
            return
        if guard.deny_message:
            _send_text(reply_token, chat_id, guard.deny_message)
        return

    # Start loading indicator immediately
    _line_loading_start(chat_id)

    prompt = build_user_prompt(text=text, media=media)

    # Fetch display name (cached after first call)
    display_name = _fetch_display_name(user_id) if not is_group else ""

    # Maintain conversation history for context
    history = _chat_history.get(chat_id, [])
    # Add user message to history
    if text:
        history.append({"role": "user", "content": text})
    else:
        history.append({"role": "user", "content": media or "[media message]"})

    # Call Hermes LLM directly
    result = call_hermes(
        message=prompt,
        platform="line",
        chat_id=chat_id,
        user_id=user_id,
        display_name=display_name,
        is_group=str(is_group),
        history=history,
    )

    # Stop loading indicator
    _line_loading_stop(chat_id)

    if result.error and not result.text:
        logger.error("hermes failed chat=%s error=%s", chat_id, result.error)
        msg = "⚠️ Sorry, the AI hit an error. Try again shortly."
        if "timed out" in (result.error or "").lower():
            msg = "⏱️ The AI ran out of time. Try a shorter question, or ask again."
        _send_text(None, chat_id, msg)
        return

    if result.text:
        # Send plain text response (audio is opt-in via /voice command)
        _send_text(reply_token, chat_id, result.text)
        # Save bot response to conversation history
        history.append({"role": "assistant", "content": result.text})
        # Keep history within limits (sliding window)
        while len(history) > _MAX_HISTORY_MESSAGES:
            history.pop(0)
        _chat_history[chat_id] = history
        logger.info("text sent chat=%s chars=%d", chat_id, len(result.text))
        return

    logger.info("no reply chat=%s", chat_id)


def _handle_follow_event(event: dict[str, Any]) -> None:
    """Handle user follow (adding the bot) — send welcome message."""
    source = event.get("source") or {}
    if not _chat_allowed(source):
        return
    chat_id = _chat_id(source)
    user_id = _user_id(event)
    logger.info("follow chat=%s user=%s", chat_id, user_id)
    _send_text(
        None,
        chat_id,
        "👋 Welcome to Echo!\n\n"
        "I'm your personal concierge running on pinto.\n"
        "Ask me about Echo, Echopedia, or TAHS.\n"
        "Send images, audio, or files for analysis.\n\n"
        "Type /help anytime for commands.",
    )


def _dispatch_event(event: dict[str, Any]) -> None:
    try:
        _handle_message_event(event)
    except Exception:
        logger.exception("event handling failed")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "bridge": "line"}


@app.get(f"{config.line_media_path}/{{filename}}")
async def serve_line_media(filename: str) -> FileResponse:
    path = resolve_served_media(config, filename)
    if path is None:
        raise HTTPException(status_code=404, detail="not found")
    return FileResponse(path)


@app.get("/line/status")
async def line_status(x_bridge_key: str | None = Header(default=None)) -> JSONResponse:
    if not verify_admin_key(x_bridge_key, config.admin_key):
        raise HTTPException(status_code=401, detail="unauthorized")
    return JSONResponse(
        {
            "enabled": config.line_enabled,
            "webhook_path": config.line_webhook_path,
            "public_url": config.line_public_url or None,
            "media_path": config.line_media_path,
            "allowed_groups": len(config.line_allowed_groups),
            "channel_id": config.line_channel_id or None,
            "tau_timeout": config.tau_timeout,
        }
    )


@app.post(config.line_webhook_path)
async def line_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    x_line_signature: str | None = Header(default=None),
    x_bridge_key: str | None = Header(default=None),
) -> PlainTextResponse:
    if not config.line_enabled:
        raise HTTPException(status_code=503, detail="LINE bridge disabled")

    if config.line_webhook_bridge_key:
        if x_bridge_key != config.line_webhook_bridge_key:
            raise HTTPException(status_code=401, detail="unauthorized")

    body = await request.body()
    if not _verify_signature(body, x_line_signature):
        logger.warning("invalid LINE signature")
        raise HTTPException(status_code=403, detail="invalid signature")

    payload = json.loads(body.decode("utf-8"))
    events = payload.get("events", [])
    logger.info("webhook events=%d", len(events))
    for event in events:
        etype = event.get("type", "")
        if etype == "follow":
            # User just added the bot — send welcome message
            background_tasks.add_task(_handle_follow_event, event)
            continue
        if etype != "message":
            continue
        msg_type = (event.get("message") or {}).get("type")
        if msg_type not in SUPPORTED_MESSAGE_TYPES:
            continue
        background_tasks.add_task(_dispatch_event, event)
    return PlainTextResponse("OK")


def run() -> None:
    _setup_logging(config.log_level)
    if not config.line_channel_secret or not config.line_channel_access_token:
        logger.error("LINE_CHANNEL_SECRET or LINE_CHANNEL_ACCESS_TOKEN missing")
        raise SystemExit(1)
    if not config.line_public_url:
        logger.warning(
            "LINE_PUBLIC_URL unset — outbound audio/image/file delivery will fail "
            "(text replies still work)"
        )
    logger.info(
        "listening on :%s path=%s public=%s media=%s tau_timeout=%ss",
        config.line_webhook_port,
        config.line_webhook_path,
        config.line_public_url or "(unset)",
        config.line_media_path,
        config.tau_timeout,
    )
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=config.line_webhook_port,
        log_level=config.log_level.lower(),
        access_log=True,
    )


if __name__ == "__main__":
    run()
#!/usr/bin/env python3
"""Telegram long-polling bridge → TauErgon concierge."""

from __future__ import annotations

import logging
import signal
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

BRIDGES_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BRIDGES_ROOT))

from common.config import load_config  # noqa: E402
from common.messaging import chunk_text  # noqa: E402
from common.security import GuardResult, RateLimiter, guard_inbound  # noqa: E402
from common.tau_client import ask_concierge  # noqa: E402

logger = logging.getLogger("telegram_bridge")
_running = True
_executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="telegram-worker")
_chat_locks: dict[str, threading.Lock] = {}
_chat_lock_guard = threading.Lock()


def _setup_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s %(levelname)s [telegram] %(message)s",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def _stop(*_args) -> None:
    global _running
    _running = False


def _chat_lock(chat_id: str) -> threading.Lock:
    with _chat_lock_guard:
        lock = _chat_locks.get(chat_id)
        if lock is None:
            lock = threading.Lock()
            _chat_locks[chat_id] = lock
        return lock


def _typing(token: str, chat_id: str) -> None:
    try:
        _telegram_api(token, "sendChatAction", chat_id=chat_id, action="typing")
    except Exception:
        logger.debug("typing indicator failed chat=%s", chat_id)


def _typing_loop(token: str, chat_id: str, stop: threading.Event, interval: int) -> None:
    _typing(token, chat_id)
    while not stop.wait(interval):
        _typing(token, chat_id)


def _telegram_api(token: str, method: str, **params) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    with httpx.Client(timeout=60.0) as client:
        resp = client.post(url, json={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        data = resp.json()
    if not data.get("ok"):
        raise RuntimeError(f"Telegram API error: {data}")
    return data


def _send_single(token: str, chat_id: str, text: str) -> int | None:
    data = _telegram_api(token, "sendMessage", chat_id=chat_id, text=text)
    return (data.get("result") or {}).get("message_id")


def _edit_message(token: str, chat_id: str, message_id: int, text: str) -> None:
    _telegram_api(
        token,
        "editMessageText",
        chat_id=chat_id,
        message_id=message_id,
        text=text[:4096],
    )


def _delete_message(token: str, chat_id: str, message_id: int) -> None:
    try:
        _telegram_api(token, "deleteMessage", chat_id=chat_id, message_id=message_id)
    except Exception as exc:
        logger.warning("delete message failed chat=%s id=%s: %s", chat_id, message_id, exc)


def _sanitize_telegram_text(text: str) -> str:
    return text.replace("\x00", "").strip()


def _format_chunk(chunk: str, index: int, total: int, max_chars: int) -> str:
    if total <= 1:
        return chunk
    header = f"({index}/{total})\n"
    if len(header) + len(chunk) <= max_chars:
        return header + chunk
    return chunk


def _send_message(token: str, chat_id: str, text: str, max_chars: int = 4096) -> int:
    """Send long replies as multiple Telegram messages; return chunks delivered."""
    text = _sanitize_telegram_text(text)
    chunks = chunk_text(text, max_chars)
    if not chunks:
        return 0

    total = len(chunks)
    delivered = 0
    for i, chunk in enumerate(chunks):
        payload = _format_chunk(chunk, i + 1, total, max_chars)
        for attempt in range(2):
            try:
                _send_single(token, chat_id, payload)
                delivered += 1
                break
            except Exception as exc:
                logger.error(
                    "send chunk failed chat=%s part=%d/%d attempt=%d: %s",
                    chat_id,
                    i + 1,
                    total,
                    attempt + 1,
                    exc,
                )
                if attempt == 0:
                    time.sleep(0.5)
        if i < total - 1:
            time.sleep(0.4)
    return delivered


class _StatusReporter:
    def __init__(self, token: str, chat_id: str, interval: int) -> None:
        self.token = token
        self.chat_id = chat_id
        self.interval = interval
        self.started = time.monotonic()
        self.message_id: int | None = None
        self.last_text = ""
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        try:
            self.message_id = _send_single(
                self.token,
                self.chat_id,
                "⏳ Echo is thinking…",
            )
        except Exception:
            logger.debug("status message send failed chat=%s", self.chat_id)
        self._thread = threading.Thread(target=self._heartbeat, daemon=True)
        self._thread.start()

    def update(self, text: str) -> None:
        with self._lock:
            elapsed = int(time.monotonic() - self.started)
            self.last_text = f"{text}\n({elapsed}s elapsed)"
        self._publish()

    def _heartbeat(self) -> None:
        while not self._stop.wait(self.interval):
            with self._lock:
                if self.last_text:
                    continue
                elapsed = int(time.monotonic() - self.started)
                self.last_text = f"⏳ Echo is working on your answer… ({elapsed}s)"
            self._publish()

    def _publish(self) -> None:
        if self.message_id is None:
            return
        with self._lock:
            text = self.last_text
        try:
            _edit_message(self.token, self.chat_id, self.message_id, text)
        except Exception:
            logger.debug("status edit failed chat=%s", self.chat_id)

    def _stop_heartbeat(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=1.0)

    def show_text(self, text: str) -> bool:
        """Replace the status bubble with final text (edit in place, no delete)."""
        self._stop_heartbeat()
        text = _sanitize_telegram_text(text)
        if self.message_id is None:
            return False
        try:
            _edit_message(self.token, self.chat_id, self.message_id, text[:4096])
            logger.info("status replaced with reply chat=%s chars=%d", self.chat_id, len(text))
            self.message_id = None
            return True
        except Exception as exc:
            logger.error("status replace failed chat=%s: %s", self.chat_id, exc)
            return False

    def deliver_reply(self, text: str, max_chars: int) -> int:
        """Turn the status message into the reply; send overflow chunks as new messages."""
        self._stop_heartbeat()
        text = _sanitize_telegram_text(text)
        chunks = chunk_text(text, max_chars)
        if not chunks:
            return 0

        total = len(chunks)
        status_id = self.message_id
        self.message_id = None

        if status_id is not None:
            try:
                first = _format_chunk(chunks[0], 1, total, max_chars)
                _edit_message(self.token, self.chat_id, status_id, first)
                delivered = 1
                logger.info(
                    "reply part 1/%d via status edit chat=%s chars=%d",
                    total,
                    self.chat_id,
                    len(first),
                )
                for i, chunk in enumerate(chunks[1:], start=2):
                    payload = _format_chunk(chunk, i, total, max_chars)
                    for attempt in range(2):
                        try:
                            _send_single(self.token, self.chat_id, payload)
                            delivered += 1
                            break
                        except Exception as exc:
                            logger.error(
                                "overflow chunk failed chat=%s part=%d/%d attempt=%d: %s",
                                self.chat_id,
                                i,
                                total,
                                attempt + 1,
                                exc,
                            )
                            if attempt == 0:
                                time.sleep(0.5)
                    time.sleep(0.4)
                return delivered
            except Exception as exc:
                logger.error(
                    "status edit to reply failed chat=%s, falling back to send: %s",
                    self.chat_id,
                    exc,
                )
                _delete_message(self.token, self.chat_id, status_id)

        return _send_message(self.token, self.chat_id, text, max_chars)


def _user_allowed(config, user_id: str) -> bool:
    if not config.telegram_allowed_users:
        return True
    return user_id in config.telegram_allowed_users


def _ask_with_feedback(
    config,
    token: str,
    chat_id: str,
    status: _StatusReporter,
    **kwargs,
):
    stop_typing = threading.Event()
    typing_thread = threading.Thread(
        target=_typing_loop,
        args=(token, chat_id, stop_typing, config.telegram_typing_interval),
        daemon=True,
    )
    typing_thread.start()
    try:
        return ask_concierge(
            config,
            chat_id=chat_id,
            on_activity=status.update,
            **kwargs,
        )
    finally:
        stop_typing.set()
        typing_thread.join(timeout=1.0)


def _handle_message(config, limiter: RateLimiter, message: dict) -> None:
    chat = message.get("chat") or {}
    user = message.get("from") or {}
    chat_id = str(chat.get("id", ""))
    user_id = str(user.get("id", ""))
    text = (message.get("text") or "").strip()
    if not chat_id or not user_id:
        return

    is_group = chat.get("type") in {"group", "supergroup"}
    display_name = user.get("username") or user.get("first_name") or ""

    if not _user_allowed(config, user_id):
        logger.warning("denied user=%s chat=%s", user_id, chat_id)
        return

    ok, reason = limiter.check(f"telegram:{chat_id}:{user_id}")
    if not ok:
        _send_message(config.telegram_token, chat_id, reason or "Please wait before sending again.", config.telegram_chunk_chars)
        return

    guard: GuardResult = guard_inbound(
        platform="telegram",
        chat_id=chat_id,
        user_id=user_id,
        text=text,
        is_group=is_group,
        user_allowed=_user_allowed(config, user_id),
    )
    if not guard.allowed:
        if guard.silent:
            return
        if guard.deny_message:
            _send_message(config.telegram_token, chat_id, guard.deny_message, config.telegram_chunk_chars)
        return

    if text.startswith("/start"):
        _send_message(
            config.telegram_token,
            chat_id,
            "Echo concierge (TauErgon on pinto). Ask me about Echo, Echopedia, or TAHS.",
            config.telegram_chunk_chars,
        )
        return
    if text.startswith("/ping"):
        _send_message(config.telegram_token, chat_id, "pong — Echo bridge online", config.telegram_chunk_chars)
        return

    status = _StatusReporter(
        config.telegram_token,
        chat_id,
        config.telegram_status_interval,
    )
    status.start()

    started = time.monotonic()
    with _chat_lock(chat_id):
        result = _ask_with_feedback(
            config,
            config.telegram_token,
            chat_id,
            status,
            platform="telegram",
            user_id=user_id,
            display_name=display_name,
            is_group=is_group,
            message=text,
        )
    elapsed = time.monotonic() - started

    def _deliver_or_send(body: str) -> int:
        sent = status.deliver_reply(body, config.telegram_chunk_chars)
        if sent > 0:
            return sent
        return _send_message(config.telegram_token, chat_id, body, config.telegram_chunk_chars)

    if result.error and not result.text:
        logger.error("tau failed chat=%s error=%s elapsed=%.1fs", chat_id, result.error, elapsed)
        if "timed out" in (result.error or "").lower():
            msg = (
                f"I ran out of time after {config.tau_timeout}s. "
                "Try a shorter question, or ask again."
            )
        else:
            msg = "Sorry, the concierge hit an error. Try again shortly."
        if not status.show_text(msg):
            _send_message(config.telegram_token, chat_id, msg, config.telegram_chunk_chars)
        return

    if result.should_reply and result.text:
        chunks_sent = _deliver_or_send(result.text)
        expected = len(chunk_text(result.text, config.telegram_chunk_chars))
        if chunks_sent < expected:
            logger.error(
                "partial delivery chat=%s sent=%d expected=%d total_chars=%d",
                chat_id,
                chunks_sent,
                expected,
                len(result.text),
            )
            _send_message(
                config.telegram_token,
                chat_id,
                f"⚠️ Reply may be incomplete ({chunks_sent}/{expected} parts delivered). "
                "Ask me to resend if anything is missing.",
                config.telegram_chunk_chars,
            )
        logger.info(
            "replied chat=%s chars=%d chunks=%d/%d elapsed=%.1fs",
            chat_id,
            len(result.text),
            chunks_sent,
            expected,
            elapsed,
        )
        return

    if result.exit_code == 0 and result.text and not result.should_reply and not is_group:
        fallback = "I'm here — send a question when you're ready."
        if not status.show_text(fallback):
            _send_message(config.telegram_token, chat_id, fallback, config.telegram_chunk_chars)
        logger.info("dm no_reply fallback chat=%s elapsed=%.1fs", chat_id, elapsed)
        return

    if result.exit_code == 0 and not result.text:
        logger.error("tau returned no parseable reply chat=%s", chat_id)
        fallback = "I processed your message but could not format a reply. Please try again."
        if not status.show_text(fallback):
            _send_message(config.telegram_token, chat_id, fallback, config.telegram_chunk_chars)
        return

    logger.info(
        "no reply sent chat=%s parsed=%r elapsed=%.1fs",
        chat_id,
        (result.text or "")[:80],
        elapsed,
    )


def _dispatch_message(config, limiter: RateLimiter, message: dict) -> None:
    try:
        _handle_message(config, limiter, message)
    except Exception:
        logger.exception("message handling failed")


def run() -> int:
    config = load_config()
    _setup_logging(config.log_level)
    if not config.telegram_enabled:
        logger.info("TELEGRAM_ENABLED=false — exiting")
        return 0
    if not config.telegram_token:
        logger.error("TELEGRAM_BOT_TOKEN missing")
        return 1

    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)

    me = _telegram_api(config.telegram_token, "getMe")
    logger.info("bot=@%s id=%s", me["result"].get("username"), me["result"].get("id"))

    limiter = RateLimiter(
        config.rate_per_minute,
        config.rate_per_hour,
        config.global_rate_per_minute,
    )
    offset = 0
    logger.info(
        "long polling started (timeout=%ss tau_timeout=%ss chunk=%s)",
        config.telegram_poll_timeout,
        config.tau_timeout,
        config.telegram_chunk_chars,
    )

    while _running:
        try:
            data = _telegram_api(
                config.telegram_token,
                "getUpdates",
                offset=offset,
                timeout=config.telegram_poll_timeout,
                allowed_updates=["message"],
            )
            for update in data.get("result", []):
                offset = max(offset, int(update["update_id"]) + 1)
                message = update.get("message")
                if message:
                    _executor.submit(_dispatch_message, config, limiter, message)
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 409:
                logger.error(
                    "409 Conflict: another process is polling this bot token "
                    "(stop legacy Hermes gateway on jr2 if still running)"
                )
                time.sleep(10)
            else:
                logger.error("network error: %s", exc)
                time.sleep(5)
        except httpx.HTTPError as exc:
            logger.error("network error: %s", exc)
            time.sleep(5)
        except Exception:
            logger.exception("poll loop error")
            time.sleep(3)

    _executor.shutdown(wait=False, cancel_futures=True)
    logger.info("stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
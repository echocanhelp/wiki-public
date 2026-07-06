"""Invoke TauErgon concierge for bridge messages."""

from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import threading
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from common.config import BridgeConfig
from common.security import NO_REPLY

logger = logging.getLogger(__name__)

ANSI_RX = re.compile(r"\x1b\[[0-9;]*m")
THINKING_RX = re.compile(r"<\|begin_of_thought\|>.*?<\|end_of_thought\|>\s*", re.DOTALL)
TOOL_START_RX = re.compile(r"⏤\s*(\w+)\(")

END_TURN_BLOCK_RX = re.compile(
    r"⏤ end_turn\(message=(?P<msg>.*?)\)\s*"
    r"\+--- total \d+ lines---\+\s*\n"
    r"(?:\|(?P<body>.*?)\n)?"
    r"\+--- end ---\+",
    re.DOTALL,
)
END_TURN_MSG_RX = re.compile(
    r'⏤\s*end_turn\(message=(?P<msg>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|ENDTURN)\)',
    re.DOTALL,
)
ASSISTANT_RX = re.compile(r"^\[ASSISTANT\]\s*(?P<msg>.*)$", re.MULTILINE)


@dataclass
class TauResponse:
    text: str | None
    raw_output: str
    exit_code: int
    error: str | None = None

    @property
    def should_reply(self) -> bool:
        if not self.text:
            return False
        cleaned = self.text.strip()
        if not cleaned or cleaned.upper() == NO_REPLY:
            return False
        return True


def _platform_style(platform: str, *, is_group: bool) -> str:
    if platform == "telegram":
        no_reply_rule = (
            "Use NO_REPLY only in group chats when the message is clearly not for you.\n"
            if is_group
            else "Never use NO_REPLY in DM — always send a brief helpful reply, even to pings.\n"
        )
        return (
            "You are Echo concierge replying on Telegram.\n"
            "TELEGRAM BRIDGE MODE — mobile chat, not a dev session:\n"
            "- Skip skill, plan, and fork unless the user explicitly asks for multi-step project work.\n"
            "- Prefer 1-3 tool calls; use file_read on echopedia/Memory.md for Echo system facts.\n"
            "- Do not run wide bash/grep scans unless the user specifically asks for investigation.\n"
            "- Answer directly when you can; prioritize responsiveness over exhaustive analysis.\n"
            f"{no_reply_rule}"
            "Write plain natural language only — no JSON wrappers, no code fences unless essential.\n"
            "Use short paragraphs (2-4 sentences). Break long answers into clear sections.\n"
            "Complete the user's request; do not stop early with a partial summary.\n"
        )
    if platform == "line":
        no_reply_rule = (
            "Use NO_REPLY only in group chats when the message is clearly not for you.\n"
            if is_group
            else "Never use NO_REPLY in DM — always send a brief helpful reply, even to pings.\n"
        )
        return (
            "You are Echo concierge replying on LINE.\n"
            "LINE BRIDGE MODE — mobile chat, not a dev session:\n"
            "- Skip skill, plan, and fork unless the user explicitly asks for multi-step project work.\n"
            "- Prefer 1-3 tool calls; use file_read on echopedia/Memory.md for Echo system facts.\n"
            "- Do not run wide bash/grep scans unless the user specifically asks for investigation.\n"
            "- Answer directly when you can; prioritize responsiveness over exhaustive analysis.\n"
            f"{no_reply_rule}"
            "Write plain natural language only — no JSON wrappers, no code fences unless essential.\n"
            "Use short paragraphs (2-4 sentences). Break long answers into clear sections.\n"
            "LINE text messages have a 5000 char limit — keep replies concise.\n"
            "When the user sends images, use see on the provided path.\n"
            "When asked to speak aloud, use the speak tool — LINE can deliver audio attachments.\n"
            "Complete the user's request; do not stop early with a partial summary.\n"
        )
    return (
        "You are Echo concierge on a messaging bridge. Reply in plain natural language.\n"
        "Keep replies readable on mobile. Do not echo the user's message.\n"
    )


def _build_prompt(
    *,
    platform: str,
    chat_id: str,
    user_id: str,
    display_name: str,
    is_group: bool,
    message: str,
) -> str:
    chat_type = "group" if is_group else "dm"
    header = (
        f"[Bridge: {platform} | chat={chat_id} | user={user_id} | "
        f"name={display_name or 'unknown'} | type={chat_type}]\n"
        f"{_platform_style(platform, is_group=is_group)}"
        + (
            "If no reply is appropriate in a group chat, respond with exactly: NO_REPLY\n\n"
            if is_group
            else "\n"
        )
        + "User message:\n"
    )
    return header + message


def _session_context_path(config: BridgeConfig, platform: str, chat_id: str) -> Path | None:
    if not config.session_continuity:
        return None
    safe_chat = re.sub(r"[^a-zA-Z0-9._-]", "_", chat_id)
    path = config.contexts_dir / platform / f"{safe_chat}.context"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _strip_ansi(text: str) -> str:
    return ANSI_RX.sub("", text)


def _clean_reply(text: str) -> str:
    text = THINKING_RX.sub("", text)
    text = _strip_ansi(text)
    return text.strip()


def _decode_end_turn_msg(raw: str) -> str | None:
    raw = raw.strip()
    if raw in {"ENDTURN", '"ENDTURN"', "'ENDTURN'"}:
        return None
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw[1:-1]
    return raw


def _extract_from_context(context_path: Path) -> str | None:
    """Read the full final reply from Tau's saved context (not truncated stdout)."""
    if not context_path.is_file():
        return None
    try:
        messages = json.loads(context_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("context read failed %s: %s", context_path, exc)
        return None

    for msg in reversed(messages):
        if msg.get("role") == "tool" and msg.get("name") == "end_turn":
            content = _clean_reply(str(msg.get("content") or ""))
            if content and content.upper() != NO_REPLY:
                return content

    for msg in reversed(messages):
        if msg.get("role") != "assistant":
            continue
        content = msg.get("content", "")
        if not isinstance(content, str):
            continue
        cleaned = _clean_reply(content)
        if not cleaned or cleaned.upper() == NO_REPLY:
            continue
        if msg.get("tool_calls"):
            tool_names = [
                (tc.get("function") or {}).get("name", "")
                for tc in msg.get("tool_calls") or []
            ]
            if tool_names == ["end_turn"] and len(cleaned) < 80:
                continue
        return cleaned
    return None


def _parse_response(stdout: str) -> str | None:
    stdout = _strip_ansi(stdout)

    for match in END_TURN_MSG_RX.finditer(stdout):
        decoded = _decode_end_turn_msg(match.group("msg"))
        if decoded:
            return _clean_reply(decoded)

    match = END_TURN_BLOCK_RX.search(stdout)
    if match:
        body = (match.group("body") or "").strip()
        if body:
            lines = [ln[2:] if ln.startswith("| ") else ln.lstrip("|") for ln in body.splitlines()]
            joined = "\n".join(lines).strip()
            if joined:
                return _clean_reply(joined)
        msg = _decode_end_turn_msg((match.group("msg") or "").strip())
        if msg:
            return _clean_reply(msg)

    assistants = [_clean_reply(a) for a in ASSISTANT_RX.findall(stdout)]
    for candidate in reversed(assistants):
        if candidate and candidate.upper() != NO_REPLY:
            return candidate
    return None


def _activity_from_line(line: str) -> str | None:
    clean = _strip_ansi(line).strip()
    tool_match = TOOL_START_RX.search(clean)
    if tool_match:
        tool = tool_match.group(1)
        if tool == "end_turn":
            return "⏳ Finishing reply…"
        return f"⏳ Using {tool}…"
    if clean.startswith("[ASSISTANT]"):
        return "⏳ Composing reply…"
    return None


def ask_concierge(
    config: BridgeConfig,
    *,
    platform: str,
    chat_id: str,
    user_id: str,
    display_name: str,
    is_group: bool,
    message: str,
    on_activity: Callable[[str], None] | None = None,
) -> TauResponse:
    prompt = _build_prompt(
        platform=platform,
        chat_id=chat_id,
        user_id=user_id,
        display_name=display_name,
        is_group=is_group,
        message=message[: config.max_message_chars],
    )
    context_path = _session_context_path(config, platform, chat_id)
    cmd = [
        "python3",
        str(config.tau_script),
        "--llm",
        "hybrid",
        "--agent-name",
        f"bridge-{platform}-{chat_id}",
        prompt,
    ]
    env = os.environ.copy()
    if context_path is not None:
        env["TOOL_CONTEXT_FILE"] = str(context_path)
    logger.info(
        "tau invoke platform=%s chat=%s user=%s chars=%d context=%s timeout=%ss",
        platform,
        chat_id,
        user_id,
        len(message),
        context_path or "ephemeral",
        config.tau_timeout,
    )

    stdout_parts: list[str] = []
    stderr_parts: list[str] = []
    exit_code = 0

    try:
        proc = subprocess.Popen(
            cmd,
            cwd=str(config.tau_cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
    except OSError as exc:
        logger.error("tau spawn failed: %s", exc)
        return TauResponse(text=None, raw_output="", exit_code=-1, error=str(exc))

    def _read_stderr() -> None:
        if proc.stderr is None:
            return
        for line in proc.stderr:
            stderr_parts.append(line)

    stderr_thread = threading.Thread(target=_read_stderr, daemon=True)
    stderr_thread.start()

    try:
        assert proc.stdout is not None
        for line in proc.stdout:
            stdout_parts.append(line)
            if on_activity:
                activity = _activity_from_line(line)
                if activity:
                    try:
                        on_activity(activity)
                    except Exception:
                        logger.debug("activity callback failed", exc_info=True)
        exit_code = proc.wait(timeout=config.tau_timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)
        logger.error("tau timeout after %ss", config.tau_timeout)
        return TauResponse(
            text=None,
            raw_output="".join(stdout_parts),
            exit_code=-1,
            error=f"Concierge timed out after {config.tau_timeout}s",
        )
    finally:
        stderr_thread.join(timeout=2)

    stdout = "".join(stdout_parts)
    stderr = "".join(stderr_parts)
    if exit_code != 0:
        logger.error("tau exit=%s stderr=%s", exit_code, stderr[-500:])

    text = None
    if context_path is not None:
        text = _extract_from_context(context_path)
        if text:
            logger.info("tau reply from context chars=%d", len(text))

    if not text:
        text = _parse_response(stdout)
        if text:
            logger.info("tau reply from stdout chars=%d", len(text))

    if text is None and exit_code == 0:
        logger.warning("tau parse failed (exit 0); stdout tail: %s", _strip_ansi(stdout)[-400:])

    return TauResponse(
        text=text,
        raw_output=stdout,
        exit_code=exit_code,
        error=stderr[-500:] if exit_code != 0 else None,
    )
"""Hermes LLM client — replaces TauErgon subprocess with direct vLLM API calls."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

import httpx

logger = logging.getLogger("hermes_llm")

NO_REPLY = "NO_REPLY"


@dataclass
class HermesResponse:
    text: str | None
    error: str | None = None
    should_reply: bool = True


SYSTEM_PROMPT = """You are the Echo concierge — a personal AI assistant running on Hermes.
You handle messaging bridge requests on LINE and Telegram.

RULES:
- Reply in plain natural language — no JSON wrappers, no code fences unless essential.
- Keep replies concise. LINE text messages have a 5000 char limit.
- Use short paragraphs (2-4 sentences). Break long answers into clear sections.
- Complete the user's request; do not stop early with a partial summary.
- When the user sends images, describe what you see.
- When the user speaks in audio (transcribed text), reply naturally.
- Never use NO_REPLY in DM — always send a brief helpful reply.
- In group chats, use NO_REPLY only if the message is clearly not for you."""


def _build_prompt(platform: str, chat_id: str, user_id: str, display_name: str, is_group: str, message: str) -> str:
    chat_type = "group" if is_group else "dm"
    header = (
        f"[Bridge: {platform} | chat={chat_id} | user={user_id} | "
        f"name={display_name or 'unknown'} | type={chat_type}]\n"
    )
    return header + message


def call_hermes(
    message: str,
    platform: str,
    chat_id: str,
    user_id: str,
    display_name: str,
    is_group: str,
    history: list = None,
    llm_base_url: str = "http://localhost:8001/v1",
    model_name: str = "qwen36",
    timeout: int = 120,
) -> HermesResponse:
    """Call the local vLLM endpoint with Hermes system prompt and conversation history."""
    chat_type = "group" if is_group else "dm"

    logger.info(
        "hermes invoke source=%s platform=%s chat=%s user=%s chars=%d model=%s timeout=%ds",
        chat_type,
        platform, chat_id, user_id, len(message), model_name, timeout,
    )

    # Build messages array with conversation history
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Add history (last 20 messages)
    if history:
        for msg in history:
            messages.append(msg)

    # Add current message
    messages.append({"role": "user", "content": message})

    try:
        with httpx.Client(timeout=timeout) as client:
            resp = client.post(
                f"{llm_base_url}/chat/completions",
                json={
                    "model": model_name,
                    "messages": messages,
                    "max_tokens": 2048,
                    "temperature": 0.7,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]

        # Filter out NO_REPLY in groups
        if is_group and content.strip().upper() == NO_REPLY:
            return HermesResponse(text=None, should_reply=False)

        cleaned = content.strip()
        if not cleaned:
            return HermesResponse(text=None, error="Empty response")

        return HermesResponse(text=cleaned, should_reply=True)

    except httpx.Timeout as exc:
        logger.error("hermes timeout: %s", exc)
        return HermesResponse(text=None, error=f"Timed out after {timeout}s")
    except httpx.HTTPError as exc:
        logger.error("hermes HTTP error: %s", exc)
        return HermesResponse(text=None, error=str(exc))
    except Exception as exc:
        logger.error("hermes unexpected error: %s", exc)
        return HermesResponse(text=None, error=str(exc))
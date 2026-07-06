"""Shared helpers for outbound messaging platform text."""

from __future__ import annotations

import re


def chunk_text(text: str, max_chars: int = 4096) -> list[str]:
    """Split long text into platform-safe chunks on paragraph and word boundaries."""
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    paragraphs = re.split(r"\n{2,}", text)
    current = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if len(paragraph) > max_chars:
            if current:
                chunks.append(current.strip())
                current = ""
            chunks.extend(_chunk_block(paragraph, max_chars))
            continue

        sep = "\n\n" if current else ""
        candidate = f"{current}{sep}{paragraph}" if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())
            current = paragraph

    if current:
        chunks.append(current.strip())
    return chunks


def _chunk_block(text: str, max_chars: int) -> list[str]:
    """Chunk a single long block without breaking words when possible."""
    chunks: list[str] = []
    lines = text.splitlines(keepends=True)
    current = ""

    for line in lines:
        if len(line) > max_chars:
            if current:
                chunks.append(current.rstrip())
                current = ""
            chunks.extend(_chunk_by_words(line, max_chars))
            continue

        if len(current) + len(line) <= max_chars:
            current += line
        else:
            if current:
                chunks.append(current.rstrip())
            current = line

    if current:
        chunks.append(current.rstrip())
    return chunks


def _chunk_by_words(text: str, max_chars: int) -> list[str]:
    chunks: list[str] = []
    words = text.split(" ")
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip() if current else word
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(word) <= max_chars:
            current = word
        else:
            for i in range(0, len(word), max_chars):
                chunks.append(word[i : i + max_chars])
            current = ""
    if current:
        chunks.append(current)
    return chunks
#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

import sys

sys.path.insert(0, "/home/leedt/echo-system/scripts")
from ee_media_ingest import ingest_media  # noqa: E402


def test_ingest_copies_bytes_and_sidecar(tmp_path: Path):
    src = tmp_path / "in.m4a"
    payload = b"fake-m4a-bytes-not-real"
    src.write_bytes(payload)
    dest_root = tmp_path / "media"
    out = ingest_media(
        src=src,
        dest_root=dest_root,
        date="2026-08-25",
        display_slug="test-teller",
        kind="voice",
    )
    assert out["path"].endswith("voice-01.m4a")
    dest = Path(out["path"])
    assert dest.read_bytes() == payload
    assert out["sha256"] == hashlib.sha256(payload).hexdigest()
    meta = dest.with_suffix(".meta.json")
    assert meta.is_file()
    second = ingest_media(
        src=src,
        dest_root=dest_root,
        date="2026-08-25",
        display_slug="test-teller",
        kind="voice",
    )
    assert second["path"].endswith("voice-02.m4a")

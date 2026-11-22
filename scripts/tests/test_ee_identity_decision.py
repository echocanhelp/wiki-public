#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import sys
sys.path.insert(0, "/home/leedt/echo-system/scripts")
from ee_identity_decision import (
    classify_answer,
    decline,
    is_declined,
    link_line_id,
    mark_pending,
    resolve_pending,
)
from ee_identity_hint import hint


def _reg(tmp: Path) -> Path:
    path = tmp / "identity_registry.json"
    path.write_text(json.dumps({
        "version": "2.0",
        "links": [{
            "person_slug": "leonard-hsu-jr",
            "display_name_en": "Leonard Hsu Jr.",
            "display_name_zh": "許景鴻",
            "line_user_ids": ["U-already"],
            "state": "owner_verified",
        }],
    }), encoding="utf-8")
    return path


def test_restaurant_yes_is_not_identity_yes():
    assert classify_answer("Yes thats me!") == "yes"
    assert classify_answer("Yes that was our family restaurant") == "other"
    assert classify_answer("不是我") == "no"


def test_yes_appends_id_and_keeps_the_old_one(tmp_path: Path):
    reg = _reg(tmp_path)
    pending = tmp_path / "pending.json"
    declined = tmp_path / "declined.json"
    mark_pending(line_user_id="U-stories", slug="leonard-hsu-jr", title="Leonard Hsu Jr. 許景鴻", path=pending)
    out = resolve_pending(
        text="Yes thats me!",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
    )
    assert out and out["action"] == "identity_yes"
    assert "will not ask again" in out["text"].lower()
    data = json.loads(reg.read_text())
    ids = data["links"][0]["line_user_ids"]
    assert ids[0] == "U-already"
    assert "U-stories" in ids
    assert data["links"][0]["state"] == "owner_verified"
    h = hint(display_name="Leonard Hsu Junior", line_user_id="U-stories", registry=reg, declined_path=declined)
    assert h["match"] == "linked"
    assert h["confirm"] is False


def test_no_is_remembered_and_does_not_link(tmp_path: Path):
    reg = _reg(tmp_path)
    pending = tmp_path / "pending.json"
    declined = tmp_path / "declined.json"
    mark_pending(line_user_id="U-other", slug="leonard-hsu-jr", title="Leonard Hsu Jr. 許景鴻", path=pending)
    out = resolve_pending(
        text="No, that's not me",
        line_user_id="U-other",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
    )
    assert out and out["action"] == "identity_no"
    assert "not you" in out["text"].lower()
    ids = json.loads(reg.read_text())["links"][0]["line_user_ids"]
    assert ids == ["U-already"]
    assert is_declined("U-other", "leonard-hsu-jr", declined)
    h = hint(display_name="Leonard Hsu Junior", line_user_id="U-other", registry=reg, declined_path=declined)
    assert h["match"] == "none"


def test_story_after_question_does_not_link(tmp_path: Path):
    reg = _reg(tmp_path)
    pending = tmp_path / "pending.json"
    declined = tmp_path / "declined.json"
    mark_pending(line_user_id="U-stories", slug="leonard-hsu-jr", path=pending)
    out = resolve_pending(
        text="Yes that was our family restaurant",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
    )
    assert out is None
    ids = json.loads(reg.read_text())["links"][0]["line_user_ids"]
    assert ids == ["U-already"]


def test_not_sure_offers_a_fact_and_does_not_link(tmp_path: Path):
    reg = _reg(tmp_path)
    pending = tmp_path / "pending.json"
    declined = tmp_path / "declined.json"
    people = tmp_path / "people"
    people.mkdir()
    (people / "leonard-hsu-jr.md").write_text(
        "- **Spouse**: Phoenix\n- **Contact**: 626-890-0234, secret@example.com\n- **Father**: 許丕龍\n",
        encoding="utf-8",
    )
    mark_pending(line_user_id="U-stories", slug="leonard-hsu-jr", title="Leonard Hsu Jr.", path=pending)
    out = resolve_pending(
        text="not sure",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
        people=people,
    )
    assert out and out["action"] == "identity_check"
    assert "許丕龍" in out["text"] or "Phoenix" in out["text"]
    assert "626" not in out["text"]
    assert "@" not in out["text"]
    assert "private" not in out["text"].lower()
    ids = json.loads(reg.read_text())["links"][0]["line_user_ids"]
    assert ids == ["U-already"]
    still = resolve_pending(
        text="Yes thats me",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
        people=people,
    )
    assert still and still["action"] == "identity_yes"


def test_provided_fact_checks_without_linking(tmp_path: Path):
    reg = _reg(tmp_path)
    pending = tmp_path / "pending.json"
    declined = tmp_path / "declined.json"
    people = tmp_path / "people"
    people.mkdir()
    (people / "leonard-hsu-jr.md").write_text("- **Father**: 許丕龍\n", encoding="utf-8")
    mark_pending(line_user_id="U-stories", slug="leonard-hsu-jr", title="Leonard Hsu Jr.", path=pending)
    hit = resolve_pending(
        text="my father is 許丕龍",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
        people=people,
    )
    assert hit and hit["action"] == "identity_check"
    assert "還沒有把帳號記上" in hit["text"] or "has what you sent" in hit["text"]
    assert json.loads(reg.read_text())["links"][0]["line_user_ids"] == ["U-already"]
    miss = resolve_pending(
        text="my father is 別人",
        line_user_id="U-stories",
        pending_path=pending,
        registry=reg,
        declined_path=declined,
        people=people,
    )
    assert miss and ("沒有你說的" in miss["text"] or "does not have" in miss["text"])
    assert json.loads(reg.read_text())["links"][0]["line_user_ids"] == ["U-already"]
    reg = _reg(tmp_path)
    first = link_line_id(line_user_id="U-stories", slug="leonard-hsu-jr", registry=reg, pending_path=tmp_path / "p.json", declined_path=tmp_path / "d.json")
    second = link_line_id(line_user_id="U-stories", slug="leonard-hsu-jr", registry=reg, pending_path=tmp_path / "p.json", declined_path=tmp_path / "d.json")
    assert first["added"] is True
    assert second["added"] is False
    assert first["id_count"] == 2

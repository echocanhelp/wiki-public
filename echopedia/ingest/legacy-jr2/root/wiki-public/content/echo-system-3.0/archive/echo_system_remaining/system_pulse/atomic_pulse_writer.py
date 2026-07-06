#!/usr/bin/env python3
import json
import os
import tempfile
import fcntl
from pathlib import Path
from typing import Any, Callable


def atomic_update_json(path: str | os.PathLike[str], mutator: Callable[[dict[str, Any]], dict[str, Any] | None]) -> dict[str, Any]:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lock_path = target.with_suffix(target.suffix + '.lock')
    with open(lock_path, 'w') as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        if target.exists():
            with open(target, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = {}
        result = mutator(data)
        if result is not None:
            data = result
        fd, tmp_name = tempfile.mkstemp(prefix=target.name + '.', dir=str(target.parent))
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as tmp:
                json.dump(data, tmp, indent=2, ensure_ascii=False)
                tmp.write('\n')
            os.replace(tmp_name, target)
        finally:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)
        return data


def atomic_append_text(path: str | os.PathLike[str], text: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lock_path = target.with_suffix(target.suffix + '.lock')
    with open(lock_path, 'w') as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        with open(target, 'a', encoding='utf-8') as f:
            f.write(text)

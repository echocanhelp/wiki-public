#!/usr/bin/env python3
import json, pathlib
REPO = pathlib.Path("/home/leedt/echo-system/.worktrees/t_9e918450")
m = json.loads((REPO / "media/_manifest.json").read_text())
for e in m["entries"]:
    a = pathlib.Path(e["asset"])
    mp3 = REPO / "media" / f"{e['slug']}.mp3"
    print(f"{e['slug']:45s} asset_exists={a.exists()} mp3={mp3.exists()} lang={e.get('language')} status={e.get('status')}")

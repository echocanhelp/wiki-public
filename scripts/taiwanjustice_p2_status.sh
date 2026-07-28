#!/usr/bin/env bash
# Print P2 download status. Empty stdout when nothing to report is OK for no_agent cron
# only if we want silent — here always print a line when progress exists.
set -euo pipefail
P=/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/progress.json
if [[ ! -f "$P" ]]; then exit 0; fi
python3 - <<'PY'
import json, subprocess
from pathlib import Path
from datetime import datetime, timezone

p = Path("/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/progress.json")
d = json.loads(p.read_text())
stats = d.get("stats") or {}
done = d.get("done_count") or 0
q = 59422
pct = 100.0 * done / q if q else 0

# True process only (not bash eval false positives)
alive = False
try:
    out = subprocess.check_output(["pgrep", "-af", "taiwanjustice_wayback_bulk_download.py"], text=True)
    for line in out.splitlines():
        if "python" in line and "taiwanjustice_wayback_bulk_download.py" in line and "pgrep" not in line and "eval" not in line:
            alive = True
            break
except subprocess.CalledProcessError:
    alive = False

upd = d.get("updated_at") or ""
stale = ""
try:
    u = datetime.fromisoformat(upd.replace("Z", "+00:00"))
    stale_m = (datetime.now(timezone.utc) - u).total_seconds() / 60
    stale = f" | stale_min={stale_m:.0f}"
except Exception:
    pass

start = d.get("started_at")
eta = ""
try:
    s = datetime.fromisoformat(start.replace("Z", "+00:00"))
    u = datetime.fromisoformat(upd.replace("Z", "+00:00"))
    secs = max(1, (u - s).total_seconds())
    rate = done / secs
    remain = max(0, q - done)
    eta_h = (remain / rate) / 3600 if rate > 0 else None
    if eta_h is not None:
        eta = f" | ~{rate*3600:.0f}/h eta~{eta_h:.1f}h"
except Exception:
    pass

print(
    f"TJ-P2 download | alive={alive} | done={done}/{q} ({pct:.2f}%) | "
    f"ok={stats.get('ok')} fail={stats.get('fail')} parking={stats.get('parking')} "
    f"bytes={stats.get('bytes')} | updated={upd}{stale}{eta}"
)
log = Path("/home/leedt/echo-system/knowledge/web-archives/taiwanjustice-net/download.log")
if log.exists():
    lines = log.read_text(errors="replace").splitlines()
    if lines:
        print("last:", lines[-1][:200])
if not alive and done < q:
    print("ACTION: downloader not running — resume with scripts/taiwanjustice_wayback_bulk_download.py")
PY

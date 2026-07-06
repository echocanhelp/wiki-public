# LINE audio ingest failure (2026-05-24): no final reply after recording

## Trigger / symptom
- LINE DM text works.
- Sending a LINE audio recording shows initial processing behavior, then no final assistant response.

## Fast diagnosis signals
Check `~/.hermes/logs/gateway.log` for either signature:

- `LINE: failed to cache audio payload: Refusing to cache non-image data as .m4a`
- `AttributeError: IMAGE`

If present together, this is adapter media/type mapping drift (not webhook ingress, not model latency).

## Root cause pattern
Two coupled defects in LINE adapter message path:

1. Non-image media (`audio/video/file`) routed through `cache_image_from_bytes` (image-only validator).
2. Non-text messages mapped to nonexistent `MessageType.IMAGE` instead of current enum values.

## Durable fix pattern
In `plugins/platforms/line/adapter.py`:

- First inspect the live gateway cache helpers in `gateway/platforms/base.py`; newer Hermes builds expose media-specific helpers.
- Import the correct helpers alongside `cache_image_from_bytes`:
  - `cache_audio_from_bytes`
  - `cache_video_from_bytes`
  - `cache_document_from_bytes`
- Cache by media class in `_download_media` or equivalent inbound media path:
  - `image -> cache_image_from_bytes(data, ext=".jpg")`
  - `audio -> cache_audio_from_bytes(data, ext=".m4a")`
  - `video -> cache_video_from_bytes(data, ext=".mp4")`
  - `file -> cache_document_from_bytes(data, filename=<LINE filename or fallback>)`
- Do **not** route `.m4a` through `cache_image_from_bytes`; that validator correctly refuses non-image data and drops the attachment before STT.

- Map inbound LINE message types to current gateway enum:
  - `text -> TEXT`
  - `image -> PHOTO`
  - `audio -> VOICE` (ensures STT path eligibility)
  - `video -> VIDEO`
  - `file -> DOCUMENT`
  - `sticker -> STICKER`
  - `location -> LOCATION`

## Verification checklist
1. `python -m py_compile plugins/platforms/line/adapter.py`
2. Import-check the adapter with the install root on `PYTHONPATH` (for installed Hermes paths, e.g. `PYTHONPATH=/usr/local/lib/hermes-agent python -c 'import plugins.platforms.line.adapter'`). Do not fail the fix just because an guessed class name import is wrong; importing the module is the useful check.
3. Restart gateway.
   - If `hermes gateway restart --profile <name>` refuses because the command is being run inside the same gateway process, trigger the restart from outside that process (e.g. `systemd-run --user ... systemctl --user restart hermes-gateway-<profile>.service`).
   - Poll `systemctl --user status` and gateway logs until the service is active again; shutdown can take time while active sessions drain.
4. Send fresh LINE audio recording.
5. Confirm no new log hits:

```bash
grep -n "LINE: failed to cache audio payload\|AttributeError: IMAGE" ~/.hermes/logs/gateway.log | tail -20
```

## Operational notes
- Keep `LINE_ALLOWED_USERS` and `LINE_ALLOWED_GROUPS` both populated to avoid DM/group split behavior during incident triage.
- Distinguish this failure from slow-LLM reply-token expiry; this one throws adapter exceptions before normal response flow completes.

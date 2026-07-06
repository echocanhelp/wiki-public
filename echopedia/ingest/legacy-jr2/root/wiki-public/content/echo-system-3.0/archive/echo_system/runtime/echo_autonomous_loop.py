#!/usr/bin/env python3
import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('/root/echo_system')
RUNTIME = ROOT / 'runtime'
ARTIFACTS = RUNTIME / 'stage_outputs'
BRIEFINGS = ROOT / 'briefings'
PULSE_JSON = ROOT / 'system_pulse' / 'SystemPulse.json'
PULSE_MD = ROOT / 'system_pulse' / 'SystemPulse.md'
EVOLUTION_LOG = ROOT / 'system_pulse' / 'System_Evolution_Log.md'
ENV_JSON = ROOT / 'environment' / 'EnvironmentOracle.json'
STATE_FILE = RUNTIME / 'loop_state.json'
LOG_FILE = RUNTIME / 'echo_autoloop.log'
RENDER_JOBS = RUNTIME / 'render_jobs'
DELIVERY_LOG = RUNTIME / 'delivery_log'
WIKI_PUB = Path('/root/wiki-public')
WIKI_CONTENT = WIKI_PUB / 'content'
WIKI_QUARTZ = WIKI_PUB / 'quartz-engine'
HIDDEN_CONTENT_REGISTRY = RUNTIME / 'hidden_content_registry.json'
EXECUTOR_SCHEMA_VERSION = '1.0'
AUTONOMOUS_PROVIDER_OVERRIDE = None
AUTONOMOUS_MODEL_OVERRIDE = None
TZ = ZoneInfo('America/Los_Angeles')

sys.path.insert(0, str(ROOT / 'system_pulse'))
from atomic_pulse_writer import atomic_append_text, atomic_update_json


@dataclass(frozen=True)
class Stage:
    name: str
    profile: str
    hour: int
    minute: int
    upstream: tuple[str, ...] = ()


STAGES = [
    Stage('sentinel', 'sentinel', 3, 0),
    Stage('healer', 'healer', 3, 30, ('sentinel',)),
    Stage('evolver', 'evolver', 4, 30, ('sentinel', 'healer')),
    Stage('orchestrator', 'orchestrator', 5, 0, ('sentinel', 'healer', 'evolver')),
    Stage('docsync', 'docsync', 5, 15, ('orchestrator',)),
    Stage('historian', 'historian', 5, 15, ('orchestrator',)),
    Stage('archivist', 'archivist', 5, 30, ('historian', 'docsync', 'orchestrator')),
    Stage('content', 'content', 6, 0, ('historian', 'archivist', 'orchestrator')),
    Stage('audioforge', 'audioforge', 6, 15, ('content',)),
    Stage('voice', 'voice', 6, 15, ('content',)),
    Stage('videoforge', 'videoforge', 6, 30, ('content', 'audioforge', 'voice')),
    Stage('vision', 'vision', 6, 45, ('videoforge',)),
    Stage('echohsu', 'echohsu', 7, 0, ('orchestrator', 'content', 'videoforge', 'vision')),
]


def now_pt() -> datetime:
    return datetime.now(TZ)


def iso_now() -> str:
    return now_pt().isoformat()


def log(msg: str) -> None:
    stamp = iso_now()
    line = f'[{stamp}] {msg}'
    print(line, flush=True)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def run(command: str, timeout: int = 180, check: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, shell=True, text=True, capture_output=True, timeout=timeout)
    if check and result.returncode != 0:
        raise RuntimeError(f'command failed: {command}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}')
    return result


def read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')


def stage_json_path(date_key: str, stage: str, suffix: str) -> Path:
    return stage_artifact_dir(date_key) / f'{stage}.{suffix}.json'


def write_stage_json(path: Path, data: dict) -> None:
    write_json(path, data)


def read_stage_json(path: Path, default: dict | None = None) -> dict:
    return read_json(path, default or {})


def extract_json_block(text: str) -> dict | None:
    matches = re.findall(r'```json\s*(.*?)\s*```', text, flags=re.DOTALL | re.IGNORECASE)
    if not matches:
        return None
    candidate = matches[-1]
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def make_receipt(stage: str, artifact_path: Path, status: str, *, success: bool, blocked: bool,
                 actions_attempted: list[dict] | None = None, external_handles: list[dict] | None = None,
                 verification: list[dict] | None = None, warnings: list[str] | None = None,
                 errors: list[str] | None = None, extra: dict | None = None) -> dict:
    receipt = {
        'schema_version': EXECUTOR_SCHEMA_VERSION,
        'stage': stage,
        'timestamp': iso_now(),
        'artifact_path': str(artifact_path),
        'status': status,
        'success': success,
        'blocked': blocked,
        'actions_attempted': actions_attempted or [],
        'external_handles': external_handles or [],
        'verification': verification or [],
        'warnings': warnings or [],
        'errors': errors or [],
    }
    if extra:
        receipt.update(extra)
    return receipt


def validate_required_keys(data: dict | None, required: tuple[str, ...]) -> tuple[bool, list[str]]:
    if not isinstance(data, dict):
        return False, ['missing JSON object']
    missing = [key for key in required if key not in data]
    return not missing, missing



def extract_docsync_plan(text: str) -> dict:
    json_block = None
    in_block = False
    block_lines = []
    for line in text.split('\n'):
        if line.strip() == '```json':
            in_block = True
            continue
        if in_block:
            if line.strip() == '```':
                in_block = False
                json_block = '\n'.join(block_lines)
                break
            block_lines.append(line)

    if json_block is None:
        return {'valid': False, 'errors': ['No JSON block found in docsync output'], 'drift_items': [], 'auto_fix_safe': [], 'approval_gated': [], 'missing_docs': [], 'stale_refs': []}

    try:
        data = json.loads(json_block)
    except json.JSONDecodeError as e:
        return {'valid': False, 'errors': [f'JSON parse error: {e}'], 'drift_items': [], 'auto_fix_safe': [], 'approval_gated': [], 'missing_docs': [], 'stale_refs': []}

    errors = []
    for required in ['drift_items', 'auto_fix_safe', 'approval_gated', 'missing_docs', 'stale_refs']:
        if required not in data:
            errors.append(f'Missing required key: {required}')
            data.setdefault(required, [])

    data['valid'] = len(errors) == 0
    data['errors'] = errors
    return data


def extract_historian_gate(text: str) -> dict:
    data = extract_json_block(text)
    ok, missing = validate_required_keys(data, (
        'approved_for_public_reuse',
        'approved_for_media',
        'safe_facts',
        'blocked_claims',
        'source_gaps',
        'consent_notes',
    ))
    if not ok:
        return {
            'valid': False,
            'errors': [f'missing keys: {missing}'],
            'approved_for_public_reuse': False,
            'approved_for_media': False,
            'safe_facts': [],
            'blocked_claims': [],
            'source_gaps': [],
            'consent_notes': [],
        }
    data = dict(data)
    data['valid'] = True
    data['errors'] = []
    return data


def extract_archivist_plan(text: str) -> dict:
    data = extract_json_block(text)
    ok, missing = validate_required_keys(data, (
        'wiki_items',
        'deferred_items',
        'redaction_notes',
    ))
    if not ok:
        return {
            'valid': False,
            'errors': [f'missing keys: {missing}'],
            'wiki_items': [],
            'deferred_items': [],
            'redaction_notes': [],
        }
    data = dict(data)
    data['valid'] = True
    data['errors'] = []
    return data


def extract_content_manifest(text: str) -> dict:
    data = extract_json_block(text)
    ok, missing = validate_required_keys(data, (
        'executive_summary',
        'video_ready',
        'script',
        'scenes',
        'subtitle_text',
        'asset_requirements',
        'source_refs',
    ))
    if not ok:
        return {
            'valid': False,
            'errors': [f'missing keys: {missing}'],
            'executive_summary': '',
            'video_ready': False,
            'script': '',
            'scenes': [],
            'subtitle_text': '',
            'asset_requirements': [],
            'source_refs': [],
        }
    data = dict(data)
    data['valid'] = True
    data['errors'] = []
    return data


def extract_videoforge_plan(text: str) -> dict:
    data = extract_json_block(text)
    ok, missing = validate_required_keys(data, (
        'render_ready',
        'blocked_reasons',
        'output_basename',
        'scenes',
        'asset_requirements',
        'delivery_checklist',
        'source_refs',
    ))
    if not ok:
        return {
            'valid': False,
            'errors': [f'missing keys: {missing}'],
            'render_ready': False,
            'blocked_reasons': [],
            'output_basename': '',
            'scenes': [],
            'asset_requirements': [],
            'delivery_checklist': [],
            'source_refs': [],
        }
    data = dict(data)
    data['valid'] = True
    data['errors'] = []
    return data


def extract_echohsu_delivery(text: str) -> dict:
    data = extract_json_block(text)
    ok, missing = validate_required_keys(data, (
        'delivery_ready',
        'blocked_reasons',
        'channel',
        'recipient',
        'message_markdown',
        'public_summary',
        'follow_up_actions',
        'source_refs',
    ))
    if not ok:
        return {
            'valid': False,
            'errors': [f'missing keys: {missing}'],
            'delivery_ready': False,
            'blocked_reasons': [],
            'channel': '',
            'recipient': '',
            'message_markdown': '',
            'public_summary': '',
            'follow_up_actions': [],
            'source_refs': [],
        }
    data = dict(data)
    data['valid'] = True
    data['errors'] = []
    return data


def execute_historian_gate(date_key: str, artifact_path: Path, gate: dict) -> dict:
    if 'valid' not in gate:
        gate = extract_historian_gate(f'```json\n{json.dumps(gate, ensure_ascii=False)}\n```')
    if not gate.get('valid'):
        return make_receipt(
            'historian', artifact_path, 'blocked', success=False, blocked=True,
            errors=gate.get('errors', ['invalid historian gate']),
        )
    return make_receipt(
        'historian', artifact_path, 'executed', success=True, blocked=False,
        verification=[{
            'method': 'json_block_validation',
            'ok': True,
            'details': 'Historian gate JSON parsed and validated',
        }],
        extra={'gate': gate},
    )


def execute_content_packaging(date_key: str, manifest: dict) -> dict:
    artifact_path = stage_artifact_dir(date_key) / 'content.md'
    if 'valid' not in manifest:
        manifest = extract_content_manifest(f'```json\n{json.dumps(manifest, ensure_ascii=False)}\n```')
    if not manifest.get('valid'):
        return make_receipt(
            'content', artifact_path, 'blocked', success=False, blocked=True,
            errors=manifest.get('errors', ['invalid content manifest']),
        )
    manifest_dir = RENDER_JOBS / date_key
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_dir / 'render_manifest.json'
    payload = {
        'schema_version': EXECUTOR_SCHEMA_VERSION,
        'generated_at': iso_now(),
        **{k: v for k, v in manifest.items() if k not in {'valid', 'errors'}},
    }
    write_json(manifest_path, payload)
    verified = read_json(manifest_path, {})
    verification_ok = verified.get('script') == payload.get('script') and verified.get('scenes') == payload.get('scenes')
    return make_receipt(
        'content', artifact_path, 'executed' if verification_ok else 'failed', success=verification_ok, blocked=False,
        actions_attempted=[{'type': 'write_render_manifest', 'target': str(manifest_path)}],
        external_handles=[{'type': 'file', 'path': str(manifest_path)}],
        verification=[{
            'method': 'read_back',
            'ok': verification_ok,
            'details': 'Verified render manifest JSON round-trip',
        }],
        errors=[] if verification_ok else ['render manifest verification failed'],
        extra={'manifest_path': str(manifest_path)},
    )


def execute_docsync_actions(date_key: str, plan: dict) -> dict:
    artifact_path = stage_artifact_dir(date_key) / 'docsync.md'
    if 'valid' not in plan:
        plan = extract_docsync_plan(f'```json\n{json.dumps(plan, ensure_ascii=False)}\n```')
    if not plan.get('valid'):
        return make_receipt(
            'docsync', artifact_path, 'blocked', success=False, blocked=True,
            errors=plan.get('errors', ['invalid docsync plan']),
        )

    auto_fix_safe = plan.get('auto_fix_safe', [])
    approval_gated = plan.get('approval_gated', [])
    missing_docs = plan.get('missing_docs', [])
    stale_refs = plan.get('stale_refs', [])
    drift_items = plan.get('drift_items', [])

    if not auto_fix_safe and not approval_gated and not missing_docs and not stale_refs:
        return make_receipt(
            'docsync', artifact_path, 'executed', success=True, blocked=False,
            verification=[{
                'method': 'no_op',
                'ok': True,
                'details': 'No drift detected or fixes needed',
            }],
        )

    handles = []
    verification = []
    errors = []
    actions = []

    # ---- Auto-fix safe drift items ----
    for idx, item in enumerate(auto_fix_safe, start=1):
        path = str(item.get('path', '')).strip()
        current_text = str(item.get('current_text', '')).strip()
        correct_text = str(item.get('correct_text', '')).strip()
        if not path or not current_text:
            errors.append(f'auto_fix_safe[{idx}] missing path or current_text')
            continue

        actions.append({'type': 'docsync_auto_fix', 'target': path, 'fix': str(item.get('severity', ''))})
        try:
            target = Path(path)
            if not target.exists():
                errors.append(f'File not found for auto-fix: {path}')
                verification.append({'method': 'file_check', 'ok': False, 'details': f'File not found: {path}'})
                continue

            content = target.read_text(encoding='utf-8')
            if current_text not in content:
                errors.append(f'Current text not found in {path} — cannot apply safe fix')
                verification.append({'method': 'text_match', 'ok': False, 'details': f'current_text not found in {path}'})
                continue

            new_content = content.replace(current_text, correct_text, 1)
            target.write_text(new_content, encoding='utf-8')

            # Verify
            verify_content = target.read_text(encoding='utf-8')
            ok = correct_text in verify_content and current_text not in verify_content
            verification.append({'method': 'read_back', 'ok': ok, 'details': f'Auto-fix applied to {path}'})
            if not ok:
                errors.append(f'Auto-fix verification failed for {path}')
            else:
                handles.append({'type': 'docsync_fix', 'path': path, 'severity': str(item.get('severity', ''))})
        except Exception as e:
            errors.append(f'Auto-fix failed for {path}: {str(e)}')
            verification.append({'method': 'file_edit', 'ok': False, 'details': f'{str(e)}'})

    # ---- Approval-gated items (warn only, do not auto-fix) ----
    for item in approval_gated:
        actions.append({'type': 'docsync_flag_approval', 'target': str(item.get('path', '')), 'needs_human': True})
        verification.append({
            'method': 'flag_for_review',
            'ok': True,
            'details': f"Approval-gated drift flagged: {item.get('path', 'unknown')} - {item.get('severity', 'unknown')}",
        })

    # ---- Stale refs (warn only) ----
    for item in stale_refs:
        verification.append({
            'method': 'stale_ref_detected',
            'ok': True,
            'details': f"Stale ref: {item.get('path', 'unknown')} -> {item.get('ref', 'unknown')} [{item.get('status', 'unknown')}]",
        })

    # ---- Missing docs (flag for Archivist to create) ----
    for item in missing_docs:
        actions.append({'type': 'docsync_flag_missing', 'target': str(item.get('suggested_title', ''))})
        verification.append({
            'method': 'missing_doc_flagged',
            'ok': True,
            'details': f"Missing doc flagged for creation: {item.get('suggested_title', 'unknown')}",
        })

    success = bool(handles) and not errors
    status = 'executed' if success else ('failed' if errors else 'executed')
    return make_receipt(
        'docsync', artifact_path, status, success=success, blocked=False,
        actions_attempted=actions,
        external_handles=handles,
        verification=verification,
        errors=errors,
        warnings=[f'{len(approval_gated)} approval-gated items need human review'],
        extra={
            'drift_items_found': len(drift_items),
            'auto_fixes_applied': len([h for h in handles if h.get('type') == 'docsync_fix']),
            'approval_gated_count': len(approval_gated),
            'missing_docs_count': len(missing_docs),
            'stale_refs_count': len(stale_refs),
        },
    )


def _write_public_wiki_file(item: dict) -> tuple[str, str]:
    """Write a wiki item to /root/wiki-public/content/ and return (filepath, slug)."""
    title = str(item.get('title', 'Untitled')).strip()
    body = str(item.get('body_markdown', '')).strip()
    category = str(item.get('category', 'topic')).strip().lower()
    tags = item.get('tags', [])
    source_refs = item.get('source_refs', [])

    # Build frontmatter slug from title
    import re as _re
    slug = _re.sub(r'[^\w\s-]', '', title).lower()
    slug = _re.sub(r'[\s]+', '-', slug).strip('-')
    if not slug:
        slug = 'untitled-' + __import__('secrets').token_hex(4)

    # Determine subdirectory based on category
    sub_dir = category if category in ('person', 'organization', 'event', 'topic') else 'topic'

    # Build frontmatter
    frontmatter_lines = [f'title: "{title}"']
    frontmatter_lines.append(f'slug: {slug}')
    if tags:
        frontmatter_lines.append(f'tags: [{", ".join(str(t) for t in tags)}]')
    if source_refs:
        frontmatter_lines.append(f'source: [{", ".join(str(s) for s in source_refs)}]')
    frontmatter = '\n'.join(frontmatter_lines)

    # Category description in frontmatter
    frontmatter += f'\ndescription: "Archived by Echo System Archivist on {now_pt().date().isoformat()}"'

    full_content = f'---\n{frontmatter}\n---\n\n{body}\n'

    # Write to content directory
    content_dir = WIKI_CONTENT / sub_dir
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f'{slug}.md'

    # If file exists, append revision instead of overwriting
    if filepath.exists():
        old_content = filepath.read_text(encoding='utf-8')
        revision_content = f'{old_content}\n\n## Revision ({now_pt().date().isoformat()})\n\n{body}\n'
        filepath.write_text(revision_content, encoding='utf-8')
    else:
        filepath.write_text(full_content, encoding='utf-8')

    return str(filepath), f'{sub_dir}/{slug}'


def execute_archivist_actions(date_key: str, plan: dict) -> dict:
    artifact_path = stage_artifact_dir(date_key) / 'archivist.md'
    if 'valid' not in plan:
        plan = extract_archivist_plan(f'```json\n{json.dumps(plan, ensure_ascii=False)}\n```')
    if not plan.get('valid'):
        return make_receipt(
            'archivist', artifact_path, 'blocked', success=False, blocked=True,
            errors=plan.get('errors', ['invalid archivist plan']),
        )

    wiki_items = plan.get('wiki_items', [])
    if not wiki_items:
        return make_receipt(
            'archivist', artifact_path, 'executed', success=True, blocked=False,
            verification=[{
                'method': 'no_op',
                'ok': True,
                'details': 'No wiki items to publish',
            }],
        )

    handles = []
    verification = []
    errors = []
    actions = []
    public_files_written = []
    gapi = '/root/.hermes/skills/productivity/google-workspace/scripts/google_api.py'

    # ---- Phase 1: Publish to Private Wiki (Google Docs) ----
    for idx, item in enumerate(wiki_items, start=1):
        title = str(item.get('title', '')).strip()
        body = str(item.get('body_markdown', '')).strip()
        if not title or not body:
            errors.append(f'wiki_items[{idx}] missing title or body_markdown')
            continue

        cmd = (
            f'python3 {shlex.quote(gapi)} docs create '
            f'--title {shlex.quote(title)} --body {shlex.quote(body)}'
        )
        actions.append({'type': 'google_docs_create', 'target': 'private_wiki', 'input_ref': title})
        result = run(cmd, timeout=300)
        if result.returncode != 0:
            errors.append(result.stderr.strip() or f'google docs create failed for {title}')
            verification.append({'method': 'read_back', 'ok': False, 'details': f'Create command failed for {title}'})
            continue
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            errors.append(f'non-JSON response from google docs create for {title}')
            verification.append({'method': 'read_back', 'ok': False, 'details': f'JSON parse failed for {title}'})
            continue
        verified = bool(payload.get('verified')) and payload.get('title') == title and body in payload.get('body', '')
        verification.append({'method': 'read_back', 'ok': verified, 'details': f'Verified Google Doc create for {title}'})
        if not verified:
            errors.append(f'read-back verification failed for {title}')
            continue
        handles.append({
            'type': 'google_doc',
            'id': payload.get('documentId'),
            'title': payload.get('title'),
            'url': payload.get('webViewLink'),
        })

    # ---- Phase 2: Publish to Public Wiki (GitHub/Quartz) ----
    for idx, item in enumerate(wiki_items, start=1):
        title = str(item.get('title', '')).strip()
        body = str(item.get('body_markdown', '')).strip()
        if not title or not body:
            continue

        try:
            filepath, slug = _write_public_wiki_file(item)
            public_files_written.append({'path': filepath, 'slug': slug, 'title': title})
            actions.append({'type': 'public_wiki_write', 'target': 'github_pages', 'slug': slug, 'input_ref': title})
            verification.append({'method': 'file_write', 'ok': True, 'details': f'Wrote public wiki file: {slug}'})
        except Exception as e:
            errors.append(f'public_wiki_write failed for {title}: {str(e)}')
            verification.append({'method': 'file_write', 'ok': False, 'details': f'Write failed for {title}: {str(e)}'})

    # ---- Phase 3: Git commit and push public wiki changes ----
    if public_files_written:
        git_actions = []
        # Check git status
        status_result = run(f'cd {shlex.quote(str(WIKI_PUB))} && git status --porcelain', timeout=30)
        if status_result.returncode == 0 and status_result.stdout.strip():
            # Stage changes
            add_result = run(
                f'cd {shlex.quote(str(WIKI_PUB))} && git add content/',
                timeout=30,
            )
            git_actions.append({'type': 'git_add', 'exit_code': add_result.returncode})

            # Commit
            commit_msg = f'Archivist: add {len(public_files_written)} wiki item(s) ({date_key})'
            commit_result = run(
                f'cd {shlex.quote(str(WIKI_PUB))} && git commit -m {shlex.quote(commit_msg)}',
                timeout=30,
            )
            git_actions.append({'type': 'git_commit', 'exit_code': commit_result.returncode, 'message': commit_msg})

            if commit_result.returncode == 0:
                # Push to origin master
                push_result = run(
                    f'cd {shlex.quote(str(WIKI_PUB))} && git push origin master',
                    timeout=120,
                )
                git_actions.append({'type': 'git_push', 'exit_code': push_result.returncode})

                if push_result.returncode == 0:
                    handles.append({
                        'type': 'github_pages_push',
                        'items_published': len(public_files_written),
                        'files': [f['slug'] for f in public_files_written],
                        'trigger': 'GitHub Actions deploy on push',
                    })
                    verification.append({
                        'method': 'git_push',
                        'ok': True,
                        'details': f'Pushed {len(public_files_written)} public wiki files — GitHub Actions will build and deploy',
                    })
                else:
                    errors.append(f'git push failed: {push_result.stderr.strip()}')
                    verification.append({
                        'method': 'git_push',
                        'ok': False,
                        'details': f'Push failed: {push_result.stderr.strip()}',
                    })
            else:
                errors.append(f'git commit failed: {commit_result.stderr.strip()}')

            actions.extend(git_actions)
        else:
            log(f'No git changes detected in {WIKI_PUB} despite writing {len(public_files_written)} files')

    success = bool(handles) and not errors
    status = 'executed' if success else ('failed' if errors else 'executed')
    return make_receipt(
        'archivist', artifact_path, status, success=success, blocked=False,
        actions_attempted=actions,
        external_handles=handles,
        verification=verification,
        errors=errors,
        extra={
            'published_private_docs': len([h for h in handles if h.get('type') == 'google_doc']),
            'published_public_wiki_items': len([h for h in handles if h.get('type') == 'github_pages_push']),
        },
    )


def execute_videoforge_packaging(date_key: str, plan: dict) -> dict:
    artifact_path = stage_artifact_dir(date_key) / 'videoforge.md'
    if 'valid' not in plan:
        plan = extract_videoforge_plan(f'```json\n{json.dumps(plan, ensure_ascii=False)}\n```')
    if not plan.get('valid'):
        return make_receipt(
            'videoforge', artifact_path, 'blocked', success=False, blocked=True,
            errors=plan.get('errors', ['invalid videoforge plan']),
        )
    if not plan.get('render_ready'):
        return make_receipt(
            'videoforge', artifact_path, 'blocked', success=False, blocked=True,
            verification=[{
                'method': 'planner_gate',
                'ok': True,
                'details': 'Video plan explicitly marked not render ready',
            }],
            warnings=plan.get('blocked_reasons', []),
            extra={'render_ready': False},
        )
    package_dir = RENDER_JOBS / date_key
    package_dir.mkdir(parents=True, exist_ok=True)
    package_path = package_dir / 'videoforge_package.json'
    payload = {
        'schema_version': EXECUTOR_SCHEMA_VERSION,
        'generated_at': iso_now(),
        **{k: v for k, v in plan.items() if k not in {'valid', 'errors'}},
    }
    write_json(package_path, payload)
    verified = read_json(package_path, {})
    verification_ok = (
        verified.get('output_basename') == payload.get('output_basename')
        and verified.get('scenes') == payload.get('scenes')
        and verified.get('render_ready') is True
    )
    return make_receipt(
        'videoforge', artifact_path, 'executed' if verification_ok else 'failed', success=verification_ok, blocked=False,
        actions_attempted=[{'type': 'write_videoforge_package', 'target': str(package_path)}],
        external_handles=[{'type': 'file', 'path': str(package_path)}],
        verification=[{
            'method': 'read_back',
            'ok': verification_ok,
            'details': 'Verified videoforge package JSON round-trip',
        }],
        errors=[] if verification_ok else ['videoforge package verification failed'],
        extra={'package_path': str(package_path), 'render_ready': True},
    )


def execute_echohsu_delivery_staging(date_key: str, delivery: dict) -> dict:
    artifact_path = stage_artifact_dir(date_key) / 'echohsu.md'
    if 'valid' not in delivery:
        delivery = extract_echohsu_delivery(f'```json\n{json.dumps(delivery, ensure_ascii=False)}\n```')
    if not delivery.get('valid'):
        return make_receipt(
            'echohsu', artifact_path, 'blocked', success=False, blocked=True,
            errors=delivery.get('errors', ['invalid echohsu delivery package']),
        )
    if not delivery.get('delivery_ready'):
        return make_receipt(
            'echohsu', artifact_path, 'blocked', success=False, blocked=True,
            verification=[{
                'method': 'planner_gate',
                'ok': True,
                'details': 'Delivery package explicitly marked not ready for channel handoff',
            }],
            warnings=delivery.get('blocked_reasons', []),
            extra={'delivery_ready': False},
        )
    package_dir = DELIVERY_LOG / date_key
    package_dir.mkdir(parents=True, exist_ok=True)
    package_path = package_dir / 'delivery_package.json'
    payload = {
        'schema_version': EXECUTOR_SCHEMA_VERSION,
        'generated_at': iso_now(),
        'staged_only': True,
        **{k: v for k, v in delivery.items() if k not in {'valid', 'errors'}},
    }
    write_json(package_path, payload)
    verified = read_json(package_path, {})
    verification_ok = (
        verified.get('channel') == payload.get('channel')
        and verified.get('recipient') == payload.get('recipient')
        and verified.get('message_markdown') == payload.get('message_markdown')
        and verified.get('staged_only') is True
    )
    return make_receipt(
        'echohsu', artifact_path, 'executed' if verification_ok else 'failed', success=verification_ok, blocked=False,
        actions_attempted=[{'type': 'stage_delivery_package', 'target': str(package_path)}],
        external_handles=[{'type': 'file', 'path': str(package_path)}],
        verification=[{
            'method': 'read_back',
            'ok': verification_ok,
            'details': 'Verified delivery package JSON round-trip; no outbound send performed in this phase',
        }],
        warnings=['Delivery package staged only; outbound send not executed by runtime'] if verification_ok else [],
        errors=[] if verification_ok else ['delivery package verification failed'],
        extra={'package_path': str(package_path), 'delivery_ready': True, 'staged_only': True},
    )


def profile_prompt(stage: str, snapshot: dict, artifact_path: Path, date_key: str) -> str:
    common = (
        f'You are running inside the Echo System autonomous loop. '
        f'Today PT date is {date_key}. '
        f'SystemPulse JSON path: {PULSE_JSON}. '
        f'EnvironmentOracle JSON path: {ENV_JSON}. '
        f'Write your final response as concise markdown suitable for archival. '
        f'Do not claim repairs or external effects unless they are present in the provided evidence. '
        f'Do not edit any files; the daemon will archive your response itself.'
    )
    payload = json.dumps(snapshot, indent=2, ensure_ascii=False)
    if stage == 'sentinel':
        return common + (
            f' Review this live system snapshot and produce sections: Status, Key Findings, Metrics, Recommended Repairs. '
            f'Evidence:\n{payload}'
        )
    if stage == 'healer':
        return common + (
            f' Review the Sentinel snapshot and daemon repair actions. Produce sections: Repairs Applied By Daemon, Remaining Issues, Exact Safe Next Repairs, Verification Notes. '
            f'Evidence:\n{payload}'
        )
    if stage == 'evolver':
        return common + (
            f' Analyze the latest Sentinel and Healer outputs plus current pulse state. Produce exactly 3 prioritized improvement proposals, each with Rationale, Expected Benefit, and Verification Method. '
            f'Evidence:\n{payload}'
        )
    if stage == 'orchestrator':
        return common + (
            f' Compile the Echo Morning Briefing draft from the current pulse and upstream artifacts. Include: System Health Score, Agent Status Table for all automated stages evidenced so far, Key Risks, Auto-fixes, and Next Actions. '
            f'Only mark downstream roles as active if artifacts or pulse evidence show they actually ran. '
            f'Evidence:\n{payload}'
        )
    if stage == 'historian':
        return common + (
            f' Review the current pulse plus upstream morning-briefing evidence and produce a verification memo. Include sections: Verification Scope, Facts Safe For Public Reuse, Facts Requiring More Sources, Cultural Accuracy Notes, Media Approval Gate. '
            f'Only approve claims grounded in the supplied evidence. '
            f'After the memo, append a final fenced JSON block labeled json with EXACT keys: approved_for_public_reuse (boolean), approved_for_media (boolean), safe_facts (array of strings), blocked_claims (array of strings), source_gaps (array of strings), consent_notes (array of strings). '
            f'Do not write anything after the JSON block. '
            f'Evidence:\n{payload}'
        )
    if stage == 'docsync':
        return common + (
            " Run a documentation drift detection scan (DocSync). "
            "Compare the following sources for divergence: "
            "(1) Canonical docs in /root/echo_system/docs/ against "
            "(2) Active runtime configurations (hermes profile configs, loop stage definitions, service state) "
            f"(3) EnvironmentOracle at {ENV_JSON} "
            f"(4) Latest SystemPulse at {PULSE_JSON} "
            "Identify: drift items (facts in canonical docs contradicted by runtime evidence), "
            "missing docs (runtime reality with no canonical documentation), "
            "stale docs (references to deprecated features, removed services, outdated paths). "
            "Classify each drift as: auto-fix-safe (timestamps, hashes, status updates, link repair) "
            "vs approval-gated (architecture changes, policy redefinition, agent role changes). "
            'Do NOT modify any files yourself. '
            "After the analysis, append a final fenced JSON block labeled json with EXACT keys: "
            "drift_items (array of objects with path, current_text, correct_text, severity, fix_type), "
            "auto_fix_safe (array of drift_items suitable for automatic correction), "
            "approval_gated (array of drift_items requiring human review), "
            "missing_docs (array of objects with suggested_title, suggested_body, rationale), "
            "stale_refs (array of objects with path, ref, status). "
            "Do not write anything after the JSON block. "
            f"Evidence:\n{payload}"
        )
    if stage == 'archivist':
        return common + (
            " Produce an archival synchronization memo from the verified morning state. "
            "Design model: PUBLISH-THEN-MODERATE. All content items that pass Historian verification "
            "should be published to BOTH private wiki AND public wiki automatically. "
            "The public wiki has a community enforcement mechanism (hide button + kanban review). "
            "Include sections: Candidate Knowledge Updates, Wiki Actions, Deferred Items, Consent Notes. "
            "Do not invent graph writes or external sync success; output only what should be archived based on evidence. "
            "After the memo, append a final fenced JSON block labeled json with EXACT keys: "
            "wiki_items (array of objects with title, body_markdown, source_refs, category (person|organization|event|topic), tags (array of strings)), "
            "deferred_items (array), redaction_notes (array of strings). "
            "Each wiki_item is published to BOTH private wiki (Google Docs) and public wiki (GitHub/Quartz). "
            "Do not write anything after the JSON block. "
            f"Evidence:\n{payload}"
        )
    if stage == 'content':
        return common + (
            f' Turn the verified morning state into a polished narrative briefing plus optional 60-90 second video script. Include sections: Executive Summary, Key Wins, Risks, Script Outline, Visual/Voiceover Cues, Verification Notes. '
            f'All story beats must be traceable to supplied evidence. '
            f'After the memo, append a final fenced JSON block labeled json with EXACT keys: executive_summary (string), video_ready (boolean), script (string), scenes (array of objects with slug, visual, voiceover), subtitle_text (string), asset_requirements (array of strings), source_refs (array of strings). '
            f'Do not write anything after the JSON block. '
            f'Evidence:\n{payload}'
        )
    if stage == 'videoforge':
        return common + (
            f' Create a production plan for any evidence-backed morning briefing video. Include sections: Render Readiness, Scene Plan, Assets Needed, Blocking Gaps, Delivery Checklist. '
            f'If evidence is insufficient for rendering, say so explicitly and list the missing requirements. '
            f'After the memo, append a final fenced JSON block labeled json with EXACT keys: render_ready (boolean), blocked_reasons (array of strings), output_basename (string), scenes (array of objects with slug, visual, voiceover), asset_requirements (array of strings), delivery_checklist (array of strings), source_refs (array of strings). '
            f'Do not write anything after the JSON block. '
            f'Evidence:\n{payload}'
        )
    return common + (
        f' Prepare the final EchoHsu delivery package for Leonard from upstream briefing artifacts. Include sections: Final Delivery Message, Public-Redacted Summary, Suggested Follow-up, Verification Footer. '
        f'You may draft a deliverable, but do not claim any message was actually sent unless the evidence shows an external delivery confirmation. '
        f'After the memo, append a final fenced JSON block labeled json with EXACT keys: delivery_ready (boolean), blocked_reasons (array of strings), channel (string), recipient (string), message_markdown (string), public_summary (string), follow_up_actions (array of strings), source_refs (array of strings). '
        f'Phase 2 rule: stage only the delivery package; do not claim outbound send success. '
        f'Do not write anything after the JSON block. '
        f'Evidence:\n{payload}'
    )


def parse_int(text: str, default: int = 0) -> int:
    try:
        return int((text or '').strip())
    except ValueError:
        return default


def recent_gateway_log_metrics(date_key: str) -> dict:
    log_path = Path('/root/.hermes/logs/gateway.log')
    metrics = {
        'redaction_disabled_warnings': 0,
        'remote_protocol_errors': 0,
        'telegram_network_errors': 0,
        'recent_warning_lines': [],
    }
    if not log_path.exists():
        return metrics
    lines = log_path.read_text(encoding='utf-8', errors='ignore').splitlines()[-1200:]
    for line in lines:
        if date_key not in line:
            continue
        if 'Secret redaction: DISABLED' in line:
            metrics['redaction_disabled_warnings'] += 1
        if 'RemoteProtocolError' in line:
            metrics['remote_protocol_errors'] += 1
        if 'Telegram network error' in line:
            metrics['telegram_network_errors'] += 1
        if any(token in line for token in ['Secret redaction: DISABLED', 'RemoteProtocolError', 'Telegram network error', 'reconnecting in']):
            metrics['recent_warning_lines'].append(line)
    metrics['recent_warning_lines'] = metrics['recent_warning_lines'][-12:]
    return metrics


def gather_snapshot() -> dict:
    today = now_pt().date().isoformat()
    commands = {
        'utc_now': "date --iso-8601=seconds",
        'gateway_active': 'systemctl --user is-active hermes-gateway || true',
        'autoloop_active': 'systemctl --user is-active echo-autoloop || true',
        'gateway_status': 'systemctl --user status hermes-gateway --no-pager || true',
        'gateway_restarts_total': 'systemctl --user show hermes-gateway -p NRestarts --value || true',
        'autoloop_restarts_total': 'systemctl --user show echo-autoloop -p NRestarts --value || true',
        'disk_root': "df -h / | tail -1",
        'memory': "free -m | sed -n '2p'",
        'cron_list': 'hermes cron list || true',
        'profiles': 'hermes profile list || true',
        'ports': "ss -ltnp | grep -E ':8079|:8080|:8090' || true",
        'public_healthz': "curl -fsS --max-time 15 https://bucked-diabetes-shucking.ngrok-free.dev/healthz || true",
    }
    snapshot = {'collected_at': iso_now(), 'checks': {}}
    for key, command in commands.items():
        result = run(command, timeout=120)
        snapshot['checks'][key] = {
            'command': command,
            'exit_code': result.returncode,
            'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip(),
        }
    disk_line = snapshot['checks']['disk_root']['stdout'].split()
    use_pct = None
    if len(disk_line) >= 5 and disk_line[4].endswith('%'):
        try:
            use_pct = int(disk_line[4].rstrip('%'))
        except ValueError:
            use_pct = None
    log_metrics = recent_gateway_log_metrics(today)
    issues = []
    cautions = []
    if snapshot['checks']['gateway_active']['stdout'].strip() != 'active':
        issues.append('hermes-gateway inactive')
    if snapshot['checks']['autoloop_active']['stdout'].strip() != 'active':
        issues.append('echo-autoloop inactive')
    if 'public-hermes-mcp-watchdog' not in snapshot['checks']['cron_list']['stdout']:
        issues.append('public MCP watchdog cron missing')
    if use_pct is not None and use_pct >= 90:
        issues.append(f'root disk usage high ({use_pct}%)')
    if not snapshot['checks']['ports']['stdout'].strip():
        issues.append('expected Hermes ports 8079/8080/8090 not listening')
    if log_metrics['redaction_disabled_warnings']:
        cautions.append('secret redaction disabled warning present in gateway logs')
    if log_metrics['remote_protocol_errors']:
        cautions.append('telegram remote protocol errors detected in gateway logs')
    if parse_int(snapshot['checks']['gateway_restarts_total']['stdout']) > 0:
        cautions.append('hermes-gateway has nonzero restart count')
    snapshot['issues'] = issues
    snapshot['cautions'] = cautions
    snapshot['derived'] = {
        'disk_root_used_pct': use_pct,
        'issue_count': len(issues),
        'caution_count': len(cautions),
        'gateway_restarts_total': parse_int(snapshot['checks']['gateway_restarts_total']['stdout']),
        'autoloop_restarts_total': parse_int(snapshot['checks']['autoloop_restarts_total']['stdout']),
        'gateway_log_metrics': log_metrics,
    }
    return snapshot


def attempt_repairs(snapshot: dict) -> list[dict]:
    repairs = []
    if snapshot['checks']['gateway_active']['stdout'].strip() != 'active':
        result = run('systemctl --user restart hermes-gateway', timeout=120)
        verify = run('systemctl --user is-active hermes-gateway || true', timeout=60)
        repairs.append({
            'action': 'restart hermes-gateway',
            'command_exit_code': result.returncode,
            'verify_status': verify.stdout.strip(),
            'stderr': result.stderr.strip(),
        })
    return repairs


def build_profile_command(profile: str, prompt: str, *, provider: str | None = None, model: str | None = None) -> str:
    parts = ['hermes', '-p', shlex.quote(profile)]
    if provider:
        parts.extend(['--provider', shlex.quote(provider)])
    if model:
        parts.extend(['-m', shlex.quote(model)])
    parts.extend(['-z', shlex.quote(prompt)])
    return ' '.join(parts)


def call_profile(profile: str, prompt: str, timeout: int = 1800) -> dict:
    cmd = build_profile_command(
        profile,
        prompt,
        provider=AUTONOMOUS_PROVIDER_OVERRIDE,
        model=AUTONOMOUS_MODEL_OVERRIDE,
    )
    result = run(cmd, timeout=timeout)
    return {
        'command': cmd,
        'exit_code': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr,
    }


def stage_artifact_dir(date_key: str) -> Path:
    path = ARTIFACTS / date_key
    path.mkdir(parents=True, exist_ok=True)
    return path


def compute_health_score(agents: dict, runtime_signals: dict) -> tuple[int, str, list[str]]:
    penalties = []
    for stage_name, block in agents.items():
        if not isinstance(block, dict):
            continue
        exit_code = block.get('key_metrics', {}).get('profile_exit_code')
        issues = block.get('issues_found', 0)
        cautions = block.get('cautions_found', 0)
        fixes = block.get('auto_fixes_applied', 0)
        if isinstance(exit_code, int) and exit_code != 0:
            penalties.append((18, f'{stage_name} exit code {exit_code}'))
        if isinstance(issues, int) and issues > 0:
            penalties.append((min(issues * 6, 24), f'{stage_name} reported {issues} issue(s)'))
        if isinstance(cautions, int) and cautions > 0:
            penalties.append((min(cautions * 2, 8), f'{stage_name} reported {cautions} caution(s)'))
        if isinstance(fixes, int) and fixes > 0:
            penalties.append((min(fixes * 2, 8), f'{stage_name} required {fixes} auto-fixes'))
    redaction_warnings = runtime_signals.get('redaction_disabled_warnings', 0)
    remote_protocol_errors = runtime_signals.get('remote_protocol_errors', 0)
    telegram_network_errors = runtime_signals.get('telegram_network_errors', 0)
    gateway_restarts_total = runtime_signals.get('gateway_restarts_total', 0)
    autoloop_restarts_total = runtime_signals.get('autoloop_restarts_total', 0)
    if redaction_warnings:
        penalties.append((10, 'secret redaction disabled warning present'))
    if remote_protocol_errors:
        penalties.append((min(8 + (remote_protocol_errors - 1) * 2, 16), f'{remote_protocol_errors} RemoteProtocolError warning(s)'))
    elif telegram_network_errors:
        penalties.append((min(telegram_network_errors, 6), f'{telegram_network_errors} Telegram network warning(s)'))
    if gateway_restarts_total:
        penalties.append((min(6 + (gateway_restarts_total - 1) * 2, 12), f'gateway restart count {gateway_restarts_total}'))
    if autoloop_restarts_total:
        penalties.append((min(6 + (autoloop_restarts_total - 1) * 2, 12), f'autoloop restart count {autoloop_restarts_total}'))
    total_penalty = sum(weight for weight, _ in penalties)
    score = max(20, 100 - total_penalty)
    if score >= 95:
        status = '🟢 Autonomous loop active'
    elif score >= 80:
        status = '🟡 Autonomous loop active with cautions'
    else:
        status = '🟠 Autonomous loop degraded'
    return score, status, [reason for _, reason in penalties]


def update_pulse(stage: str, details: dict) -> None:
    def mutator(data: dict) -> dict:
        agents = data.setdefault('agents', {})
        block = agents.setdefault(stage, {})
        block['status'] = details['status']
        block['last_scan'] = details['last_scan']
        block['issues_found'] = details.get('issues_found', 0)
        block['auto_fixes_applied'] = details.get('auto_fixes_applied', 0)
        block['cautions_found'] = details.get('cautions_found', 0)
        block['notes'] = details.get('notes', '')
        if 'key_metrics' in details:
            block['key_metrics'] = details['key_metrics']
        data['timestamp'] = details['last_scan']
        runtime_signals = details.get('runtime_signals', {})
        score, status, reasons = compute_health_score(agents, runtime_signals)
        data['system_health_score'] = score
        data['overall_status'] = status
        summary = data.get('summary')
        if not isinstance(summary, dict):
            summary = data['summary'] = {}
        summary['compatibility_profiles_repaired'] = []
        summary['autonomous_loop'] = {
            'service': 'echo-autoloop.service',
            'timezone': 'America/Los_Angeles',
            'stages': [stage_def.name for stage_def in STAGES],
            'last_updated': details['last_scan'],
            'runtime_signals': runtime_signals,
            'health_penalties': reasons,
        }
        return data
    atomic_update_json(PULSE_JSON, mutator)


def refresh_pulse_markdown() -> None:
    pulse = read_json(PULSE_JSON, {})
    lines = [
        '# Echo System Pulse',
        '',
        f"- Timestamp: {pulse.get('timestamp', 'unknown')}",
        f"- Health score: {pulse.get('system_health_score', 'unknown')}",
        f"- Status: {pulse.get('overall_status', 'unknown')}",
        '',
        '## Agents',
    ]
    for name, block in pulse.get('agents', {}).items():
        if not isinstance(block, dict):
            continue
        lines.append(f"- {name}: {block.get('status', 'unknown')} | last_scan={block.get('last_scan')} | issues={block.get('issues_found', 0)} | cautions={block.get('cautions_found', 0)} | auto_fixes={block.get('auto_fixes_applied', 0)}")
    lines.append('')
    lines.append('## Autonomous Loop')
    loop = pulse.get('summary', {}).get('autonomous_loop', {})
    if loop:
        lines.append(f"- Service: {loop.get('service')}")
        lines.append(f"- Timezone: {loop.get('timezone')}")
        lines.append(f"- Stages: {', '.join(loop.get('stages', []))}")
        lines.append(f"- Last updated: {loop.get('last_updated')}")
        runtime = loop.get('runtime_signals', {})
        if runtime:
            lines.append(f"- Gateway restarts: {runtime.get('gateway_restarts_total', 0)}")
            lines.append(f"- Autoloop restarts: {runtime.get('autoloop_restarts_total', 0)}")
            lines.append(f"- Redaction warnings: {runtime.get('redaction_disabled_warnings', 0)}")
            lines.append(f"- Remote protocol errors: {runtime.get('remote_protocol_errors', 0)}")
            lines.append(f"- Telegram network warnings: {runtime.get('telegram_network_errors', 0)}")
        penalties = loop.get('health_penalties', [])
        if penalties:
            lines.append('')
            lines.append('## Health Penalties')
            lines.extend(f"- {item}" for item in penalties)
    PULSE_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def append_evolution_log(text: str) -> None:
    atomic_append_text(EVOLUTION_LOG, f'\n## {iso_now()}\n\n{text.strip()}\n')


def phase1_structured_output(stage: str, stdout: str) -> tuple[str | None, dict | None]:
    if stage == 'historian':
        return 'gate', extract_historian_gate(stdout)
    if stage == 'docsync':
        return 'plan', extract_docsync_plan(stdout)
    if stage == 'archivist':
        return 'plan', extract_archivist_plan(stdout)
    if stage == 'content':
        return 'manifest', extract_content_manifest(stdout)
    if stage == 'videoforge':
        return 'plan', extract_videoforge_plan(stdout)
    if stage == 'echohsu':
        return 'delivery', extract_echohsu_delivery(stdout)
    return None, None


def phase1_execute(stage: str, date_key: str, artifact_path: Path, structured: dict | None) -> dict | None:
    if structured is None:
        return None
    if stage == 'historian':
        return execute_historian_gate(date_key, artifact_path, structured)
    if stage == 'docsync':
        return execute_docsync_actions(date_key, structured)
    if stage == 'archivist':
        return execute_archivist_actions(date_key, structured)
    if stage == 'content':
        return execute_content_packaging(date_key, structured)
    if stage == 'videoforge':
        return execute_videoforge_packaging(date_key, structured)
    if stage == 'echohsu':
        return execute_echohsu_delivery_staging(date_key, structured)
    return None


def run_stage(stage: Stage, date_key: str) -> None:
    artifacts = stage_artifact_dir(date_key)
    artifact_path = artifacts / f'{stage.name}.md'
    snapshot = gather_snapshot()
    repairs = []
    if stage.name == 'healer':
        repairs = attempt_repairs(snapshot)
        snapshot['repairs'] = repairs
    if stage.upstream:
        upstream = {}
        for dep in stage.upstream:
            dep_path = artifacts / f'{dep}.md'
            if dep_path.exists():
                upstream[dep] = dep_path.read_text(encoding='utf-8')[-12000:]
        snapshot['upstream_artifacts'] = upstream
        snapshot['pulse'] = read_json(PULSE_JSON, {})
    prompt = profile_prompt(stage.name, snapshot, artifact_path, date_key)
    profile_result = call_profile(stage.profile, prompt)
    artifact = []
    artifact.append(f'# {stage.name.title()} autonomous loop artifact')
    artifact.append('')
    artifact.append(f'- Timestamp: {iso_now()}')
    artifact.append(f'- Profile: {stage.profile}')
    artifact.append(f'- Exit code: {profile_result["exit_code"]}')
    artifact.append(f'- Issues seen: {len(snapshot.get("issues", []))}')
    artifact.append(f'- Cautions seen: {len(snapshot.get("cautions", []))}')
    if repairs:
        artifact.append(f'- Repairs attempted: {len(repairs)}')
    artifact.append('')
    artifact.append('## Model Output')
    artifact.append('')
    artifact.append(profile_result['stdout'].strip() or '(no stdout)')
    if snapshot.get('cautions'):
        artifact.append('')
        artifact.append('## Runtime Cautions')
        artifact.append('')
        artifact.extend(f'- {item}' for item in snapshot['cautions'])
    warning_lines = snapshot.get('derived', {}).get('gateway_log_metrics', {}).get('recent_warning_lines', [])
    if warning_lines:
        artifact.append('')
        artifact.append('## Supporting Gateway Warnings')
        artifact.append('')
        artifact.extend(f'- {line}' for line in warning_lines)
    if profile_result['stderr'].strip():
        artifact.append('')
        artifact.append('## STDERR')
        artifact.append('')
        artifact.append(profile_result['stderr'].strip())
    artifact_path.write_text('\n'.join(artifact) + '\n', encoding='utf-8')

    structured_suffix, structured_data = phase1_structured_output(stage.name, profile_result['stdout'])
    structured_path = None
    receipt = None
    receipt_path = None
    if structured_suffix and structured_data is not None:
        structured_path = stage_json_path(date_key, stage.name, structured_suffix)
        write_stage_json(structured_path, structured_data)
        receipt = phase1_execute(stage.name, date_key, artifact_path, structured_data)
        if receipt is not None:
            receipt_path = stage_json_path(date_key, stage.name, 'receipt')
            write_stage_json(receipt_path, receipt)

    issues_found = len(snapshot.get('issues', []))
    cautions_found = len(snapshot.get('cautions', []))
    receipt_status = (receipt or {}).get('status')
    receipt_success = (receipt or {}).get('success')
    receipt_blocked = (receipt or {}).get('blocked')
    profile_ok = profile_result['exit_code'] == 0
    if profile_ok and issues_found == 0 and cautions_found == 0 and receipt_success is not False:
        status = '🟢'
    elif profile_ok and receipt_blocked:
        status = '🟡'
    elif profile_ok:
        status = '🟡'
    else:
        status = '🔴'
    notes = f'Artifact: {artifact_path}.'
    if structured_path:
        notes += f' Structured: {structured_path}.'
    if receipt_path:
        notes += f' Receipt: {receipt_path}.'
    notes += f' Issues: {snapshot.get("issues", [])[:5]}. Cautions: {snapshot.get("cautions", [])[:5]}'
    details = {
        'status': status,
        'last_scan': iso_now(),
        'issues_found': issues_found,
        'cautions_found': cautions_found,
        'auto_fixes_applied': len(repairs),
        'notes': notes,
        'key_metrics': {
            'artifact_path': str(artifact_path),
            'profile_exit_code': profile_result['exit_code'],
            'repairs_attempted': len(repairs),
            'runtime_issue_count': issues_found,
            'runtime_caution_count': cautions_found,
            'structured_path': str(structured_path) if structured_path else '',
            'receipt_path': str(receipt_path) if receipt_path else '',
            'executor_status': receipt_status or '',
            'executor_success': bool(receipt_success) if receipt is not None else False,
            'executor_blocked': bool(receipt_blocked) if receipt is not None else False,
            'verified_handles_count': len((receipt or {}).get('external_handles', [])),
        },
        'runtime_signals': {
            'gateway_restarts_total': snapshot.get('derived', {}).get('gateway_restarts_total', 0),
            'autoloop_restarts_total': snapshot.get('derived', {}).get('autoloop_restarts_total', 0),
            **snapshot.get('derived', {}).get('gateway_log_metrics', {}),
        },
    }
    update_pulse(stage.name, details)
    refresh_pulse_markdown()
    if stage.name == 'evolver':
        append_evolution_log(profile_result['stdout'])
    if stage.name == 'orchestrator':
        brief_path = BRIEFINGS / f'{date_key}_morning_briefing.md'
        brief_path.parent.mkdir(parents=True, exist_ok=True)
        brief_path.write_text(profile_result['stdout'], encoding='utf-8')
        log(f'Wrote morning briefing draft to {brief_path}')
    elif stage.name == 'content':
        polished_path = BRIEFINGS / f'{date_key}_morning_briefing_polished.md'
        polished_path.parent.mkdir(parents=True, exist_ok=True)
        polished_path.write_text(profile_result['stdout'], encoding='utf-8')
        log(f'Wrote polished narrative briefing to {polished_path}')
    elif stage.name == 'videoforge':
        render_plan_path = BRIEFINGS / f'{date_key}_video_summary_plan.md'
        render_plan_path.parent.mkdir(parents=True, exist_ok=True)
        render_plan_path.write_text(profile_result['stdout'], encoding='utf-8')
        log(f'Wrote video summary plan to {render_plan_path}')
    elif stage.name == 'echohsu':
        delivery_path = BRIEFINGS / f'{date_key}_morning_briefing_delivery.md'
        delivery_path.parent.mkdir(parents=True, exist_ok=True)
        delivery_path.write_text(profile_result['stdout'], encoding='utf-8')
        log(f'Wrote EchoHsu delivery package to {delivery_path}')
    log(f'Completed stage {stage.name}; artifact={artifact_path}')


def load_state() -> dict:
    return read_json(STATE_FILE, {'runs': {}})


def save_state(state: dict) -> None:
    write_json(STATE_FILE, state)


def should_run(stage: Stage, state: dict, current: datetime, force_all: bool) -> bool:
    if force_all:
        return True
    day = current.date().isoformat()
    done_for_day = state.get('runs', {}).get(day, {})
    if done_for_day.get(stage.name):
        return False
    return (current.hour, current.minute) >= (stage.hour, stage.minute)


def mark_run(stage: Stage, state: dict, current: datetime) -> None:
    day = current.date().isoformat()
    state.setdefault('runs', {}).setdefault(day, {})[stage.name] = current.isoformat()
    old_days = sorted(state.get('runs', {}))[:-14]
    for d in old_days:
        state['runs'].pop(d, None)
    save_state(state)


def loop_forever(poll_seconds: int = 60) -> None:
    log('Echo autonomous loop service started')
    while True:
        current = now_pt()
        state = load_state()
        for stage in STAGES:
            if should_run(stage, state, current, False):
                log(f'Starting scheduled stage {stage.name}')
                run_stage(stage, current.date().isoformat())
                mark_run(stage, state, current)
        time.sleep(poll_seconds)


def run_once(force_all: bool) -> None:
    current = now_pt()
    state = load_state()
    ran = False
    for stage in STAGES:
        if should_run(stage, state, current, force_all):
            log(f'Starting one-shot stage {stage.name}')
            run_stage(stage, current.date().isoformat())
            mark_run(stage, state, current)
            ran = True
    if not ran:
        log('No stages were due in one-shot mode')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--force-all', action='store_true')
    parser.add_argument('--poll-seconds', type=int, default=60)
    args = parser.parse_args()
    RUNTIME.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    BRIEFINGS.mkdir(parents=True, exist_ok=True)
    RENDER_JOBS.mkdir(parents=True, exist_ok=True)
    DELIVERY_LOG.mkdir(parents=True, exist_ok=True)
    if args.once:
        run_once(args.force_all)
    else:
        loop_forever(args.poll_seconds)


if __name__ == '__main__':
    main()

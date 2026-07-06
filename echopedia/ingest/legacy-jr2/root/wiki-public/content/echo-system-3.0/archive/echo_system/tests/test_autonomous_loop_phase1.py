import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = "/root/echo_system/runtime/echo_autonomous_loop.py"


def load_module():
    spec = importlib.util.spec_from_file_location("echo_autonomous_loop_under_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AutonomousLoopPhase1Tests(unittest.TestCase):
    def test_build_profile_command_uses_oneshot_and_model_overrides(self):
        module = load_module()
        cmd = module.build_profile_command(
            "sentinel",
            "Reply with exactly OK.",
            provider="openai-codex",
            model="gpt-5.4",
        )
        self.assertIn("hermes -p sentinel", cmd)
        self.assertIn("--provider openai-codex", cmd)
        self.assertIn("-m gpt-5.4", cmd)
        self.assertIn(" -z ", cmd)
        self.assertNotIn(" chat -Q -q ", cmd)

    def test_historian_prompt_requires_trailing_json_block(self):
        module = load_module()
        prompt = module.profile_prompt("historian", {"pulse": {}}, Path("/tmp/historian.md"), "2026-05-09")
        self.assertIn("final fenced JSON block labeled json", prompt)
        self.assertIn("approved_for_public_reuse", prompt)

    def test_extract_json_block_prefers_last_fenced_json_block(self):
        module = load_module()
        text = """
        # Header

        ```json
        {"first": true}
        ```

        trailing memo

        ```json
        {"second": 2, "nested": {"ok": true}}
        ```
        """
        data = module.extract_json_block(text)
        self.assertEqual(data["second"], 2)
        self.assertTrue(data["nested"]["ok"])

    def test_execute_content_packaging_writes_manifest_and_receipt(self):
        module = load_module()
        manifest = {
            "executive_summary": "System stable enough for draft packaging.",
            "video_ready": False,
            "script": "Narration draft",
            "scenes": [{"slug": "scene-1", "visual": "dashboard", "voiceover": "hello"}],
            "subtitle_text": "hello",
            "asset_requirements": ["logo"],
            "source_refs": ["historian", "archivist", "orchestrator"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(module, "ROOT", root), \
                 patch.object(module, "RUNTIME", root / "runtime"), \
                 patch.object(module, "ARTIFACTS", root / "runtime" / "stage_outputs"), \
                 patch.object(module, "BRIEFINGS", root / "briefings"), \
                 patch.object(module, "PULSE_JSON", root / "system_pulse" / "SystemPulse.json"), \
                 patch.object(module, "PULSE_MD", root / "system_pulse" / "SystemPulse.md"), \
                 patch.object(module, "EVOLUTION_LOG", root / "system_pulse" / "System_Evolution_Log.md"), \
                 patch.object(module, "ENV_JSON", root / "environment" / "EnvironmentOracle.json"), \
                 patch.object(module, "STATE_FILE", root / "runtime" / "loop_state.json"), \
                 patch.object(module, "LOG_FILE", root / "runtime" / "echo_autoloop.log"), \
                 patch.object(module, "RENDER_JOBS", root / "runtime" / "render_jobs"), \
                 patch.object(module, "DELIVERY_LOG", root / "runtime" / "delivery_log"):
                receipt = module.execute_content_packaging("2026-05-09", manifest)
                manifest_path = root / "runtime" / "render_jobs" / "2026-05-09" / "render_manifest.json"
                self.assertTrue(manifest_path.exists())
                saved_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual(saved_manifest["script"], "Narration draft")
                self.assertEqual(receipt["status"], "executed")
                self.assertTrue(receipt["success"])
                self.assertFalse(receipt["blocked"])
                self.assertEqual(receipt["external_handles"][0]["path"], str(manifest_path))

    def test_execute_archivist_actions_records_verified_doc_handle(self):
        module = load_module()
        plan = {
            "private_wiki_updates": [
                {
                    "title": "Echo Morning Briefing 2026-05-09",
                    "body_markdown": "Verified body text",
                    "source_refs": ["historian", "orchestrator"],
                }
            ],
            "public_wiki_safe_items": [],
            "deferred_items": [],
            "redaction_notes": [],
        }
        fake_stdout = json.dumps({
            "status": "created",
            "verified": True,
            "documentId": "doc-123",
            "title": "Echo Morning Briefing 2026-05-09",
            "body": "Verified body text",
            "webViewLink": "https://docs.google.com/document/d/doc-123/edit",
        })

        class Result:
            def __init__(self, stdout, stderr="", returncode=0):
                self.stdout = stdout
                self.stderr = stderr
                self.returncode = returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(module, "ROOT", root), \
                 patch.object(module, "RUNTIME", root / "runtime"), \
                 patch.object(module, "ARTIFACTS", root / "runtime" / "stage_outputs"), \
                 patch.object(module, "BRIEFINGS", root / "briefings"), \
                 patch.object(module, "PULSE_JSON", root / "system_pulse" / "SystemPulse.json"), \
                 patch.object(module, "PULSE_MD", root / "system_pulse" / "SystemPulse.md"), \
                 patch.object(module, "EVOLUTION_LOG", root / "system_pulse" / "System_Evolution_Log.md"), \
                 patch.object(module, "ENV_JSON", root / "environment" / "EnvironmentOracle.json"), \
                 patch.object(module, "STATE_FILE", root / "runtime" / "loop_state.json"), \
                 patch.object(module, "LOG_FILE", root / "runtime" / "echo_autoloop.log"), \
                 patch.object(module, "RENDER_JOBS", root / "runtime" / "render_jobs"), \
                 patch.object(module, "DELIVERY_LOG", root / "runtime" / "delivery_log"), \
                 patch.object(module, "run", return_value=Result(fake_stdout)):
                receipt = module.execute_archivist_actions("2026-05-09", plan)
                self.assertEqual(receipt["status"], "executed")
                self.assertTrue(receipt["success"])
                self.assertEqual(receipt["external_handles"][0]["id"], "doc-123")
                self.assertTrue(receipt["verification"][0]["ok"])

    def test_videoforge_prompt_requires_trailing_json_block(self):
        module = load_module()
        prompt = module.profile_prompt("videoforge", {"pulse": {}}, Path("/tmp/videoforge.md"), "2026-05-09")
        self.assertIn("final fenced JSON block labeled json", prompt)
        self.assertIn("render_ready", prompt)
        self.assertIn("delivery_checklist", prompt)

    def test_execute_videoforge_packaging_writes_package_and_receipt(self):
        module = load_module()
        plan = {
            "render_ready": True,
            "blocked_reasons": [],
            "output_basename": "echo-morning-2026-05-09",
            "scenes": [{"slug": "scene-1", "visual": "dashboard", "voiceover": "hello"}],
            "asset_requirements": ["logo"],
            "delivery_checklist": ["verify final mp4"],
            "source_refs": ["content", "historian", "archivist"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(module, "ROOT", root), \
                 patch.object(module, "RUNTIME", root / "runtime"), \
                 patch.object(module, "ARTIFACTS", root / "runtime" / "stage_outputs"), \
                 patch.object(module, "BRIEFINGS", root / "briefings"), \
                 patch.object(module, "PULSE_JSON", root / "system_pulse" / "SystemPulse.json"), \
                 patch.object(module, "PULSE_MD", root / "system_pulse" / "SystemPulse.md"), \
                 patch.object(module, "EVOLUTION_LOG", root / "system_pulse" / "System_Evolution_Log.md"), \
                 patch.object(module, "ENV_JSON", root / "environment" / "EnvironmentOracle.json"), \
                 patch.object(module, "STATE_FILE", root / "runtime" / "loop_state.json"), \
                 patch.object(module, "LOG_FILE", root / "runtime" / "echo_autoloop.log"), \
                 patch.object(module, "RENDER_JOBS", root / "runtime" / "render_jobs"), \
                 patch.object(module, "DELIVERY_LOG", root / "runtime" / "delivery_log"):
                receipt = module.execute_videoforge_packaging("2026-05-09", plan)
                package_path = root / "runtime" / "render_jobs" / "2026-05-09" / "videoforge_package.json"
                self.assertTrue(package_path.exists())
                saved = json.loads(package_path.read_text(encoding="utf-8"))
                self.assertEqual(saved["output_basename"], "echo-morning-2026-05-09")
                self.assertEqual(receipt["status"], "executed")
                self.assertTrue(receipt["success"])
                self.assertEqual(receipt["external_handles"][0]["path"], str(package_path))

    def test_execute_echohsu_delivery_staging_writes_package_and_receipt(self):
        module = load_module()
        delivery = {
            "delivery_ready": True,
            "blocked_reasons": [],
            "channel": "sms",
            "recipient": "Leonard Hsu",
            "message_markdown": "Verified delivery package.",
            "public_summary": "Redacted summary.",
            "follow_up_actions": ["confirm receipt manually"],
            "source_refs": ["orchestrator", "content", "videoforge"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(module, "ROOT", root), \
                 patch.object(module, "RUNTIME", root / "runtime"), \
                 patch.object(module, "ARTIFACTS", root / "runtime" / "stage_outputs"), \
                 patch.object(module, "BRIEFINGS", root / "briefings"), \
                 patch.object(module, "PULSE_JSON", root / "system_pulse" / "SystemPulse.json"), \
                 patch.object(module, "PULSE_MD", root / "system_pulse" / "SystemPulse.md"), \
                 patch.object(module, "EVOLUTION_LOG", root / "system_pulse" / "System_Evolution_Log.md"), \
                 patch.object(module, "ENV_JSON", root / "environment" / "EnvironmentOracle.json"), \
                 patch.object(module, "STATE_FILE", root / "runtime" / "loop_state.json"), \
                 patch.object(module, "LOG_FILE", root / "runtime" / "echo_autoloop.log"), \
                 patch.object(module, "RENDER_JOBS", root / "runtime" / "render_jobs"), \
                 patch.object(module, "DELIVERY_LOG", root / "runtime" / "delivery_log"):
                receipt = module.execute_echohsu_delivery_staging("2026-05-09", delivery)
                package_path = root / "runtime" / "delivery_log" / "2026-05-09" / "delivery_package.json"
                self.assertTrue(package_path.exists())
                saved = json.loads(package_path.read_text(encoding="utf-8"))
                self.assertEqual(saved["channel"], "sms")
                self.assertEqual(receipt["status"], "executed")
                self.assertTrue(receipt["success"])
                self.assertEqual(receipt["external_handles"][0]["path"], str(package_path))

    def test_run_stage_writes_structured_and_receipt_artifacts_for_content(self):
        module = load_module()
        stage = next(s for s in module.STAGES if s.name == "content")
        content_output = """# Content memo

```json
{
  "executive_summary": "Verified summary",
  "video_ready": false,
  "script": "Narration draft",
  "scenes": [{"slug": "scene-1", "visual": "dashboard", "voiceover": "hello"}],
  "subtitle_text": "hello",
  "asset_requirements": ["logo"],
  "source_refs": ["historian", "archivist", "orchestrator"]
}
```
"""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "system_pulse").mkdir(parents=True, exist_ok=True)
            (root / "environment").mkdir(parents=True, exist_ok=True)
            (root / "briefings").mkdir(parents=True, exist_ok=True)
            (root / "system_pulse" / "SystemPulse.json").write_text("{}\n", encoding="utf-8")
            (root / "environment" / "EnvironmentOracle.json").write_text("{}\n", encoding="utf-8")

            with patch.object(module, "ROOT", root), \
                 patch.object(module, "RUNTIME", root / "runtime"), \
                 patch.object(module, "ARTIFACTS", root / "runtime" / "stage_outputs"), \
                 patch.object(module, "BRIEFINGS", root / "briefings"), \
                 patch.object(module, "PULSE_JSON", root / "system_pulse" / "SystemPulse.json"), \
                 patch.object(module, "PULSE_MD", root / "system_pulse" / "SystemPulse.md"), \
                 patch.object(module, "EVOLUTION_LOG", root / "system_pulse" / "System_Evolution_Log.md"), \
                 patch.object(module, "ENV_JSON", root / "environment" / "EnvironmentOracle.json"), \
                 patch.object(module, "STATE_FILE", root / "runtime" / "loop_state.json"), \
                 patch.object(module, "LOG_FILE", root / "runtime" / "echo_autoloop.log"), \
                 patch.object(module, "RENDER_JOBS", root / "runtime" / "render_jobs"), \
                 patch.object(module, "DELIVERY_LOG", root / "runtime" / "delivery_log"), \
                 patch.object(module, "gather_snapshot", return_value={"issues": [], "cautions": [], "derived": {"gateway_restarts_total": 0, "autoloop_restarts_total": 0, "gateway_log_metrics": {}}}), \
                 patch.object(module, "call_profile", return_value={"command": "hermes ...", "exit_code": 0, "stdout": content_output, "stderr": ""}):
                module.run_stage(stage, "2026-05-09")

            structured_path = root / "runtime" / "stage_outputs" / "2026-05-09" / "content.manifest.json"
            receipt_path = root / "runtime" / "stage_outputs" / "2026-05-09" / "content.receipt.json"
            self.assertTrue(structured_path.exists())
            self.assertTrue(receipt_path.exists())
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "executed")
            pulse = json.loads((root / "system_pulse" / "SystemPulse.json").read_text(encoding="utf-8"))
            self.assertEqual(pulse["agents"]["content"]["key_metrics"]["executor_status"], "executed")


if __name__ == "__main__":
    unittest.main()

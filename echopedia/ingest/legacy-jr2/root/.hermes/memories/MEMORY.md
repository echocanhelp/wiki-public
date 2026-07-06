Echo media profiles now exist: content (gpt-5.3-codex), videoforge (grok-imagine-video), audioforge (grok-imagine-audio), voice (grok-tts-1), vision (grok-2-vision-latest). Content profile is not yet on grok-imagine-image-quality.
§
The user's project (Echo System 3.0) utilizes a Three-Layer Architecture: 1. Semantic (Google Drive Markdown Wiki), 2. Episodic/Relational (Session/Personal context), and 3. Procedural (Skills/Workflows). The system requires Layer 4+ verification for all critical tasks.
§
User's goal for Echo System 3.0 is to achieve a "24/7 autonomous loop" where the system is fully hands-off once a trigger is provided. He prefers a "Mission-first" architecture involving a permanent background Dispatcher (via systemd) rather than manual task claiming.
§
Orchestrator profile: xai-oauth provider with grok-4.3 default. All grok access is direct via xai-oauth OAuth. Echo System 3.0 LINE Bridge: Custom Node.js Express app at `~/.hermes/line-bridge/`. Webhook: `https://bucked-diabetes-shucking.ngrok-free.dev/line/webhook`. Channel ID: `2010102838`.
§
Echo System 3.0 project philosophy: "Public First + Fast Correction" — publish quickly, use Instant Hide + review as safety net. Current focus: EchoFeelings Phase 2 (narrative/emotional memory system).
§
xAI OAuth pitfall: `hermes auth reset xai-oauth` CLEARS the credential entirely (does NOT just reset exhaustion). When credential shows "exhausted", wait for timer to expire or re-run `hermes auth add xai-oauth --type oauth`. Tokens expire every 6h (21600s). ~15 grok models available via single OAuth (grok-4.3, grok-2-vision-latest, grok-imagine-image-quality, grok-imagine-video, grok-imagine-audio, grok-tts-*).
§
Quartz Wiki: echocanhelp/wiki-public (GitHub Pages). CI/CD via GitHub Actions. Correct framework: jackyzha0/quartz v4.5.2+. Entry point: quartz/bootstrap-cli.mjs. See skill github-actions-cicd/references/quartz-v4-deployment.md.
§
Current active model context switched to OpenAI Codex (`gpt-5.5`) from prior models; adjust self-identification/model references accordingly during profile/status updates.
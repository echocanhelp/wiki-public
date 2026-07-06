"""Load bridge configuration from environment."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

BRIDGES_ROOT = Path(__file__).resolve().parents[1]
ECHO_ROOT_DEFAULT = BRIDGES_ROOT.parent


def _bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _csv(value: str | None) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def _int(value: str | None, default: int) -> int:
    try:
        return int(value) if value is not None else default
    except ValueError:
        return default


@dataclass
class BridgeConfig:
    echo_root: Path
    admin_key: str
    rate_per_minute: int
    rate_per_hour: int
    global_rate_per_minute: int
    tau_timeout: int
    max_message_chars: int
    session_continuity: bool
    telegram_typing_interval: int
    telegram_progress_after: int
    telegram_chunk_chars: int
    telegram_status_interval: int
    line_progress_after: int
    line_loading_seconds: int
    whisper_url: str
    line_media_path: str
    log_level: str

    telegram_enabled: bool
    telegram_token: str
    telegram_allowed_users: set[str]
    telegram_home_channel: str
    telegram_poll_timeout: int

    line_enabled: bool
    line_channel_secret: str
    line_channel_access_token: str
    line_channel_id: str
    line_allowed_groups: set[str]
    line_allow_all_users: bool
    line_allowed_users: set[str]
    line_webhook_port: int
    line_webhook_path: str
    line_public_url: str
    line_webhook_bridge_key: str
    line_group_mention_only: bool

    tau_script: Path = field(init=False)
    tau_cwd: Path = field(init=False)
    contexts_dir: Path = field(init=False)
    media_dir: Path = field(init=False)
    logs_dir: Path = field(init=False)
    pids_dir: Path = field(init=False)

    def __post_init__(self) -> None:
        self.tau_script = self.echo_root / "tauergon" / "src" / "tau.py"
        self.tau_cwd = self.echo_root / "tauergon"
        self.contexts_dir = BRIDGES_ROOT / "contexts"
        self.media_dir = BRIDGES_ROOT / "media"
        self.logs_dir = BRIDGES_ROOT / "logs"
        self.pids_dir = BRIDGES_ROOT / "pids"


def load_config(env_path: Path | None = None) -> BridgeConfig:
    env_file = env_path or (BRIDGES_ROOT / ".env")
    if env_file.exists():
        load_dotenv(env_file, override=False)

    echo_root = Path(os.getenv("ECHO_ROOT", str(ECHO_ROOT_DEFAULT))).resolve()

    return BridgeConfig(
        echo_root=echo_root,
        admin_key=os.getenv("BRIDGE_ADMIN_KEY", os.getenv("API_SERVER_KEY", "")),
        rate_per_minute=_int(os.getenv("BRIDGE_RATE_LIMIT_PER_MINUTE"), 6),
        rate_per_hour=_int(os.getenv("BRIDGE_RATE_LIMIT_PER_HOUR"), 30),
        global_rate_per_minute=_int(os.getenv("BRIDGE_GLOBAL_RATE_PER_MINUTE"), 60),
        tau_timeout=_int(os.getenv("BRIDGE_TAU_TIMEOUT"), 600),
        max_message_chars=_int(os.getenv("BRIDGE_MAX_MESSAGE_CHARS"), 4096),
        session_continuity=_bool(os.getenv("BRIDGE_SESSION_CONTINUITY"), True),
        telegram_typing_interval=_int(os.getenv("TELEGRAM_TYPING_INTERVAL"), 4),
        telegram_progress_after=_int(os.getenv("TELEGRAM_PROGRESS_AFTER"), 15),
        telegram_chunk_chars=_int(os.getenv("TELEGRAM_CHUNK_CHARS"), 4096),
        telegram_status_interval=_int(os.getenv("TELEGRAM_STATUS_INTERVAL"), 12),
        line_progress_after=_int(os.getenv("LINE_PROGRESS_AFTER"), 15),
        line_loading_seconds=_int(os.getenv("LINE_LOADING_SECONDS"), 60),
        whisper_url=os.getenv("ECHO_WHISPER_URL", "http://localhost:8002/v1"),
        line_media_path=os.getenv("LINE_MEDIA_PATH", "/line/media"),
        log_level=os.getenv("BRIDGE_LOG_LEVEL", "INFO").upper(),
        telegram_enabled=_bool(os.getenv("TELEGRAM_ENABLED"), True),
        telegram_token=os.getenv("TELEGRAM_BOT_TOKEN", ""),
        telegram_allowed_users=_csv(os.getenv("TELEGRAM_ALLOWED_USERS")),
        telegram_home_channel=os.getenv("TELEGRAM_HOME_CHANNEL", ""),
        telegram_poll_timeout=_int(os.getenv("TELEGRAM_POLL_TIMEOUT"), 30),
        line_enabled=_bool(os.getenv("LINE_ENABLED"), True),
        line_channel_secret=os.getenv("LINE_CHANNEL_SECRET", ""),
        line_channel_access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN", ""),
        line_channel_id=os.getenv("LINE_CHANNEL_ID", ""),
        line_allowed_groups=_csv(os.getenv("LINE_ALLOWED_GROUPS")),
        line_allow_all_users=_bool(os.getenv("LINE_ALLOW_ALL_USERS"), False),
        line_allowed_users=_csv(os.getenv("LINE_ALLOWED_USERS")),
        line_webhook_port=_int(os.getenv("LINE_WEBHOOK_PORT"), 8787),
        line_webhook_path=os.getenv("LINE_WEBHOOK_PATH", "/line/webhook"),
        line_public_url=os.getenv("LINE_PUBLIC_URL", "").rstrip("/"),
        line_webhook_bridge_key=os.getenv("LINE_WEBHOOK_BRIDGE_KEY", ""),
        line_group_mention_only=_bool(os.getenv("LINE_GROUP_MENTION_ONLY"), True),
    )
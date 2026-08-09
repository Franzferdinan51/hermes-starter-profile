#!/usr/bin/env python3
"""Audit an installed Starter Hermes profile without probing providers."""

from __future__ import annotations

import os
from pathlib import Path

import yaml

ALLOWED_TOOLSETS = {"clarify", "image_gen", "search", "tts", "vision"}
ALLOWED_TOOLS = {
    "clarify", "image_generate", "text_to_speech", "vision_analyze", "web_search",
}
PLATFORMS = {
    "cli", "telegram", "discord", "slack", "whatsapp", "whatsapp_cloud",
    "signal", "bluebubbles", "email", "homeassistant", "mattermost", "matrix",
    "dingtalk", "feishu", "wecom", "wecom_callback", "weixin", "qqbot",
    "yuanbao", "webhook", "api_server", "cron",
}
REQUIRED_DISABLED = {
    "code_execution", "computer_use", "cronjob", "delegation", "desktop_ui",
    "file", "homeassistant", "kanban", "memory", "project", "session_search",
    "skills", "terminal", "video", "video_gen", "x_search",
}


def main() -> int:
    root = Path(os.environ.get("HERMES_HOME") or Path(__file__).resolve().parents[1]).resolve()
    os.environ["HERMES_HOME"] = str(root)
    path = root / "config.yaml"
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(cfg, dict):
        print(f"FAIL: {path} must contain a YAML mapping")
        return 1

    errors: list[str] = []
    disabled = set((cfg.get("agent") or {}).get("disabled_toolsets") or [])
    missing_disabled = REQUIRED_DISABLED - disabled
    if missing_disabled:
        errors.append("required global toolset denies missing: " + ", ".join(sorted(missing_disabled)))

    configured = cfg.get("platform_toolsets") or {}
    for platform in sorted(PLATFORMS):
        declared = set(configured.get(platform) or [])
        if declared != ALLOWED_TOOLSETS:
            errors.append(
                f"platform_toolsets.{platform}={sorted(declared)!r}; "
                f"expected {sorted(ALLOWED_TOOLSETS)!r}"
            )

    memory = cfg.get("memory") or {}
    if memory.get("memory_enabled") is not False:
        errors.append("memory.memory_enabled must be false")
    if memory.get("user_profile_enabled") is not False:
        errors.append("memory.user_profile_enabled must be false")
    if (cfg.get("privacy") or {}).get("redact_pii") is not True:
        errors.append("privacy.redact_pii must be true")
    if (cfg.get("curator") or {}).get("enabled") is not False:
        errors.append("curator.enabled must be false")
    if cfg.get("mcp_servers"):
        errors.append("mcp_servers must be empty")
    if cfg.get("hooks"):
        errors.append("hooks must be empty")
    if cfg.get("quick_commands"):
        errors.append("quick_commands must be empty")
    if (cfg.get("security") or {}).get("allow_lazy_installs") is not False:
        errors.append("security.allow_lazy_installs must be false")
    for required_path in (".no-bundled-skills", "SOUL.md", "distribution.yaml"):
        if not (root / required_path).is_file():
            errors.append(f"{required_path} is missing")

    try:
        from hermes_cli.tools_config import _get_platform_tools
        from toolsets import resolve_toolset

        disabled_tools: set[str] = set()
        for toolset in disabled:
            disabled_tools.update(resolve_toolset(toolset))

        for platform in sorted(PLATFORMS):
            resolved = set(_get_platform_tools(cfg, platform))
            if resolved != ALLOWED_TOOLSETS:
                errors.append(
                    f"resolver mismatch on {platform}: got {sorted(resolved)!r}, "
                    f"expected {sorted(ALLOWED_TOOLSETS)!r}"
                )
            tool_names: set[str] = set()
            for toolset in resolved:
                tool_names.update(resolve_toolset(toolset))
            tool_names -= disabled_tools
            if tool_names != ALLOWED_TOOLS:
                errors.append(
                    f"tool expansion mismatch on {platform}: got {sorted(tool_names)!r}, "
                    f"expected {sorted(ALLOWED_TOOLS)!r}"
                )
    except Exception as exc:
        errors.append(f"could not exercise Hermes tool resolver: {exc}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"FAIL: {len(errors)} starter-profile invariant(s) violated")
        return 1

    print(f"PASS: {len(PLATFORMS)} platform policies and starter-profile invariants verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

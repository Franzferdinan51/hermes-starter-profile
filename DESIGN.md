# Design

Starter Hermes is a low-overwhelm profile for people learning Hermes Agent. The design goal is a useful first experience without exposing the full system-administration surface.

## Enabled baseline

- `clarify` for focused follow-up questions
- `search` for current research without page extraction or browser automation
- `vision` for image understanding
- `image_gen` for creative visual work
- `tts` for spoken output

Provider-gated tools appear only when their backend is available.

## Disabled by default

- Terminal and process execution
- File reading, writing, and patching
- Code execution
- Browser and desktop automation
- Delegation and multi-agent orchestration
- Scheduled jobs
- Persistent memory, session search, and skill management
- MCP servers, hooks, quick commands, and external integrations
- Home Assistant, social media, and platform administration tools

## Why two policy layers?

`platform_toolsets` defines the exact baseline for every shipped surface. `agent.disabled_toolsets` is applied afterward and blocks dangerous component toolsets even if another resolution path attempts to recover them.

Hermes has composite toolsets whose safe and unsafe members overlap. The profile therefore verifies the final resolved tool names rather than globally disabling broad composites that would also remove permitted search, vision, or clarification.

## Privacy defaults

Persistent memory and user-profile memory are off. PII and secret redaction are on. Runtime dependency installation is off. The profile still stores ordinary local session history as Hermes normally does; users control the host and provider retention settings.

## Trust boundary

This is a constrained starting configuration, not a sandbox against the machine owner. Someone who can edit the profile can expand it. The audit script catches accidental drift from the published baseline.

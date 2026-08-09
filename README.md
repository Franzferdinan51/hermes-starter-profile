# Hermes Starter Profile

A focused Hermes profile for people learning the agent without starting with its full system-administration toolset.

## Install

```bash
hermes profile install github.com/teknium1/hermes-starter-profile --alias
starter-hermes model
starter-hermes chat
```

Read [GETTING_STARTED.md](GETTING_STARTED.md) for setup and first prompts.

## What is enabled

- Clarifying questions
- Web search
- Image understanding
- Image generation
- Text-to-speech

Tools appear only when their provider is configured.

## What is disabled

- Terminal, processes, and code execution
- Host file access
- Browser and desktop automation
- Subagents and scheduled jobs
- Persistent memory and skill management
- MCP servers, hooks, quick commands, and external integrations
- Platform administration and Home Assistant tools

The profile stays useful for research, writing, brainstorming, explanations, visual work, and learning how tool-enabled agents behave. The machine owner can expand it later through the normal Hermes configuration flow.

## Verify the baseline

```bash
HERMES_HOME="$HOME/.hermes/profiles/starter-hermes" \
  python "$HOME/.hermes/profiles/starter-hermes/scripts/audit_profile.py"
```

The audit exercises Hermes' real platform resolver and fails if the installed profile drifts outside the published tool boundary.

## Design

[DESIGN.md](DESIGN.md) explains the tool policy, privacy defaults, and trust boundary.

## License

MIT

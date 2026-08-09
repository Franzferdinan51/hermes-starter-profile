# Getting started

## Install the profile

```bash
hermes profile install github.com/teknium1/hermes-starter-profile --alias
```

The installer creates the `starter-hermes` alias.

## Choose a model

```bash
starter-hermes model
```

Pick any provider and model you already use with Hermes. Credentials remain isolated inside this profile.

## Start chatting

```bash
starter-hermes chat
```

Useful first prompts:

- `Explain what this profile can and cannot do.`
- `Research the latest images from the James Webb Space Telescope and cite sources.`
- `Help me turn a rough idea into a one-page project plan.`
- `Create three visual directions for a poster about deep-sea life.`
- `Explain this diagram.`

Some tools appear only after their provider is configured. Search may use your configured web backend or a Nous-managed backend. Image generation, vision, and text-to-speech follow the normal Hermes tool setup.

## Add a capability later

The starter profile is deliberately narrow. To review or change tools as the profile owner:

```bash
starter-hermes tools
```

The global `agent.disabled_toolsets` list is an additional ceiling. Enabling a tool in the picker does not override that list. To expand the profile deliberately, update both `platform_toolsets` and `agent.disabled_toolsets` in:

```text
~/.hermes/profiles/starter-hermes/config.yaml
```

Then start a new session so the prompt cache and tool schema are rebuilt intentionally.

## Optional gateway

Configure Telegram, Discord, or another messaging platform through the normal gateway setup:

```bash
starter-hermes gateway setup
```

This distribution does not ship user IDs, bot tokens, platform allowlists, or operator access policy. Those belong to each install.

## Audit the profile

```bash
HERMES_HOME="$HOME/.hermes/profiles/starter-hermes" \
  python "$HOME/.hermes/profiles/starter-hermes/scripts/audit_profile.py"
```

The command must end with `PASS`.

## Update

```bash
hermes profile update starter-hermes
```

A normal update preserves your existing `config.yaml`. Use `--force-config` only when you intentionally want to restore the distribution's baseline.

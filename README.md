# Hermes Starter Profile

### A Beginner's Welcome Bundle — Built on the Warrior Way

> *"Learn matters most. Set the guardrails. Be partners in this work."*
> — Huber Heights City Schools AI Community Playbook

This is a friendly, calm way to try **Hermes Agent** for the first time, without turning on the full system-administration toolset. We wrote it for **students, families, and educators** who want to learn by doing, with the same spirit as the HHCS AI Playbook: **process over product, transparency over shortcuts, and people at the center of learning.**

You don't need to know Git, Python, YAML, or what an "agent profile" is. We start at zero and walk through it together.

---

## Our Three Pillars (from the HHCS Playbook)

Everything in this profile is shaped by three commitments from the playbook. We follow them because they help us learn well.

| Pillar | What it means here |
| --- | --- |
| **Empower Educators** | Hermes handles the small stuff so you can spend more time on what only you can do — the thinking, the questions, the relationships. |
| **Enhance Learning** | Use Hermes as a learning assistant and a tutor. It can break down hard ideas, find study paths, and be available 24/7. |
| **Protect Integrity** | We value **how you learn** (the process) as much as the final answer (the product). AI should support the process, not skip it. |

> *"We utilize AI to enhance learning. It does not replace developing student learning."*
> — HHCS AI Playbook

---

## What you will get

After following the five steps below, you will have a separate command named `starter-hermes`. Imagine it as a **study buddy in a small box** — it can:

- answer questions and explain unfamiliar topics in plain language;
- search the web and cite sources when search is configured;
- look at images and tell you what is in them;
- draw pictures for creative projects;
- read text out loud; and
- help with writing, brainstorming, research, and planning.

It **cannot** open a terminal, change files, take over your browser, control your computer, run tasks while you sleep, or make other AI helpers. We leave those off on purpose so your first time with Hermes is easier to understand. Less noise, more learning.

---

## Five-step setup (about five minutes)

> **Before we start.** A computer takes a lot of language literally. The commands below need to be typed **exactly** as shown, but the *ideas* behind them are simple. We explain each one in plain words first.

### Step 1 — Install Hermes Agent

**Already have Hermes?** Open a terminal and run:

```bash
hermes --version
```

If it prints a version number (like `hermes 0.20.0`), skip to Step 2. You're already on the team.

**If you have never used a terminal before**, that's okay. A terminal is just a text window where you can talk to the computer. Open one like this:

- **Windows:** open **PowerShell** from the Start menu.
- **macOS:** open **Terminal** from Applications → Utilities.
- **Linux:** open your system's **Terminal** application.

#### Easiest option on Windows or macOS

Download and run the Hermes Desktop installer from
[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/).
The installer includes the command used by this guide.

#### Command-line option on macOS, Linux, or WSL2

Paste this into the terminal and press Enter:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

#### Command-line option on native Windows

Paste this into PowerShell and press Enter:

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

When installation finishes, close the terminal, open a new one, and verify it:

```bash
hermes --version
```

Do not continue until that command prints a version number. If it says `command not found`, see [Troubleshooting](#troubleshooting) at the bottom of this page.

### Step 2 — Install this starter profile

A **profile** is just a separate workspace for Hermes. It has its own model, its own settings, and its own personality. Installing this profile does **not** change your normal Hermes setup. Think of it like a separate notebook for a separate class.

Copy this whole command into the terminal:

```bash
hermes profile install github.com/teknium1/hermes-starter-profile --alias
```

Hermes will show you a preview of what is about to change. Confirm when it asks. The command creates:

- a separate profile named `starter-hermes`; and
- a shortcut command, also named `starter-hermes`.

Check that the shortcut works:

```bash
starter-hermes --version
```

If the shortcut is not found, use this equivalent form for every command:

```bash
hermes -p starter-hermes --version
```

For example, `hermes -p starter-hermes chat` means the same thing as `starter-hermes chat`.

### Step 3 — Connect a model

A **model** is the AI that writes the responses. A **provider** is the service that runs that model. This profile does not include an account, subscription, or API key, so you choose your own.

#### Recommended beginner option: Nous Portal

Run:

```bash
starter-hermes setup --portal
```

Your browser will open. Sign in and approve the connection. This configures a model and Nous-managed tools without asking you to copy API keys into files.

#### Use another provider

If you already use OpenAI Codex, Anthropic, OpenRouter, Google, or another supported provider, run:

```bash
starter-hermes model
```

Follow the menu to choose the provider and model. Hermes will either open an official sign-in page or ask for that provider's API key.

> **Important, please read.**
>
> - Run setup through `starter-hermes`, not plain `hermes`. Every profile keeps its own credentials and settings.
> - Never paste an API key into a chat message, GitHub issue, or public file. Treat keys like a password.
> - Charges and subscription limits are controlled by the provider you choose, not by this repository.

### Step 4 — Start your first chat

Run:

```bash
starter-hermes chat
```

When the prompt appears, type:

```text
Explain what you can help me with in five bullet points.
```

You should receive a normal response. That means installation, profile setup, and model access are all working.

Try these next:

```text
Explain black holes without assuming I know physics.
```

```text
Research three recent developments in reusable rockets and cite the sources.
```

```text
Help me turn a rough app idea into a one-page plan.
```

Type `/quit` to leave the chat.

> **From the playbook: cite the AI you used.** When you use chat output for school work, name the tool and what you asked it to do. This is the same as citing a book or website. It's required on **yellow** (limited use) and **green** (open use) assignments. See [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) for the full citation steps.

### Step 5 — Check the profile

Run:

```bash
starter-hermes status
```

For a deeper configuration check, run:

```bash
starter-hermes doctor
```

You now have a working starter profile. Nice work — you did the hard part.

---

## What is a profile, really?

A profile is a separate Hermes setup. It has its own model selection, credentials, personality, sessions, and tool settings.

Installing this profile does **not** replace or modify your normal Hermes profile. Its files live at:

```text
~/.hermes/profiles/starter-hermes/
```

The `starter-hermes` shortcut simply tells Hermes to use that directory.

You can have many profiles. Each one is a different learning room.

---

## Why a tool may be unavailable

This profile permits web search, image understanding, image generation, and text-to-speech, but a permitted tool still needs a working provider.

If normal chat works but a tool does not:

1. Run `starter-hermes status` and read the provider/tool status.
2. If you use Nous Portal, run `starter-hermes portal status`.
3. Open the tool setup screen with `starter-hermes tools`.
4. Start a new chat after changing tool settings.

The profile deliberately blocks terminal, file, browser-control, automation, memory, skill-management, and subagent toolsets. **A disabled capability is not an installation failure.** It is a guardrail. We protect the boundary so you can focus on the learning.

---

## Shared language: a small glossary

The playbook says *"shared language is shared power."* Here are the words you'll see most in this profile.

| Term | What it means |
| --- | --- |
| **Profile** | A separate Hermes workspace with its own settings and personality. |
| **Model** | The AI that writes the response. |
| **Provider** | The service that runs the model (e.g., Nous Portal, OpenAI, Anthropic). |
| **Prompt** | The question or instruction you give the AI. Better prompts = better results. |
| **Hallucination** | When AI states something confidently that is actually wrong or made up. **Always verify AI output before using it.** |
| **Disclosure** | Naming the AI tool you used and describing what it helped you do. |
| **Process vs. Product** | We value how you learn (the process) as much as the final answer (the product). |

---

## Update the profile

Pull the newest personality, documentation, and audit script with:

```bash
hermes profile update starter-hermes
```

A normal update preserves your local `config.yaml`. This prevents an update from silently replacing settings you chose.

To intentionally restore the repository's current tool baseline as well, run:

```bash
hermes profile update starter-hermes --force-config
```

Then start a new chat.

> **From the playbook:** We update this profile at least once a year. The playbook is a living document. So is this.

---

## Remove the profile

Deleting this profile removes its local settings and conversation data. It does **not** uninstall Hermes itself.

```bash
hermes profile delete starter-hermes
```

Read the confirmation carefully before accepting it. The same rule from the playbook applies here: **before any consequences, we read carefully.**

---

## Troubleshooting

### `hermes` is not recognized or says `command not found`

Close and reopen the terminal after installing Hermes, then run:

```bash
hermes --version
```

On macOS or Linux, the executable is normally installed under `~/.local/bin`. If reopening the terminal does not help, follow the official [installation troubleshooting guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

### `starter-hermes` is not recognized

Close and reopen the terminal. You can always use the full profile form:

```bash
hermes -p starter-hermes chat
```

### Hermes says no model or provider is configured

Run one of these, then retry the chat:

```bash
starter-hermes setup --portal
```

```bash
starter-hermes model
```

### Authentication failed

Check the saved authentication state:

```bash
starter-hermes auth status
```

Then run `starter-hermes model` and sign in again or replace the rejected API key. **Do not post keys in a support request.**

### The profile is already installed

Update the existing installation:

```bash
hermes profile update starter-hermes
```

If you truly want to start over, delete the profile first. Deletion also removes its local sessions and settings.

### Chat works, but search or media tools do not

The selected model provider and the optional tool providers are separate. Run `starter-hermes portal status`, `starter-hermes tools`, and `starter-hermes doctor` to see what is configured.

### You still need help

Run:

```bash
starter-hermes dump
```

Share that diagnostic summary, **not** your `.env`, `auth.json`, API keys, or tokens. The main Hermes documentation is at [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/).

---

## Optional: verify the narrow tool baseline

This repository includes an audit for people who want to verify that the installed profile still resolves to the intended toolsets.

On macOS, Linux, or WSL2:

```bash
HERMES_HOME="$HOME/.hermes/profiles/starter-hermes" \
  python "$HOME/.hermes/profiles/starter-hermes/scripts/audit_profile.py"
```

The last line should begin with `PASS`. This audit is optional; it is not required to start chatting.

---

## Design and limitations

[`DESIGN.md`](DESIGN.md) explains the exact tool policy and privacy defaults.

This profile reduces tool access; it is **not** an operating-system sandbox and it does not guarantee that every model response will be correct or appropriate. Review important information and use a qualified professional for consequential medical, legal, or financial decisions.

> *"Learning takes effort. Use AI when approved, not to skip the thinking."*
> — HHCS AI Playbook, Student Commitments

---

## A note for families and educators

This profile is built on the same principles as the HHCS AI Community Playbook: **learning is a human endeavor.** Hermes is a tool, not a teacher. The guardrails in `config.yaml` are designed to keep the first experience with an AI agent focused on:

- **supporting**, not replacing, the thinking process;
- **transparency** about what AI was used and how; and
- **protecting** privacy — no memory, no PII, no secret keys stored in the profile.

If you are a parent or educator, see [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) for a kid-friendly version of the AI Playbook that ships with this profile.

---

## License

MIT

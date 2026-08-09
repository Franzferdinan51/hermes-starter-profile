# Hermes Starter Profile

### A Beginner's Welcome Bundle — Built on the Warrior Way

> *"Learn matters most. Set the guardrails. Be partners in this work."*
> — Huber Heights City Schools AI Community Playbook

A friendly, calm way to try **Hermes Agent** for the first time without turning on the full system-administration toolset. We wrote it for **students, families, and educators** who want to learn by doing, with the same spirit as the HHCS AI Playbook: **process over product, transparency over shortcuts, and people at the center of learning.**

You don't need to know Git, Python, YAML, or what an "agent profile" is. We start at zero and walk through it together.

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Profile version](https://img.shields.io/badge/version-0.3.0-blue)](distribution.yaml)
[![HHCS compatibility test](https://img.shields.io/badge/HHCS-compatibility%20test-orange)](STUDENT_GUIDE.md)
[![Hermes](https://img.shields.io/badge/Hermes-%E2%89%A5%200.20.0-purple)](https://hermes-agent.nousresearch.com/)

> ## Important: compatibility test, not HHCS approval
>
> This repository is a **test to see whether this Hermes starter profile is compatible with the attached HHCS AI Community Playbook** (updated May 2026, Policy EDEC). It is **not** an HHCS product, district approval, legal interpretation, or official implementation of the plan. I may be unaware of additional HHCS rules, Board policies, teacher instructions, approved-tool requirements, age limits, privacy requirements, or later updates. **Those rules may be stricter than this repository.**
>
> The official HHCS rules and the student's teacher or administrator always control. If they conflict with this README, `STUDENT_GUIDE.md`, or the profile, **stop and follow HHCS guidance**. Ask the teacher or district before using this profile for schoolwork. No assignment may use AI unless the educator has labeled it GREEN or YELLOW; RED assignments are human-only. Even when use is allowed, use the district's Approved Tool List and follow every disclosure, verification, privacy, and citation requirement.
>
> **This is not a complete HHCS compliance review.** The public HHCS information I could verify does not establish every current classroom rule, building rule, approved-tool decision, privacy condition, age requirement, or implementation detail. Treat this repository as an experiment that needs HHCS review before school deployment.
---

## What's in this README

1. [Our three pillars](#our-three-pillars-from-the-hhcs-playbook)
2. [What you will get](#what-you-will-get)
3. [Five-step setup](#five-step-setup)
4. [What is a profile, really?](#what-is-a-profile-really)
5. [Why a tool may be unavailable](#why-a-tool-may-be-unavailable)
6. [Shared language: a small glossary](#shared-language-a-small-glossary)
7. [Update, remove, troubleshoot](#update-the-profile)
8. [A note for families and educators](#a-note-for-families-and-educators)
9. [Official HHCS sources checked](#official-hhcs-sources-checked)
10. [Design, limitations, and license](#design-and-limitations)

> **Looking for the kid-friendly version?** Open [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) — a student-facing companion to the HHCS AI Playbook that ships with this profile.

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

After following the five-step setup, you will have a separate command named `starter-hermes`. Imagine it as a **study buddy in a small box** — it can:

- answer questions and explain unfamiliar topics in plain language;
- search the web and cite sources when search is configured;
- look at images and tell you what is in them;
- draw pictures for creative projects;
- read text out loud; and
- help with writing, brainstorming, research, and planning.

It **cannot** open a terminal, change files, take over your browser, control your computer, run tasks while you sleep, or make other AI helpers. We leave those off on purpose so your first time with Hermes is easier to understand. Less noise, more learning.

### A quick "before you start" card

| ✅ This profile is for you if… | ❌ This profile is **not** for you if… |
| --- | --- |
| You want to learn, not just get answers. | You want Hermes to run terminal commands, edit files, or take over your computer. |
| You want a calm, low-overwhelm way to start. | You want every Hermes tool turned on with no guardrails. |
| You're a student, family, or educator exploring AI. | You want full system-administration power — install a different profile. |
| You want to follow your school's AI guidelines. | You want AI to do an assignment for you without thinking. |

> **Privacy, plain and short.** This profile has **memory off**, **PII redaction on**, and **no secret keys stored**. It may still send your prompts to the model provider you choose, and the provider's privacy and retention rules also apply. Never enter confidential student or staff information. The HHCS playbook and official district privacy rules take priority over this profile.

> **What to do next.** Skip to [Five-step setup](#five-step-setup) if you're ready. If you want a one-paragraph explainer first, read [What is a profile, really?](#what-is-a-profile-really). If a word confused you, jump to [Shared language](#shared-language-a-small-glossary).

---

## Five-step setup

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
hermes profile install github.com/Franzferdinan51/hermes-starter-profile --alias
```

> **Which URL is this?** This profile lives at `github.com/Franzferdinan51/hermes-starter-profile`, a fork of `teknium1/hermes-starter-profile`. The fork carries the playbook-aligned personality and the `STUDENT_GUIDE.md`. Installing from the fork makes sure you get the version this README describes.

Hermes will show you a preview of what is about to change. It should mention:

- a new profile named `starter-hermes`, and
- a new shortcut command, also named `starter-hermes`.

Confirm when it asks. Then check that the shortcut works:

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

> **Schoolwork rule.** This profile cannot decide whether an assignment is RED, YELLOW, or GREEN. Your educator decides. If use is allowed, HHCS says students and teachers should use software on the [District Approved List](https://sdpc.a4l.org/district_listing.php?districtID=4804). Verify that `starter-hermes` is approved before using it for schoolwork; if it is not listed, do not use it for that assignment. Follow any stricter classroom, building, district, state, or federal rule.
>
> **From the playbook: cite the AI you used.** When you use permitted chat output for school work, name the tool and what you asked it to do. This is the same as citing a book or website. It is required on **yellow** (limited use) and **green** (open use) assignments. See [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) for the full disclosure steps.

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

### Where to go next

- **Read [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md)** for the kid-friendly version of the playbook that ships with this profile.
- **Try a school-style prompt** (and disclose it): *"Explain the Pythagorean theorem step-by-step, then give me two practice problems. I'll show my work for each."*
- **Talk it through.** If a response looks wrong, ask the model where it got the information. That is the human-in-the-loop part.

---

## What is a profile, really?

A profile is a separate Hermes setup. It has its own model selection, credentials, personality, sessions, and tool settings.

Installing this profile does **not** replace or modify your normal Hermes profile. Its files live at:

```text
~/.hermes/profiles/starter-hermes/
```

The `starter-hermes` shortcut simply tells Hermes to use that directory.

You can have many profiles. Each one is a different learning room.

> **From the playbook:** *"Ensure equitable access — AI should not widen the digital divide."* A separate profile means a student can experiment with AI without affecting the family's normal setup, and a teacher can give every student the same clean starting point.

---

## Why a tool may be unavailable

This profile permits web search, image understanding, image generation, and text-to-speech, but a permitted tool still needs a working provider.

If normal chat works but a tool does not:

1. Run `starter-hermes status` and read the provider/tool status.
2. If you use Nous Portal, run `starter-hermes portal status`.
3. Open the tool setup screen with `starter-hermes tools`.
4. Start a new chat after changing tool settings.

The profile deliberately blocks terminal, file, browser-control, automation, memory, skill-management, and subagent toolsets. **A disabled capability is not an installation failure.** It is a guardrail. We protect the boundary so you can focus on the learning.

> **Not sure what a word means?** Open [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) and look at the **Shared language** section. Every term used in this README is defined there in plain language.

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
| **Human-in-the-loop** | A person (you or your teacher) always reviews, verifies, and takes responsibility for any AI-generated content. |
| **Process vs. product** | We value how you learn (the process) as much as the final answer (the product). |

---

## A note for families and educators

This profile is built on the same principles as the HHCS AI Community Playbook: **learning is a human endeavor.** Hermes is a tool, not a teacher. The guardrails in [`config.yaml`](config.yaml) are designed to keep the first experience with an AI agent focused on:

- **supporting**, not replacing, the thinking process;
- **transparency** about what AI was used and how; and
- **protecting** privacy — no memory, no PII, no secret keys stored in the profile.

If you are a parent or educator, see [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) for a kid-friendly version of the AI Playbook that ships with this profile. It includes the Red / Yellow / Green framework, the AI glossary, the response protocol, and the role commitments for students, families, educators, and district leadership.

If a first AI-misuse moment happens, **the playbook's response is the playbook's response here too:** start with a conversation, not a punishment. Ask what the student was learning, what they asked the AI to do, and how they verified the output. Transparency tools the conversation. Trust first, judgment second.

---

## Update, remove, troubleshoot

### Update the profile

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

### Remove the profile

Deleting this profile removes its local settings and conversation data. It does **not** uninstall Hermes itself.

```bash
hermes profile delete starter-hermes
```

Read the confirmation carefully before accepting it. The same rule from the playbook applies here: **before any consequences, we read carefully.**

### Troubleshooting

#### `hermes` is not recognized or says `command not found`

Close and reopen the terminal after installing Hermes, then run:

```bash
hermes --version
```

On macOS or Linux, the executable is normally installed under `~/.local/bin`. If reopening the terminal does not help, follow the official [installation troubleshooting guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

#### `starter-hermes` is not recognized

Close and reopen the terminal. You can always use the full profile form:

```bash
hermes -p starter-hermes chat
```

#### Hermes says no model or provider is configured

Run one of these, then retry the chat:

```bash
starter-hermes setup --portal
```

```bash
starter-hermes model
```

#### Authentication failed

Check the saved authentication state:

```bash
starter-hermes auth status
```

Then run `starter-hermes model` and sign in again or replace the rejected API key. **Do not post keys in a support request.**

#### The profile is already installed

Update the existing installation:

```bash
hermes profile update starter-hermes
```

If you truly want to start over, delete the profile first. Deletion also removes its local sessions and settings.

#### Chat works, but search or media tools do not

The selected model provider and the optional tool providers are separate. Run `starter-hermes portal status`, `starter-hermes tools`, and `starter-hermes doctor` to see what is configured.

#### You still need help

Run:

```bash
starter-hermes dump
```

Share that diagnostic summary, **not** your `.env`, `auth.json`, API keys, or tokens. The main Hermes documentation is at [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/).

---

## Optional: verify the narrow tool baseline

This repository includes an audit for people who want to verify that the installed profile still resolves to the intended toolsets.

On macOS, Linux, or WSL2, use **Python 3.11 or newer**. Hermes' resolver uses modern Python type syntax, so an older system Python may report an import error even when the profile is configured correctly:

```bash
HERMES_HOME="$HOME/.hermes/profiles/starter-hermes" \
  python3.11 "$HOME/.hermes/profiles/starter-hermes/scripts/audit_profile.py"
```

If your system does not have `python3.11`, install a current Python release or use the Python executable bundled with your Hermes environment. The last line should begin with `PASS`. This audit is optional; it is not required to start chatting.

---

## Official HHCS sources checked

This README was checked against the attached **HHCS AI Community Playbook** (updated May 2026, Policy EDEC) and the following publicly available Huber Heights City Schools sources:

- [HHCS Board of Education policy portal](https://go.boarddocs.com/oh/huhe/Board.nsf/Public?open=&id=policies) — official location for Board policies, including Policy EDEC. The portal may require its own search or access path.
- [HHCS Technology](https://www.myhhcs.org/technology) — identifies Technology Services as supporting the district's operational and educational technology environments.
- [HHCS Curriculum & Instruction](https://www.myhhcs.org/curriculum-instruction) — identifies the department responsible for curriculum, instructional resources, assessment, and staff development.
- [HHCS official Facebook post about the AI Playbook](https://www.facebook.com/HHCSdistrict/posts/huber-heights-city-schools-created-its-ai-playbook-in-the-spring-of-2026-hhcs-en/1611769114285691) — public district communication about the playbook's purpose and learning-focused approach.
- [HHCS official Facebook post about student AI use](https://www.facebook.com/HHCSdistrict/posts/huber-heights-city-schools-district-surveys-showed-that-hhcs-students-are-alread/1613582240771045) — public district communication indicating that HHCS students are already engaging with AI.

These sources support the need for a careful, learning-centered compatibility test. They do **not** prove that this Hermes profile is approved for use by HHCS. The attached playbook and current direction from HHCS staff remain the controlling sources. Re-check the official HHCS policy portal and district communications for updates before relying on this profile.

---

## Design and limitations

[`DESIGN.md`](DESIGN.md) explains the exact tool policy and privacy defaults.

This profile reduces tool access; it is **not** an operating-system sandbox and it does not guarantee that every model response will be correct or appropriate. Review important information and use a qualified professional for consequential medical, legal, or financial decisions.

> *"Learning takes effort. Use AI when approved, not to skip the thinking."*
> — HHCS AI Playbook, Student Commitments

---

## A closing thought

> *"We want to be partners in this. Tell us the rules, tell us the tools, and help us help our kids at home."*
> — HHCS Parent

This profile is one small part of that partnership. Help the learner **think**, **cite**, and **keep going**. That's the whole job.

---

## License

MIT

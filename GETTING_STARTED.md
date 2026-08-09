# Getting started

> *"Learn matters most. Set the guardrails. Be partners in this work."*
> — Huber Heights City Schools AI Community Playbook

The complete beginner walkthrough now lives in [`README.md`](README.md). It covers installing Hermes, installing this profile, connecting a model, starting the first chat, troubleshooting, updating, and removing the profile.

We keep this file short because **process over product** — the goal is for you to start learning, not to read another wall of setup.

### The shortest path for an existing Hermes installation

```bash
hermes profile install github.com/Franzferdinan51/hermes-starter-profile --alias
starter-hermes model
starter-hermes chat
```

Before `starter-hermes model`, start the LM Studio Developer server at `http://localhost:1234/v1`. Select **LM Studio** and choose a loaded local model. This profile defaults to LM Studio; cloud providers are optional. See the [LM Studio setup section in the README](README.md#step-3--connect-a-local-model-in-lm-studio).

### Before you start chatting

> **From the playbook:** *"Verify AI output; it can 'hallucinate' wrong or made-up information."*

This profile defaults to LM Studio, but local does not mean automatically approved for HHCS schoolwork. Check the HHCS District Approved List and ask the educator before using it for an assignment.

AI is a learning assistant. The thinking is yours. When you use permitted chat output for school work, **disclose** what you used and how:

1. **Name the tool** — e.g., `starter-hermes`.
2. **Describe the use** — e.g., *"I asked the AI to brainstorm five essay topics."*
3. **Show verification** — what did you check, and what did you change?

For the full kid-friendly guide (Red / Yellow / Green assignments, glossary, and your role as a learner), open [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md).

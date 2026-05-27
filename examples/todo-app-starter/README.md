[![Built with Vibe Coding Protocols](https://img.shields.io/badge/Built%20with-Vibe%20Coding%20Protocols-blue)](https://github.com/Gudvin82/vibe-coding-protocols)

# todo-app-starter

> Synthetic example — not a real production project.
> Use it to understand the workflow, not as a production template.

Synthetic runnable example for the Starter path.

This is a learning example, not a production app.

It demonstrates:
- how a tiny Product Brief becomes a first vertical slice;
- how `AGENTS.md`, `PROJECT_MAP.md` and `ARCHITECTURE.md` keep project memory explicit;
- how `AUDIT_BACKLOG.md` records hardening follow-up;
- how to run `vibe-check` against a small project.

## What is in this example

- minimal Node.js app using the built-in `http` module;
- one in-memory task list;
- basic smoke test with Node's built-in test runner;
- `.env.example`, but no real `.env`;
- starter artifacts and hardening notes.

## Run it

```bash
npm install
npm test
npm start
```

Then open:
- `http://localhost:3000/health`
- `http://localhost:3000/api/tasks`

## Run vibe-check

From the repository root:

```bash
bash scripts/vibe-check.sh --starter
```

## Before / after hardening example

```js
// before: secret in code
const token = "example-token-do-not-use";

// after: read from env
const token = process.env.APP_TOKEN;
```

## How this maps to VCP

- `PRODUCT_BRIEF.md` explains the first safe slice.
- `AGENTS.md` constrains AI behavior.
- `PROJECT_MAP.md` shows the small code surface.
- `ARCHITECTURE.md` keeps the architecture summary short and explicit.
- `AUDIT_BACKLOG.md` tracks what still needs hardening.

## Notes

- No database is used here.
- No real secrets are used here.
- This example is intentionally small so teams can copy the structure without inheriting unnecessary complexity.

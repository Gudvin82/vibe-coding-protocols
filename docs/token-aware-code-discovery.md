# Token-Aware Code Discovery

## Goal

Find relevant code without burning context on the whole repository.

## Default read order

1. `README.md`
2. `AGENTS.md` / `CLAUDE.md`
3. `PROJECT_MAP.md`
4. `ARCHITECTURE_SOURCE_OF_TRUTH.md`
5. package/build/config files
6. routes/endpoints/components relevant to the task
7. tests relevant to the touched surface
8. only then deeper search

## Repository size tiers

### Tiny repo
Read README, file tree and relevant files.

### Small repo
Use `PROJECT_MAP.md` first, then targeted search.

### Medium repo
Use an evidence map: path, symbol, snippet, why it matters.

### Large repo
Delegate broad discovery to a cheaper or faster subagent if available,
then return a compact evidence map.

## Discovery-agent pattern

When broad code discovery is needed, keep the main agent focused on decisions and implementation.

Use a cheaper, faster or read-only discovery agent when available.

The discovery agent must return only a compact evidence map:

| path:line | symbol / route / component | snippet / signature | why it matters |
|---|---|---|---|
| `src/api/tasks.js:18` | `createTask()` | `createTask(input)` | writes user-controlled data |
| `app/routes/admin.ts:4` | `/admin` | `router.get('/admin')` | sensitive route requires review |

The main agent must:
- use the evidence map for targeted reading;
- verify critical findings before editing;
- avoid reading the whole repo unless needed;
- update `PROJECT_MAP.md` if discovery reveals outdated project memory.

## Model routing

For large repositories, use model routing:
- discovery model for search;
- implementation model for edits;
- reviewer model for independent review.

Never pass a huge search transcript to the implementation agent.
Pass a compact evidence map.

Evidence map format:

| path:line | symbol / route / component | evidence | why it matters | confidence |
|---|---|---|---|---|
| `src/auth/session.ts:44` | `issueSessionCookie()` | `setCookie('session', ...)` | auth cookie policy matters | `medium` |
| `app/routes/login.ts:19` | `POST /login` | `router.post('/login')` | brute-force protection surface | `high` |

### Codex

If available, delegate broad repository search to a cheaper or faster Codex subagent such as Codex Spark.
If Spark is not available, use the least expensive capable read-only agent.

### Claude Code

Use a read-only subagent for repository discovery when available.
The implementation agent should receive only the evidence map, not the whole search transcript.

### Cursor / Windsurf / Copilot

Use the same principle manually: first ask for a compact map of relevant files, then ask for targeted implementation.

## Measurement note

Do not claim token savings without measurement.

If you want to measure savings, record:
- model used;
- number of files inspected;
- approximate tokens or context used;
- number of implementation iterations;
- final validation result.

## Stop reading when

- the relevant entrypoint is found;
- the touched surface is clear;
- more reading is not changing the plan;
- a `PROJECT_MAP.md` refresh is needed.

## Report format

- paths inspected;
- relevant symbols;
- files not inspected;
- confidence;
- next targeted read.

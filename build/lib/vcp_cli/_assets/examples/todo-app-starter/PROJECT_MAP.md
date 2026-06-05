# PROJECT_MAP

## Overview

Small runnable todo service with one list/create/complete flow.

## Entrypoints

- `src/index.js`
- `tests/smoke.test.js`

## Main routes

- `GET /health`
- `GET /api/tasks`
- `POST /api/tasks`
- `POST /api/tasks/:id/complete`

## Main components

- `createApp()` — creates the HTTP handler and in-memory store
- `readJsonBody()` — minimal request parsing helper
- `sendJson()` — consistent response helper

## Active / deferred surfaces

- active: backend/API, test, starter docs
- deferred: auth, database, admin, background jobs, rate limiting

## Known risks

- no persistence
- no auth
- basic input validation only
- no rate limiting

# ARCHITECTURE

## Purpose

Runnable starter example for learning the VCP workflow.

## Main flow

1. Client checks `/health`
2. Client lists tasks via `GET /api/tasks`
3. Client creates a task via `POST /api/tasks`
4. Client marks a task complete via `POST /api/tasks/:id/complete`

## Data model

In-memory array of:
- `id`
- `title`
- `completed`
- `createdAt`

## Env / secrets policy

- use `.env.example` for documented env names only
- keep real secrets out of the repository
- prefer env-based config over hardcoded tokens

## Deploy path

Local run only for this example.

## Known risks

- no persistence
- no auth boundary
- no abuse controls
- no production logging or monitoring

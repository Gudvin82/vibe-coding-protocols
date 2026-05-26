# PROJECT_MAP

## Overview

A small task management app with one main user journey.

## Entrypoints

- `app/page.tsx`
- `app/api/tasks/route.ts`
- `lib/db.ts`

## Main routes

- `/`
- `/api/tasks`

## Data model

- `users`
- `tasks`

## Integrations

- PostgreSQL or Supabase-compatible database

## Active / deferred surfaces

- active: web, backend/API, database
- deferred: mobile, admin, AI assistant, payments

## Risks

- auth model still minimal
- rate limit strategy not defined yet
- mobile QA deferred until Light Hardening

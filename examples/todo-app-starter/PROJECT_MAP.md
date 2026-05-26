# PROJECT_MAP

## Overview

Small web application with one main task list flow.

## Entrypoints

- `app/page.tsx`
- `app/api/tasks/route.ts`

## Main routes

- `/`
- `/api/tasks`

## Data model

- `users`
- `tasks`

## Integrations

- `postgresql` or `supabase-compatible database`

## Active / deferred surfaces

- active: web, backend/API, database
- deferred: mobile, payments, AI features, admin

## Known risks

- auth still basic
- indexes for larger lists deferred until hardening

# Example: AI-generated MVP hardening

Условный пример, не реальный клиентский кейс.

## Situation

AI собрал MVP.

## What was found

- secret-looking placeholder in public code
- no `PROJECT_MAP.md`
- scanner status unknown
- no `AUDIT_BACKLOG.md`
- auth flow not clearly documented

## Hardening route

- start with Light Hardening
- create `PROJECT_MAP.md`
- create `AUDIT_BACKLOG.md`
- mark scanners `not run` if unavailable
- run independent diff review before deploy

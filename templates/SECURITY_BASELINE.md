# SECURITY_BASELINE.md

## Secrets
- secrets are not stored in repo
- `.env` is ignored
- `.env.example` is sanitized
- no tokens in frontend code

## Access
- admin routes are protected
- internal endpoints are not exposed without reason
- least privilege for workers and scanners

## Public exposure
- no `.git/`
- no `.env`
- no backups / dumps / logs in public root
- no stack traces / debug routes in public mode

## Supply chain
- dependencies are reviewed
- install scripts are known
- external repos/APIs are tracked
- update path is explicit

## Validation
- build/test status known
- scanner status known or marked `not run`
- follow-ups added to backlog

<!-- vcp-artifact: SECURITY_BASELINE -->
<!-- vcp-version: v0.2.0 -->
<!-- methodology-version: v1.4 -->

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

## Auth/session baseline
- [ ] Auth cookies use HttpOnly
- [ ] Auth cookies use Secure in production
- [ ] Auth cookies use SameSite=Lax/Strict
- [ ] Password hashing uses argon2id, bcrypt or scrypt
- [ ] Login/password reset endpoints are rate-limited
- [ ] Credential stuffing protection considered
- [ ] Admin auth has stronger controls
- [ ] User enumeration risks reviewed

## Public exposure
- no `.git/`
- no `.env`
- no backups / dumps / logs in public root
- no stack traces / debug routes in public mode
- Content-Security-Policy / frame-ancestors / X-Frame-Options / Referrer-Policy / Permissions-Policy considered

## Supply chain
- dependencies are reviewed
- install scripts are known
- external repos/APIs are tracked
- update path is explicit

## Validation
- build/test status known
- scanner status known or marked `not run`
- follow-ups added to backlog

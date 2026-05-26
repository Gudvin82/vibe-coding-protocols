# Auth and Session Security

## Auth cookies baseline

- Use `HttpOnly` for session cookies.
- Use `Secure` in production.
- Use `SameSite=Lax` or `SameSite=Strict` where practical.
- Keep TTL short where practical.
- Document refresh token policy.
- Invalidate sessions on logout where applicable.
- Rotate sessions after password reset or equivalent recovery flow.
- Do not default to storing auth tokens in `localStorage` unless explicitly justified.

## Credential stuffing

- Add rate limits for login and password reset.
- Detect suspicious login spikes.
- Use lockout, throttling or progressive delay where appropriate.
- Consider invisible captcha, Turnstile or equivalent challenge where abuse risk is high.
- Require MFA for admin accounts where practical.
- Monitor repeated failed login patterns.

## Password hashing

Do not use:
- MD5
- SHA-1
- SHA-256 directly for passwords

Use:
- `argon2id`
- `bcrypt`
- `scrypt`

## Session hijacking caveat

`HttpOnly`, `Secure` and `SameSite` are baseline protections.
They are not complete account takeover defense.

Modern protection may also involve:
- device fingerprinting;
- IP or GEO anomaly detection;
- user-agent mismatch checks;
- impossible travel detection;
- risk-based re-authentication.

Do not treat cookie flags as complete anti-fraud protection.

## Tests to add

- session cookie has `HttpOnly`
- session cookie has `Secure` in production
- `SameSite` is set
- password reset is rate-limited
- login endpoint is rate-limited
- admin route requires stronger auth

## Notes

This document is a baseline guide, not a guarantee.
Projects with payments, regulated data or high-abuse surfaces usually need deeper product, security and infrastructure work.

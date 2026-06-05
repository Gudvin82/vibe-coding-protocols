# Testing Cookbook

These test ideas are stack-neutral.
Use them as prompts, pseudo-tests or acceptance criteria before asking AI to generate framework-specific tests.

## Auth boundary test

What it catches:
- anonymous access to protected routes;
- missing backend checks;
- frontend-only auth.

Pseudo-test:
```text
Call a protected route without auth.
Expect 401/403.
Repeat with valid auth and expect success.
```

AI prompt:
```text
Generate an auth boundary test for the protected routes in this repo.
Cover anonymous, valid user and expired-token cases.
```

Common mistakes:
- testing only the UI redirect;
- not checking the backend response.

## Permission / role test

What it catches:
- admin actions exposed to regular users;
- role checks applied only in one layer.

Pseudo-test:
```text
User A has reader role.
User A attempts admin action.
Expect denial and audit log entry if logging exists.
```

AI prompt:
```text
Generate permission tests for reader, editor and admin roles on the risky endpoints.
```

Common mistakes:
- no negative cases;
- assuming “logged in” means “authorized”.

## Webhook idempotency test

What it catches:
- duplicate processing;
- replay bugs;
- queue duplication.

Pseudo-test:
```text
Send the same webhook payload twice.
Expect one business effect, one stored event or idempotent duplicate handling.
```

AI prompt:
```text
Generate an idempotency test for repeated webhook delivery using the current event handler contract.
```

Common mistakes:
- checking only HTTP 200;
- not checking downstream duplicate side effects.

## Payment callback test

What it catches:
- forged callbacks;
- inconsistent order state;
- double payment confirmation.

Pseudo-test:
```text
Send valid signed callback.
Expect correct state transition.
Send invalid signature.
Expect rejection.
```

AI prompt:
```text
Generate payment callback tests with valid signature, invalid signature and duplicate callback cases.
```

Common mistakes:
- trusting callback payload without signature;
- not testing repeated callback delivery.

## API rate-limit test

What it catches:
- unlimited public endpoints;
- brute-force risk;
- cost runaway on AI endpoints.

Pseudo-test:
```text
Call the same public endpoint N times quickly.
Expect throttling, retry response or explicit quota behavior.
```

AI prompt:
```text
Generate a rate-limit smoke test for public auth, form and AI endpoints.
```

Common mistakes:
- testing only happy path;
- not checking error shape and retry behavior.

## File upload validation test

What it catches:
- invalid file types;
- oversized uploads;
- unsafe filenames.

Pseudo-test:
```text
Upload allowed file -> accept.
Upload disallowed type -> reject.
Upload oversized file -> reject.
```

AI prompt:
```text
Generate upload validation tests covering size, type and dangerous filename handling.
```

Common mistakes:
- validating only file extension;
- no backend-side size/type check.

## Migration rollback smoke test

What it catches:
- one-way schema change panic;
- broken rollback path;
- incompatible deploy sequence.

Pseudo-test:
```text
Apply migration in staging-like environment.
Run minimal critical query.
Roll back.
Run minimal critical query again.
```

AI prompt:
```text
Generate a migration rollback smoke checklist and test skeleton for the current database layer.
```

Common mistakes:
- testing only apply, not rollback;
- no backup point before risky migration.

## UI critical path smoke test

What it catches:
- happy path broken after AI edits;
- missing routing or state wiring.

Pseudo-test:
```text
Open main page.
Complete the primary user flow.
Confirm expected final state and visible success signal.
```

AI prompt:
```text
Generate a UI smoke test for the primary user path in this repo.
Use the current routes and user-visible success states.
```

Common mistakes:
- testing components in isolation only;
- no primary end-to-end smoke path.

## AI / LLM endpoint cost limit test

What it catches:
- runaway usage;
- missing quota/cost guardrails;
- repeated retries without budget.

Pseudo-test:
```text
Trigger repeated LLM calls past expected quota.
Expect refusal, throttle or budget guard behavior.
```

AI prompt:
```text
Generate tests for AI endpoint quota, retry limits and cost guardrails.
```

Common mistakes:
- testing only success output;
- not checking retry/cost boundaries.

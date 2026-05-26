# DATABASE_LOAD_READINESS

## Current notes

- expected high-growth tables: users, subscriptions, events, jobs
- migration history required
- indexes needed for subscriptions and event lookups
- long-running exports should be async
- rate limits and idempotency are required for webhooks

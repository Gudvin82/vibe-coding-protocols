# DATABASE_LOAD_READINESS

## Notes

- expected high-growth tables: users, subscriptions, jobs, events
- migration history required
- indexes needed for webhook and subscription lookups
- heavy exports should be async
- rate limits and idempotency are required

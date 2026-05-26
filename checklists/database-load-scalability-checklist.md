# Database / load / scalability checklist

## When to use

После first slice и перед production-like growth claims.

## Checklist
- migrations exist
- indexes match query patterns
- no obvious N+1 in critical path
- sync vs async operations reviewed
- retries / backoff / idempotency considered
- external API/LLM bottlenecks identified
- backup / restore path known
- scalability backlog updated

## Protocol

See: [../protocols/ai-project-hardening-protocol.md](../protocols/ai-project-hardening-protocol.md)

Choose a stack and explain why it fits this project.

Return:
- recommended stack;
- simpler alternative;
- safer production-ready alternative;
- primary database;
- expected growing entities / tables;
- migration strategy;
- index strategy;
- background jobs needed now / later;
- caching needed now / later;
- rate limit / external API quota risks;
- idempotency needs;
- first likely bottleneck;
- what is intentionally deferred.

Consider modern 2025+ stack options where relevant:
- Edge runtime: Cloudflare Workers, Vercel Edge
- Serverless Postgres: Neon, Supabase, Turso
- Auth: Clerk, Better Auth, Supabase Auth
- Queues/jobs: Cloudflare Queues, BullMQ, Temporal
- AI apps: rate limits, cost caps, prompt injection defense

Mention these only when they fit the project constraints.
Do not propose complexity without a reason. If the chosen path creates an architectural dead end at moderate growth, say so clearly and suggest a more durable alternative without overengineering.

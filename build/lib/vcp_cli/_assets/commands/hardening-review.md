# Hardening Review Command

Use when the project already has AI-generated code and needs a structured hardening pass.

Prompt:

Review this repository using the Hardening route.

1. Do token-aware discovery first.
2. Return an evidence map for the touched security surfaces.
3. Check auth, secrets, external dependencies, error handling, tests and deployment risk.
4. Add or update `AUDIT_BACKLOG.md` findings.
5. Separate blockers, accepted risks and follow-up work.
6. Do not rewrite broad parts of the repository unless the map proves it is necessary.

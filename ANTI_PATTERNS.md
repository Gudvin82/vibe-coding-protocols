# Vibe Coding Anti-Patterns

These are common failure modes in AI-assisted / vibe-coded projects.

## 1. Infinite generation loop

AI fixes one issue and breaks another, then loops.

How VCP helps:
- Stop Conditions
- smaller diffs
- validation before next change
- independent diff review

## 2. Dependency hallucination

AI invents libraries, packages or APIs.

How VCP helps:
- safe third-party intake
- package existence check
- lockfile review
- supply-chain checklist

## 3. Beautiful empty code

The code looks clean but does not implement the actual product flow.

How VCP helps:
- Product Brief
- active/deferred surfaces
- critical path tests

## 4. Frontend-only security

Auth or access control exists only in UI.

How VCP helps:
- Hardening Protocol
- backend validation
- security baseline

## 5. Accidental production exposure

Internal docs, env, logs or debug routes become public.

How VCP helps:
- self-protection checklist
- public exposure checks
- private/sanitized docs policy

## 6. Massive rewrite by AI

AI rewrites architecture instead of making a scoped change.

How VCP helps:
- Stop Conditions
- AGENTS.md
- approval gates
- rollback plan

## 7. Migration panic

AI-generated DB migration breaks data.

How VCP helps:
- migration rollback checklist
- staging check
- backup before production migration

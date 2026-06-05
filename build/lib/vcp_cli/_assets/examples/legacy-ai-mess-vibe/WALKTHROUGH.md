# Hardening Walkthrough

> Synthetic dirty example — not a real production case.

## 1. What was wrong

- hard-coded fake admin token example;
- no input validation;
- overly broad admin route;
- mixed config and route logic;
- weak error handling;
- no audit or rate-limit note.

## 2. Evidence map

- `before/app.js` mixes auth, config and route behavior;
- `before/app.js` accepts arbitrary `action` values;
- `before/app.js` can succeed with unsafe fallback behavior.

## 3. Findings

- auth behavior was not explicit enough;
- input validation was missing;
- high-risk admin operations had no backlog or security notes.

## 4. What changed

- moved token handling to environment config;
- added basic validation for `userId` and `action`;
- removed success-on-error behavior;
- added `PROJECT_MAP`, `AUDIT_BACKLOG` and `SECURITY_BASELINE`.

## 5. What stayed accepted risk

- no durable audit log yet;
- no rate limiting yet;
- still a tiny example, not a production-ready admin service.

## 6. What vibe-check catches

- missing or weak project memory files;
- env hygiene and obvious secret handling problems;
- content-quality gaps in backlog and baseline docs.

## 7. What vibe-check does not catch

- subtle auth logic flaws;
- framework-specific security details;
- business logic abuse cases without human review.

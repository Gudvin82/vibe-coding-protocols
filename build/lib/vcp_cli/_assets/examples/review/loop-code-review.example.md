# Example: Review With Findings, Fixes and Acceptance

Synthetic example. Not a real project claim.

## Situation

An AI task changed a small checkout flow and updated one API adapter.
The code passed unit tests, but the diff touched public request handling and error formatting.

## Review pass 1

Blocking findings:
- `src/api/checkout.ts:42` returns a raw upstream error body and may leak internal fields.
- `src/routes/checkout.ts:19` accepts a missing `currency` field and falls back silently, changing public behavior.

Non-blocking findings:
- `tests/checkout.test.ts` does not cover the error-shape branch added in this task.

## Fixes applied

- sanitized upstream error mapping in `src/api/checkout.ts`;
- restored explicit `currency` validation in `src/routes/checkout.ts`;
- added focused test coverage for the error-shape path.

## Validation

- `npm test -- checkout` -> passed
- `npm run lint` -> passed
- `npm run typecheck` -> passed

## Review pass 2

- no actionable findings
- optional score: `9.7/10`

## Acceptance

Accepted because:
- validation is green;
- follow-up review reports no actionable findings;
- public contract and error behavior are preserved.

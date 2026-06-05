<!-- vcp-version: v0.6.1 -->
<!-- methodology-version: v1.4 -->

# Spec Escape Hatch

Spec can be skipped only when the task is genuinely small and non-behavioral.

## Safe skip examples

- copy-only README fix
- typo fix
- local variable rename
- formatting-only edit
- small CSS polish with no behavior change

## Unsafe skip examples

- auth/session changes
- payments or billing
- persistence or migrations
- user data handling
- permissions
- production operations
- external APIs
- legal/compliance-sensitive work

## Rule

Skipping spec does not mean skipping validation.
Skipping spec does not mean skipping review when behavior changed.

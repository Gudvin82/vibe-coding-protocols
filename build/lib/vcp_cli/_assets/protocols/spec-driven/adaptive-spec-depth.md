<!-- vcp-version: v0.6.1 -->
<!-- methodology-version: v1.4 -->

# Adaptive Spec Depth Protocol

Use this protocol before forcing spec work.

## Goal

Choose the smallest safe spec depth for the requested change.

## Decision rule

1. If the task is mechanical and non-behavioral, allow `no-spec`.
2. If the task is an ordinary feature with bounded risk, choose `spec-lite`.
3. If the task touches auth, persistence, external APIs, user data, or cross-layer behavior, choose `full-spec`.
4. If the task is production-critical, billing-sensitive, migration-heavy, shared-engine, or compliance-sensitive, choose `governed-spec`.

## Required outputs

- recommended spec depth
- reason for the recommendation
- required artifacts
- required validation
- stop conditions

## Stop conditions

Stop and escalate when:
- the task looks tiny at first but hides cross-layer changes
- the user wants to skip spec for payments, auth, migrations, or external API work
- public release scope exists without review and release evidence

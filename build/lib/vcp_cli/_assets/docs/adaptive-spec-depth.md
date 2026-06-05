# Adaptive Spec Depth

VCP chooses the smallest safe workflow for your AI-assisted project.

Adaptive Spec Depth is the rule set that keeps VCP from becoming a bureaucratic spec-only kit.
It helps the repo choose between:
- `no-spec`
- `spec-lite`
- `full-spec`
- `governed-spec`

## Why this exists

Not every task needs a PRD.
A typo fix, copy edit, or local formatting pass should not be forced through the same flow as a payment webhook, auth migration, or public release.

## Spec depth table

| Task type | Recommended spec depth | Required artifacts | Gates |
|---|---|---|---|
| Typo, copy edit, small rename, non-behavioral formatting | `no-spec` | short note or backlog item, validation command | validation only |
| Ordinary feature, small UI flow, simple endpoint | `spec-lite` | one-page feature brief, acceptance criteria, validation plan, backlog item | validation + backlog linkage |
| Auth, persistence, external API, user data, cross-layer feature | `full-spec` | feature spec or PRD, acceptance criteria, tasks, architecture impact, backlog linkage | validation plan + review gate |
| Production-critical, billing, migrations, permissions, regulated or shared-engine work | `governed-spec` | PRD, feature spec, tasks, risk review, architecture update, release gate evidence | validation + review + release discipline |

## No-spec

Use for:
- typo
- copy edit
- small CSS tweak
- simple rename
- local docs update
- non-behavioral formatting
- dependency metadata update with no behavior change

Still required:
- short note or backlog item
- explicit validation command

## Spec-lite

Use for:
- ordinary feature
- small UI flow
- simple API endpoint
- low-to-medium risk task

Required:
- one-page feature brief
- acceptance criteria
- validation plan
- backlog item

## Full spec

Use for:
- complex feature
- auth/session
- payments or billing-adjacent flows
- persistence or migrations
- external API or SDK integration
- user data
- cross-layer changes

Required:
- PRD or feature spec
- acceptance criteria
- tasks
- architecture impact note
- review gate

## Governed spec

Use for:
- production-critical flows
- regulated data
- shared engine behavior
- billing/payment
- permissions
- migrations
- public release
- compliance-sensitive work

Required:
- PRD
- feature spec
- acceptance criteria
- task breakdown
- risk review
- architecture update
- validation plan
- post-task review
- release gate
- hardening route if needed

## Related

- [../protocols/spec-driven/adaptive-spec-depth.md](../protocols/spec-driven/adaptive-spec-depth.md)
- [spec-escape-hatch.md](./spec-escape-hatch.md)
- [spec-retrofit.md](./spec-retrofit.md)

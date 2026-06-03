# Anti-patterns

These are common AI-assisted development mistakes that VCP is designed to reduce.

## 1. README-only evaluation

Symptom:
- the repository is judged from top-level marketing text only

Why it is risky:
- routes, manifests, benchmarks, and limitations are missed

VCP countermeasure:
- `AI_EVALUATION_GUIDE.md`
- `AGENTS.md`
- `llms-full.txt`

## 2. AI writes code before Product Brief

Symptom:
- implementation starts before scope is stable

Why it is risky:
- AI fills in missing requirements with guesses

VCP countermeasure:
- Starter Protocol
- `START_HERE.md`

## 3. No architecture memory

Symptom:
- every new task rediscovers the same system shape

Why it is risky:
- cross-layer breakage and stale assumptions

VCP countermeasure:
- `PROJECT_MAP.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`

## 4. Copy every template blindly

Symptom:
- the whole toolkit is copied into a project without selection

Why it is risky:
- noise, confusion, and drift from the real repo context

VCP countermeasure:
- Adoption Packs
- `vcp adopt --dry-run`

## 5. No stop conditions

Symptom:
- AI keeps editing even after risk has changed

Why it is risky:
- scope creep and unsafe changes in production-sensitive areas

VCP countermeasure:
- route stop conditions
- root `AGENTS.md`

## 6. No post-task review

Symptom:
- meaningful AI-generated changes move forward without acceptance

Why it is risky:
- subtle regressions get normalized

VCP countermeasure:
- Post-Task Code Review Gate
- `protocols/review/post-task-code-review.md`

## 7. No validation before next feature

Symptom:
- work continues even though validation was not checked

Why it is risky:
- hidden failures accumulate

VCP countermeasure:
- `vcp check`
- `vcp benchmark run`
- `vcp manifest validate`

## 8. External API added without intake

Symptom:
- API code appears before owner/auth/terms/fallback are documented

Why it is risky:
- secret leaks, brittle integrations, and unknown legal/data boundaries

VCP countermeasure:
- Third-party API Intake
- `templates/THIRD_PARTY_REGISTRY.md`

## 9. Production logs ignored until users complain

Symptom:
- no read-only capture loop exists

Why it is risky:
- repeated failures stay anecdotal instead of actionable

VCP countermeasure:
- Production Error Capture
- Daily Error Triage

## 10. Backlog lives only in chat

Symptom:
- important work exists only in conversation history

Why it is risky:
- follow-up disappears and accountability drops

VCP countermeasure:
- `PROJECT_BACKLOG.md`
- `vcp backlog`

## 11. UI drift from hardcoded styles

Symptom:
- page-level visual logic spreads unpredictably

Why it is risky:
- frontend becomes expensive to maintain

VCP countermeasure:
- UI Component Ownership route

## 12. Refactoring without characterization tests

Symptom:
- behavior-preserving work is attempted without a validation path

Why it is risky:
- regressions hide inside “cleanup” work

VCP countermeasure:
- Maintenance Refactoring route
- focused validation before and after edits

## 13. Security checklist treated as optional

Symptom:
- sensitive repos are treated like toy demos

Why it is risky:
- production and regulated changes move forward without real gates

VCP countermeasure:
- Hardening routes
- security review scope
- review gate

## 14. Public site launched without `llms.txt`, sitemap, or structured-data discipline

Symptom:
- public content exists but is poorly explained to crawlers and answer engines

Why it is risky:
- weak discoverability and inconsistent trust signals

VCP countermeasure:
- Public Site Readiness
- Public Growth
- `docs/geo-ai-visibility.md`

## 15. AI-generated content published without review

Symptom:
- public pages go live because they look plausible

Why it is risky:
- misleading claims, mismatched schema, or low-trust content

VCP countermeasure:
- page brief
- public-growth audit
- review gate for meaningful claim changes

## 16. No progressive disclosure for large repos

Symptom:
- AI reads random top-level files or tries to scan the whole repository

Why it is risky:
- context is wasted and important layers are skipped anyway

VCP countermeasure:
- `.vcp/index.json`
- `.vcp/cards/`
- `docs/progressive-disclosure.md`

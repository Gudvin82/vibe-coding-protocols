# The VCP Anti-Patterns for AI-Assisted Code

These anti-patterns describe common ways AI-generated code becomes hard to maintain, unsafe to ship, or impossible to review.

## 1. README-only evaluation

Symptom:
- the repository is judged from top-level text only

Why it happens with AI:
- the model optimizes for the shortest visible context

Production risk:
- routes, manifests, benchmarks, and limitations are missed

VCP countermeasure:
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `.vcp/index.json`

Minimum fix:
- inspect index, cards, manifests, and lifecycle docs before scoring maturity

## 2. Implementation before scope clarity

Symptom:
- code starts before the product brief is stable

Why it happens with AI:
- models fill requirement gaps with plausible guesses

Production risk:
- wrong feature shape, hidden acceptance gaps, and rework

VCP countermeasure:
- adaptive spec depth
- Spec Lane
- question engine

Minimum fix:
- choose no-spec, spec-lite, full-spec, or governed-spec explicitly

## 3. No architecture memory

Symptom:
- every task rediscovers the same system shape

Why it happens with AI:
- local context windows forget cross-layer design history

Production risk:
- drift, regression, and broken assumptions

VCP countermeasure:
- `PROJECT_MAP.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`

Minimum fix:
- update architecture memory when cross-layer behavior changes

## 4. No review gate before merge

Symptom:
- AI-generated changes are accepted because they look plausible

Why it happens with AI:
- speed hides the need for acceptance discipline

Production risk:
- subtle regressions land without clear ownership

VCP countermeasure:
- `review-diff`
- post-task code review

Minimum fix:
- inspect diff impact and require validation evidence before merge

## 5. No validation before the next task

Symptom:
- work continues even though validation was not checked

Why it happens with AI:
- models optimize for task completion, not release discipline

Production risk:
- failures pile up silently

VCP countermeasure:
- `vcp check`
- `vcp benchmark run`
- `vcp manifest validate`

Minimum fix:
- keep the validation path visible in every non-trivial change

## 6. External API added without intake

Symptom:
- API code appears before owner, auth, terms, or fallback are documented

Why it happens with AI:
- SDK examples make integration look cheaper than it is

Production risk:
- secret leaks, legal gaps, brittle integrations, and hidden vendor risk

VCP countermeasure:
- Third-party API Intake
- `templates/THIRD_PARTY_REGISTRY.md`

Minimum fix:
- classify auth, data flow, fallback, and owner before implementation

## 7. Backlog lives only in chat

Symptom:
- important work exists only in conversation history

Why it happens with AI:
- models treat chat as temporary task memory

Production risk:
- follow-up disappears and accountability drops

VCP countermeasure:
- `PROJECT_BACKLOG.md`
- `vcp backlog`

Minimum fix:
- write the next real task into backlog before continuing

## 8. Public proof without evidence

Symptom:
- adoption, safety, or visibility claims are published without support

Why it happens with AI:
- models tend to smooth over proof gaps with confident language

Production risk:
- trust loss, misleading docs, and public overclaim

VCP countermeasure:
- `ADOPTERS.md`
- case-study labels
- `docs/public-proof-roadmap.md`

Minimum fix:
- label assets as real, sanitized, synthetic, or template

## 9. Platform compatibility overclaim

Symptom:
- docs imply official integrations where there are only repository workflows

Why it happens with AI:
- platform lists are easy to inflate with vague wording

Production risk:
- misleading adoption claims and support confusion

VCP countermeasure:
- platform status taxonomy
- platform cards with `official_integration: false`

Minimum fix:
- say documented, prompt-compatible, rules-compatible, CLI-compatible, or experimental

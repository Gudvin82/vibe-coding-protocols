# Maintenance Refactoring Protocol

Use when a working project is becoming hard to maintain or risky to extend.
This route is for existing projects,
post-MVP cleanup
and periodic repository health passes.

## Non-goals

- not refactoring for aesthetics;
- not rewriting from scratch;
- not imposing a new architecture unless the current one is clearly failing;
- not broad cleanup across the whole repository;
- not changing behavior,
  public contracts,
  security behavior,
  permissions,
  data formats,
  database or schema contracts,
  error shapes
  or business rules unless explicitly requested.

## Valid outcomes

Allowed outcomes:
- no changes needed;
- separate product task;
- narrow scope;
- proceed with one small high-value refactor.

`NO_CHANGES_NEEDED` is a successful outcome when no safe,
high-value,
behavior-preserving refactor exists.

## Operating rules

- follow repository instructions first;
- read `AGENTS.md`, `README.md`, architecture docs, package scripts,
  CI config, relevant tests and local conventions;
- check `git status` before editing;
- preserve user or unrelated changes;
- prefer one small high-value improvement over a broad rewrite;
- do not edit production code until a scope proposal and challenge checkpoint
  are complete;
- do not change public API or behavior unless explicitly requested.

## Discovery

Before proposing edits, identify:
- stack and validation workflow;
- relevant module boundaries;
- existing architecture;
- tests and coverage signals;
- changed or uncommitted files;
- owner layer for the code under review.

## Candidate smells

High-impact maintenance signals include:
- business logic inside UI, transport, controllers, jobs, middleware,
  ORM code or API clients;
- god files or mixed responsibilities;
- duplicated business rules;
- hidden dependencies on time, randomness, env, globals, filesystem,
  network or framework context;
- shared or common utils dumping grounds;
- code that is only testable through slow or broad paths;
- code likely to make the next feature copy a bad pattern;
- large functions or components with unclear ownership;
- behavior only understandable by reading multiple unrelated layers.

## Responsibility boundaries

- Entry, transport or UI: input or output mapping and context reading.
- Application or use-case: scenario orchestration, permissions,
  transactions and coordination.
- Domain or rules: pure rules, invariants, state transitions, decisions
  and calculations.
- Infrastructure or adapters: database, ORM, SDKs, external APIs, queues,
  filesystem and platform services.
- Wiring or composition: assembling concrete dependencies.

Rules:
- if it answers "what should happen?", it belongs in application or domain;
- if it answers "how do we talk to an external system?", it belongs in infrastructure;
- if it answers "how do we receive input and return output?", it belongs in entry, transport or UI.

## Scope proposal

Before editing, propose at most 1 to 3 small scopes.

For each scope include:
- concrete smell;
- preserved behavior and public contracts;
- smallest useful change;
- main risk;
- validation signal;
- whether characterization test is needed, already exists or is disproportionate.

## Risk classification

### Low risk

- pure extraction within one file;
- renaming local helper variables;
- moving formatting or presentation helpers without changing behavior;
- removing dead code with evidence;
- improving names in private or internal scope.

### Medium risk

- moving logic across internal modules with tests;
- extracting use-case or application services;
- consolidating duplicated business rules;
- changing dependency injection or wiring inside one bounded area;
- moving code between UI and application layers while preserving contracts.

### High risk

- auth or session behavior;
- permissions;
- payments or billing;
- persistence or database writes;
- migrations;
- API contracts;
- error shapes;
- data deletion;
- personal data handling;
- external integrations;
- security-sensitive behavior.

## Stop conditions

Stop or escalate when:
- behavior change is required;
- public contract change is required;
- auth, session or permissions are touched;
- payments or billing are touched;
- data deletion or migration is involved;
- no validation path exists for the proposed change;
- the refactor would require broad architecture changes;
- the agent cannot explain preserved behavior.

## Maintenance vs Hardening vs Product Task

- Maintainability-only improvement -> Maintenance Refactoring.
- Security or production readiness -> Hardening.
- New behavior, feature or product decision -> product task or Extended.
- Broad architecture change -> Extended.

## Escalation rule

High-risk changes must not proceed as routine maintenance refactoring.
Route them to Hardening or Extended Protocol unless the user explicitly approves
a narrow,
tested scope.

If the proposed refactor touches auth,
payments,
permissions,
persistence
or public API contracts,
the challenge checkpoint should default to
`NARROW_SCOPE` or `SEPARATE_PRODUCT_TASK`.

## Challenge checkpoint

Before implementation, run a challenge checkpoint.
If subagents are available, use a separate challenge agent.
If not, do a separate critical self-review pass.

The checkpoint must answer:
- is this worth doing;
- is scope small enough;
- what behavior or contract could break;
- is there a simpler improvement;
- is this overengineering;
- what characterization test should protect behavior;
- should we proceed, narrow scope, do nothing or turn into a product task.

The checkpoint must end with exactly one:
- `PROCEED_WITH_SCOPE`
- `NARROW_SCOPE`
- `NO_CHANGES_NEEDED`
- `SEPARATE_PRODUCT_TASK`

Do not edit production code unless the decision is
`PROCEED_WITH_SCOPE` or `NARROW_SCOPE`.

## Characterization tests

Before behavior-preserving production edits:
- add or identify focused characterization coverage when proportional;
- test observable behavior, contracts, boundaries and invariants;
- avoid heavy test harnesses if disproportionate;
- run the test before production edits when added;
- do not encode known bugs as desired behavior unless explicitly asked.

Good characterization tests often include:
- one request/response assertion for an existing handler;
- one public method call that preserves return shape;
- one regression test for an invariant already relied on by callers.

Disproportionate tests often include:
- building a full integration harness for a two-line extraction;
- snapshotting a huge surface just to rename one helper;
- introducing a new test framework only for a tiny internal cleanup.

If the repository has no test layer,
use the smallest observable validation path available,
such as a focused script,
existing build/lint command,
manual route reproduction
or a clearly documented dry-run check.

## Implementation loop

For each accepted scope:
- inspect surrounding code and tests;
- confirm preserved behavior and risks;
- add or reuse a focused test if needed;
- make the minimal connected diff;
- move decisions to the owner layer;
- avoid patching symptoms in low-level helpers if the wrong decision is higher up;
- run relevant checks.

## Avoid

- rewriting from scratch;
- adding frameworks or dependencies;
- adding interfaces, factories, event buses, CQRS, repositories,
  ports or mediators without current value;
- splitting simple code into many files just to look clean;
- unrelated cleanup or doc churn;
- TODOs instead of finishing;
- architecture that makes code harder to read;
- moving business scenarios into infrastructure, query or client code.

## Example decision shape

- risk level: Medium
- challenge decision: `NARROW_SCOPE`
- characterization coverage: reused one regression test and added one focused boundary test
- validation signal: targeted test command plus lint
- preserved contracts: response shape,
  status handling
  and existing caller-visible error wording

## Final report

The final report must include:
- overall result;
- risk level;
- escalation decision;
- scopes inspected;
- challenge checkpoint decision;
- scopes changed;
- what improved and why it matters;
- public contracts preserved;
- characterization coverage added, reused or skipped with reason;
- primary validation signal;
- secondary checks run;
- docs status;
- remaining risks or future cleanup;
- suggested commit message.

# AI Project Hardening Protocol

A markdown-first hardening protocol for existing AI-generated projects.

## Modes

### Light Hardening

Use when the project has just come out of Starter and still contains only
its first one or two features.

Check:
- layer boundaries;
- secrets hygiene;
- active and deferred surfaces;
- buildability;
- database or migration dead-ends;
- whether README, AGENTS, PROJECT_MAP and architecture docs exist;
- next backlog items.

### Standard Hardening

Use for a working MVP before staging or a limited release.

### Full Hardening

Use before production-like claims, when scanners, legal or payment review,
deeper self-protection and broader readiness really matter.

## If you came from Starter

Reuse the artifacts you already created:
- Product Brief;
- `README.md`;
- `AGENTS.md`;
- `PROJECT_MAP.md`;
- `ARCHITECTURE_MAP.md`, if the project has multiple surfaces;
- `ARCHITECTURE.md` or Architecture Source of Truth;
- `SECURITY.md`;
- `docs/PROMPTS.md`;
- `AUDIT_BACKLOG.md`.

If these files do not exist, create at least `PROJECT_MAP.md` and
`ARCHITECTURE.md` first.

If the existing project is chaotic, reconstruct Architecture Map before editing.

## Code discovery

Start the audit with an evidence map:
- key entrypoints;
- routes and endpoints;
- services;
- data model;
- auth;
- integrations;
- scripts, build and test commands;
- active and deferred surfaces.

Use token-aware discovery. Return an evidence map first. Avoid reading
the whole repository unless the project map is missing or unreliable.

## Project map and architecture

Create or update:
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when a compact surfaces map is missing
- `ARCHITECTURE.md` or Architecture Source of Truth

Architecture should describe the real project, not an idealized diagram
written after the fact.

## Security baseline

Check:
- secrets;
- auth and session boundaries;
- input validation;
- logs;
- uploads;
- debug mode;
- exposed docs or stack traces;
- approval gates for risky changes.

## Self-protection

Confirm that the project protects itself:
- `.env`, `.git`, backups, logs and source maps are not exposed;
- private docs do not sit in a public webroot;
- admin or internal endpoints are not publicly reachable without controls;
- scanners, workers or browser automation do not run with excessive rights.

## Supply chain and safe integration

Every external repo, package, action, image or dataset is a supply-chain risk.

Check:
- origin;
- maintainer;
- license;
- install scripts;
- workflows;
- binaries or obfuscation;
- secrets access;
- quarantine process;
- safe update path;
- docs freshness for third-party libraries.

## Starter template intake

If the project came from a public starter template, review:
- what stack it enforced;
- which surfaces it turned on by default;
- which cloud assumptions it made;
- which credentials it expected;
- what should be removed for this project.

See [../docs/starter-template-intake.md](../docs/starter-template-intake.md).

## Scanners

### Full path

If available, use real scanners such as:
- Trivy;
- Gitleaks;
- OSV-Scanner;
- package-manager audit tools.

### Light fallback

If full scanners are unavailable:
- do not pretend they ran;
- write `not run` explicitly;
- start with package-manager audit;
- review lockfiles;
- grep for `SECRET`, `API_KEY`, `TOKEN` and `PASSWORD`;
- check `.env` and `.gitignore`;
- record manual follow-up commands.

## Database, load and scalability readiness

Check:
- data model or ERD;
- migration history;
- indexes;
- unique constraints and FKs;
- N+1 risk;
- pagination or limits;
- sync versus async operations;
- queue or worker model;
- retries and backoff;
- idempotency;
- rate limits;
- external API or LLM bottlenecks;
- backup and restore;
- scalability backlog.

## Legal and payment checks

If relevant to the project, check:
- privacy contour;
- forms and consent;
- cookies;
- offer or terms wording;
- payment and fiscalization;
- refund or access wording.

## Device and browser QA

For most public web or MVP projects:
- mobile viewport;
- Safari or iOS WebView;
- Chrome Android;
- desktop Chrome or Firefox;
- then edge cases.

For internal or desktop-first projects, the priority may differ.

## Independent diff review

A separate reviewer should inspect only the active git diff.

Rules:
- the reviewer does not edit files;
- the reviewer does not inherit the implementation session assumptions;
- the reviewer looks at `git status`, `git diff`, touched files and validation output;
- the reviewer returns only actionable findings.

See [../prompts/independent-diff-review-prompt.md](../prompts/independent-diff-review-prompt.md).

## Troubleshooting

If the AI goes in the wrong direction:
- stop the task;
- return to AGENTS or plan;
- compare the diff;
- break the change into smaller steps;
- do not fake scanner results;
- defer risky work into backlog if needed.

## Emergency recovery

If the AI broke working code:
1. capture `git status` and the list of touched files;
2. capture build, test or runtime errors;
3. return to the last known-good state deliberately;
4. do not run destructive commands without approval;
5. make a smaller recovery plan;
6. add an incident note to `AUDIT_BACKLOG.md`.

## AI-generated migration rollback

Before migrations:
- take a backup;
- test on staging or a copy of data;
- prepare a down migration or rollback plan;
- review destructive operations;
- use expand-and-contract for zero-downtime where needed;
- run smoke tests and monitor after applying.

## AI-generated test strategy

Tests should cover:
- critical path;
- found regressions;
- auth, payment or webhook flows when active;
- mocked external APIs or LLMs.

Do not add a new test framework without approval and do not generate
flaky tests.

## Final report

The final report should include:
- verdict;
- blockers;
- findings by severity;
- scanner status;
- self-protection status;
- database and load status;
- migration rollback status;
- tests run and not run;
- accepted risks;
- next steps;
- updated `AUDIT_BACKLOG.md`.

## Exit criteria

The project passed the selected hardening mode when:
- the mode was chosen explicitly;
- the audit report exists;
- blockers are classified;
- critical and high findings are fixed or accepted with reason;
- scanner status is recorded;
- self-protection was checked;
- database and load readiness were assessed;
- legal and payment areas were checked when relevant;
- independent diff review was done or explicitly deferred;
- `AUDIT_BACKLOG.md` was updated.

Important: `Passed Light Hardening` does not mean `production-ready`.

# Prompt Drift Control

Long AI instruction files become weaker when they try to carry every rule forever.

## Keep core rules short

Your core `AGENTS.md` should stay focused on:
- role;
- Memory Bank;
- stop conditions;
- approval gates;
- remote safety;
- reporting expectations.

## Push extended material into artifacts

Do not force one giant prompt to do everything.
Use separate project memory files instead:
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`
- `SECURITY_BASELINE.md`

## Important rules may need light repetition

AI agents can lose track of long mid-file sections.
Repeat the most important constraints briefly near the start and near the end when needed:
- do not expose secrets;
- stop on auth, payments, migrations or CI changes;
- verify remote safety before push or deploy.

## Do not inflate for style

A longer instruction file is not automatically safer.
If a new rule belongs in an artifact or checklist, put it there instead.

## Signs of prompt drift

Prompt drift is likely when:
- `AGENTS.md` becomes a dumping ground for every new idea;
- the middle of the file contains rules nobody checks anymore;
- security notes contradict README or templates;
- tool-specific notes dominate the core workflow.

## Preferred fix

Shorten the core instructions and link to the right artifact.
That keeps AI behavior more stable than endlessly appending paragraphs.

# Integration Setup Playbook

Use this page when you want to adopt VCP into another repository with:

- Claude Code;
- Codex;
- Cursor;
- GitHub Copilot;
- GitHub Actions.

This is a repository integration workflow, not an official plugin suite.

## Shared pattern

For every tool:

1. copy the smallest matching instruction file;
2. keep route selection explicit;
3. run local validation after installation;
4. do not copy every VCP file blindly.

## Claude Code

Recommended files:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/AGENTS.claude.md` -> `CLAUDE.md`

Export path:

```bash
python3 -m vcp_cli agents template --agent claude --output ./CLAUDE.md --confirm
```

Best follow-up:

- ask Claude Code to read `START_HERE.md` first;
- keep broad discovery read-only first;
- require validation in the final report.

## Codex

Recommended files:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/agents/CODEX.md` -> `CODEX.md`

Export path:

```bash
python3 -m vcp_cli agents template --agent codex --output ./CODEX.md --confirm
```

Best follow-up:

- ask Codex to choose the smallest safe route;
- require inspected files, skipped files, and validation before code changes.

## Cursor

Recommended files:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/AGENTS.cursor.md` -> `CURSOR_RULES.md`
- optionally adapt `CURSOR_RULES.md` into `.cursorrules` or your editor-native rules surface

Export path:

```bash
python3 -m vcp_cli agents template --agent cursor --output ./CURSOR_RULES.md --confirm
```

Best follow-up:

- keep route selection explicit;
- keep changed-files plan explicit;
- run validation after each meaningful slice.

## GitHub Copilot

Recommended files:

- `templates/AGENTS.md` -> `AGENTS.md`
- `templates/agents/COPILOT_INSTRUCTIONS.md` -> `.github/copilot-instructions.md`

Export path:

```bash
mkdir -p .github
python3 -m vcp_cli agents template --agent copilot --output ./.github/copilot-instructions.md --confirm
```

Best follow-up:

- use Copilot as a repository control layer, not as an autonomous VCP runtime;
- attach route docs and report templates only when they are relevant to the current task.

## GitHub Actions

Recommended file:

- `ci-examples/github-actions/vcp-pr-gate.yml` -> `.github/workflows/vcp-pr-gate.yml`

This gives you a repository-side PR Gate example. It is not a GitHub Marketplace action.

## Minimal validation after install

Run these in the target repository:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli check --fast --json
```

If the target repository is not a production repo, replace the route profile with the closest real one.

## What this does not mean

- not an official plugin;
- not automatic model switching;
- not automatic PR creation;
- not automatic merge/deploy approval;
- not native slash-command support unless the tool actually supports it.

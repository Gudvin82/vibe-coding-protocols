# Scanner Integration

`vibe-check` can optionally call external scanners when they are already installed.

This is meant to improve engineering signal, not to create a heavy mandatory stack.

## What vibe-check can run if installed

- `gitleaks detect --no-git --source .`
- `trivy fs .`
- `semgrep --config auto`
- `npm audit --audit-level=high`
- `pnpm audit`
- `pip-audit`
- `cargo audit`

## Why missing tools are WARN, not FAIL

External scanners are optional.
The toolkit should stay usable on a clean machine, inside an AI IDE, or in a small repo without forcing users to install a full security stack first.

If a tool is missing:
- `vibe-check` warns about it;
- default mode still exits successfully if there are no FAIL findings;
- `--strict` can still turn those warnings into a non-zero exit.

## When to use which scanner

### Gitleaks
Use for secret-like tokens, keys and credentials in the working tree.

### Trivy
Use for filesystem vulnerability and misconfiguration checks, especially when Docker, lockfiles or deployment artifacts are present.

### Semgrep
Use for code pattern checks when you want more semantic findings than simple grep-based signals.

### npm audit / pnpm audit
Use when the repository has a JavaScript package manager and lockfiles.

### pip-audit
Use when the repository has Python requirements or a Python project file and `pip-audit` is installed.

### cargo audit
Use when the repository has `Cargo.lock` and Rust dependency review matters.

## What output means

- `PASS`: scanner ran and returned no blocking signal in this lightweight pass.
- `WARN`: scanner found issues, could not run cleanly, or is not installed.
- `FAIL`: reserved for baseline structural failures or strict-mode escalation, not for a generic “scanner exists” condition.

## Sample CI snippet

```yaml
- name: Audit vibe check
  run: bash scripts/vibe-check.sh --audit

- name: Optional scanner stage
  run: bash scripts/vibe-check.sh --audit --scanners || true
```

Keep the main structure gate lightweight. Add stricter scanner-specific jobs only when the team is ready to maintain them.

## Example local flow

```bash
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --hardening --scanners || true
```

## Notes

- Scanner output still needs triage.
- Findings still need owners and evidence in `AUDIT_BACKLOG.md`.
- This is not a pentest.

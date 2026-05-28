# Update Copied Artifacts

Use this guide when your project already contains copied VCP templates.

## Why copied files drift

Copied artifacts change over time:
- new stop conditions appear;
- safer wording replaces risky shortcuts;
- security-related templates gain new sections;
- version markers change.

VCP does not overwrite your project files automatically.
Customized files should be reviewed manually.

## Read the markers first

Most copy-ready templates include markers such as:

```md
<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.4.1 -->
<!-- methodology-version: v1.4 -->
```

Use them as orientation, not as proof that the file is complete.

## Safe update workflow

1. Open your local copied file.
2. Open the matching file in `templates/`.
3. Compare version markers and key sections.
4. Merge changes manually.
5. Keep your local project-specific notes.
6. Re-run `bash scripts/vibe-check.sh --doctor` and `bash scripts/vibe-check.sh --update-advice`.

## Compare `AGENTS.md` carefully

Do not overwrite a customized `AGENTS.md` blindly.

Review these sections first:
- Stop Conditions
- Memory Bank
- Remote safety
- token-aware discovery
- approval gates
- maintenance routing and challenge checkpoint rules

Project-specific instructions should usually stay local.
Toolkit-wide safety improvements should usually be merged in.

## What to update cautiously

Be especially careful with:
- `AGENTS.md`
- `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`
- `SECURITY.md`
- `SECURITY_BASELINE.md`
- `SECURITY_OPERATIONS_BASELINE.md`

These files often contain project-specific decisions and accepted risks.

## After a security-related update

If the toolkit update touches security-related templates:
- compare your local baselines against the new template;
- note accepted differences in `AUDIT_BACKLOG.md`;
- confirm owners, cadence and rollback notes still make sense;
- re-run your preferred review route;
- review [migration/v0.3.0-to-v0.4.0.md](./migration/v0.3.0-to-v0.4.0.md) if you are adopting maintenance artifacts after an older copy.

## If you are unsure

Use `bash scripts/vibe-check.sh --update-advice`.
It will show detected artifact versions and remind you to review changes manually.

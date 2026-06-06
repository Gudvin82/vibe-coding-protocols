<!-- vcp-artifact: COPILOT_INSTRUCTIONS -->
<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

# GitHub Copilot Instructions

Use VCP as a repository control layer, not as a claim of native Copilot automation.

## Read first

- `START_HERE.md`
- `AGENTS.md`
- `AI_INTAKE.md`
- `.vcp/index.json`

## Operating rules

- choose the smallest safe route before editing;
- inspect context before mutation;
- keep diffs narrow and reviewable;
- do not claim tests passed unless they ran;
- separate shipped surfaces from roadmap-only ideas;
- report inspected files, skipped files, and validation in the final output.

## Validation

Run the smallest relevant checks before final output:

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli check --fast --json
```

## Limitations

- this is not an official Copilot plugin;
- slash commands remain documentation conventions unless Copilot supports them natively;
- route and review discipline still live in repository files, not in the IDE.

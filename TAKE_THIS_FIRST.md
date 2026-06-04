# TAKE_THIS_FIRST.md — How to adopt VCP without copying everything

Use this file when someone says: study VCP and take only what helps my project.

## First classify, then adopt

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
```

## Tracks

- new idea or founder brief -> New Project Track
- existing repo or MVP -> Existing Project Track
- public-facing growth work -> Existing Project Track + public-growth checks

## Use safe adoption outputs

```bash
python3 -m vcp_cli adopt plan --pack production --json
python3 -m vcp_cli adopt plan --pack production --copy-list
python3 -m vcp_cli adopt plan --pack production --patch
```

These commands are non-destructive.
They do not auto-write into the target project by default.

## Good adoption answer format

Return:
- project type;
- recommended track;
- recommended tier;
- recommended route;
- pack to inspect;
- files to copy;
- files not to copy;
- manual steps;
- stop conditions.

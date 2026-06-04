# TAKE_THIS_FIRST.md — How to adopt VCP without copying everything

Use this file when someone says: study VCP and take only what helps my project.

## First classify, then adopt

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
```

## Tracks

If the user asks for the fastest first path, start with `docs/10-minute-adoption-path.md` before expanding into deeper packs.

- new idea or founder brief -> New Project Track
- existing repo or MVP -> Existing Project Track
- public-facing growth work -> Existing Project Track + public-growth checks

## MVP shortcut

If the project is already an AI-generated MVP, inspect:
- `docs/mvp-adoption-track.md`
- `docs/demos/raw-ai-mvp-to-controlled-launch.md`

## If the user asks about integrations or dashboard surfaces

Inspect:
- `docs/integrations/status-model.md`
- `.vcp/integrations.json`
- `docs/dashboard.md`
- `docs/plugins/README.md`
- `docs/metrics-board.md`

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

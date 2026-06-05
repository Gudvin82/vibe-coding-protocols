# Lite Adoption Path

Use this if you are a solo builder or MVP project and do not want the full Extended path.

## Copy only these files first

1. `templates/AGENTS.md` as `AGENTS.md`
2. `templates/PROJECT_MAP.md`
3. `templates/AUDIT_BACKLOG.md`
4. `prompts/product-brief-prompt_en.md` or `prompts/product-brief-prompt.md`

These copy-ready templates include lightweight version markers so you can review them against newer toolkit releases later.
Do not copy root `AGENTS.md` blindly into your project.

If the project has multiple surfaces, also create `ARCHITECTURE_MAP.md` before asking AI to generate code.
Use:
- `templates/ARCHITECTURE_MAP.md`
- `prompts/architecture-map-prompt.md`

## Run

```bash
bash scripts/vibe-check.sh --starter
```

## Do not start with

- full security operations baseline;
- full compliance checklist;
- all templates;
- all commands;
- all docs.

## Add Extended path later when

- the project is public;
- the project has auth, payments or personal data;
- the project is client-facing;
- deployment is production-bound.

# Adoption Packs

Adoption packs help teams adopt a focused slice of VCP instead of copying the whole repository.

## Practical path

Always start with:

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
```

## Safe outputs

`vcp adopt plan` can return:
- JSON plan;
- `--copy-list` instructions;
- `--patch` preview.

It does not auto-apply changes.

## Recommended packs

- `spec-foundation` / `spec-first` for new-project foundation
- `brownfield-rescue` for existing repos with weak control
- `production` for governed release discipline
- `public-growth` for public-facing trust and GEO checks

## Selection rule

Pick the smallest pack that gives you control.

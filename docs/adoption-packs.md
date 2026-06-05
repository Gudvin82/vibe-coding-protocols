# Adoption Packs

Adoption packs help teams adopt a focused slice of VCP instead of copying the whole repository.

## Practical path

Always start with:

```bash
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --json
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
```

## Safe outputs

`vcp adopt plan` can return:
- JSON plan;
- `--copy-list` instructions;
- `--patch` preview.

`vcp adopt apply` is now available as an explicit safe mode:
- requires `--target`;
- requires `--confirm` unless `--dry-run` is used;
- does not overwrite existing files by default;
- skips conflicts and records them;
- writes an adoption log on confirmed apply.

## Recommended packs

- `spec-foundation` / `spec-first` for new-project foundation
- `brownfield-rescue` for existing repos with weak control
- `production` for governed release discipline
- `public-growth` for public-facing trust and GEO checks

## Selection rule

Pick the smallest pack that gives you control.

## Safe apply boundary

`vcp adopt apply` copies only explicit safe assets.
It does not:
- overwrite files by default;
- copy `.env`;
- modify CI by default;
- modify source code by default;
- access secrets;
- silently create a destructive migration path.

## SaaS AI-MVP hardening

Use `python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json` when an AI-generated SaaS MVP needs auth, billing, contracts, release readiness, and PR Gate made explicit.

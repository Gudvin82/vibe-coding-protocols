# Protocol Pack Security

VCP packs must be inspectable before they are adopted.

## Trust levels

- `core`
- `local`
- `workspace`
- `external`
- `experimental`
- `deprecated`

## Safe adoption rule

External or higher-risk packs must go through:
- `vcp classify`;
- `vcp adopt plan`;
- `vcp adopt apply --dry-run`;
- manual review of files touched;
- validation commands;
- PR Gate or equivalent review path.

## Safe apply rule

For `v0.8.1`, safe apply means:
- explicit `--target`;
- explicit `--confirm` for real writes;
- no overwrite by default;
- no `.env` copy;
- no hidden CI mutation by default;
- adoption log written for confirmed apply.

## Never do this

- do not apply packs blindly;
- do not let a pack overwrite CI or release gates without explicit review;
- do not hide network behavior;
- do not weaken VCP safety boundaries.

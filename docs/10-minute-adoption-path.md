# 10-Minute Adoption Path

Use this path when you want one fast, practical VCP walkthrough without reading the whole repository first.

## Main path

```bash
git clone https://github.com/Gudvin82/vibe-coding-protocols
cd vibe-coding-protocols
python3 -m pip install .
vcp doctor
vcp onboard --json
vcp classify --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
vcp release-check --json
```

## Module fallback

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli onboard --json
python3 -m vcp_cli classify --json
python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list
python3 -m vcp_cli adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
python3 -m vcp_cli release-check --json
```

## What each step does

- `python3 -m pip install .`: installs the local CLI from the current clone.
- `vcp doctor`: checks that the local environment and package surfaces are usable.
- `vcp onboard --json`: gives the first practical route into VCP.
- `vcp classify --json`: classifies whether you are in a new-project or existing-project path.
- `vcp adopt plan --pack brownfield-rescue --copy-list`: shows the first files worth adopting without changing the target project.
- `vcp adopt apply --dry-run --json`: previews a safe apply run and surfaces collisions before writing anything.
- `vcp release-check --json`: checks launch and release-control surfaces before you treat the MVP as shippable.

## Stop conditions

- Do not use `adopt apply` without `--dry-run` first.
- Do not use confirmed apply on a production repository without review.
- Do not treat VCP as a guarantee of production safety or launch success.
- Do not auto-publish or auto-deploy from this path.

## Expected result

After this path, you should have:

- a selected route;
- visible risks and control gaps;
- a copy-list for the first adoption slice;
- a safe apply preview;
- a launch/readiness check result.

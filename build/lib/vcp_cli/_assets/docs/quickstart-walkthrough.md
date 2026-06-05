# Quickstart Walkthrough

This is a synthetic but realistic walkthrough.
It is not a measured case study,
not a production proof artifact,
and not a security audit.

## Scenario

A small AI-generated SaaS or MVP is already working.
The owner is unsure whether it is ready for production and does not want to copy the whole toolkit blindly.

## Step 1 — Identify route

Command:

```bash
python3 -m vcp_cli route --profile production
```

Expected result:
VCP recommends a production hardening path rather than Starter.

## Step 2 — Generate adoption plan

```bash
python3 -m vcp_cli adopt --pack production --dry-run
```

What happens:
The dry-run shows which files are relevant,
which files should be merged manually,
and which protected files should not be overwritten blindly.

## Step 3 — Check current toolkit readiness

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score
```

What happens:
You see whether the toolkit surfaces are present,
which docs and manifests exist,
and whether the repository is wired for evaluation and validation.

## Step 4 — Capture tasks into backlog

```bash
python3 -m vcp_cli backlog add --title "Review auth/session handling" --type security --priority P1 --dry-run
```

What happens:
Instead of leaving findings in chat,
VCP turns them into visible follow-up work before implementation begins.

## Step 5 — Use review gate before next feature

```bash
python3 -m vcp_cli review plan
```

What happens:
The active diff is treated as something that needs acceptance,
not as something AI generated therefore automatically trusted.

## Step 6 — Validate

```bash
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
```

What happens:
The toolkit’s route/adoption surfaces are checked so that workflow claims remain consistent with repository reality.

## What VCP found in this walkthrough

- no architecture memory should be treated as a risk;
- production work should use Hardening, not Starter;
- review gate is required before accepting active changes;
- backlog prevents user ideas and findings from staying only in chat;
- public sites may also need Public Growth and GEO readiness.

## What this walkthrough is not

- not a real case study;
- not measured production proof;
- not a security audit;
- not a ranking guarantee.

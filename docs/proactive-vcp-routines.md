# Proactive VCP Routines

VCP routines make repeated governance visible without turning VCP into a personal assistant or autonomous agent.

## Before merge

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli score --json
```

## Weekly project health

```bash
python3 -m vcp_cli diagnose --json
python3 -m vcp_cli benchmark run
```

## Before release

```bash
python3 scripts/check-public-version-surfaces.py
python3 scripts/check-readme-parity.py
python3 -m vcp_cli manifest validate
python3 -m vcp_cli cards validate
python3 -m vcp_cli index validate
```

## Daily production-error review

If the project uses error capture:
- inspect `errors/`;
- convert repeat issues to backlog work;
- do not auto-fix without review.

## Spec freshness review

```bash
python3 -m vcp_cli spec freshness --json
```

## Backlog aging review

- identify stale P0 and P1 items;
- archive rejected ideas;
- move done items;
- keep architecture decisions linked.

These are routines, not autonomous notifications.

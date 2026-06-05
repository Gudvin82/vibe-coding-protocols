# MVP-to-Launch Path

Это guided path для raw или semi-working AI-generated MVP, которому нужен launch control.

## Команды

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp pr-gate explain --json
vcp dashboard build --output ./vcp-dashboard --json
```

## Что этот путь не делает

- не деплоит;
- не сертифицирует production readiness;
- не заменяет human launch decision.

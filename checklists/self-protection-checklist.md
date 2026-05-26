# Self-protection checklist

## When to use

Когда нужно проверить, что проект не раскрывает лишнюю внутреннюю информацию.

## Checklist
- `.env` / `.git` / backups / logs not public
- private docs not in public webroot
- admin/internal endpoints protected
- no debug traces in public mode
- worker/scanner permissions restricted
- update path is review-gated

## Protocol

See: [../protocols/ai-project-hardening-protocol.md](../protocols/ai-project-hardening-protocol.md)

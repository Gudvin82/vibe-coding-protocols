# Perimeter Security Checklist

Use this checklist when a project is exposed to the public internet.

## Public exposure

- [ ] List all public domains and subdomains
- [ ] List all public endpoints
- [ ] Confirm admin/internal endpoints are not public
- [ ] Confirm staging/test routes are not public or are protected
- [ ] Confirm debug routes are disabled
- [ ] Confirm source maps are not public unless intentionally allowed
- [ ] Confirm directory listing is disabled
- [ ] Confirm backups/dumps/logs are not public

## Ports and services

- [ ] Inventory open ports
- [ ] Confirm only required ports are open
- [ ] Confirm database ports are not public
- [ ] Confirm Redis/queues/internal services are not public
- [ ] Confirm SSH access is restricted
- [ ] Confirm firewall rules are documented

## WAF / CDN / reverse proxy

- [ ] WAF/CDN/reverse proxy is documented
- [ ] Basic bot filtering is enabled where applicable
- [ ] Rate limits are configured for forms/API/auth
- [ ] Upload size limits are configured
- [ ] Request body limits are configured
- [ ] Suspicious traffic logging is enabled

## Admin protection

- [ ] Admin routes require authentication
- [ ] Admin routes have MFA or stronger access control where possible
- [ ] Admin routes are IP allowlisted / VPN / private where possible
- [ ] Admin actions are logged
- [ ] Default admin URLs are avoided or protected

## Security headers

- [ ] HSTS considered
- [ ] CSP considered
- [ ] X-Frame-Options / frame-ancestors configured
- [ ] Referrer-Policy configured
- [ ] Permissions-Policy considered
- [ ] Cookies use Secure / HttpOnly / SameSite where applicable

## Abuse cases

- [ ] Public forms have rate limits
- [ ] Auth endpoints have brute-force protection
- [ ] Webhooks have signature/idempotency checks
- [ ] AI/LLM endpoints have cost limits
- [ ] File uploads are size/type limited
- [ ] Bot/Telegram endpoints have abuse controls

## Evidence

- Date checked:
- Commands/tools used:
- Findings:
- Accepted risks:
- Follow-up:

# External Exposure Checklist

Use this checklist to review what an external scanner or curious visitor can see.

## Domains and routing

- [ ] List all production domains and subdomains
- [ ] List all staging/test/demo domains and subdomains
- [ ] Confirm parked or deprecated domains are removed or redirected safely
- [ ] Confirm wildcard DNS is intentional

## Public surfaces

- [ ] Confirm public homepage/landing pages are expected
- [ ] Confirm public APIs are intentional
- [ ] Confirm OpenAPI/Swagger is protected or intentionally public
- [ ] Confirm GraphQL playground/introspection is disabled or protected in production
- [ ] Confirm health/debug/status endpoints are reviewed

## Files and assets

- [ ] Confirm source maps are not public unless intentionally allowed
- [ ] Confirm backups/dumps/logs are not public
- [ ] Confirm old archives (`.zip`, `.tar`, `.sql`) are not public
- [ ] Confirm robots.txt and sitemap.xml do not reveal sensitive routes
- [ ] Confirm `.well-known` files are intentional

## Docs and internals

- [ ] Confirm internal docs are not public
- [ ] Confirm architecture docs are sanitized if public
- [ ] Confirm admin route hints are not leaked in public docs
- [ ] Confirm test/staging credentials are not exposed in docs or comments

## Expected scanner findings

- [ ] Review what a basic HTTP/header scanner would see
- [ ] Review what a port scanner would see at the host/load-balancer level
- [ ] Review what a crawler would discover from links, sitemap and robots
- [ ] Review what search engines could index

## Evidence

- Date checked:
- Public surfaces reviewed:
- Findings:
- Accepted risks:
- Follow-up:

<!-- vcp-artifact: PROJECT_MAP -->
<!-- vcp-version: v0.2.0 -->
<!-- methodology-version: v1.4 -->

# PROJECT_MAP

## Routes / Endpoints
- `POST /api/admin/do-anything`

## Components / Modules
- `app.js` handles routing and validation
- env-driven config is created in `createConfig`

## Active / Deferred surfaces
- active now: admin action validation and auth gate
- deferred until later: rate limiting, audit log storage, admin UI

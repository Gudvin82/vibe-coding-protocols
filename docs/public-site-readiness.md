# Public Site Readiness

Use this checklist for VCP itself or for projects that publish AI-assisted products publicly.

## Basics

Check:
- canonical URLs;
- `sitemap.xml`;
- `robots.txt`;
- `llms.txt`;
- OpenGraph and Twitter cards;
- favicon and social preview image;
- readable docs index;
- release page links;
- security/contact page;
- license and contribution links.

## Structured data

Use schema.org JSON-LD only when it matches visible content.
Typical types:
- `Organization`
- `WebSite`
- `SoftwareSourceCode`
- `BreadcrumbList`
- `FAQPage`, only when visible FAQ content exists
- `HowTo`, only when visible step-by-step content exists

Validate structured data with external search-engine tools.

## Performance

Review:
- LCP;
- INP;
- CLS;
- image optimization;
- whether static pages are enough instead of heavy client-side docs.

## Trust signals

Expose:
- GitHub link;
- release link;
- `SECURITY.md`;
- `CHANGELOG.md`;
- license;
- limitations;
- a short “what this is not” note.

## AI crawler readiness

Use `llms.txt` as a curated entrypoint if helpful,
but do not claim guaranteed AI visibility or ranking.
Keep it short,
current
and linked to authoritative docs.

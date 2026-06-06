# Public Growth Playbook

Use this playbook when an AI-assisted project has a public surface that must be discoverable, trustworthy, machine-readable, and commercially useful.

Legend:
- `[U]` Universal: needed by most sites.
- `[RU]` Russia/CIS specifics.
- `[INT]` International / multilingual specifics.
- `[AI/GEO]` AI search, LLM, and generative-engine visibility.
- `[OPT]` Optional or situational.

## 0. Business, product, and strategy `[U]`

Start with:
- target audience segments and decision-makers;
- JTBD and current search motivation;
- pains, fears, and objections;
- offers for cold, warm, and hot demand;
- product or service line priorities;
- economics: average order, LTV, CAC, acceptable lead cost, traffic-to-sale model.

## 1. Baseline audit `[U]`

Review:
- technical SEO blockers, indexing, duplicates, canonical, sitemap, robots, redirects, CWV, mobile, URL structure, internal links;
- content gaps, stale pages, thin content, cannibalization, missing intent, missing CTA;
- commercial signals, trust blocks, cases, reviews, pricing, guarantees, contacts, delivery/payment terms.

Add specific layers:
- `[AI/GEO]` AI mention audit, citation sources, hallucination risks, non-JS visibility, `llms.txt` readiness;
- `[RU]` Yandex Webmaster, Metrika, Yandex Business, Maps, 2GIS, commercial factors, Minusinsk/Baden-Baden/affiliate risks;
- `[INT]` Google/Bing/regional webmaster surfaces, localization, hreflang, local trust signals.

## 2. Competitors and demand map `[U]`

Compare:
- search competitors by cluster;
- product competitors by offer, trust, price, and proof;
- `[AI/GEO]` who ChatGPT, Perplexity, Gemini, AI Overviews, and Yandex Neuro cite instead of you.

## 3. KPI, baseline, and dashboard `[U]`

Track 3, 6, and 12 month targets for:
- organic traffic;
- rankings;
- branded searches;
- conversions and sales;
- AI Share of Voice;
- AI citations and referred traffic where measurable.

Dashboards may include:
- `[U/INT]` Looker Studio, GA4, GSC;
- `[RU]` Metrika, Yandex Webmaster, DataLens;
- `[INT/AI]` Bing Webmaster Tools and regional equivalents where relevant.

## 4. Site architecture and funnel `[U]`

Document:
- page types: homepage, services/products, categories, item pages, cases, blog, FAQ, contacts, about, reviews, pricing, legal pages, `sitemap.xml`, `robots.txt`;
- optional layers: comparison pages, alternatives, geo pages, industry pages, calculators, quizzes, glossary, docs, marketplace pages `[OPT]`;
- TOFU/MOFU/BOFU coverage with CTA per page type;
- page matrix: cluster, query set, intent, page type, URL, funnel stage, CTA, KPI, priority, owner, status.

## 5. Technical SEO `[U]`

Cover:
- indexing, crawlability, robots, sitemaps, canonical, noindex, pagination, filters, duplicates, orphan pages, redirects, status codes;
- SSR/SSG and bot-visible HTML;
- Core Web Vitals;
- image SEO;
- HTTPS, headers, anti-spam, backups, staging protection;
- accessibility and WCAG.

Specifics:
- `[RU]` Yandex mirrors, regionality, filters, commercial factors;
- `[INT]` hreflang, language sitemaps, local webmaster tools;
- `[AI/GEO]` GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Googlebot, Bingbot, YandexBot access where appropriate.

## 6. Content and on-page `[U]`

For each page, review:
- title, description, H1-H3, intro, TL;DR, FAQ, tables, lists, images, schema, internal links, CTA, breadcrumbs;
- answer-ready formatting for humans and machines;
- E-E-A-T signals, authorship, sources, update dates, cases, real numbers, contacts, legal trust.

Add AI-native content layers:
- definitions, glossary, Q&A, short answers, structured data, unique data, quoteable wording, branded answers, `llms.txt`, `llms-full.txt`.

## 7. GEO / AI visibility `[AI/GEO]`

Check:
- crawler access without accidental CDN/WAF blocks;
- HTML visibility without JS;
- `llms.txt`, `llms-full.txt`, `ai.txt`;
- entity authority and consistent brand naming;
- AI Share of Voice across ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews/Mode, Bing Copilot, Yandex Neuro, Alice, GigaChat, and relevant regional tools;
- hallucination monitoring and correction plan.

## 8. Off-page, PR, and citations `[U]`

Track:
- donor quality and link profile;
- digital PR, interviews, research, guest posts, podcasts, webinars;
- reputation platforms and reviews;
- `[AI/GEO]` whether your site appears in the sources LLMs actually read.

## 9. CRO, UX, and conversion readiness `[U]`

Review:
- TOFU, MOFU, BOFU journeys;
- forms, callbacks, messengers, quizzes, calculators, audit/quote CTAs;
- analytics event flow, thank-you pages, CRM delivery, UTM preservation;
- `[RU]` behavioral risks without manipulation.

## 10. Local, regional, and international search `[U]`

Cover:
- NAP consistency, hours, photos, categories, services, geo pages, local links;
- `[RU]` Yandex Business, Maps, 2GIS, Zoon, Flamp, Otzovik, IRecommend;
- `[INT]` Google Business Profile, Apple Maps, Bing Places, Yelp, Trustpilot, G2, Capterra, regional map/listing systems.

## 11. Content ops and governance `[U]`

Define:
- editorial flow from idea to indexation and reporting;
- fact-check and expert approval ownership;
- AI-content labeling policy;
- rules for updates, merges, deletions, redirects, canonical decisions.

## 12. Roles and RACI `[U]`

Map roles such as:
- business owner, product owner, project manager;
- SEO specialist, content strategist, editor, expert/fact-checker;
- designer, developer, analyst;
- PR/link builder, SERM specialist;
- legal reviewer `[OPT]`.

Clarify RACI for:
- SEO tasks;
- content production;
- development changes;
- analytics;
- PR / SERM.

## 13. Definition of Done `[U]`

Use page-level DoD:
- URL approved, page published, title/description/H1 ready, intent closed, CTA present, form working, schema valid, page in sitemap, indexation correct, internal links added, analytics events configured, expert/editor approval complete.

Use SEO-task DoD:
- task executed, result checked, evidence attached, no side effects, KPI impact understood, backlog/report updated.

Use AI/GEO DoD:
- AI bots can access the page, non-JS content visible, `llms.txt` updated, FAQ/schema present, branded answer wording exists, target AI systems checked, AI visibility delta recorded, hallucination findings logged.

## 14. Risks and anti-patterns `[U]`

Do not rely on:
- thin content, doorway pages, spam links, broken redirects, junk indexation, bad UX;
- `[RU]` PF manipulation, Yandex filter bait, over-optimization;
- `[AI/GEO]` blocked AI crawlers, contradictory content, weak entity authority, no external proof, no structured answers, no `llms.txt`;
- `[INT]` wrong hreflang, machine translation without localization, domain/locale mismatch, legal mismatch.

## 15. Recommended tooling `[U]`

Possible stacks:
- `[U]` crawl, analytics, schema, UX, and performance tools;
- `[RU]` Yandex tooling, regional rank or marketplace tools;
- `[AI/GEO]` AI visibility, brand monitoring, and manual AI audit;
- `[INT]` international SEO, localization, and review platforms.

## 16. Rollout roadmap `[U]`

Suggested phases:
- month 0-1: baseline, audit, semantics, analytics, robots/sitemap, quick wins;
- month 2-3: page structure, BOFU pages, FAQ, early content, schema, CTA, forms, Definition of Done;
- month 3-6: clusters, cases, comparison/alternatives, PR, local SEO, SERM, AI audit, `llms.txt`, AI Share of Voice;
- month 6-12: programmatic layers `[OPT]`, international expansion `[INT]`, marketplaces `[OPT]`, content cleanup, crisis SEO process.

## Outcome

The output should be a prioritized Public Growth backlog that separates:
- must-fix technical blockers;
- content and page gaps;
- RU / INT / AI-specific gaps;
- reputation and legal risks;
- analytics and reporting gaps;
- ownership and DoD gaps.

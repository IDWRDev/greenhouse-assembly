# GreenHouse Assembly Master Restructure - Discovery and Execution Plan

## Milestone 0 status

Discovery is complete enough to define the production programme. No redesign has been implemented in this milestone. The repository was reviewed across its public pages, legal pages, stylesheets, JavaScript, documentation, brand assets, image variants, PDFs, navigation paths, configuration, and recent project history.

## Product understanding

### Ministry identity

The GreenHouse Assembly Ministries is best understood as a Christian formation movement: a house where people are cultivated into mature, purposeful, Kingdom-minded lives. The greenhouse metaphor is the strongest owned idea in the product. It naturally connects environment, light, roots, patient growth, nurture, fruitfulness, and multiplication.

### Mission direction

The current public material points toward cultivating Christ-centred people through biblical teaching, prayer, worship, discipleship, community, and practical service. This wording is a strong editorial direction, but the final mission statement still requires owner and doctrinal approval.

### Vision direction

The emerging vision is a spiritually healthy, intellectually serious, creatively excellent community whose members carry Kingdom life into family, work, culture, leadership, and public life. The site should make formation visible as a journey from knowing truth to becoming mature, belonging in community, serving faithfully, and influencing wisely.

### Audience

Primary audiences are first-time visitors, spiritually curious people, new and growing believers, existing members, families, young people, leaders, creatives, volunteers, partners, publishers, and a Nigerian/Black-global diaspora audience. Each needs a clear route without having to understand church vocabulary first.

### Communication style

The strongest voice is calm, intelligent, warm, assured, and invitational. It should combine theological depth with plain language, avoid pressure and hype, and sound more like thoughtful formation than generic church promotion. The new directive adds useful emphasis on Kingdom intelligence, mind renewal, creative dominion, purpose, leadership, truth, and transformation.

### Theology represented in the repository

The current site presents Scripture, Christ-centred formation, prayer, worship, community, service, stewardship, and whole-person growth. It does not contain an approved doctrinal statement, formal history, leadership biographies, or enough source material to make detailed denominational or doctrinal claims. Those remain approval boundaries.

### Design language

The owned visual language uses deep greenhouse green, warm gold, cream, a house/greenhouse outline, a seedling, and a beam of light. The homepage adds editorial serif typography and cinematic imagery. The most promising direction is “cultivated intelligence”: botanical warmth, architectural structure, African dignity, editorial restraint, and luminous cinematic media.

## Current strengths

- A distinctive name and visual metaphor with strong long-term brand potential.
- A recognizable green, gold, cream, seedling, house, and light identity.
- Broad page coverage: Home, About, Ministries, Teaching, Resources, Events, Give, Contact, legal pages, and 404.
- Honest handling of missing operational facts and credentials.
- Good baseline accessibility patterns: skip links, semantic landmarks, focus styles, reduced-motion support, labelled forms, Escape-to-close navigation, and honest inactive controls.
- A useful central configuration file for future contact, giving, schedules, maps, registration, newsletter, and social activation.
- Existing editorial systems for teaching, resources, ministries, events, and the Know -> Become -> Belong -> Serve -> Influence formation journey.
- A strong cinematic `hero-gathering.png` asset and several owner-supplied brand/logo files.

## Current weaknesses and launch risks

### Experience and content

- The homepage and inner pages feel like two different design systems, navigation systems, and editorial products.
- The site repeatedly tells visitors that content is pending, unavailable, simulated, or in preparation. This protects accuracy but makes the public ministry feel unfinished and small.
- Dynamic Sprint 4 content is appended client-side after the main page content, creating very long pages, weak editorial prioritisation, duplicated ideas, and JavaScript-dependent discoverability.
- The Divine Art of Violence is named but not presented as a premium flagship resource; the repository lacks its approved cover, author line, synopsis, publication status, and destination.
- Leadership, ministry history, beliefs, location, gathering schedule, and a real contact route are absent, so the core trust questions remain unanswered.
- No real testimony, sermon, event, resource download, newsletter, giving provider, map, or social destination is active.

### Brand and media

- The homepage uses remote Unsplash images while an owned cinematic hero asset is unused.
- Image sourcing is visually inconsistent and depends on third-party URLs at runtime.
- Several brand assets are exact duplicates stored in multiple folders.
- Source logo and roll-up files are extremely oversized for web use; three roll-up files exceed 120 megapixels.
- The roll-up artwork contains a WhatsApp number and `@GreenhouseAssembly`, but these are not configured on the site and must be explicitly confirmed before publication.
- The logo system contains several variants without a documented canonical-use hierarchy.

### Technical, SEO, and accessibility

- Canonical URLs, sitemap.xml, Open Graph images, Twitter images, and full Organization/Church structured data are missing.
- `robots.txt` does not advertise a sitemap.
- The two PDFs (`privacy-policy.pdf` and `terms.pdf`) are effectively blank one-page Google Docs exports and should not be public launch artifacts.
- Legal HTML exists, but legal wording still needs appropriate owner/legal approval before launch.
- `package.json` is a directory rather than a package manifest, so there is no reliable build/test command surface.
- Header/menu logic is duplicated across `main.js` and `mobile-navigation.js` with different markup and breakpoints.
- The homepage contains root-relative section links where visitors expect page navigation, while inner pages use a separate full-page navigation model.
- Contact fallback through `mailto:` can expose form content to a local email client and is not a robust production submission workflow.
- Current social metadata uses a basic summary card and lacks absolute image URLs.
- Real browser, keyboard, zoom, screen-reader, performance, and deployed-site verification has not been completed.

## Recommended information architecture

1. Home - identity, promise, proof, featured teaching, flagship book, ministries, gatherings, visit, stories, and next steps.
2. Our House - story, mission, vision, beliefs, leadership, values, and the formation model.
3. Grow - teaching library, series, articles, devotionals, study guides, and The Divine Art of Violence.
4. Belong - ministries, groups, prayer/care, volunteering, and community pathways.
5. Gather - service information, events, first visit, location, accessibility, and FAQs.
6. Give - stewardship, impact, safeguards, and the approved secure provider.
7. Connect - contact, prayer, media, publishing, partnership, and newsletter routes.

“Teaching” and “Resources” can remain separate URLs for search clarity while sharing one Grow discovery system.

## Production execution plan

### Milestone 1 - Foundation, brand system, and shared shell

Create the canonical design system, responsive header/footer, page shell, typography, colour tokens, spacing, buttons, cards, forms, icon rules, motion rules, media treatment, and reusable content components. Consolidate menu behaviour and remove duplicated header logic. Define the logo hierarchy and web-optimised asset set.

Acceptance: one coherent system across every page; responsive and keyboard-operable at 320-1920px; no horizontal overflow; reduced-motion support; no broken local routes.

### Milestone 2 - Content architecture and flagship narratives

Rewrite and restructure Home and Our House around the greenhouse metaphor, Kingdom formation, transformation, mind renewal, purpose, creative dominion, leadership, and community. Establish the Know -> Become -> Belong -> Serve -> Influence journey. Add carefully labelled editorial drafts for leadership/beliefs where approval is still needed, without filling factual gaps with invented claims.

Acceptance: a new visitor can identify what the ministry is, why it exists, what it believes at a high level, how it helps people grow, and what next step to take.

### Milestone 3 - Teaching, resources, and The Divine Art of Violence

Replace the appended preview sprawl with server-visible semantic content records and curated library views. Build search/filter-ready teaching and resource components, series pages/templates, media states, transcripts/notes architecture, and a premium featured-book experience.

Acceptance: content is useful without JavaScript; preview and published states are unambiguous; filters work; the flagship book has an approved factual record or an elegant clearly marked pre-publication state.

### Milestone 4 - Belong, Gather, Give, and Connect journeys

Build ministry discovery, volunteering, prayer/care, first visit, events, giving, contact, newsletter, map, social, and FAQ experiences. Keep integrations inactive until verified credentials and destinations are supplied, but avoid presenting dead controls as if they work.

Acceptance: every enabled action completes successfully; every unavailable action has a useful alternative; privacy and safeguarding guidance is appropriate; mobile form completion is excellent.

### Milestone 5 - Original media and storytelling

Create or commission a consistent visual suite using the documented cinematic direction: Nigerian and Black-global representation, natural light, greenhouse architecture, deep greens, warm gold, honest documentary emotion, and generous negative space. Produce responsive WebP/AVIF variants, teaching thumbnails, book imagery, and 1200x630 social previews. Replace remote stock dependencies.

Acceptance: every major page has intentional media; no random stock language; licences/sources are registered; crops, alt text, sizes, and loading behaviour are verified.

### Milestone 6 - SEO, accessibility, performance, legal, and launch QA

Add canonical URLs, sitemap.xml, robots sitemap reference, full social metadata, Organization/Church/WebSite/Breadcrumb/Event/Article schema where factual, clean heading structures, and final alt text. Remove or replace blank PDFs. Run link, HTML, accessibility, performance, keyboard, zoom, screen-reader, responsive, console, and deployed-domain tests.

Acceptance: no critical accessibility defects; no broken links or console errors; all structured data validates; Core Web Vitals and Lighthouse results meet agreed production thresholds; legal and operational content has recorded approval.

### Milestone 7 - Deployment and launch operations

Configure analytics and search tools only with approved accounts, verify the custom domain, redirects, HTTPS, forms, email delivery, donation provider, newsletter, maps, social links, cache rules, and rollback procedure. Create a post-launch content and monitoring checklist.

Acceptance: the approved deployment matches the reviewed build; all external flows are manually tested; ownership and recovery access are documented.

## Access and approvals required later

- Approved mission, vision, doctrine, history, leadership names/biographies/photos, and safeguarding contacts.
- Confirm whether the WhatsApp number and `@GreenhouseAssembly` shown in owner artwork are current and public.
- Public location, gathering schedule, office hours, first-visit details, and accessibility information.
- Secure form provider or endpoint, ministry email addresses, newsletter provider, CAPTCHA decision, and privacy retention policy.
- Approved giving provider, account owner, currencies, recurring-gift policy, and compliance copy.
- The Divine Art of Violence manuscript or approved synopsis, author identity, cover rights, publication status, formats, price/retailer links, and media kit.
- Teaching files, speaker names, transcripts, notes, thumbnails, release permissions, and YouTube/podcast destinations.
- Approved photography, licences, social accounts, maps account, analytics/search-console access, DNS/domain/hosting access, and legal approval.

## Assumptions for the next milestone

- Preserve the ministry name, greenhouse/seedling symbol, deep green and gold equity.
- Treat all new copy as an editorial draft until owner approval, while making it polished enough for review in context.
- Do not publish invented leaders, dates, attendance, testimonies, addresses, payment details, statistics, or credentials.
- Build the static site progressively: semantic HTML first, JavaScript as enhancement, and integrations activated only from verified configuration.
- Keep `greenhouseassembly.org` as the intended canonical domain unless the owner says otherwise.

## Approval gate

The recommended next action is Milestone 1: Foundation, brand system, and shared shell. Implementation should begin only after this plan and direction are approved.

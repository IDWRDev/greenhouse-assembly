# Professional Website Completion Map

## Goal

Deliver a premium, accessible and operational public website for The GreenHouse Assembly Ministries while preserving the existing ministry vision and never inventing leaders, schedules, addresses, payment details or published media.

## Brand and ministry foundation

- Christian formation expressed through faith, formation and flourishing.
- Whole-person discipleship: spirit, mind and body under Christ.
- A Black-global visual and editorial identity, grounded in Nigerian heritage and welcoming Nigerians in the diaspora and the wider global community.
- The shared journey: Know → Become → Belong → Serve → Influence.
- A calm, intelligent and hospitable tone rather than hype, pressure or unsupported claims.

## Delivery stages

### 1. Foundation and truth system

- Preserve the restored website as the content baseline.
- Centralise all missing operational facts in `js/site-config.js`.
- Keep unavailable actions visibly honest until configured.
- Preserve verified brand assets and prepare replacement-ready media slots.

Acceptance: no fabricated public facts; one clear location for owner-supplied details.

### 2. Shared premium experience

- One sticky header and accessible responsive menu.
- One consistent footer across every public page.
- Unified colour, typography, spacing, buttons, cards, forms and focus states.
- Mobile-first layouts without page-level horizontal overflow.

Acceptance: consistent navigation and branding at 320–1920px; keyboard and reduced-motion support.

### 3. Page completion

- Home: strong welcome, formation framework, global community, ministries, teaching, resources, visit and giving pathways.
- About: purpose, heart, mission/vision drafts, values, beliefs, formation model, leadership pending state and invitation.
- Ministries: Grow/Belong/Serve, 16 honest pathways, participation journey, service pathway and FAQs.
- Teaching: series, learning paths and replacement-ready video/audio records.
- Resources: articles, guides, devotionals, reading plans, book framework and honest downloads.
- Events: gathering concepts, first-visit guidance and future registration architecture.
- Give: stewardship, safeguards and secure-provider activation.
- Contact: enquiry categories, validation, privacy guidance and configured delivery.
- Legal and 404: shared global experience and correct recovery paths.

Acceptance: every public page has a clear purpose, next step, responsive layout and truthful status.

### 4. Operational activation

- Contact delivery activates when `contactEmail` or `contactEndpoint` is supplied.
- Newsletter activates when `newsletterAction` is supplied.
- Giving activates only when an approved HTTPS `givingUrl` is supplied.
- Map, phone, service schedule and social links render only from verified configuration.
- Event registration remains inactive until an approved registration destination is supplied.

Acceptance: no control claims to submit, donate, register or download unless its destination is configured and tested.

### 5. Production verification

- Validate local links, assets, headings, form labels and JavaScript syntax.
- Test navigation, forms and focus behaviour.
- Check 320, 375, 430, 768, 1024, 1440 and 1920px layouts.
- Test keyboard navigation, 200% zoom and reduced motion.
- Add approved canonical domain, social images and structured organisation data.
- Verify GitHub Pages after owner-approved commit and push.

## Owner configuration still required

Complete the empty values in `js/site-config.js`:

1. Public contact email and/or secure form endpoint.
2. Phone number and office hours, if public.
3. Physical address, map URL and verified gathering schedule.
4. Approved HTTPS giving-provider URL.
5. Newsletter provider action URL.
6. Approved social profile URLs.
7. Approved event-registration URL.
8. Leadership, ministry-status and published-media approvals.

## Definition of done

The project is complete when all static acceptance checks pass, owner configuration has been supplied, every enabled external destination has been manually verified, browser/device testing is complete, and the deployed GitHub Pages version matches the approved local build.

No commit or push is included in this execution map.

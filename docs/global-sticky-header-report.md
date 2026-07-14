# Global Sticky Header Report

## Implementation method

The existing homepage `.site-header` and inner-page `.site-header` now use the same CSS behaviour: `position: sticky`, `top: 0`, and `z-index: 1000`.

No page-specific sticky-header component was added. The existing fallback header built by `js/mobile-navigation.js` for legal and 404 pages uses the same `.site-header` class, so it receives the same global behaviour.

## Files modified

- `css/style.css`
- `css/pages.css`

## Shared components covered

- Homepage header and desktop/mobile navigation
- Inner-page header and desktop/mobile navigation
- Legal-page and 404 fallback header
- Existing Give button and mobile hamburger behaviour

## Accessibility measures

- Skip links now sit above the sticky header.
- Anchor targets, page headers, and sections use scroll margins to avoid being obscured.
- Existing keyboard, Escape-to-close, focus-return, and visible-focus behaviour remain unchanged.
- No scroll animation or JavaScript scroll listener was added.

## Static verification

- CSS diff formatting checked.
- Shared navigation script syntax checked.
- All public HTML pages reference the common header CSS/script paths already used by the project.

## Remaining verification

Real browser testing remains required at 320, 375, 430, 768, 1024, 1440, and 1920 pixels, including scroll, menu, focus, and console checks.

No commit or push was performed.

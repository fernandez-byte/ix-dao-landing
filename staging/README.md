# Handoff: IX DAO Landing Page

## Overview
Marketing landing page for **IX DAO** — the support organisation of the INFAXIA metaverse gaming platform. The core message is "Complete the Job, Get Paid": community members earn USDT by completing real tasks (social shares, game reviews, UX feedback, bug hunts) after qualifying with IX Free Points (IX FP). The page's job is to drive visitors to join the IX DAO Discord and register on INFAXIA.

## About the Design Files
The files in this bundle are **design references created in HTML** — a prototype showing the intended look, layout, and behavior. They are **not production code to copy directly**.

The task is to **recreate this design in your target codebase's environment** (React, Vue, Next.js, etc.), using its established components, styling approach, and conventions. If no frontend environment exists yet, pick the most appropriate framework for the project and implement there. Treat the HTML as the visual/behavioral spec, not the deliverable.

The prototype is authored as a "Design Component" (`.dc.html`) with a small runtime (`support.js`) and a drag-and-drop `image-slot` web component. **You do not need either in production** — replace `<image-slot>` elements with normal `<img>` tags (assets are provided in `assets/`), and re-implement the tweakable props (colorway, glow, section toggles) as normal component props or config.

## Fidelity
**High-fidelity (hifi).** Final colors, typography, spacing, gradients, and interactions are all specified below and present in the HTML. Recreate pixel-perfectly using your codebase's libraries and patterns.

## Screens / Views
Single long-scroll landing page, max content width **1200px**, centered, `40px` horizontal padding. Sections top to bottom:

1. **Sticky Nav** — translucent blurred bar. Left: IX DAO mark (link icon) + "IX DAO" wordmark. Right: text links (Jobs, How It Works, Eligibility, FAQ) + gradient "Join Us" pill button. Height ~66px, `1px` bottom border.
2. **Hero** — 2-column grid (`minmax(360px,1fr)` each, `52px` gap). Left: eyebrow pill ("Now Accepting Members — Limited Spots") with pulsing dot, H1 "Complete the Job, / Get Paid." (second line gradient + shimmer), sub-paragraph, two CTAs (primary gradient "Join IX DAO Discord", ghost "See Available Jobs"), two trust rows (shield/check icons). Right: 5:4 image card with gradient glow border and a floating "0.1 USDT / reward per completed job" glass chip. Animated floating orbs + sweeping horizontal lines in background.
3. **Stats strip** — 4-cell grid (Job Types 4 / USDT 0.1 / Verified 100% / Free), hairline dividers, rounded container.
4. **Features** — 3 cards (Zero Risk, Real Tasks, Real Pay), each = icon badge + title + one-line body. Neon hover (glow border + lift). No images.
5. **Ecosystem** — 2 cards (IX DAO / INFAXIA), each = 16:9 image + label + title + 3 icon rows.
6. **Gallery ("Inside INFAXIA")** — asymmetric image grid: 4 columns, `150px` rows; one 2×2 feature cell + five smaller cells.
7. **How It Works** — 6 numbered step cards (`01`–`06`), icon badge + title + body; step 06 is gradient-highlighted ("Get Paid in USDT"). Neon hover on 01–05.
8. **Available Jobs** — 4 cards (Social Share, Game Review, User Experience, Bug Hunt), each = 16:10 image + icon+title + body + reward chips (USDT + IX FP) + "Requires IX Vanguard role" note with lock icon. Card #1 has a "500 followers" overlay badge. Neon hover.
9. **Testimonials** — 4 quote cards (quotation glyph, quote text, circular avatar + name + role).
10. **Rules ("Who Can Join & The Rules")** — 3 cards: To Qualify (accent checks), Not Allowed (red X marks, `#E86A6A`), USDT Payout (gradient badge, accent checks).
11. **FAQ** — accordion, max width 780px, 6 items; chevron rotates 180° and body expands `max-height 0 → 240px` on open. First item open by default.
12. **CTA** — full-bleed background image (cyberpunk characters) with dark gradient overlay + radial accent glow; centered white H2 "Ready to complete your first job?", sub-paragraph, two buttons. Background is absolute-fill so the section height is driven by content.
13. **Footer** — mark + wordmark + tagline on the left; Discord & X icon buttons (rounded square, hover glow + lift) on the right; copyright line "© 2026 IX DAO. Not a financial product."

## Image Placement (CRITICAL — read this before coding)
A previous implementation got the image positions wrong. Every image below is a **plain `<img>` that fills its container with `width:100%; height:100%; object-fit:cover; display:block`**, and the container has `overflow:hidden` + the card's border-radius. Images are NEVER inline/auto-sized and NEVER pushed below content — they sit inside a fixed-ratio box. In the prototype these are `<image-slot>` custom elements; **replace each with a normal `<img src="assets/…">`** exactly as mapped here.

| Section | Container (aspect-ratio + position) | object-fit | Asset | Notes |
|---|---|---|---|---|
| Hero | `aspect-ratio:5/4`, right column of hero grid, `border-radius:22px`, gradient glow border, `overflow:hidden` | cover | `slot-ixdao-hero.webp` | Floating "0.1 USDT" glass chip is **absolutely positioned** over the bottom of this image (`bottom:18px; left:18px; right:18px`), not below it. |
| Ecosystem ×2 | `aspect-ratio:16/9`, **top** of each card, card `border-radius:22px`, image has bottom hairline border | cover | `slot-ixdao-org1.webp`, `slot-ixdao-org2.webp` | Text block sits BELOW the image, inside `padding:28px`. |
| Gallery | CSS grid `grid-template-columns:repeat(4,1fr); grid-auto-rows:150px; gap:14px`. Cell 1 = `grid-column:span 2; grid-row:span 2`; cells 2,3,5,6 = 1×1; cell 4 = `grid-column:span 2`. Each cell `border-radius:18px; overflow:hidden` | cover | `slot-ixdao-gal1..6.webp` (gal1 is the 2×2 feature) | Images fill each cell fully. |
| Jobs ×4 | `aspect-ratio:16/10`, **top** of each card, card `border-radius:20px`, image has bottom hairline border | cover | `slot-ixdao-job1..4.webp` | Text (icon+title, body, reward chips, lock note) sits BELOW the image. Card #1 has a "500 followers" pill **absolutely positioned** at `top:12px; left:12px` over the image. |
| Testimonials ×4 | `width:40px; height:40px; border-radius:50%; overflow:hidden` avatar, inline with name/role | cover | `slot-ixdao-avatar-1..4.webp` | Circular; keyed to testimonial `id`. |
| CTA | **absolute-fill** background: wrapper `position:relative; overflow:hidden; border-radius:26px`; image in `position:absolute; inset:0` with `object-fit:cover`; dark gradient overlay + radial glow are sibling absolute layers ON TOP; text/buttons are `position:relative` above all layers | cover | `ixdao-cta-bg.jpg` | Section height is driven by the TEXT, not the image. Image must NOT be a normal flow block (that was the bug — it made the section huge). |
| Nav / Footer logo | Nav `width:44px; height:34px`; Footer `width:40px; height:30px`; `object-fit:contain` | contain | `ixdao-mark.png` | Sits left of the "IX DAO" wordmark text. Contain (not cover) so the mark isn't cropped. |

## Interactions & Behavior
- **Scroll reveal**: every `<section>` fades in + rises `translateY(30px) → 0`, `opacity 0 → 1`, transition `.7s cubic-bezier(.16,.8,.3,1)`, triggered by IntersectionObserver at `threshold 0.08`, `rootMargin 0px 0px -6% 0px`. Include a safety timeout that reveals all after 2.5s, and honor `prefers-reduced-motion`.
- **Buttons**: primary/secondary lift `translateY(-3px)` + stronger glow on hover (`.22s ease`). Primary buttons have a living-gradient animation (`background-size:200% auto`, `btnFlow` keyframes, 5s linear infinite).
- **Cards** (features, jobs, steps 01–05): hover → accent border, `0 0 30px` accent glow, `translateY(-4px)`, `.28s ease`.
- **FAQ accordion**: click toggles one open item; chevron rotates; body animates via `max-height`.
- **Hero decorations**: floating orbs (`floatA` 9s / `floatB` 11s), sweeping lines (`lineSweep` 6s & 9s reverse), "Get Paid." shimmer (`shimmerText` 5s), eyebrow dot pulse (`pulseDot` 2.4s).

## State Management
- `openFaq` (index of open FAQ item; default `0`, `-1` = none).
- Config/props (were prototype "tweaks"): `colorway` (`volt` default | `cyan` | `indigo` | `ember` | `gold`), `glowIntensity` (0.2–1.8), `showStats` (bool), `showTestimonials` (bool).
- Static content arrays: testimonials (4), FAQ items (6). No data fetching.

## Design Tokens
**Neutral palette (dark navy base)**
- `--bg #0C1026` · `--bg2 #111634` · `--card #181E42` · `--card2 #202856`
- `--line rgba(150,175,240,0.18)` · `--text #EBEFFF` · `--muted #A6B2D6` · `--muted2 #6E7AA6`
- Page background: `radial-gradient(ellipse 90% 60% at 72% -5%, #1B2358, var(--bg) 58%)`
- Borders use `color-mix(in srgb, var(--accent) 22%, var(--line))`; accent-dim = `color-mix(in srgb, var(--accent) 16%, transparent)`.
- Danger (Not Allowed): `#E86A6A`. Lock note icon: `#F5A623`.

**Colorways (accent / accent2 / gradient / on-accent text)**
- **cyan** (default): `#35DCF0` / `#4C7BFF` / `linear-gradient(120deg,#35DCF0,#4C7BFF)` / on-accent `#06121C`
- **indigo**: `#8A93FF` / `#5B6BFF` / `linear-gradient(120deg,#5B6BFF,#8A7BFF)` / on-accent `#FFFFFF`
- **volt**: `#3DE6A6` / `#35DCF0` / `linear-gradient(120deg,#24D68F,#35DCF0)` / on-accent `#052018`

**Typography**
- Display/headings: **Space Grotesk** (700 hero/H2, 600 card titles). H1 `clamp(40px,5.6vw,68px)`, line-height 1.02, letter-spacing -0.02em. H2 `clamp(30px,4vw,46px)`.
- Body/UI: **IBM Plex Sans** (400/500/600). Body 14.5–17.5px, line-height ~1.55.
- Eyebrows/mono labels: **IBM Plex Mono** (400/500), 11–11.5px, uppercase, letter-spacing 0.06–0.14em, accent color + `text-shadow 0 0 14px` accent glow.

**Radii**: buttons/badges 10–14px · cards 18–22px · CTA 26px · pills 100px.
**Shadows/glow**: neon glows use `0 0 20–46px` of `color-mix(accent, transparent)`. No hard drop shadows.
**Spacing**: sections ~60–70px vertical padding; card padding 22–32px; grid gaps 14–24px.

## Assets
All in `assets/` (copied from the prototype's filled image slots):
- `ixdao-mark.png` — IX DAO link/infinity brand mark (nav + footer logo). Pairs with a text "IX DAO" wordmark.
- `slot-ixdao-hero.webp` — hero image (IX DAO circuit art).
- `slot-ixdao-org1.webp`, `slot-ixdao-org2.webp` — ecosystem cards (IX DAO / INFAXIA).
- `slot-ixdao-gal1..6.webp` — gallery grid images.
- `slot-ixdao-job1..4.webp` — job card thumbnails.
- `slot-ixdao-avatar-1..4.webp` — testimonial avatars.
- `ixdao-cta-bg.jpg` — CTA full-bleed background (cyberpunk characters).

Icons are inline SVGs in the HTML (shield, wallet, gamepad, bug, share graph, star, discord, X, chevron, check, etc.) — copy the SVG paths directly or swap for your icon library's equivalents. Discord/X footer icons are standard brand glyphs.

## Files
- `IX DAO Landing.dc.html` — the full design prototype (structure, inline styles, animations, logic). **Primary reference.**
- `image-slot.js`, `support.js` — prototype runtime only; not needed in production (see note above).
- `assets/` — all images.

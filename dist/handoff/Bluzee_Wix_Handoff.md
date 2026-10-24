# Bluzee — Website redesign concept and Wix handoff

Prepared 24 October 2026. This is a separate private design concept. The existing Bluzee Wix website has not been changed. Implementation and launch in Wix remain separate steps.

## Review package

- Open the homepage in `dist/index.html` or the private concept URL supplied with this package.
- Open `dist/design-notes/index.html` for the visual direction, linked sitemap, page layouts, source mapping and Wix implementation notes.
- Ten brochure PDFs are in `dist/brochures/`: the original nine plus the newly supplied six-page workshop brochure. The 26-page ERP guide is in `dist/resources/`. All are linked from appropriate pages.
- All 12 offering records and suggested page copy are in `content.py` and `dist/handoff/offerings-cms.csv`.
- `preservation-inventory.json` contains original proof URLs, media IDs and legacy route recommendations. `Wix_Implementation_Research.md` contains official references.

## Information architecture

Primary navigation: Home; About Us; Our Offerings; Events; Testimonials; Contact Us.

Our Offerings → Products: Bluzee DealTailor™, Bluzee Dimaq™. Keep QSRPro, Tradesphere and Nexus visible as the wider portfolio.

Our Offerings → Services:

- Bluzee ERP Consulting Services: Odoo ERP Consulting, Odoo ERP Implementation, ERP Talent Outsourcing, ERP Support.
- Bluzee Academy of Experience: Bluzee ERP Experience Hub™, Bluzee AI Experience Hub.
- Professional Workshop: Design Your Professional Character™.

Events and Testimonials are dedicated primary destinations. The former Stories & Sessions route remains available as a full media archive. Retain existing SAP, ZATCA, industries, careers, blog and legal destinations. The separate concept review page is a review utility, not a proposed production menu item.

## Visual direction

Deep navy `#030914`; electric blue `#3979FF`; cyan `#7AE7FF`; deep burgundy `#74172F` and brand red `#EF3340`; pale blue `#EDF5FB`; text ink `#102B4B`.

Use Space Grotesk for expressive headlines and Manrope for readable body text. The concept hosts both locally. Preserve the transparent original Bluzee logo geometry. Use white lettering with a bright red U on navy, and navy lettering with a bright red U on pale blue. The concept uses an alpha mask over the original PNG; prepare equivalent transparent brand assets from the original vector for Wix. No white logo box. Odoo Learning Partner artwork appears on relevant service pages.

A cinematic intelligence core gives the homepage a distinctive visual anchor. New conceptual modular ERP and digital-guide images align with their section content; an illustrative project-delivery scene supports the Academy. Brochure imagery supports the offering pages. Actual event and participant imagery is always the original source material, never generated event evidence.

Use high contrast, generous spacing and constrained paragraph widths. The review implementation responds from 320 pixels upward. Wix Studio implementation should set explicit desktop, tablet and mobile breakpoints and check intermediate widths.

## Homepage layout and suggested copy

1. **Hero:** “Intelligence. Put to work.” Supporting copy: “Convert intent into opportunity. Data into decisions. Skills into experience. Make your next move with Bluzee.” CTAs: Explore our AI products; Start a conversation.
2. **Session experience strip:** IIM Kozhikode, IIT Madras, NIT Calicut and Volvo. Label these as workshop/session experience, not product customers or institutional endorsements.
3. **Two AI product cards:** DealTailor™ — individual enquiries, context-rich conversations and sales handovers. Dimaq™ — authorised enterprise data and actions beyond familiar dashboards. Each includes a dedicated-page route and correct PDF.
4. **Wider portfolio:** QSRPro, Tradesphere, Nexus, each linked to its own page.
5. **ERP services:** “Every module. A business reason.” An editorial introduction explains how Bluzee helps avoid irrelevant ERP scope and protect budgets; a modular architecture visual supports a phased roadmap, followed by four service routes and Odoo Learning Partner artwork.
6. **Academy:** “Build the experience. Show what you can deliver.” A six-month introduction connects scoped assignments, reviewed work, documented contributions and a completion-based Bluzee experience certificate. Employer acceptance and job eligibility remain role-dependent. Both hubs and the burgundy workshop feature remain visible.
7. **Original proof:** IIM, Volvo and IIT recordings, followed by the full searchable archive.
8. **ERP reference:** “A clearer path. Before you begin.” A modern digital-guide visual responds to cursor movement with bounded depth and a spotlight; the original 26-page July 2024 PDF is unchanged.
9. **People and purpose:** A homepage teaser leads to the inherited leadership profiles and vision/mission sections on About.
10. **Contact:** General and AI product email routes, UAE WhatsApp, and UAE/India telephone links. Full regional addresses on Contact; Dubai Trade License 786627 in the footer and Dubai office details.

## Offering page layout

Breadcrumb; offering name; impact headline; concise description; relevant visual; next-step CTA; matching brochure; value overview; four capabilities; offering-specific section; practical steps; scope and fit; related offerings; contact.

- DealTailor™: illustrative Understand / Engage / Progress tabs; controlled deployment, AWS-managed model access and administrator boundaries.
- Dimaq™: Finance / Sales / Operations examples; platform-agnostic positioning with connector and permission qualifications; private AI and administrator controls; advisory role retained.
- Consulting: Phase 1 / Later phases / Defer or exclude, grounded in business continuity and relevance.
- Implementation: customer involvement, AI-assisted work with human review, weekly playback and industry-informed testing. No guaranteed implementation duration.
- Support: eight operational checklist accordions, transition readiness and agreed service scope.
- ERP Hub: six-month pathway, participant voices and existing registration route; access and outcomes qualified.
- AI Hub: separate six-part curricula for AI Application Developer and AI-powered Full-Stack Developer; comparison table; shared evidence portfolio; illustrative industries; permanent, contract and freelance pathways. No employment or universal recognition guarantee.
- Workshop: correct VCS Method (Value Creator Signature), S2VC Pathway (Student to Value Creator), original sessions and feedback.

## Practical Wix build

1. Confirm Editor vs Studio. Wix now supports an unpublished Studio version for eligible Premium Editor sites. Design is rebuilt; some dashboard and app data remains shared. Avoid live data mutations. A separate Wix duplicate is another option.
2. Use native Studio grids, stacks, containers and responsive constraints. Recommended Wix breakpoints: 1001px+, 751–1000px, 320–750px. Collapse the menu on small screens and preserve native scrolling.
3. Use a three-level native menu or accessible mega menu. Keep links as real menu items. Test keyboard access, focus, Escape and mobile scrolling.
4. Use an **Offerings** CMS collection: slug, group, category, title, short title, headline, summary, image, tags, overview, capabilities, process, scope, brochure Document field, CTA, related items and template variant. Flagship product pages can remain static; common services can use a dynamic template.
5. Use a **Proof** CMS collection: title, type, institution/participant, date, source URL, original video/media ID, poster, attribution, permissions/consent status and sort order. Do not replace the original Wix Video items.
6. Use normal buttons linked to CMS Document fields for brochure downloads. Wix’s dedicated Document Button currently cannot bind directly to a collection file field.
7. Replace the concept’s email-draft form with Wix Forms, configured recipients, spam protection, appropriate privacy wording and confirmed-success behaviour. This concept sends no enquiry and has no CRM integration.
8. Use native entrance and hover effects for 450–650ms reveals, portrait/card transitions and image zoom. The enhanced concept adds hero light trails, a capability marquee, ocean waves, a mission orbit and a reading-progress line. Custom CSS/SVG is needed for the exact wave/orbit/trail treatments; recreate as small decorative embeds or custom elements only where native effects cannot match. Optional Velo/custom-element code handles pointer depth and global motion preference. Preserve semantic content in native Wix elements. Keep pointer motion on fine-pointer devices, pause offscreen/hidden-tab effects, and honour reduced-motion preferences. The always-available motion control must stop all decorative motion. Do not autoplay session videos or hijack scrolling.
9. Workflow examples can use native multi-state boxes and buttons. CMS filtering can use native dataset controls; Velo is optional for more complex filter state or custom interactions. A full-site iframe is unnecessary.
10. Configure titles, descriptions, alt text, social images, production canonicals and sitemap. The concept is deliberately marked noindex; remove that only for the approved production site.
11. Apply reviewed 301 redirects for moved pages, retain original blog/legal content and audit all PDF/video destinations.
12. Review using Wix Preview / Get Client Feedback. Publishing requires a separate launch decision. A Studio plan may be required; publishing a Studio branch prevents republishing the original Editor branch.

## Content and source qualifications

The eight service/DealTailor™ PDFs are supplied source files. The specifically named October 2026 Dimaq™ PDF was unavailable; the current `Bluzee_Dimaq_Brochure.pptx` was converted to a 13-page PDF, visually reviewed and attached. QSRPro, Tradesphere and Nexus use the corporate presentation summaries; no individual PDFs were supplied for them. Their pages therefore have discussion CTAs without unrelated brochure downloads.

Privacy depends on model, region, logging, retention, permissions and connected-service configuration. Integration depends on APIs, connectors, versions and customisation. Do not turn qualified source language into guarantees.

Approved website contacts: general enquiries inbox@bluzee.xyz; AI product enquiries ai@bluzee.xyz; UAE WhatsApp +971 58 653 1493; UAE calls +971 58181 7499; India calls +91 88610 56458. Every page includes the WhatsApp icon, new number, both email addresses and Dubai Trade License 786627. Four regional addresses are retained. The legacy Saudi WhatsApp number stays in the audit inventory only.

The concept form prepares an email draft: DealTailor™ and Dimaq™ enquiries go to ai@bluzee.xyz, with inbox@bluzee.xyz copied. Other offerings use the general inbox. Configure and test equivalent Wix Forms automations/recipient rules before launch; no mailbox or backend has been provisioned by this concept.

## Preserve and repair

Preserved: seven directly available original recordings, four named student testimonial routes, the original Volvo appreciation letter, existing registration forms, existing resource PDF, and legacy blog/legal/service destinations.

Student testimonial videos link to the existing Wix gallery because their public direct endpoints did not resolve reliably. Keep the original Wix players/media IDs during migration. Do not rewrite testimonial quotes or claim that all recordings were transcribed.

Repair before Wix launch: the broken inauguration story destination and erroneous Wix Instagram link. Do not import placeholder About copy, generic Wix portfolio project entries or the third-party Captivea methodology text. Refer to the full preservation inventory for exact routes and evidence.

## Validation

The concept was checked for local page/asset/anchor links, unique headings/IDs, correct PDF mapping, current Dimaq™ naming, desktop and narrow layouts, menu operation, tab behaviour, filtering/search, original IIM playback, enquiry preselection and draft generation, and motion pause. The Dimaq™ PDF conversion was rendered and visually inspected. Native Wix configuration, recipient routing, every historical recording, consent records and production SEO must be validated again in the actual Wix implementation.


## Final review additions — 24 October 2026

- **Brand:** red U throughout the shared header/footer; Bluzee™ at both logo placements on the landing page; DealTailor™ and Dimaq™ throughout website copy. Source PDFs remain unchanged, including their historical contact details and trademark styling.
- **Leadership:** seven inherited portraits and names/titles, grouped as leadership and advisors/consulting. Preserve original profile links. Only Mukundakumar KG has a source-supported supplementary biography; no biographies were invented for the other entries. “Adlan — Consulting House” follows the original website without inferred expansion. See `leadership-source-inventory.json` and `leadership-cms.csv`.
- **Purpose:** complete original vision and mission statements are retained on About, alongside an animated blue-ocean illustration and mission orbit.
- **ERP guide:** original July 2024 PDF copied unchanged from the current website; available from Home, every footer and Stories & Sessions.
- **Workshop reach:** 23 academic institution labels from the supplied six-page brochure plus SCMS Cochin, for 24 in total. Volvo Group India is shown separately as corporate workshop experience. Institution names follow the source labels; no new endorsements or logos are implied. See `workshop-institutions-cms.csv`.
- **Brochures:** the six-page corporate workshop brochure is now the main workshop download. The original four-page detailed pathway brochure remains available from a secondary link.

### Additional Wix collections

Use **Leadership** (name, title, portrait, biography, profile URL, category, order); **Workshop Reach** (institution name, type, source, order); **Company Details** (general email, AI email, WhatsApp display number/link, call numbers, license, offices, vision, mission); and **Resources** (title, edition, cover, PDF). Keeping company details in a single collection/global component prevents inconsistent contacts.

### Review evidence and limits

The revision was checked across 18 pages for local page/asset/anchor links, trademarks, contact destinations, logo treatment and license text. Desktop and 390/320-pixel responsive review frames were inspected; checked content widths were 375/305 pixels after scrollbars, without horizontal overflow. Seven leadership images loaded. The workshop list contains 24 names. AI and general email-draft routing were exercised without sending. Hero animation and pause were checked in-browser; reduced-motion, fine-pointer and offscreen/hidden-tab handling were inspected in the source. This is not a complete device/accessibility certification. Original videos, testimonials and registration routes remain preserved. Wix implementation, real form delivery and production launch remain separate.

Current screenshots: `Bluzee_Dynamic_Homepage.jpg` and `Bluzee_Dynamic_Academy.jpg`. Source PDFs are intentionally preserved unchanged.


## Dynamic concept revision and media split

The final navigation includes **Events** (`/events/`) and **Testimonials** (`/testimonials/`). Preserve `/stories/` as the legacy full archive or implement a carefully reviewed redirect once the production migration is approved.

### Events content

- Six original event/session recordings: ERP Experience Hub inauguration, DYPC at IIM Kozhikode, Volvo, IIT Madras and NIT Calicut, and the Dubai mindfulness workshop.
- One additional ERP Hub programme introduction.
- Fourteen original gallery photographs: seven inauguration images and seven mindfulness images, preserving source order and high-resolution source links.
- Three archived event stories: RSET MoU, ERP Hub operational launch and the May 2025 recruitment drive, with four associated source images. Publication and event dates are distinguished.
- The verified launch is the **ERP Experience Hub inauguration on 22 May 2025**, not a separately verified corporate Bluzee launch. No additional corporate-launch recording was discoverable.

### Testimonials content

- Four named participant video cards link to the existing Wix gallery; retain the actual Wix Video player/collection and media IDs during Wix implementation. Stable standalone MP4 endpoints were not available for these four, so the concept does not pretend to embed migrated copies.
- The original Volvo appreciation letter is retained.
- Six original partner identities are shown in a separate partner section: RSET, Sequantix, Cloudvalley, Odoo, DSTI and Techative. No accreditation level, endorsement or relationship scope is inferred from logos.

Source evidence is in `events-testimonials-source-inventory.json`; implementation exports are `events-cms.csv`, `event-gallery-cms.csv` and `partners-cms.csv`. Event photographs are optimized derivatives of original media, not generated replacements. All four new illustrative assets, generation method and prompts are documented in `visual-assets-v3.json`.

### Motion implementation

The hero combines image breathing, 14 floating light particles, three orbit paths, moving SVG beams and fine-pointer parallax. The ERP, guide and Academy visuals use event-driven requestAnimationFrame updates with a bounded perspective transform. The guide adds a cursor spotlight. These are decorative effects; navigation and copy stay usable without JavaScript.

In Wix, use native grids, typography, menus and image elements. Match basic entrance and hover effects natively. Exact orbit paths, particles and pointer depth need a small scoped custom element/CSS implementation. Apply the existing pause/reduced-motion control to every effect, pause offscreen and hidden-tab animation, and disable cursor effects for coarse pointers. Avoid a whole-site iframe or heavy animation library.

The revised dark blue foundation is #030914, with slightly raised navy panels. Pale sections remain for readable contrast. The logo U is #EF3340 across every page; preserve the original logo geometry and alpha.


## Vision & Mission — cinematic revision

The About page now presents two distinct editorial chapters with original conceptual imagery. The full source Vision and Mission statements remain verbatim, including the two Vision paragraphs. New headlines introduce the source statements without replacing them. The five Mission principles use phrases from the source statement; no additional claims were added.

- Vision: architectural gateway toward an open blue ocean; navy, electric blue and cyan.
- Mission: glass and burgundy forms converging toward a shared direction; warm red accents.
- Desktop: alternating two-column chapters, 630–670px tall image windows, spacious reading columns, and a chapter navigator. Below 800px: text and imagery stack naturally; no horizontal scrolling.
- Use native Wix text and image elements, semantic heading levels, section anchors `purpose`, `vision`, `mission`, and `leadership`. Preserve the full statements as selectable page text.
- Five Mission principles form a keyboard-operable tab group. Arrow keys, Home and End switch focus and content. Do not auto-rotate these statements. Use a Wix tabs component if it provides equivalent semantics; otherwise retain the supplied small scoped behavior.
- Artwork entrances use opacity and 24px vertical movement. Slow 24-second image breathing and a very low-opacity light pass add depth. Pointer movement is visual-only and limited to 6px horizontally and 5px vertically.
- The exact image treatment needs scoped CSS/custom elements in Wix; the image windows, typography, grid and basic entrance effects can be built natively. The complete proof-of-concept styles and behavior are in `dist/assets/purpose.css` and `purpose.js`.
- Keep the site-wide Pause motion control, reduced-motion support, offscreen animation pause and hidden-tab pause. Do not scroll-jack or autoplay video. Official statements remain visible regardless of JavaScript or motion settings.
- New image sources, prompts and web-ready sizes are recorded in `visual-assets-v4.json`. No generated image represents a real Bluzee location, staff member, event or client.


## Events & Testimonials — cinematic revision

Events and Testimonials now each have a distinct original conceptual backdrop. Actual event photographs, original recording posters, participant videos, appreciation and partner logos remain separate source evidence. No testimonial quotes, ratings, endorsements or achievements were generated.

### Events

- Full-width sculptural blue stage artwork with a dark reading gradient; original launch and leadership photographs appear as floating foreground frames.
- Featured ERP Experience Hub inauguration: 22 May 2025, Kochi Marriott Hotel. Its original recording is available from the hero, spotlight and full archive.
- Existing seven recordings retain their original endpoints, filters, search, modal playback and source links. A duplicate presentation of the launch recording is intentional; it is one original event.
- Fourteen original event-gallery photographs and the three original event journal stories remain available. The gallery uses a larger lead photograph with supporting tiles, and every tile retains its original source link.

### Testimonials

- A separate blue-glass visual expresses voice and resonance, with original participant thumbnails and a decorative animated waveform. This is not an audio player.
- Four larger participant-video cards preserve names, original posters and original Wix video-gallery links. Direct MP4 access remains unavailable for these four testimonials. In Wix, retain the original Video players and media IDs recorded in the preservation inventory.
- Volvo appreciation remains the original letter; the visual treatment adds a document frame without rewriting the feedback.
- All six original partner logos are displayed unchanged in a new grid. Do not add certification, endorsement or relationship-scope claims.

### Wix construction & motion

Use native text, buttons, anchors, section grids and media for all content. Build the event photo composition with layered containers. Add native entrance/hover effects where suitable; exact floating frames, background light passes, and pointer depth require the supplied scoped CSS/custom-element treatment. Source files: `media_experience.py`, `dist/assets/media-experience.css`, `dist/assets/media-experience.js`. Original generation prompts and output asset locations are recorded in `visual-assets-v5.json`.

Motion uses transform and opacity, bounded fine-pointer depth, 22-second background breathing, 8–10-second photo movement and decorative waveform scaling. It never auto-rotates stories, plays audio, or hijacks scrolling. Existing Pause motion and reduced-motion preferences suppress these effects. Hero animations pause offscreen or when the browser tab is hidden. All content and calls to action remain available with motion disabled.

Responsive views stack the hero content and photographs, change the chapter navigation to rows, and use one-column participant cards on narrow screens. Original posters retain their proportions. Partner logos remain readable on their pale backgrounds.


## Homepage — human-centred landing revision

The homepage hero now uses a calm illustrative workplace scene with three professionals collaborating in natural daylight. This replaces the abstract intelligence-core background. The original headline, introductory copy, AI product links, trademark styling and enquiry routes remain unchanged. A discreet image caption and accessible description identify the scene as illustrative; it does not depict actual Bluzee staff or clients.

The hero keeps its navy reading area, pale cyan title and small burgundy accent in the photograph. Typography is sized to avoid covering faces. On mobile, the image sits below the copy with a soft transition, preserving readable text and all three people. The original orbit, particle and beam elements are removed from the homepage.

Use `dist/assets/hero-human-v6.webp` (desktop) and `hero-human-v6-small.webp` (mobile). The image uses a 30-second, 3% camera-style zoom with a very small response to pointer position; a 20-second soft daylight fade adds atmosphere. The copy is immediately readable and does not blur or animate. Pause motion, reduced-motion, offscreen and hidden-tab behavior are retained.

In Wix, build the copy and CTA buttons as native elements; use the image as a background with a dark overlay. At the mobile breakpoint, reserve a separate lower image area rather than placing text over faces. The exact camera and daylight effects are in `dist/assets/human-hero.css`; simpler native slow pan/zoom can be used if equivalent reduced-motion and pause behavior is maintained. The full prompt and image provenance are recorded in `visual-assets-v6.json`.

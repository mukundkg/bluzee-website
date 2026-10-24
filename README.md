# Bluzee website redesign concept

A separate private concept for Wix implementation. No live Wix site changes have been made.

Open `dist/index.html`, or serve the `dist/` directory using any static server. Browser JavaScript is progressively enhanced; all offering copy is present in static HTML. Live historical recordings require internet access. The contact form only prepares an email draft and does not send anything.

Start the design review at `dist/design-notes/index.html`. Handoff notes, offering CMS content and the preservation audit are in `dist/handoff/`. Ten brochures are included in `dist/brochures/`; the original 26-page ERP guide is in `dist/resources/`.

Edit copy in `content.py`, layout in `build.py`, `enhancements.py` and `v3_experience.py`, inherited company details in `content-source/leadership-vision-mission-guide.json`, styling in `dist/assets/styles.css`, and behaviour in `dist/assets/app.js`. Rebuild using `python build.py` (Pillow required); existing optimised assets and PDFs remain in `dist/`. Original research paths in the preservation inventory are historical audit metadata and are not runtime dependencies. Validate links using `python validate.py`; syntax-check JavaScript using `node --check dist/assets/app.js`.

`prepare_assets.py` documents the original asset preparation workflow; the prebuilt assets are already included. It is not required to run the website.

Do not upload the entire concept as an iframe into Wix. Recreate the approved design using native Wix Studio sections, CMS, menus, forms and media; use the included notes for implementation.

The dynamic revision adds dedicated Events and Testimonials pages, source-verified partner logos and event galleries. Its additional content is in `content-source/events-partners-v3.json`. New visual asset prompts, CMS exports and current QA evidence are in `dist/handoff/`.

Events and Testimonials cinematic revision: `media_experience.py` wraps the preserved source content; `dist/assets/media-experience.css` and `media-experience.js` provide scoped presentation and motion. Read the updated handoff for Wix construction and original media preservation. Page-only rebuilds preserve prepared proof images byte-for-byte.

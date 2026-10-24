# Bluzee redesign: Wix implementation notes

Research checked against official Wix documentation on 24 October 2026. These notes specify a future Wix implementation; no live site was edited or published during this research.

## Recommended implementation route

Use Wix Studio for the responsive design, keeping the review concept separate from the live Bluzee site. First inspect the current site's editor, plan and apps. Current Wix documentation supports creating an unpublished Studio branch of a Premium Wix Editor site. The original remains live while the new design is rebuilt. The design itself does not carry over. Publishing the branch requires a Studio plan and replaces the live Editor branch; Wix says the original Editor branch cannot then be republished. [1]

Before any future migration, preserve a copy and a complete URL/content inventory. Most dashboard data and apps are shared between branches, while some apps and old Wix Forms submissions do not transfer. Because data is shared, treat dashboard or content changes as potentially affecting the live site; isolate proposed content instead of overwriting live records. Check app compatibility and forms explicitly. [2]

If the account cannot create a Studio branch, implement in an unpublished duplicate or separate Studio project and reconcile assets/data before launch. A duplicate does not preserve every business record or third-party setting, so it is not a full operational backup. [3]

## Native Wix implementation and special setup

| Design requirement | Preferred Wix implementation | Custom code or special setup |
| --- | --- | --- |
| Shared header and footer | Global sections with Site Styles, brand logo and reusable buttons | None for the main layout |
| Our Offerings navigation | New Studio menu with three layers: Our Offerings → Products / Services → individual offering | Use actual menu items for page links; do not build navigation only from buttons placed in dropdown containers |
| Desktop and mobile navigation | Horizontal desktop menu; hamburger layout at tablet/mobile, with visible section headings | Native layout switching; keyboard and touch QA still required |
| Product and service pages | Static flagship pages for DealTailor and Dimaq; reusable CMS dynamic template for consistent service pages | Bespoke sections can be static when content shape differs; no need to force every offering into one rigid template |
| Brochure downloads | Upload original PDFs to Media Manager; store each in a Document field; connect a regular button to that field | The specialized Document Button element currently cannot bind to CMS; a regular button or linked image can [5] |
| Testimonials and recordings | Existing media records/URLs, presented in Wix Video channels or a CMS-driven proof library | Manually verify every original video ID, quote, attribution, poster and external link |
| Filters for the proof library | CMS categories and repeater filters, grouped as testimonials, sessions, IIM content and student stories | Use Velo only if the selected filter interaction cannot be built with native controls |
| Reveal and hover animation | Native entrance, hover and click effects | Reserve CSS for small decorative details; no animation framework is required |
| Contact form | Wix Forms with labelled fields, offering selector, validation and a clear success state | Configure recipients and Wix Automations; test delivery before launch |
| SEO and legacy URLs | Preserve existing slugs where possible; use Wix URL Redirect Manager for changed paths | Maintain an explicit old → new mapping; test each redirect |

New Studio menus provide three navigation layers. In the current menu experience, sub-items beneath a dropdown item remain visible within the dropdown rather than opening another flyout. This suits a grouped Products/Services menu. Wix notes that linked elements placed inside dropdown containers are not fully accessible; use native dropdown items for navigation and decorative images only as supporting content. [4]

## Suggested content structure

Create an `Offerings` collection containing: title, slug, group, category, strapline, short introduction, hero image, image description, overview, outcomes, scope qualifications, ordered feature blocks, CTA label, CTA destination, brochure document, brochure filename, SEO title and description, and display order. Keep Dimaq as the current name and preserve any legacy Pilora URL as a redirect only.

Dynamic pages use a shared layout, with a unique item URL for every collection record. [6] Use a separate `Proof` collection to preserve the original item title, type, speaker/student name, role/institution where verified, exact testimonial text, original page URL, video source URL/ID, poster, captions/transcript, display order and verification status. Keep these records independent of offering copy so that a future brochure update cannot accidentally remove a testimonial.

Store the nine supplied brochures with an explicit offering-to-file mapping. Do not use an unrelated brochure on QSRPro, Tradesphere or Nexus. If their dedicated pages are included without a matching supplied PDF, the page should provide the verified portfolio overview and a contact next step; add a brochure only when one is supplied or approved.

## Responsive layout specification

Start with Studio's desktop, tablet and mobile breakpoints: desktop 1001px+, tablet 751–1000px and mobile 320–750px. Set the header and footer breakpoints as well as page breakpoints. Desktop changes cascade down; smaller-screen overrides do not change larger screens. Structural edits and element replacement can affect all breakpoints. [7]

Use grid cells and vertical stacks rather than overlapping manually positioned text. On desktop, use a constrained content width and generous margins; on mobile, make sections one column, keep supporting graphics below the headline, and make primary actions easy to reach. Keep brochure links visible without hover. Test at 320, 390, 768, 1024 and 1440px, including long headings and the longest service title. Refresh after changing browser width when testing native animation, as Wix notes that some animation measurements are calculated at page load. [8]

## Motion and performance

Recommended motion system: one short entrance reveal per section; 12–20px movement with opacity over approximately 450–650ms; a 150–220ms button hover transition; and very restrained decorative movement. These timing values are design recommendations, not Wix requirements. Keep essential copy visible if motion is unavailable.

Wix Studio supports entrance, hover, click, scroll and loop effects natively. Effects vary by element and cannot all be stacked on the same element; forms and embeds have restrictions. [8] Avoid continuous scroll hijacking, long entrance delays, animated paragraphs and autoplay testimonials. Use click-to-play video with accessible controls and a poster. Wix's accessibility guidance recommends limiting autoplay and scroll effects and providing control for prolonged moving content. [9]

For custom decoration only, Wix Studio supports `global.css` and assigned custom classes. [10] Include a reduced-motion rule such as:

```css
@media (prefers-reduced-motion: reduce) {
  .bluzee-orbit, .bluzee-reveal {
    animation: none !important;
    transition: none !important;
    transform: none !important;
    opacity: 1 !important;
  }
}
```

Scope the rule to Bluzee-owned decorative classes, then test the full page under reduced motion. Do not assume that a rule targeting a wrapper will control every Wix-managed animation. Native motion should be tested separately. Wix documents that system reduced-motion and performance preferences can suppress animations and videos. [11]

Use compressed responsive images, lazy-load below-fold media, avoid loading every video player on initial page load, and keep third-party scripts to the required minimum. A static visual is the mobile/reduced-motion fallback for any elaborate hero treatment. These are implementation recommendations; actual performance needs measurement on the finished Wix site.

## Media, contact and custom-code boundaries

Preserve the existing session and testimonial source URLs. Wix Video supports public YouTube, Vimeo and Facebook embeds and groups videos into channels. Embedding limitations and privacy settings can prevent playback, so test the exact preserved sources. Do not delete and replace recordings just to match the visual design. [12]

Build the final contact form using Wix Forms and configure submission routing through Wix Automations. Use Name, Work email, Company, Offering and Message as the concise default, with a separate optional phone field. A general inquiry must not silently become a marketing subscription. The production success message should appear only after a successful submission. Wix's default form notification is to the site owner; configure the intended Bluzee recipients explicitly. [13]

The concept's HTML/CSS is a design and content specification, not a claim of a native Wix implementation. Recreate navigational, editorial, form and download elements natively in Wix. If a bespoke interactive graphic is essential, use a Wix-hosted custom element with its own accessibility and reduced-motion handling. Wix supports custom elements from a `public/custom-elements` Velo file or an HTTPS external script. [14] Use custom elements only for the bounded graphic, not to place the whole website inside an iframe.

## Preservation, SEO and review gates

1. Export an inventory of current URLs, page titles, proof items, video sources, brochure links and form/app dependencies before the Wix build.
2. Keep original testimonials, IIM content, student videos and session recordings intact and reachable through a clear Proof / Sessions area linked from Home and About Us.
3. Preserve high-value existing paths. Where a path changes, map it to the closest equivalent new page; do not redirect every old page to Home.
4. Configure 301 redirects in Wix and verify them. Wix automatically redirects some changed page slugs, but Blog URLs are an explicit exception requiring manual redirects. [15]
5. Confirm page-specific titles/descriptions, heading order, image alternative text, preview cards, canonical URLs and indexability. Keep the concept/staging version out of search indexing until approved.
6. Test every brochure download, video, contact action, nested menu, focus order, Escape behavior, visible focus state, mobile layout and reduced-motion state.
7. Present the Wix version through Preview / Get Client Feedback rather than publishing it. Wix provides a shareable feedback link; review its access/expiry and use Preview across breakpoints. Test sites have their own prerequisites, so they should not be confused with a never-published preview. [16]
8. Only after explicit approval and preservation sign-off should the production launch be scheduled. This concept task does not authorize that launch.

## Official sources

1. [Creating a Studio version of a Wix Editor site](https://support.wix.com/en/article/studio-editor-creating-a-studio-version-of-a-wix-editor-site)
2. [About Studio branches of Wix Editor sites](https://support.wix.com/en/article/studio-editor-about-studio-branches-of-wix-editor-sites)
3. [Duplicating your site](https://support.wix.com/en/article/duplicate-html5-site)
4. [Managing dropdowns in a menu](https://support.wix.com/en/article/studio-editor-managing-dropdowns-in-a-menu)
5. [CMS Document Button limitation and regular-button workaround](https://support.wix.com/en/article/cms-request-connecting-document-buttons-to-files-in-collections)
6. [CMS: About dynamic pages](https://support.wix.com/en/article/cms-about-dynamic-pages)
7. [Designing across breakpoints](https://support.wix.com/en/article/studio-editor-designing-across-breakpoints)
8. [Studio Editor: About animations](https://support.wix.com/en/article/studio-editor-about-animations)
9. [Accessibility: Reducing motion](https://support.wix.com/en/article/accessibility-reducing-motion)
10. [Studio Editor: About CSS editing](https://support.wix.com/en/article/editor-x-about-css-editing)
11. [Accessibility: Videos and animation not playing](https://support.wix.com/en/article/wix-editor-videos-and-animation-not-playing-on-live-site)
12. [Wix Video: Adding videos to the library](https://support.wix.com/en/article/wix-video-adding-videos-to-your-video-library)
13. [Wix Forms: Adding and setting up a form](https://support.wix.com/en/article/wix-forms-adding-and-setting-up-a-form-on-your-site)
14. [Velo: Add a custom element](https://dev.wix.com/docs/velo/velo-only-apis/%24w/custom-element/add-a-custom-element)
15. [Setting up a 301 redirect](https://support.wix.com/en/article/setting-up-a-301-redirect-for-a-page-on-your-site)
16. [Studio Editor: Saving, previewing and publishing](https://support.wix.com/en/article/studio-editor-saving-previewing-and-publishing-your-site)

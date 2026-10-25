BLUZEE PRELAUNCH READINESS UPDATE — 25 OCTOBER 2026

This update follows the deployed media and direct-enquiry updates.
Apply it over the existing bluzee-website repository; it is not a full replacement.

NEXT ACTION
1. Extract Bluzee_Prelaunch_Readiness_Update.zip.
2. Open bluzee-website in GitHub Desktop, select main and Fetch/Pull first.
3. Repository > Show in Explorer.
4. Copy the extracted contents into the repository folder. Merge folders and
   replace matching files. Keep all existing images, videos, brochures and source.
5. Commit with summary: Preserve legacy pages and prepare website launch.
6. Push origin and wait for a successful Cloudflare Pages deployment.
7. Review the new Blog, SAP, Industries, Careers and Privacy pages using the footer.
8. Confirm both General and AI enquiry routes reach their intended mailboxes.
9. Return for domain connection guidance. Do not cancel Wix or alter mail DNS yet.

WHAT IS INCLUDED
- All 10 captured blog posts, with original article text, author and publication
  details, plus their original images. Minor display whitespace and trademark
  styling are normalised. Historical articles are explicitly labelled as archive
  material; the archive label does not certify the accuracy of every old claim.
  The original site's blog sitemap was checked and lists those same 10 posts.
- 34 optimised original image assets used by articles and supporting pages.
- Original SAP capability PDF, preserved byte-for-byte.
- SAP capabilities, ZATCA e-invoicing, Industries and Careers destinations.
- Six Bluzee-specific website notices replacing the unrelated Termly templates:
  Privacy policy, Website information, Scope of website information, Service
  quality/delivery approach, Company information, Content/copyright notice.
- Existing internal links point to the new local destinations.
- Legacy route redirects, a genuine 404 page, canonical URLs and sitemap.
  The old portfolio landing route redirects to Our Offerings. Unrelated Wix
  sample design-project entries are not presented as Bluzee customer projects.
- Search indexing permitted on the custom domain; Pages development/preview
  hostnames receive noindex headers. Headers and redirects must be verified on
  Cloudflare after deployment because the local preview does not emulate them.
- Public Concept notes links removed. Old design-notes and handoff routes
  redirect to About; the design-notes HTML is replaced with a simple redirect.

CONTENT CHOICES TO REVIEW
SAP: Gold Partner status remains attributed to the strategic partner, not Bluzee.
Partner credentials, references and resource availability must be confirmed for
each engagement. The original SAP PDF retains its original statements.
ZATCA: Scope and validation wording replaces blanket 100% compliance and fixed
implementation-time promises from the old page.
Careers: Initial enquiries use the general contact form with role, experience,
availability and résumé link in the message. No vacancy is promised. The previous
Wix application form is preserved in the legacy backup, not recreated with DOB
collection or a paid attachment-upload service.
Legal/privacy: These are website notice drafts based on the known setup, not a
legal certification. Review the company details, operational practices and actual
record-retention arrangements before custom-domain launch. The new notices do
not create contractual SLAs, product guarantees or a legal-compliance claim.

WHAT REMAINS FOR DOMAIN CUTOVER
After this update is deployed and reviewed:
- Add www.bluzee.xyz and bluzee.xyz through the Pages project's Custom domains
  workflow, so Cloudflare associates and provisions them for this project.
- Change only website records needed for the Pages connection.
- Preserve Namecheap MX records, SPF, DKIM and any other email-verification records.
- Choose www.bluzee.xyz as canonical and configure an apex-to-www redirect using
  Cloudflare Redirect Rules/Bulk Redirects, preserving paths and query strings.
  This ZIP does not install a host-level redirect or change DNS.
- Confirm HTTPS, domain redirects, legacy paths, images, videos, PDFs and both
  enquiry routes. Test ordinary incoming and outgoing Namecheap email again.
- Submit https://www.bluzee.xyz/sitemap.xml to Search Console after cutover.
- Keep Wix available during validation and rollback. Cancel only after the new
  domain and all required content are working independently of Wix.

ROLLBACK
Use the previous successful Cloudflare Pages deployment if this update has an
issue. The patch does not affect the live Wix website or domain DNS. If rolling
back after a future domain cutover, use the DNS records recorded before that
cutover; do not guess or change mail-related records.

SOURCE MAINTENANCE
content-source/legacy-content.json contains the portable, sanitised article
content and original-source provenance. launch_ready.py builds the new pages,
local link mappings, metadata, redirects, headers and sitemap.
The full original capture is separately preserved in Bluzee_Legacy_Content_Backup.zip.
It does not need to be copied into this repository or uploaded to R2.

Build/check commands (Cloudflare can continue deploying the prebuilt dist folder):
python build.py
python validate.py
python validate_media.py
python validate_visuals.py
python validate_launch.py
node validate_enquiry.cjs

Account-side recipient settings remain in Formspree:
mbgggrko = General -> inbox@bluzee.xyz
mjyyyboo = DealTailor/Dimaq -> ai@bluzee.xyz
If ai@bluzee.xyz is monitored by DealTailor, verify it replies to the visitor's
Reply-To address and does not treat the Formspree notification sender as the lead.

OFFICIAL DEPLOYMENT REFERENCES
https://developers.cloudflare.com/pages/configuration/custom-domains/
https://developers.cloudflare.com/pages/configuration/redirects/
https://developers.cloudflare.com/pages/configuration/headers/
https://developers.cloudflare.com/pages/configuration/serving-pages/

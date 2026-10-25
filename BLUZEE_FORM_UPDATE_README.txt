BLUZEE DIRECT WEBSITE ENQUIRIES — 25 OCTOBER 2026

Apply this small update over your existing bluzee-website repository.
It is not a replacement for the whole repository.

INSTALL
1. Extract Bluzee_Direct_Enquiry_Update.zip.
2. In GitHub Desktop, select bluzee-website and the main branch. Fetch/Pull any changes first.
3. Open Repository > Show in Explorer.
4. Copy every file/folder INSIDE the extracted ZIP into that repository folder.
   Merge the dist and content-source folders and replace matching files.
   Do not delete existing repository folders. Do not upload the ZIP itself to R2.
5. In GitHub Desktop, commit with summary: Enable direct website enquiries.
6. Click Push origin. Wait for the Cloudflare Pages production deployment to succeed.
7. Open the Contact Us page on your Pages website and refresh it with Ctrl+F5.

ENDPOINT MAPPING
The two URLs were supplied without labels. This update follows the requested order:
General: https://formspree.io/f/mbgggrko — expected recipient inbox@bluzee.xyz
AI products: https://formspree.io/f/mjyyyboo — expected recipient ai@bluzee.xyz
DealTailor and Dimaq use the AI endpoint. All other offerings, including the
AI Experience Hub, use the General endpoint. Selecting an offering updates
the visible recipient note. Product-page enquiry links preselect the offering.
Actual email recipients are controlled in your Formspree account. The public
endpoint does not expose or prove that setting. Confirm each form's Email action
has the intended verified recipient. No additional CC recipient is added.

LIVE DELIVERY TEST — PLEASE COMPLETE AFTER DEPLOYMENT
1. Use an email address you can access as the visitor email.
2. Submit a General enquiry with message: Website launch test — general.
3. Confirm the on-screen submission confirmation, the Formspree submission,
   and receipt in inbox@bluzee.xyz. Check spam/junk as well.
4. Submit a Bluzee Dimaq enquiry with message: Website launch test — AI.
5. Confirm it appears under the second Formspree form and reaches ai@bluzee.xyz.
6. Reply to each notification and verify the reply reaches the visitor email.
   If DealTailor monitors ai@bluzee.xyz, verify it identifies the visitor from
   the Reply-To/email field rather than treating Formspree as the lead.
7. If a security check is requested, use Continue with secure verification.
   Keep the provider's spam protection enabled. Additional custom CAPTCHA keys,
   if required by your account settings, must be configured separately.
8. If delivery fails, share the visible error/screenshot and which route failed.
   No passwords, API secrets or verification codes are needed.

WHAT CHANGED
- Direct form submission with offering-based selection of the two endpoints.
- Required fields, enquiry-processing acknowledgement and reply email field.
- Accessible pending, success and failure states; duplicate clicks prevented.
- Network/timeout errors retain input, with copy, email and WhatsApp alternatives.
- Success only follows an explicit accepted response from Formspree. This is not
  a guarantee that the notification has arrived in the destination mailbox.
- Additional security-check responses provide a deliberate native Formspree
  submission option; no automatic retry or automatic duplicate submission.
- Separate website enquiry privacy notice, linked from the Contact page.
- Contact form readability improvements and mobile-friendly 16px input text.
- Existing imagery, recordings, brochures and visual motion remain unchanged.

PRIVACY AND CONFIGURATION
Formspree processes/stores submission details and can process them internationally.
The new notice describes this specific form; it does not replace the pending
review of all legacy legal pages or assert legal compliance.
The Free plan currently has a shared 50-submission monthly allowance and 30-day
dashboard history. Email copies have separate retention. Monitor account usage.
If restricting form origins, permit your production Pages hostname while testing
and www.bluzee.xyz/bluzee.xyz before domain launch. Preview hostnames require their
own allowed-origin setup if you choose to test a branch preview.
The integration does not modify Namecheap email hosting or any DNS records.

VALIDATION COMPLETED
- 29 offline checks: routing for all options, trademark variants, deep-link
  preselection, validation/consent, both successful routes, server/rate-limit
  failures, invalid responses, security fallback, network errors, timeout,
  duplicate-click protection, reset and input retention.
- Browser review of the desktop form and a 390px mobile-width frame.
- Simulated browser submissions verified both endpoint/payload selections and
  visible mobile confirmation. Temporary QA pages are not in this ZIP.
- Full static checks: 21 pages, 42 distinct editorial images, 13 mapped videos,
  internal links, assets, unique IDs and JavaScript syntax passed.
- No live Formspree submission or notification email was sent by this validation.
- The endpoint URLs reject ordinary GET requests with HTTP 405, which is normal
  for submission-only endpoints; this does not verify recipient settings.

BUILD / MAINTENANCE
Cloudflare can continue deploying the prebuilt dist folder with its current setup.
Source and prebuilt output are both included. For future local rebuilds:
python build.py
python validate.py
python validate_media.py
python validate_visuals.py
node validate_enquiry.cjs
Edit content-source/enquiry-forms.json to change the endpoint mapping, then rebuild.

KEEP WIX ACTIVE
This update completes the form integration for testing. Domain cutover, legacy
page migration/redirects, production search indexing and full legal-page review
remain separate launch steps. Do not cancel Wix yet.

REFERENCES
https://help.formspree.io/articles/building-your-form/submit-forms-with-javascript-ajax
https://help.formspree.io/articles/account-management/account-limits
https://help.formspree.io/articles/form-and-project-settings/changing-a-form-email-address
https://formspree.io/legal/privacy-policy/

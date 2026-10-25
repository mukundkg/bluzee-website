"""Direct enquiry integration for the prebuilt Cloudflare Pages site."""
import json
import re
from html import escape
from pathlib import Path


def install(ns):
    root = Path(__file__).parent
    config = json.loads((root / 'content-source/enquiry-forms.json').read_text())
    for key in ('general', 'ai'):
        if not re.fullmatch(r'https://formspree\.io/f/[a-zA-Z0-9]+', config[key]['endpoint']):
            raise ValueError('Invalid Formspree endpoint')
    old_contact = ns['contact_page']

    def contact_page():
        page = old_contact()
        start = page.index('<form class="enquiry-form"')
        end = page.index('</form>', start) + len('</form>')
        original = page[start:end]
        fields = original[original.index('<div class="form-grid">'):original.index('<p class="recipient-note"')]
        cfg = escape(json.dumps(config), quote=True)
        form = f'''<form class="enquiry-form direct-enquiry" id="enquiry-form" method="post" action="{config['general']['endpoint']}" data-enquiry-config="{cfg}" aria-describedby="enquiry-processing">
<p class="eyebrow">SEND AN ENQUIRY</p><h2>What would you like to explore?</h2>
<fieldset class="enquiry-fields"><legend class="sr-only">Your enquiry details</legend>{fields}
<p class="recipient-note" aria-live="polite">General enquiries: <strong>inbox@bluzee.xyz</strong></p>
<p class="form-note" id="enquiry-processing">Your details are sent through Formspree to Bluzee to handle your enquiry. Please avoid confidential or sensitive information. <a href="../enquiry-privacy/index.html" target="_blank" rel="noopener">How we handle your enquiry ↗</a></p>
<label class="enquiry-consent"><input type="checkbox" name="enquiry_consent" value="I agree to the processing of my enquiry as described in the website enquiry privacy notice." required><span>I agree to Bluzee processing my details through Formspree to respond to this enquiry. *</span></label>
</fieldset>
<button class="btn enquiry-submit" type="submit" disabled>Send enquiry <span class="arrow" aria-hidden="true">↗</span></button>
<noscript><p class="form-note">Please enable JavaScript to submit this form, or contact us using the email and WhatsApp links on this page.</p></noscript>
<div class="enquiry-status" role="status" aria-live="polite" aria-atomic="true" tabindex="-1" hidden></div>
<div class="enquiry-recovery" hidden><button type="button" class="btn secondary enquiry-verify" hidden>Continue with secure verification ↗</button><button type="button" class="btn secondary enquiry-copy">Copy my message</button><p class="enquiry-copy-status" role="status"></p></div>
<button type="button" class="btn secondary enquiry-another" hidden>Send another enquiry</button>
<p class="form-note enquiry-alternatives">Prefer another way? <a class="enquiry-email" href="mailto:inbox@bluzee.xyz">Email Bluzee</a> or <a href="https://wa.me/971586531493" target="_blank" rel="noopener">WhatsApp +971 58 653 1493 ↗</a>.</p>
</form>'''
        return page[:start] + form + page[end:]

    ns['contact_page'] = contact_page
    old_decorate = ns['decorate_html']

    def decorate(html, path):
        html = old_decorate(html, path)
        if path in ('contact/index.html', 'enquiry-privacy/index.html'):
            assets = '<link rel="stylesheet" href="../assets/enquiry.css?v=20261025">'
            if path == 'contact/index.html':
                assets += '<script src="../assets/enquiry.js?v=20261025" defer></script>'
                html = html.replace('src="../assets/app.js"', 'src="../assets/app.js?v=enquiry-20261025"')
            html = html.replace('href="https://www.bluzee.xyz/privacy-policy">Privacy policy', 'href="../enquiry-privacy/index.html">Enquiry privacy')
            html = html.replace('</head>', assets + '</head>')
        return html

    ns['decorate_html'] = decorate
    ns['enquiry_privacy'] = privacy_page


def privacy_page():
    return '''<section class="standard-hero"><div class="wrap"><p class="eyebrow">BLUZEE / WEBSITE ENQUIRIES</p><h1>Your enquiry.<br>Handled with clarity.</h1><p class="lede">How information submitted through this website’s enquiry form is processed.</p></div></section>
<section class="section light"><div class="wrap enquiry-privacy-copy">
<h2>Information you share</h2><p>The enquiry form collects your name, email address, selected offering, message, optional organisation and acknowledgement of this notice. Bluzee IT Consultants L.L.C. uses these details to review and respond to your enquiry.</p>
<h2>How it reaches Bluzee</h2><p>Formspree receives and stores the submission and sends an email notification to Bluzee. DealTailor™ and Dimaq™ enquiries are directed to ai@bluzee.xyz; other enquiries are directed to inbox@bluzee.xyz. Bluzee’s email is hosted with Namecheap Private Email. This website is hosted on Cloudflare.</p>
<p>Formspree may also process technical information such as IP address, browser details and referral information for service operation and security. Its processing can involve the United States and other countries where it operates. See the <a href="https://formspree.io/legal/privacy-policy/" target="_blank" rel="noopener">Formspree privacy policy ↗</a> for its processing and retention details.</p>
<h2>Copies and retention</h2><p>A submission may exist both in Formspree’s records and in Bluzee’s email correspondence. The submission history available in Formspree depends on the account plan; that archive limit does not automatically delete email copies. Contact Bluzee to ask about retention, access, correction or deletion of your enquiry information.</p>
<h2>Your choice</h2><p>You can use the email or WhatsApp links instead of this form. Those channels are handled through their respective services. Please do not submit passwords, payment information, identity documents or confidential business records through this initial enquiry form.</p>
<h2>Contact</h2><p><a href="mailto:inbox@bluzee.xyz">inbox@bluzee.xyz</a><br>Bluzee IT Consultants L.L.C.<br>Ontario Tower, Office #1703-026, Business Bay, Dubai, UAE<br>Dubai Trade License 786627</p>
<p class="form-note">This notice covers the website enquiry form. Data handling within a Bluzee product or customer deployment is governed by the relevant agreement and configuration.</p><a class="btn" href="../contact/index.html#enquiry-form">Back to the enquiry form ↗</a>
</div></section>'''

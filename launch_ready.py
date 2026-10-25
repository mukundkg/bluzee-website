"""Preserve legacy destinations and prepare the static site for domain cutover."""
from pathlib import Path
from html import escape as E, unescape
from urllib.parse import urlsplit, urlunsplit
import json,re,posixpath

ROOT=Path(__file__).parent
DIST=ROOT/'dist'
DATA=json.loads((ROOT/'content-source/legacy-content.json').read_text())
DOMAIN='https://www.bluzee.xyz'
ALIASES={
 '/about-us':'/about/', '/services-3':'/offerings/', '/portfolio':'/offerings/',
 '/experiencehub':'/services/erp-experience-hub/', '/general-7-1':'/services/erp-experience-hub/',
 '/workshop':'/services/professional-character/', '/general-7':'/services/odoo-erp-implementation/',
 '/about-3':'/services/odoo-erp-implementation/',
 '/post/bluzee-erp-experience-hub-inauguration-22nd-may-2025':'/events/#erp-hub-launch',
 '/_files/ugd/0ae95f_60106f199a8d4a958d1ccda3b803c8d8.pdf':'/resources/Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf',
 '/_files/ugd/933a8b_3b8a6118ca3b4a99b09c5c9748f97139.pdf':'/resources/Bluzee_SAP_Capability_Snapshot.pdf',
 '/design-notes':'/about/',
}

def hero(kicker,title,intro):
 return f'<section class="standard-hero archive-hero"><div class="wrap"><p class="eyebrow">{E(kicker)}</p><h1>{title}</h1><p class="lede">{intro}</p></div></section>'

def article_page(post,u):
 body=post['body_html'].replace('@@ROOT@@',u(''))
 return hero('BLUZEE / INSIGHTS & UPDATES',E(post['title']),f'{E(post["date_label"])} · {E(post["author"])}')+f'<section class="section light"><article class="wrap legacy-article"><p class="archive-context">From the Bluzee archive. This article retains its original publication date and content; dated events, opportunities and product references should be read in that context.</p>{body}<div class="article-return"><a class="text-link" href="{u("blog/index.html")}">All insights & updates ↗</a><a class="text-link" href="{u("events/index.html")}">Watch our events ↗</a></div></article></section>'

def blog(u):
 cards=''.join(f'<article class="archive-card"><p class="eyebrow">{E(p["date_label"])}</p><h2><a href="{u("post/"+p["slug"]+"/index.html")}">{E(p["title"])}</a></h2><p>{E(p["excerpt"])}</p><span class="archive-byline">{E(p["author"])}</span><a class="text-link" href="{u("post/"+p["slug"]+"/index.html")}">Read the article ↗</a></article>' for p in DATA['posts'])
 return hero('BLUZEE / INSIGHTS & UPDATES','Ideas. Milestones.<br><span class="accent">Experience in action.</span>','Explore original articles, partnerships and milestones from the Bluzee archive.')+f'<section class="section light"><div class="wrap"><div class="archive-grid">{cards}</div><div class="article-return"><a class="btn" href="{u("events/index.html")}">Explore event recordings ↗</a></div></div></section>'

def text_page(kicker,title,intro,body):
 return hero(kicker,title,intro)+'<section class="section light"><div class="wrap legacy-copy">'+body+'</div></section>'

def supporting(u):
 contact=u('contact/index.html')
 cta=f'<div class="article-return"><a class="btn" href="{contact}">Discuss your requirements ↗</a></div>'
 sap=text_page('BLUZEE / ENTERPRISE DELIVERY','SAP expertise.<br><span class="accent">Connected delivery.</span>','SAP support and transformation delivered through Bluzee’s leadership and partner ecosystem.',
 '<h2>Leadership, delivery and accountability</h2><p>Bluzee’s SAP delivery capability combines the experience of its SAP-certified co-founders with a strategic alliance with a certified SAP Gold Partner organisation. The Gold Partner status belongs to the partner organisation.</p><p>The existing Bluzee capability profile describes more than 35 years of combined leadership experience across SAP implementations, rollouts and support programmes, with delivery across manufacturing, retail, energy and public-sector environments.</p>'
 '<h2>A defined delivery model</h2><ul><li>Client engagement and delivery governance under Bluzee’s leadership.</li><li>SAP delivery resources through the partner network.</li><li>Regionally anchored coordination across Dubai, India and Saudi Arabia.</li><li>Support transition, pilot support phases and workshops scoped to the customer’s SAP environment.</li></ul>'
 '<h2>Experience through the partner ecosystem</h2><p>The existing profile references ECC-to-S/4HANA migration, SAP application management and FI/CO and MM support engagements delivered through the partner ecosystem. Specific references, partner credentials, resource availability and delivery scope should be confirmed for the proposed engagement.</p>'
 '<div class="legacy-gallery">'+''.join(x.replace('@@ROOT@@',u('')) for x in DATA['sap_images'])+'</div>'
 f'<h2>Explore the capability profile</h2><p>The original SAP snapshot is available for reference. Its partner credentials and project examples retain their original attribution.</p><a class="btn" href="{u(DATA["sap_pdf"])}" download>Download SAP capability snapshot ↓</a>'+cta)
 zatca=text_page('BLUZEE / E-INVOICING','Connect your invoices.<br><span class="accent">Clarify your next step.</span>','Assess ZATCA e-invoicing integration for your ERP or point-of-sale environment.',
 '<h2>From invoice data to electronic exchange</h2><p>Bluzee’s offering covers invoice-data upload and validation, XML generation, reporting through ZATCA integration, PDF/A-3 output with embedded XML, electronic exchange and cloud storage options in Saudi Arabia.</p><h2>Start with the existing system</h2><p>Review your ERP or POS version, invoice flows, data quality, integration interfaces and applicable requirements before agreeing the solution. Reporting and dashboard needs can be considered as part of the scope.</p><h2>Scope and validation</h2><p>Compatibility, implementation timing, storage arrangements and acceptance checks depend on the customer environment and agreed scope. Compliance must be assessed against the requirements applicable to the business and validated before production use.</p>'+cta)
 industries=hero('BLUZEE / INDUSTRY CONTEXT','Business understanding.<br><span class="accent">Across sectors.</span>','Explore the industry areas presented in Bluzee’s existing portfolio.')+'<section class="section light"><div class="wrap"><div class="legacy-industry-grid">'+''.join('<article>'+x['html'].replace('@@ROOT@@',u(''))+'<h2>'+E(x['name'])+'</h2></article>' for x in DATA['industries'])+'</div>'+cta+'</div></section>'
 careers=text_page('BLUZEE / CAREERS','Bring your experience.<br><span class="accent">Explore a conversation.</span>','Tell us about the role you are seeking and the contribution you can make.',
 '<h2>Share your profile</h2><p>For an initial careers enquiry, include your preferred role, relevant experience, availability and a link to your résumé. Use a shareable résumé link with access limited to the information you intend Bluzee to review.</p><p>Please do not include identity documents or sensitive personal details in your initial message. Opportunities and selection depend on current requirements; submitting an enquiry does not confirm a vacancy or employment offer.</p>'
 f'<a class="btn" href="{contact}?offering=General%20enquiry">Send a careers enquiry ↗</a><p class="archive-context">Choose General enquiry and mention “Careers” and your preferred role in the message. Your enquiry will use the website’s general contact route.</p>')
 return [('sap-capabilities','SAP capabilities',sap),('zatca','ZATCA e-invoicing',zatca),('team-4','Industries',industries),('careers','Careers',careers)]

def legal_pages(u):
 contact=f'<p>Contact <a href="mailto:inbox@bluzee.xyz">inbox@bluzee.xyz</a> or <a href="{u("contact/index.html")}">visit Contact Us</a>.</p>'
 company='<p>Bluzee IT Consultants L.L.C.<br>Dubai Trade License 786627<br>Ontario Tower, Office #1703-026, Business Bay, Dubai, UAE</p>'
 privacy='''<h2>Website enquiries</h2><p>We collect the information you provide to contact Bluzee: your name, email address, selected offering, message, optional organisation and acknowledgement of the enquiry notice. We use this information to review and respond to your request.</p><p>Formspree processes and stores website form submissions and sends notifications to Bluzee’s Namecheap-hosted email. The website and its media are hosted through Cloudflare. Formspree may process request information such as IP address and browser details for service operation and security, including in the United States and other countries where it operates.</p><h2>Records and choices</h2><p>Enquiry records can exist in both Formspree and email correspondence. Formspree’s available submission history depends on the account plan and does not automatically delete email copies. You can contact Bluzee about retention, access, correction or deletion of your enquiry details.</p><p>The form asks for permission to process your enquiry; it does not include a mailing-list subscription. Please avoid passwords, payment details, identity documents and confidential business information in this initial message.</p><h2>Website preferences and external services</h2><p>Your motion preference can be saved in your browser. Links to WhatsApp, social platforms and external registration forms open services governed by their own privacy notices. Review those notices before sharing information.</p><h2>Service and product data</h2><p>Data handling for a customer project or product deployment depends on the relevant agreement, hosting arrangement, access controls and configuration. This website notice does not replace those terms.</p>'''+f'<p>Read the <a href="{u("enquiry-privacy/index.html")}">website enquiry notice</a> and <a href="https://formspree.io/legal/privacy-policy/" target="_blank" rel="noopener">Formspree privacy policy ↗</a>.</p><h2>Contact Bluzee</h2>'+company+contact
 disclaimer='''<h2>Information and scope</h2><p>This website introduces Bluzee’s offerings and provides reference material. Features, availability, implementation scope, delivery schedules and support commitments are confirmed in the applicable proposal or agreement.</p><h2>Illustrations and original evidence</h2><p>Concept imagery and illustrative product workflows explain ideas; they are not live product output or evidence of a completed customer engagement. Original recordings, feedback and attributed partner materials are presented in their relevant context.</p><h2>Historical material and external links</h2><p>Archived articles and downloads retain their original context and may describe past events, opportunities or capabilities. External websites are managed by their respective operators. Contact Bluzee to confirm current information before relying on it for a business decision.</p><h2>Professional review</h2><p>General website material does not replace advice or assessment specific to your organisation, including technical, legal, tax or regulatory review where required.</p>'''+contact
 quality='''<h2>Business relevance first</h2><p>Bluzee’s ERP consulting approach starts with the business need: prioritising relevant capabilities, planning phases and considering business continuity before implementation.</p><h2>Engagement throughout delivery</h2><p>The implementation approach includes customer involvement, regular progress playbacks, functional design informed by industry experience, and testing against the agreed requirements.</p><h2>Prepare the transition to support</h2><p>Support readiness includes transition templates, operational checklists and agreed handling processes to prepare the move from build to run. Specific deliverables, service levels, acceptance criteria and responsibilities belong in the engagement agreement.</p>'''+contact
 copyright='''<h2>Content and attribution</h2><p>Bluzee branding, original materials and third-party materials are presented with their respective identities. Product names and trademarks belong to their respective owners. The appearance of an institution or company in an event, article or testimonial does not by itself imply endorsement of every Bluzee offering.</p><h2>Reuse enquiries</h2><p>Contact Bluzee before commercially reusing website material. Rights in third-party logos, photographs, recordings and documents may need to be cleared with their respective owners.</p><h2>Corrections and rights requests</h2><p>If you believe material needs correction or raises a rights concern, identify the page and the material when contacting us so it can be reviewed.</p>'''+contact
 return [('privacy-policy','Privacy policy',privacy),('legal-disclaimer','Website information & terms of use',disclaimer),('non-liability','Scope of website information',disclaimer),('quality-policy','Service quality & delivery approach',quality),('imprint','Company information',company+contact),('copyright-notice','Content & copyright notice',copyright)]

def relative_target(path,current):
 split=urlsplit(path)
 target=split.path
 if target.endswith('/'):target+='index.html'
 elif '.' not in target.rsplit('/',1)[-1]:target+='/index.html'
 if not (DIST/target.lstrip('/')).exists():return None
 rel=posixpath.relpath(target.lstrip('/'),str(Path(current).parent))
 return urlunsplit(('', '',rel,split.query,split.fragment))

def finalise(ns):
 write=ns['write'];u=ns['u']
 write('blog/index.html','Insights & updates','Original articles, partnerships and milestones from Bluzee.',lambda:blog(u))
 for post in DATA['posts']:
  write('post/'+post['slug']+'/index.html',post['title'],post['excerpt'],lambda post=post:article_page(post,u))
 # Build each page with its own relative-link prefix.
 for slug,title in [('sap-capabilities','SAP capabilities'),('zatca','ZATCA e-invoicing'),('team-4','Industries'),('careers','Careers')]:
  write(slug+'/index.html',title,'Explore Bluzee '+title.lower()+'.',lambda slug=slug:next(body for key,_,body in supporting(u) if key==slug))
 for slug,title in [(p[0],p[1]) for p in legal_pages(u)]:
  write(slug+'/index.html',title,title+' for the Bluzee website.',lambda slug=slug,title=title:text_page('BLUZEE / INFORMATION',E(title),'Information about this website and its services.',next(body for key,_,body in legal_pages(u) if key==slug)))
 write('404.html','Page not found','Find your way to Bluzee products, services and contact details.',hero('BLUZEE / 404','Let’s find your<br><span class="accent">next destination.</span>','This page could not be found.')+'<section class="section"><div class="wrap"><a class="btn" href="/">Visit the homepage ↗</a> <a class="btn secondary" href="/contact/">Contact Bluzee ↗</a></div></section>')
 pages=list(DIST.rglob('*.html'))
 added={f'post/{p["slug"]}/index.html' for p in DATA['posts']}|{p[0]+'/index.html' for p in supporting(u)}|{p[0]+'/index.html' for p in legal_pages(u)}|{'blog/index.html','404.html'}
 for page in pages:
  path=page.relative_to(DIST).as_posix()
  if path=='design-notes/index.html':
   page.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=../about/"><title>About Bluzee</title></head><body><h1>Bluzee</h1><p><a href="../about/index.html">Continue to About Bluzee</a></p></body></html>');continue
  text=page.read_text()
  text=re.sub(r'Bluzee ERP Experience Hub(?!™)', 'Bluzee ERP Experience Hub™', text)
  text=re.sub(r'Design Your Professional Character(?!™)', 'Design Your Professional Character™', text)
  if path=='events/index.html':text=text.replace('class="event-spotlight-player"','id="erp-hub-launch" class="event-spotlight-player"',1)
  text=re.sub(r'<a class="review-link"[^>]*>.*?</a>','',text)
  def links(match):
   value=unescape(match.group(1));x=urlsplit(value)
   if x.netloc not in ('www.bluzee.xyz','bluzee.xyz'):return match.group(0)
   target=ALIASES.get(x.path.rstrip('/'),x.path)
   if x.query:target+=('?' if '?' not in target else '&')+x.query
   if x.fragment and '#' not in target:target+='#'+x.fragment
   rel=relative_target(target,path)
   return 'href="'+E(rel,quote=True)+'"' if rel else match.group(0)
  text=re.sub(r'href="([^"]+)"',links,text)
  # Normalise long-standing links to the newly maintained privacy policy.
  text=text.replace('href="../enquiry-privacy/index.html">Enquiry privacy','href="../privacy-policy/index.html">Privacy policy')
  if path in added:
   css=posixpath.relpath('assets/legacy.css',str(Path(path).parent))
   text=text.replace('</head>',f'<link rel="stylesheet" href="{css}"></head>')
  if path=='404.html':text=text.replace('<head>','<head><base href="/">')
  canonical=DOMAIN+('/' if path=='index.html' else '/'+path.removesuffix('index.html'))
  noindex=path=='404.html'
  text=text.replace('content="noindex,nofollow"','content="'+('noindex,follow' if noindex else 'index,follow')+'"',1)
  title=re.search(r'<title>(.*?)</title>',text).group(1)
  desc=re.search(r'<meta name="description" content="([^"]*)"',text).group(1)
  meta=f'<link rel="canonical" href="{canonical}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website"><meta name="twitter:card" content="summary">'
  text=text.replace('</head>',meta+'</head>')
  page.write_text(text)
 indexable=[p.relative_to(DIST).as_posix() for p in pages if p.relative_to(DIST).as_posix() not in ['404.html','design-notes/index.html']]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+DOMAIN+('/' if p=='index.html' else '/'+p.removesuffix('index.html'))+'</loc></url>\n' for p in sorted(indexable))+'</urlset>\n'
 (DIST/'sitemap.xml').write_text(sitemap)
 (DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /design-notes/\nDisallow: /handoff/\nSitemap: '+DOMAIN+'/sitemap.xml\n')
 redirects=['# Legacy Wix routes preserved for the new Cloudflare Pages website.']
 for source,target in ALIASES.items():
  redirects.append(source+' '+target+' 301')
  if not source.endswith('.pdf'):redirects.append(source+'/ '+target+' 301')
 redirects+=['/design-notes/* /about/ 301','/handoff/* /about/ 301']
 (DIST/'_redirects').write_text('\n'.join(redirects)+'\n')
 (DIST/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n\nhttps://:project.pages.dev/*\n  X-Robots-Tag: noindex\n\nhttps://:version.:project.pages.dev/*\n  X-Robots-Tag: noindex\n\n/404.html\n  X-Robots-Tag: noindex\n\n/design-notes/*\n  X-Robots-Tag: noindex\n\n/handoff/*\n  X-Robots-Tag: noindex\n')
 (ROOT/'content-source/launch-pages.json').write_text(json.dumps({'page_count':len(pages),'indexable':indexable,'aliases':ALIASES,'blog_posts':len(DATA['posts']),'domain':DOMAIN},indent=2))
 print('Launch preparation:',len(pages),'pages;',len(indexable),'sitemap entries')

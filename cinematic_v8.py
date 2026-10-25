"""Bluzee v8: luminous architecture, human context and accessible cinematic motion."""
from pathlib import Path
from html import escape as E
import json,re
ROOT=Path(__file__).parent
SOURCE=json.loads((ROOT/'content-source/leadership-vision-mission-guide.json').read_text())
ASSETS={
 'dealtailor':'dealtailor-human','dimaq':'private-ai',
 'odoo-erp-consulting':'erp-world','odoo-erp-implementation':'erp-world',
 'erp-talent-outsourcing':'academy-future','erp-support':'engineering-ai',
 'erp-experience-hub':'academy-future','ai-experience-hub':'engineering-ai',
 'professional-character':'workshop-human','qsrpro':'erp-world',
 'tradesphere':'erp-world','nexus':'private-ai'}

def replace_section(html, marker, replacement):
    start=html.find(marker)
    if start<0: raise ValueError('Missing section: '+marker)
    depth=0
    for match in re.finditer(r'</?section\b[^>]*>',html[start:]):
        depth+= -1 if match.group().startswith('</') else 1
        if depth==0:return html[:start]+replacement+html[start+match.end():]
    raise ValueError('Unclosed section: '+marker)

def install(ns):
    u=ns['u'];button=ns['button'];link=ns['link'];contact=ns['contact'];href=ns['href'];brochure=ns['brochure'];BY=ns['BY_SLUG'];OFFERINGS=ns['OFFERINGS']
    def scene(asset,eager=False,real=False):
        path='assets/'+asset if real else 'assets/v8/'+asset+'.webp'
        source=f'<img src="{u(path)}" alt="" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'
        if not real: source=f'<picture><source media="(max-width:700px)" srcset="{u("assets/v8/"+asset+"-mobile.webp")}">{source}</picture>'
        return '<div class="v8-scene" aria-hidden="true">'+source+'</div><div class="v8-shade" aria-hidden="true"></div><div class="v8-glow" aria-hidden="true"></div>'
    def hero(asset,eyebrow,title,description,actions='',light=False,extra='',real=False):
        return f'''<section class="v8-hero v8-cinema {'v8-pale' if light else ''}" data-v8-scene>{scene(asset,True,real)}<div class="wrap v8-hero-inner"><p class="eyebrow v8-enter">{eyebrow}</p><h1 class="v8-enter">{title}</h1><p class="lede v8-enter">{description}</p><div class="actions v8-enter">{actions}</div>{extra}</div><div class="wrap v8-hero-foot"><span>IDEAS WITH PURPOSE. PROGRESS WITH PEOPLE.</span><a href="#v8-next" class="v8-scroll" aria-label="Explore the next section"><span>Scroll to explore</span><i aria-hidden="true">↓</i></a></div><div class="v8-orbit" aria-hidden="true"></div></section>'''
    def next_marker():return '<div id="v8-next" class="v8-anchor"></div>'
    def rail(title,body,path,number):return f'<a class="v8-rail" href="{u(path)}"><span class="v8-index">{number}</span><div><h3>{title}</h3><p>{body}</p></div><span class="v8-round-arrow" aria-hidden="true">↗</span></a>'
    old_cta=ns['cta']
    def cta():
        out=old_cta().replace('<section class="section cta-section">','<section class="section cta-section v8-cinema" data-v8-scene>'+scene('purpose-ocean'))
        return out.replace('Your next move<br>starts with a conversation.','Let’s turn possibility<br>into <em class="v8-serif">progress.</em>')
    ns['cta']=cta
    def guide():
        return f'''<section class="v8-guide section light"><div class="wrap v8-guide-grid"><div class="v8-guide-art" data-v8-depth><div class="v8-guide-ring" aria-hidden="true"></div><a class="v8-book" href="{u('resources/Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf')}" download aria-label="Download the Bluzee ERP guide"><img src="{u('assets/erp-guide-cover.webp')}" alt="Bluzee ERP Implementation Methodology — original guide cover" loading="lazy"><span aria-hidden="true"></span></a><span class="v8-art-note">A PRACTICAL PERSPECTIVE<br>ON ENTERPRISE DELIVERY</span></div><div class="v8-reveal"><p class="eyebrow">THE BLUZEE ERP GUIDE</p><h2>A clearer view.<br>A stronger <em class="v8-serif">starting point.</em></h2><p class="lede">Explore Bluzee’s practical reference for successfully implementing ERP engagements. An informed beginning makes the journey more purposeful.</p><p class="v8-metadata">26 PAGES &nbsp; / &nbsp; JULY 2024 EDITION &nbsp; / &nbsp; PDF</p>{button('Download the ERP guide',u('resources/Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf'),False,'download')}</div></div></section>'''
    ns['guide_section']=guide
    def product_scene(slug,number,title,description,points):
        o=BY[slug]
        return f'''<section class="v8-product v8-cinema" data-v8-scene>{scene(ASSETS[slug])}<div class="wrap v8-product-grid"><div class="v8-product-label"><span>{number} / PRIVATE AI</span><span>{E(o['name'])}</span></div><div class="v8-product-copy v8-reveal"><p class="eyebrow">{E(o['kicker'])}</p><h2>{title}</h2><p class="lede">{description}</p><ul class="v8-capabilities">{''.join('<li>'+p+'</li>' for p in points)}</ul><div class="actions">{button('Explore '+o['name'],u(href(o)))}{brochure(o)}</div></div><span class="v8-scene-word" aria-hidden="true">{o['short']}</span></div></section>'''
    def homepage():
        opening=hero('home-horizon','BLUZEE™ / AI. ENTERPRISE. EXPERIENCE.','Intelligence.<br>With a <em class="v8-serif">human purpose.</em>','Private AI, thoughtful ERP consulting and experience that prepares people to contribute. Connected by an understanding of your business.',button('Discover our AI products','#ai-products')+link('Start a conversation',contact()),extra='<div class="v8-hero-tags"><span>PRIVATE BY DESIGN</span><span>BUSINESS LED</span><span>PEOPLE FIRST</span></div>')
        intro=f'''<section class="section light v8-intro" id="v8-next"><div class="wrap"><div class="v8-intro-grid"><p class="eyebrow">THE BLUZEE PERSPECTIVE</p><h2 class="v8-reveal">Technology creates possibility.<br><span>Understanding makes it <em class="v8-serif">valuable.</em></span></h2><p class="lede v8-reveal">Engage the right leads. Make informed decisions. Implement what your business needs. Build experience through meaningful work.</p></div><div class="v8-pathways">{rail('Private AI','Intelligence for conversations and decisions.','offerings/index.html?category=Products','01')}{rail('Enterprise services','Clarity from ERP planning through production.','offerings/index.html?category=ERP','02')}{rail('Academy of Experience','Purposeful work. Demonstrable contribution.','offerings/index.html?category=Academy','03')}</div></div></section>'''
        product_intro='<section class="v8-section-label" id="ai-products"><div class="wrap"><p class="eyebrow">PRIVATE AI / TWO DISTINCT ADVANTAGES</p><span>From the first conversation to the next decision.</span></div></section>'
        products=product_scene('dealtailor','01','Every conversation.<br>A meaningful <em class="v8-serif">next step.</em>','Bluzee DealTailor™ engages leads, understands intent and helps your sales team focus on the next useful action.',['Private AI lead engagement','Lead qualification and sales handover','Customer-controlled deployment, within agreed scope'])+product_scene('dimaq','02','See beyond reports.<br>Prepare for <em class="v8-serif">what’s next.</em>','Bluzee Dimaq™ helps business owners and department heads turn authorised enterprise data into meeting-ready insight and actions.',['Platform-agnostic decision intelligence','Role-based access to approved enterprise data','AWS-managed model options and administrator-controlled access'])
        portfolio=f'<div class="v8-portfolio"><div class="wrap"><span>EXPLORE THE WIDER PORTFOLIO</span>'+''.join(link(BY[s]['name'],u(href(BY[s]))) for s in ['qsrpro','tradesphere','nexus'])+'</div></div>'
        services=f'''<section class="v8-erp v8-cinema v8-pale" data-v8-scene>{scene('erp-world')}<div class="wrap v8-editorial-grid"><div class="v8-editorial-copy v8-reveal"><p class="eyebrow">BLUZEE ERP CONSULTING SERVICES</p><h2>The right ERP.<br>The right scope.<br><em class="v8-serif">A better investment.</em></h2><p class="lede">Avoid spending time and budget on features your business does not need. Bluzee helps you assess business priorities, protect continuity and phase your ERP investment with clarity.</p><div class="actions">{button('Plan your ERP journey',contact(BY['odoo-erp-consulting']))}</div></div><div class="v8-service-list">{rail('Odoo ERP Consulting','Prioritise what matters. Plan each phase.','services/odoo-erp-consulting/index.html','01')}{rail('Odoo ERP Implementation','AI-assisted delivery. Weekly customer playbacks.','services/odoo-erp-implementation/index.html','02')}{rail('ERP Talent Outsourcing','Relevant expertise for defined responsibilities.','services/erp-talent-outsourcing/index.html','03')}{rail('ERP Support','Prepare the transition from build to run.','services/erp-support/index.html','04')}</div></div></section>'''
        academy=f'''<section class="v8-academy v8-cinema" data-v8-scene>{scene('academy-future')}<div class="wrap"><div class="v8-academy-copy v8-reveal"><p class="eyebrow">BLUZEE ACADEMY OF EXPERIENCE</p><h2>Move beyond learning.<br>Build work you can<br><em class="v8-serif">stand behind.</em></h2><p class="lede">Employers look for evidence of what you can deliver. Bluzee’s six-month experience pathway connects skills with scoped assignments, mentoring and reviewed contributions—so you can demonstrate how you work.</p><p class="v8-small-copy">Experience documentation follows programme terms and demonstrated participation. Role eligibility and employer recognition depend on the relevance of your work.</p><div class="v8-academy-links">{link('Bluzee ERP Experience Hub™',u('services/erp-experience-hub/index.html'))}{link('Bluzee AI Experience Hub',u('services/ai-experience-hub/index.html'))}</div></div><div class="v8-academy-caption"><span>LEARN → APPLY → DEMONSTRATE</span><p>Experience is the<br>work behind the words.</p></div></div></section>'''
        workshop=f'''<section class="section v8-workshop"><div class="wrap v8-workshop-inner"><div><p class="eyebrow">DESIGN YOUR PROFESSIONAL CHARACTER™</p><h2>Capability matters.<br><em class="v8-serif">Character carries it.</em></h2></div><div><p class="lede">Build the ownership, trust and professional habits that turn skills into a contribution others can count on.</p>{link('Discover the workshop',u('services/professional-character/index.html'))}</div></div></section>'''
        proof=f'''<section class="section light v8-proof-home"><div class="wrap"><div class="section-head"><div><p class="eyebrow">REAL PEOPLE. ORIGINAL MOMENTS.</p><h2>Ideas in the room.<br><em class="v8-serif">Perspectives that stay.</em></h2></div><div class="actions">{link('Explore events',u('events/index.html'))}{link('Hear participant voices',u('testimonials/index.html'))}</div></div><div class="proof-grid">{''.join(ns['proof_card'](k) for k in ['iim-kozhikode-session','iit-madras-session','volvo-session'])}</div></div></section>'''
        purpose=f'''<section class="v8-purpose-teaser v8-cinema" data-v8-scene>{scene('purpose-ocean')}<div class="wrap v8-reveal"><p class="eyebrow">PEOPLE &amp; PURPOSE</p><h2>A wider horizon.<br>A shared <em class="v8-serif">direction.</em></h2><p class="lede">Explore the vision, mission and people behind Bluzee.</p><div class="actions">{button('Our vision & mission',u('about/index.html#purpose'))}{link('Meet our leadership',u('about/index.html#leadership'))}</div></div></section>'''
        return opening+intro+product_intro+products+portfolio+services+academy+workshop+proof+guide()+purpose+cta()
    ns['homepage']=homepage
    old_offering=ns['offering']
    def offering(o):
        out=old_offering(o)
        headline=E(o['headline']).replace('\n','<br>')
        hero_html=hero(ASSETS[o['slug']],E(o['name']),headline,E(o['intro']),button(o['cta'],contact(o))+brochure(o),light=o['slug'] in ['odoo-erp-consulting','odoo-erp-implementation','erp-talent-outsourcing','ai-experience-hub'])
        out=replace_section(out,'<section class="detail-hero"',hero_html+next_marker())
        return out
    ns['offering']=offering
    def purpose():
        vision=''.join('<p>'+E(p)+'</p>' for p in SOURCE['vision']['paragraphs'])
        mission=E(SOURCE['mission']['exact_text'])
        return f'''<section class="v8-purpose v8-cinema" id="purpose" data-v8-scene>{scene('purpose-ocean')}<div class="wrap"><div class="v8-purpose-heading"><p class="eyebrow">OUR VISION &amp; MISSION</p><h2>Beyond boundaries.<br>Into <em class="v8-serif">possibility.</em></h2></div><div class="v8-purpose-chapters"><article class="v8-purpose-chapter v8-reveal"><span>01 / OUR VISION</span><h3>A blue ocean<br>of opportunity.</h3><p>Empowering businesses to create their own space, discover new possibilities and pursue sustainable growth.</p><details><summary>Read our full vision <i aria-hidden="true">+</i></summary><div>{vision}</div></details></article><article class="v8-purpose-chapter v8-reveal"><span>02 / OUR MISSION</span><h3>Lasting relationships.<br>Meaningful progress.</h3><p>{mission}</p></article></div></div></section>'''
    old_about=ns['about']
    def about():
        out=old_about()
        out=replace_section(out,'<section class="standard-hero"',hero('home-horizon','ABOUT BLUZEE™','Business understanding.<br><em class="v8-serif">Human ambition.</em>','Enterprise consulting, practical AI and experience-led development. We connect technology with the people and processes that make it useful.',button('Meet our people','#leadership')+link('Our vision & mission','#purpose'))+next_marker())
        out=replace_section(out,'<section class="purpose-cinematic"',purpose())
        return out
    ns['about']=about
    old_listing=ns['listing']
    def listing():
        return replace_section(old_listing(),'<section class="standard-hero"',hero('erp-world','OUR OFFERINGS','Find your next<br><em class="v8-serif">advantage.</em>','Private AI, enterprise services and practical experience. Explore the capabilities that connect your ambitions to meaningful progress.',button('Explore the portfolio','#v8-next'),True)+next_marker())
    ns['listing']=listing
    old_events=ns['events']
    def events():
        out=old_events()
        return replace_section(out,'<section class="media-hero events-hero"',hero('events/mindfulness-gallery-06.webp','BLUZEE / EVENTS','In good company.<br>Inspiring <em class="v8-serif">perspectives.</em>','Revisit the launch moments, professional character workshops and leadership conversations that bring people and ideas together.',button('Watch the recordings','#event-recordings')+link('Explore the photographs','#event-gallery'),real=True)+next_marker())
    ns['events']=events
    old_testimonials=ns['testimonials']
    def testimonials():
        out=old_testimonials()
        faces=''.join(f'<div class="v8-voice-portrait"><img src="{u("assets/proof-"+k+".webp")}" alt="" loading="eager"></div>' for k in ['manas-aravind','muhammed-ansil-pa','anirudh-vk','vaishnav-pm'])
        visual=f'<div class="v8-voice-wall" aria-hidden="true">{faces}</div>'
        h=f'''<section class="v8-hero v8-testimonial-hero v8-cinema" data-v8-scene>{visual}<div class="v8-shade" aria-hidden="true"></div><div class="wrap v8-hero-inner"><p class="eyebrow v8-enter">BLUZEE / TESTIMONIALS</p><h1 class="v8-enter">Their experience.<br>Their <em class="v8-serif">own words.</em></h1><p class="lede v8-enter">The most meaningful perspective belongs to the people who have taken part. Hear their stories, in their own voices.</p><div class="actions v8-enter">{button('Hear the participant voices','#participant-voices')}{link('Our partner network','#partners')}</div></div></section>'''
        return replace_section(out,'<section class="media-hero voices-hero"',h+next_marker())
    ns['testimonials']=testimonials
    old_stories=ns['stories']
    def stories():
        return replace_section(old_stories(),'<section class="standard-hero"',hero('workshop-human','THE BLUZEE MEDIA ARCHIVE','Conversations worth<br><em class="v8-serif">coming back to.</em>','Browse original event recordings, participant perspectives and written appreciation.',button('Browse the archive','#v8-next'))+next_marker())
    ns['stories']=stories
    old_contact=ns['contact_page']
    def contact_page():
        out=old_contact().replace('<h1>','<h2>',1).replace('</h1>','</h2>',1)
        return hero('purpose-ocean','LET’S START A CONVERSATION','What comes <em class="v8-serif">next?</em>','A business challenge, an ERP milestone or a new experience pathway. Let’s explore it together.',button('Make an enquiry','#enquiry-form')+link('WhatsApp +971 58 653 1493','https://wa.me/971586531493'))+next_marker()+out
    ns['contact_page']=contact_page
    def notes():
        return hero('home-horizon','CONCEPT V8 / REVIEW NOTES','A more immersive<br><em class="v8-serif">Bluzee.</em>','A complete visual refresh designed around luminous environments, human perspective and purposeful movement.',button('Return to the homepage',u('index.html')))+next_marker()+'''<section class="section light"><div class="wrap v8-review-copy"><h2>Designed to feel open.</h2><p>Full-width imagery replaces isolated decorative image boxes. Deep navy editorial chapters alternate with luminous pale blue sections. The red U in the Bluzee logo, approved contact details and trademarks remain consistent.</p><h3>Motion with intention</h3><p>Backgrounds move gently with scrolling and pointer position. Hero imagery breathes through slow zooms; text enters in a measured sequence. The ERP guide responds to pointer movement. Event galleries and participant recordings retain their native controls. No scroll hijacking or automatic video playback is used.</p><h3>Real evidence, preserved</h3><p>All original recordings, participant images, leadership portraits, source qualifications, brochure downloads and the ERP guide remain available. The working R2 media mapping is retained. Generated architecture and people are conceptual marketing imagery, not representations of actual Bluzee premises, clients, staff or events.</p><h3>Built for the current hosting plan</h3><p>The concept remains static HTML, CSS and JavaScript for Cloudflare Pages. Large recordings remain in R2. Local responsive WebP images reduce download weight. No paid animation service or additional framework is required.</p><h3>Accessibility and performance</h3><p>A visible Pause motion control is available. Reduced-motion preferences disable movement. Pointer effects are restricted to fine-pointer devices; offscreen scenes and hidden tabs stop animating. Controls remain available by keyboard and page content does not depend on animation.</p><h3>Before production launch</h3><p>Review this private concept before copying it to the public Pages repository. The existing launch recording and retained legacy pages still need migration before cancelling Wix. The enquiry form prepares an email draft; real form delivery, production media hostname, redirects and indexing remain separate launch tasks.</p></div></section>'''
    ns['notes']=notes
    old_decorate=ns['decorate_html']
    def decorate(html,path):
        html=old_decorate(html,path)
        html=html.replace('Concept review · Wix handoff ↗','Concept notes ↗')
        html=html.replace('<body>','<body class="v8-design">')
        html=html.replace('</head>',f'<link rel="stylesheet" href="{u("assets/cinematic-v8.css")}"><script src="{u("assets/cinematic-v8.js")}" defer></script></head>')
        replacements={'dealtailor':'dealtailor-human','dimaq':'private-ai','consulting':'erp-world','implementation':'erp-world','talent':'academy-future','support':'engineering-ai','erp-hub':'academy-future','ai-hub':'engineering-ai','ai-application':'private-ai','full-stack':'engineering-ai','dypc':'workshop-human','network':'private-ai'}
        for old,new in replacements.items():html=html.replace('src="'+u('assets/'+old+'.webp')+'"','src="'+u('assets/v8/'+new+'.webp')+'"')
        return html
    ns['decorate_html']=decorate

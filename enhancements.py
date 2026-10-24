"""October 24 review updates: branding, contacts, people, purpose and motion."""
from pathlib import Path
from html import escape as E
from urllib.parse import quote
import json,re
ROOT=Path(__file__).parent
SOURCE=json.loads((ROOT/'content-source/leadership-vision-mission-guide.json').read_text())
INSTITUTIONS=[
'IIT Madras','IIM Kozhikode','NIT Calicut','College of Engineering Trivandrum (CET)',
'Barton Hill Govt. Engineering College','TKM College of Engineering','TKM Institute of Management','Kerala Digital University',
'Institute of Management in Kerala','IHRD Kozhikode','Holy Cross Kozhikode',"St Joseph’s College Devagiri",'Rajagiri School of Commerce (MBA)','St Alberts Ernakulam','Bharat Mata College Ernakulam','PSMO College',
'SNES Chathamangalam','Faroke College Kozhikode','Garden City University Bangalore','Ramiah University Bangalore','ISBM Bangalore','RSET Rajagiri','FISAT Ernakulam','SCMS Cochin']
GUIDE='Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf'
WA_NUMBER='+971 58 653 1493'
WA_URL='https://wa.me/971586531493'
WA_ICON='<svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M27.4 15.3a11.3 11.3 0 0 1-16.8 9.9L4 27l1.8-6.4A11.3 11.3 0 1 1 27.4 15.3Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M11.2 9.1c-.5-.3-1.5.1-1.7.7-.7 1.8.7 4.7 3.1 7.1 2.4 2.5 5.4 3.8 7.2 3.2.7-.3 1.1-1.3.8-1.8l-2-2c-.3-.3-.8-.3-1.1 0l-1 1c-1.9-.8-3.7-2.6-4.5-4.5l1-1c.3-.3.3-.8 0-1.1l-1.8-1.6Z" fill="currentColor"/></svg>'

def install(ns):
    u=ns['u'];button=ns['button'];link=ns['link'];img=ns['img'];A=ns['A'];contact=ns['contact']
    def wa(label='Enquire on WhatsApp',offering=None,cls='btn whatsapp-button'):
        text='Hello Bluzee, I would like to enquire about '+offering+'.' if offering else 'Hello Bluzee, I would like to make an enquiry.'
        return f'<a class="{cls}" href="{WA_URL}?text={quote(text)}" target="_blank" rel="noopener" aria-label="{E(label)} — WhatsApp {WA_NUMBER}">{WA_ICON}<span>{E(label)}</span></a>'
    def contact_details():return f'''<div class="contact-short"><small>General enquiries</small><a href="mailto:inbox@bluzee.xyz">inbox@bluzee.xyz</a><small>AI product enquiries</small><a href="mailto:ai@bluzee.xyz">ai@bluzee.xyz</a><small>UAE · WhatsApp</small>{wa(WA_NUMBER,cls='whatsapp-contact')}<div class="phone-pair"><div><small>UAE · Call</small><a href="tel:+971581817499">+971 58181 7499</a></div><div><small>India · Call</small><a href="tel:+918861056458">+91 88610 56458</a></div></div></div>'''
    def cta():return f'''<section class="section cta-section"><div class="wrap"><div class="reveal"><p class="eyebrow">LET’S MAKE IT USEFUL</p><h2>Your next move<br>starts with a conversation.</h2><p class="lede">Tell us where you want to go. We’ll explore the AI, ERP or experience pathway that fits.</p><div class="actions">{button('Talk to Bluzee',contact())}{wa()}</div></div>{contact_details()}</div></section>'''
    ns['cta']=cta
    old_footer=ns['footer']
    def footer():
        text=old_footer()
        extra=f'''<div class="footer-contactbar"><div><small>General enquiries</small><a href="mailto:inbox@bluzee.xyz">inbox@bluzee.xyz</a></div><div><small>AI product enquiries</small><a href="mailto:ai@bluzee.xyz">ai@bluzee.xyz</a></div><div><small>UAE WhatsApp</small>{wa(WA_NUMBER,cls='whatsapp-contact')}</div><div><small>ERP resource</small><a href="{u('resources/'+GUIDE)}" download>Download the ERP guide ↓</a></div></div>'''
        text=text.replace('<div class="footer-legacy">',extra+'<div class="footer-legacy">')
        text=text.replace('© 2026 BLUZEE IT CONSULTANTS L.L.C</span>','© 2026 BLUZEE IT CONSULTANTS L.L.C<br><span class="license">Dubai Trade License 786627</span></span>')
        text=text.replace(f'<a href="{u("about/index.html")}">About Bluzee</a>',f'<a href="{u("about/index.html")}">About Bluzee</a><a href="{u("about/index.html#leadership")}">Leadership team</a><a href="{u("about/index.html#purpose")}">Vision &amp; mission</a>')
        text+=wa('WhatsApp',cls='whatsapp-float')
        return text
    ns['footer']=footer
    def guide_section():
        return f'''<section class="section-sm resource-section"><div class="wrap"><div class="guide-feature reveal" data-tilt><div class="guide-cover"><img src="{u('assets/erp-guide-cover.webp')}" alt="Original Bluzee ERP Implementation Methodology guide cover" loading="lazy" width="816" height="459"></div><div class="guide-copy"><p class="eyebrow">THE BLUZEE ERP GUIDE</p><h2>A reference for<br>the road ahead.</h2><p>A practical guide to successfully implementing ERP engagements. Explore Bluzee’s existing implementation methodology reference.</p><div class="resource-meta"><span>26 pages</span><span>July 2024 edition</span><span>PDF download</span></div><div class="actions">{button('Download the ERP guide',u('resources/'+GUIDE),False,'download')}{link('Explore ERP services',u('offerings/index.html?category=ERP'))}</div></div><div class="guide-lines" aria-hidden="true"></div></div></div></section>'''
    ns['guide_section']=guide_section
    def purpose():
        from purpose_experience import render_purpose
        return render_purpose(u,SOURCE)
    def leader_card(x,index):
        path=Path(x['portrait_local_path']);ext=path.suffix
        source=u('assets/leadership/'+path.name)
        profile=link('LinkedIn profile',x['profile_url'],'target="_blank" rel="noopener"') if x.get('profile_url') else ''
        bio=f'<p class="leader-bio">{E(x["supplementary_bio"]["editorial_summary"])}</p>' if x.get('supplementary_bio') else ''
        return f'''<article class="leader-card reveal" style="--i:{index}" data-tilt><div class="leader-photo"><img src="{source}" alt="{E(x['name'])}" loading="lazy" width="600" height="640"><span class="leader-no">0{index+1}</span></div><div class="leader-info"><p>{E(x['title'])}</p><h3>{E(x['name'])}</h3>{bio}{profile}</div></article>'''
    def leadership():
        leaders=SOURCE['leadership']
        return f'''<section class="section light leadership-section" id="leadership"><div class="wrap"><div class="section-head"><div><p class="eyebrow">LEADERSHIP</p><h2>People with perspective.<br>Purpose in common.</h2></div><p class="lede">Meet Bluzee’s leadership, advisors and consulting support.</p></div><div class="leader-grid executives stagger">{''.join(leader_card(x,i) for i,x in enumerate(leaders[:3]))}</div><div class="advisors-heading"><p class="eyebrow">ADVISORS &amp; CONSULTING</p><h3>Connected perspectives.</h3></div><div class="leader-grid advisors stagger">{''.join(leader_card(x,i+3) for i,x in enumerate(leaders[3:]))}</div></div></section>'''
    def institution_section():
        items=''.join(f'<li><span>{i+1:02d}</span><strong>{E(n)}</strong>{"<em>New addition</em>" if n=="SCMS Cochin" else ""}</li>' for i,n in enumerate(INSTITUTIONS))
        return f'''<section class="section institution-section" id="workshop-reach"><div class="wrap"><div class="section-head"><div><p class="eyebrow">DESIGN YOUR PROFESSIONAL CHARACTER™ / REACH</p><h2>Across campuses.<br>Into the workplace.</h2></div><div class="reach-stat"><strong>24</strong><span>academic institutions<br>in our workshop reach</span></div></div><div class="reach-intro"><p>Conversations on professional character, ownership and value creation, shared across academic institutions and the corporate workplace.</p><div class="corporate-proof"><small>CORPORATE WORKSHOP EXPERIENCE</small><b>Volvo Group · India</b>{link('Watch the session',u('events/index.html?category=DYPC'))}</div></div><ul class="institution-grid">{items}</ul><div class="reach-actions">{button('Download the corporate workshop brochure',u('brochures/Bluzee_DYPC_Brochure.pdf'),False,'download')}{wa('Bring the workshop to your institution','Design Your Professional Character™',cls='btn secondary whatsapp-button')}</div></div></section>'''
    old_special=ns['special']
    def special(o):
        result=old_special(o)
        if o['slug']=='professional-character':
            start=result.find('<section class="section light">')
            result=result[:start]+institution_section()+result[start:] if start!=-1 else result+institution_section()
            result+=f'<section class="section-sm"><div class="wrap">{link("Explore the detailed workshop pathways",u("brochures/Bluzee_Design_Your_Professional_Character.pdf"),"download")}</div></section>'
        return result
    ns['special']=special
    old_home=ns['homepage']
    def homepage():
        out=old_home()
        beams='''<div class="hero-motion" aria-hidden="true"><svg viewBox="0 0 1400 760" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="beam-color"><stop stop-color="#7ae7ff" stop-opacity="0"/><stop offset=".48" stop-color="#7ae7ff"/><stop offset=".7" stop-color="#3979ff"/><stop offset="1" stop-color="#9a254f" stop-opacity="0"/></linearGradient></defs><path class="beam beam-one" d="M480 790C680 230 1080 920 1320-100"/><path class="beam beam-two" d="M640 800C1220 350 820 240 1450 80"/><circle class="orbit-node" r="5" cx="1060" cy="410"/></svg></div>'''
        out=out.replace('<div class="hero-shade"></div>','<div class="hero-shade"></div>'+beams)
        marquee='''<div class="capability-marquee" aria-label="Private AI, enterprise clarity and experience in action"><div class="marquee-track" aria-hidden="true">'''+''.join('<span>PRIVATE AI <i>✦</i> ENTERPRISE CLARITY <i>✦</i> EXPERIENCE IN ACTION <i>✦</i> </span>' for _ in range(2))+'</div></div>'
        marker='<section class="section" id="ai-products">'
        out=out.replace(marker,marquee+marker)
        marker='<section class="section"><div class="wrap"><div class="academy-block">'
        out=out.replace(marker,guide_section()+marker)
        teaser=f'''<section class="section-sm light"><div class="wrap about-teaser"><div><p class="eyebrow">THE PEOPLE &amp; PURPOSE BEHIND BLUZEE</p><h2>Built on trust.<br>Looking beyond boundaries.</h2></div><div><p>Meet our leadership and explore the vision and mission that guide Bluzee.</p><div class="actions">{button('Meet the leadership',u('about/index.html#leadership'))}{link('Our vision & mission',u('about/index.html#purpose'))}</div></div></div></section>'''
        out=out.replace(cta(),teaser+cta())
        out=out.replace('Turn capability into trust, ownership and meaningful contribution.</p>', 'Turn capability into trust, ownership and meaningful contribution. Explore our workshop reach across 24 academic institutions, including SCMS Cochin.</p>')
        return out
    ns['homepage']=homepage
    old_offering=ns['offering']
    def offering(o):
        result=old_offering(o)
        if o['slug']=='professional-character':result=result.replace('<a href="#approach">Approach</a>','<a href="#workshop-reach">Institutions</a><a href="#approach">Approach</a>')
        return result
    ns['offering']=offering
    old_about=ns['about']
    def about():
        out=old_about()
        marker='<section class="section light">'
        out=out.replace(marker,purpose()+leadership()+marker,1)
        return out
    ns['about']=about
    old_contact=ns['contact_page']
    def contact_page():
        out=old_contact()
        start=out.index('<a class="big-contact"')
        end=out.index('</div><form',start)
        out=out[:start]+contact_details()+out[end:]
        out=out.replace('Business Bay, Dubai, UAE</p>','Business Bay, Dubai, UAE<br><strong class="office-license">Dubai Trade License 786627</strong></p>')
        out=out.replace('<p class="form-note">Nothing is sent', '<p class="recipient-note" aria-live="polite">General enquiries: <strong>inbox@bluzee.xyz</strong></p><p class="form-note">Nothing is sent')
        out=out.replace('<h3>Your email draft is ready.</h3>','<h3>Your email draft is ready.</h3><p class="draft-recipient"></p>')
        out=out.replace('</pre><a class="btn draft-link"','</pre><a class="btn draft-link"')
        return out
    ns['contact_page']=contact_page
    old_notes=ns['notes']
    def notes():
        out=old_notes().replace('with a white treatment on navy and its original colours on pale blue','with white lettering and a deep maroon U on navy, and navy lettering with the same maroon U on pale blue')
        out=out.replace('Short opacity/18-pixel entrance reveals; subtle slow hero movement; restrained hover transitions.','Calm people-centred homepage motion, moving capability typography, cinematic Vision and Mission chapters, staggered reveals, and gentle pointer-driven image depth. A reading-progress line responds to scrolling.')
        additions='''<h3>October 24 review updates</h3><ul><li>Original logo geometry retained through a CSS alpha mask; the U is deep maroon. For Wix, reproduce the same colour treatment using the original vector or a faithful transparent export.</li><li>WhatsApp enquiries: +971 58 653 1493, linked using wa.me/971586531493. A labelled icon is available on every page; contact areas retain the UAE and India call numbers.</li><li>AI product enquiries: ai@bluzee.xyz. The concept’s email draft routes DealTailor and Dimaq to this address and copies inbox@bluzee.xyz; other offerings retain the general address. Configure equivalent recipient routing in Wix Forms. No email is sent by the concept.</li><li>Leadership portraits, names, titles and available profile links are inherited from the current About page. Only source-supported biography text is used. Adlan’s displayed title, Consulting House, is retained without expansion.</li><li>Vision and mission statements are preserved from the existing About page, with animated visual treatments.</li><li>The original 26-page ERP guide (July 2024) is available locally, unchanged, from Home, the footer and the existing-resource link.</li><li>The corporate workshop brochure supplies 23 academic institutions. SCMS Cochin is added per this review instruction, bringing the displayed list to 24. Volvo is shown separately as corporate workshop experience. Institution names follow the brochure labels.</li><li>The newly supplied six-page corporate workshop brochure is the main workshop download; the previous detailed pathway brochure remains available. Downloaded historical/source PDFs are preserved unchanged, including their original contact details and trademark styling.</li><li>DealTailor and Dimaq carry ™ throughout website copy; Bluzee carries ™ at the logo. Dubai Trade License 786627 appears in the footer and Dubai office details.</li><li>Stronger motion pauses when off screen or the browser tab is hidden, stops for reduced-motion preferences, and can be paused using the visible top motion control. Pointer depth is limited to fine-pointer devices.</li></ul>'''
        out=out.replace('<h3>Official implementation references</h3>',additions+'<h3>Official implementation references</h3>')
        return out
    ns['notes']=notes
    def decorate_html(html,path):
        def logo(m):
            src=m.group(1)
            return f'<span class="brand-mark" style="--logo-source:url(\'{src}\')"><img src="{src}" alt="Bluzee" width="1116" height="221"><i aria-hidden="true" style="-webkit-mask-image:url(\'{src}\');mask-image:url(\'{src}\')"></i></span><sup class="logo-tm" aria-label="trademark">™</sup>'
        html=re.sub(r'<img[^>]*src="([^"]*assets/bluzee-logo.png)"[^>]*>',logo,html)
        html=re.sub(r'\b(DealTailor|Dimaq)(?!™)',r'\1™',html)
        html=html.replace('Existing Bluzee resource PDF','Download the ERP guide · July 2024')
        html=html.replace('https://www.bluzee.xyz/_files/ugd/0ae95f_60106f199a8d4a958d1ccda3b803c8d8.pdf',u('resources/'+GUIDE))
        html=html.replace('<body>','<body><div class="reading-progress" aria-hidden="true"></div><button class="motion-quick" aria-label="Pause animation" aria-pressed="false"><span aria-hidden="true">Ⅱ</span><span class="motion-label">Pause motion</span></button>')
        return html
    ns['decorate_html']=decorate_html

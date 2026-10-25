"""Bluzee v9: horizon art direction and purposeful interaction, preserving v8 content."""
from html import escape as E
from cinematic_v8 import replace_section
from r2_media import media_url
import json
from pathlib import Path
MEDIA=json.loads((Path(__file__).parent/'content-source/r2-media.json').read_text())

def install(ns):
    u=ns['u'];button=ns['button'];link=ns['link'];contact=ns['contact'];BY=ns['BY_SLUG'];brochure=ns['brochure'];href=ns['href']
    def image(asset,cls='',eager=False):
        return f'<picture class="{cls}"><source media="(max-width:700px)" srcset="{u("assets/v9/"+asset+"-mobile.webp")}"><img src="{u("assets/v9/"+asset+".webp")}" alt="" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'></picture>'
    def hero():
        choices=[('arrival','01','Perspective','A wider view of what is possible.'),('ai-conversation','02','Intelligence','Conversations with a meaningful next step.'),('ascent','03','Experience','Progress begins with people.')]
        scenes=''.join(f'<div class="v9-hero-scene {"selected" if i==0 else ""}" data-hero-image="{key}">{image(key,eager=i==0)}</div>' for i,(key,*_) in enumerate(choices))
        controls=''.join(f'<button class="v9-perspective" type="button" data-hero-choice="{key}" aria-pressed="{str(i==0).lower()}"><span>{num}</span><strong>{label}</strong><i aria-hidden="true">↗</i></button>' for i,(key,num,label,_) in enumerate(choices))
        return f'''<section class="v9-home-hero" data-v9-landscape><div class="v9-hero-stage">{scenes}<canvas class="v9-water-lens" aria-hidden="true"></canvas><div class="v9-hero-shade" aria-hidden="true"></div><div class="v9-horizon-lines" aria-hidden="true"><i></i><i></i><i></i></div><div class="wrap v9-home-copy"><p class="eyebrow">BLUZEE™ / AI. ENTERPRISE. EXPERIENCE.</p><h1><span class="v9-line"><span>A wider perspective.</span></span><span class="v9-line"><span>A more <em>intelligent</em></span></span><span class="v9-line"><span>way forward.</span></span></h1><p class="lede">Private AI. Purposeful ERP. Experience that matters.<br>Bring your next possibility into view.</p><div class="actions">{button('Explore our AI products','#ai-products')}{link('Start a conversation',contact())}</div></div><div class="wrap v9-hero-bottom"><a href="#v8-next" class="v9-scroll"><span class="v9-scroll-line" aria-hidden="true"></span>SCROLL TO DISCOVER</a><div class="v9-perspectives" aria-label="Choose a visual perspective">{controls}</div></div><div class="v9-scene-caption" aria-hidden="true">PERSPECTIVE / CONNECTION / EXPERIENCE</div></div></section>'''
    def ai_stage():
        definitions=[('dealtailor','ai-conversation','01','Engage','Every conversation.<br>A meaningful <em>next step.</em>','Bluzee DealTailor™ engages leads, understands intent and helps your sales team focus on the next useful action.',['Private AI lead engagement','Lead qualification and sales handover','Customer-controlled deployment, within agreed scope']),('dimaq','ai-intelligence','02','Decide','See beyond reports.<br>Prepare for <em>what’s next.</em>','Bluzee Dimaq™ helps business owners and department heads turn authorised enterprise data into meeting-ready insight and actions.',['Platform-agnostic decision intelligence','Role-based access to approved enterprise data','AWS-managed model options and administrator-controlled access'])]
        tabs='';panels='';photos=''
        for i,(slug,asset,num,label,title,desc,points) in enumerate(definitions):
            o=BY[slug]
            tabs+=f'<button type="button" role="tab" id="ai-tab-{slug}" aria-controls="ai-panel-{slug}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" data-ai-choice="{slug}"><small>{num} / {label.upper()}</small><span>{E(o["name"])}</span><i aria-hidden="true">↗</i></button>'
            photos+=f'<div class="v9-ai-image {"selected" if i==0 else ""}" data-ai-image="{slug}">{image(asset)}</div>'
            panels+=f'<article role="tabpanel" id="ai-panel-{slug}" aria-labelledby="ai-tab-{slug}" class="v9-ai-panel"'+(' hidden' if i else '')+f'><p class="eyebrow">{E(o["kicker"])}</p><h2>{title}</h2><p class="lede">{desc}</p><ul class="v8-capabilities">'+''.join('<li>'+p+'</li>' for p in points)+f'</ul><div class="actions">{button("Explore "+o["name"],u(href(o)))}{brochure(o)}</div></article>'
        motion='<div class="v9-intelligence-art" aria-hidden="true"><canvas class="v9-morph-network"></canvas><span class="v9-network-label top">ENQUIRY</span><span class="v9-network-label middle">UNDERSTANDING</span><span class="v9-network-label bottom">NEXT ACTION</span><p>ILLUSTRATIVE INTELLIGENCE FLOW</p></div>'
        return f'<section class="v9-ai-stage" id="ai-products" data-v9-landscape>{photos}<div class="v9-ai-shade" aria-hidden="true"></div><div class="wrap v9-ai-inner"><div class="v9-ai-top"><p class="eyebrow">PRIVATE AI / TWO DISTINCT ADVANTAGES</p><p>Choose a perspective. Discover the product.</p></div><div class="v9-ai-tabs" role="tablist" aria-label="Bluzee private AI products">{tabs}</div><div class="v9-ai-panels">{panels}</div>{motion}</div></section>'
    def motion_film(key,poster,title):
        src=media_url(MEDIA['videos'][key])
        start,end=(16,20.8) if key=='iit-madras-session' else (12,26)
        return f'<div class="v9-motion-film" data-motion-film><video muted playsinline preload="none" poster="{u(poster)}" data-preview-src="{src}" data-loop-start="{start}" data-loop-end="{end}" aria-label="Silent excerpt: {title}"></video><div class="v9-film-shade" aria-hidden="true"></div><div class="v9-film-label"><span>REAL PEOPLE / REAL MOMENTS</span><button type="button" class="v9-film-toggle" aria-pressed="false">Play silent preview ▷</button><a href="{u("events/index.html#event-recordings")}">Watch original recordings ↗</a></div></div>'
    def guide():
        pdf=u('resources/Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf')
        chapters=[('05','Key drivers','Start with the essentials.','Explore scope, people, communication and customer expectations.'),('07','Managing change','Bring people with you.','See how engagement, training and support shape adoption.'),('14','Implementation phases','Give the journey structure.','Follow the phases from analysis and kick-off to go-live and support.'),('24','Progress tracking','Make progress visible.','Explore reporting, regular updates and milestone tracking.')]
        controls=''.join(f'<button type="button" role="tab" id="guide-tab-{page}" aria-selected="{str(i==0).lower()}" aria-controls="guide-topic-{page}" tabindex="{0 if i==0 else -1}" data-guide-page="{page}"><span>0{i+1}</span>{title}<i aria-hidden="true">↗</i></button>' for i,(page,title,_,_) in enumerate(chapters))
        panels=''.join(f'<div role="tabpanel" id="guide-topic-{page}" aria-labelledby="guide-tab-{page}"'+(' hidden' if i else '')+f'><p class="v9-guide-page-label">INSIDE THE GUIDE / PAGE {int(page)}</p><h3>{title}</h3><p>{desc}</p><a class="text-link" href="{pdf}#page={int(page)}" target="_blank" rel="noopener">Read this page <span aria-hidden="true">↗</span></a></div>' for i,(page,_,title,desc) in enumerate(chapters))
        pages=''.join(f'<img src="{u("assets/v9/guide-page-"+page+".webp")}" alt="Original ERP guide, page {int(page)}: {title}" data-guide-image="{page}" loading="lazy"'+(' hidden' if i else '')+'>' for i,(page,title,_,_) in enumerate(chapters))
        return f'''<section class="v9-guide" id="erp-guide" data-v9-landscape>{image('atlas','v9-guide-landscape')}<div class="v9-guide-shade" aria-hidden="true"></div><div class="wrap"><div class="v9-guide-heading"><p class="eyebrow">THE BLUZEE ERP GUIDE / AN INTERACTIVE PREVIEW</p><h2>A little perspective.<br>A <em>better beginning.</em></h2><p class="lede">Open the guide. Explore the thinking.<br>Take a clearer direction into your ERP journey.</p></div><div class="v9-guide-workspace"><div class="v9-guide-navigation"><div class="v9-guide-tabs" role="tablist" aria-label="Explore topics from the ERP guide">{controls}</div><div class="v9-guide-topic">{panels}</div></div><div class="v9-folio-stage" data-v9-tilt><div class="v9-folio-shadow" aria-hidden="true"></div><div class="v9-folio"><div class="v9-folio-sheets" aria-hidden="true"></div><a class="v9-folio-page" href="{pdf}#page=5" target="_blank" rel="noopener" aria-label="Read the selected original ERP guide page">{pages}</a><button class="v9-folio-cover" type="button" aria-expanded="false" aria-label="Open the ERP guide preview"><span class="v9-cover-brand">BL<span class="v9-cover-red">U</span>ZEE<span>™</span></span><span class="v9-cover-rule"></span><span class="v9-cover-kicker">A PRACTICAL PERSPECTIVE</span><span class="v9-cover-title">ERP<br>Implementation<br><em>Methodology.</em></span><span class="v9-cover-bottom">JULY 2024 / 26 PAGES <span>OPEN THE GUIDE ↗</span></span><span class="v9-cover-orbit" aria-hidden="true"></span></button></div><button type="button" class="v9-close-folio" hidden>Close preview <span aria-hidden="true">↙</span></button><p class="v9-folio-hint">OPEN THE COVER · EXPLORE A TOPIC</p></div></div><div class="v9-guide-download"><p>Keep the complete perspective.<span>Original Bluzee guide · PDF · July 2024</span></p>{button('Download the complete guide',pdf,False,'download')}</div></div></section>'''
    old_home=ns['homepage']
    def homepage():
        out=old_home()
        out=replace_section(out,'<section class="v8-hero',hero())
        start=out.index('<section class="v8-section-label"');end=out.index('<div class="v8-portfolio"',start)
        out=out[:start]+ai_stage()+out[end:]
        out=replace_section(out,'<section class="v8-guide',guide())
        out=out.replace('<section class="v8-erp v8-cinema v8-pale"','<section class="v8-erp v8-cinema v8-pale v9-erp"')
        labels=[('Assess business priorities.','odoo-erp-consulting'),('Deliver with engagement.','odoo-erp-implementation'),('Bring in the right expertise.','erp-talent-outsourcing'),('Prepare for life in production.','erp-support')]
        for i,(label,slug) in enumerate(labels):
            needle=f'<a class="v8-rail" href="{u("services/"+slug+"/index.html")}"'
            out=out.replace(needle,needle+f' data-erp-focus="{i}" data-erp-label="{label}"')
        out=out.replace('<div class="v8-service-list">','<div class="v8-service-list"><div class="v9-erp-position"><span class="v9-erp-progress" aria-hidden="true"></span><p>Assess business priorities.</p></div>')
        flow='<div class="v9-enterprise-flow" aria-label="ERP services: prioritise, implement, resource and support"><svg viewBox="0 0 500 90" aria-hidden="true"><path d="M15 65 C70 65 75 25 140 25 S210 65 265 65 S340 25 390 25 S450 65 485 65"/><path class="v9-flow-packets" d="M15 65 C70 65 75 25 140 25 S210 65 265 65 S340 25 390 25 S450 65 485 65"/><circle cx="15" cy="65" r="5"/><circle cx="170" cy="30" r="5"/><circle cx="330" cy="42" r="5"/><circle cx="485" cy="65" r="5"/></svg><div><span>Prioritise</span><span>Implement</span><span>Resource</span><span>Support</span></div></div>'
        out=out.replace('<div class="v9-erp-position">',flow+'<div class="v9-erp-position">')
        marker='<div class="v8-academy-caption">'
        pos=out.index(marker);end=out.index('</div>',pos)+6
        out=out[:pos]+motion_film('iit-madras-session','assets/proof-iit-madras-session.webp','Design Your Professional Character at IIT Madras')+out[end:]
        return out
    ns['homepage']=homepage;ns['guide_section']=guide
    old_notes=ns['notes']
    def notes():
        out=old_notes().replace('CONCEPT V8 / REVIEW NOTES','CONCEPT V9 / REVIEW NOTES').replace('A more immersive','A wider perspective for')
        out=out.replace('Backgrounds move gently with scrolling and pointer position. Hero imagery breathes through slow zooms; text enters in a measured sequence. The ERP guide responds to pointer movement.','The homepage offers three visual perspectives, cursor-responsive water refraction, cinematic image reveals and an interactive private-AI showcase. Backgrounds respond to pointer movement and scrolling. The ERP guide opens as a three-dimensional folio, with four original PDF pages to explore and a download of the complete guide. Navigation uses a short, reduced-motion-aware curtain transition.')
        out=out.replace('No scroll hijacking or automatic video playback is used.','No scroll hijacking is used. Short silent excerpts from existing workshop recordings can play when visible on desktop, with a pause control. Mobile and reduced-motion visitors can choose to play. Original recordings remain unchanged.')
        out=out.replace('Local responsive WebP images reduce download weight.','Local responsive WebP images reduce download weight. The interaction layer uses native CSS, JavaScript and a progressively enhanced 2D canvas; the site does not depend on WebGL.')
        return out
    ns['notes']=notes
    old_events=ns['events']
    def events():
        out=old_events()
        start=out.index('<div class="wrap v8-hero-inner">')
        return out[:start]+motion_film('mindfulness-session','assets/events/mindfulness-gallery-06.webp','Mindfulness leadership workshop, Dubai')+out[start:]
    ns['events']=events
    old_decorate=ns['decorate_html']
    def decorate(html,path):
        html=old_decorate(html,path)
        html=html.replace('class="v8-design"','class="v8-design v9-design"')
        html=html.replace(f'<script src="{u("assets/cinematic-v8.js")}" defer></script>','')
        html=html.replace('</head>',f'<link rel="stylesheet" href="{u("assets/horizon-v9.css")}"><script src="{u("assets/horizon-v9.js")}" defer></script></head>')
        replacements={'home-horizon':'arrival','dealtailor-human':'ai-conversation','private-ai':'ai-intelligence','erp-world':'pathways','academy-future':'ascent','engineering-ai':'ai-intelligence','workshop-human':'ascent'}
        for old,new in replacements.items():
            for suffix in ['', '-mobile']:
                html=html.replace('assets/v8/'+old+suffix+'.webp','assets/v9/'+new+suffix+'.webp')
        html=html.replace('</body>','<div class="v9-page-curtain" aria-hidden="true"><span></span><span></span></div><div class="v9-pointer-orbit" aria-hidden="true"><span>EXPLORE</span></div></body>')
        return html
    ns['decorate_html']=decorate

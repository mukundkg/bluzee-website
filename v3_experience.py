"""Dynamic homepage and dedicated event/testimonial destinations, October 2026."""
from pathlib import Path
from html import escape as E
import json,re
from r2_media import CONFIG as R2_CONFIG, media_url
ROOT=Path(__file__).parent

def install(ns):
 u,button,link,img,href,contact=(ns[k] for k in ['u','button','link','img','href','contact'])
 O=ns['OFFERINGS'];P=ns['PROOF'];A=ns['A']
 def scene(name,alt,cls=''):
  return f'<img src="{u("assets/"+name+".webp")}" alt="{E(alt)}" class="{cls}" loading="lazy" decoding="async" width="1536" height="1024">'
 def erp_intro():
  services=''.join(f'<a class="erp-service-tile reveal" href="{u(href(o))}"><span class="tile-index">0{i+1}</span><h3>{o["short"]}</h3><p>{o["intro"]}</p>{A}</a>' for i,o in enumerate(O[2:6]))
  return f'''<section class="section erp-introduction" id="erp-services"><div class="wrap"><div class="erp-intro-grid"><div class="erp-editorial reveal"><p class="eyebrow">BLUZEE ERP CONSULTING SERVICES</p><h2>Every module.<br><span class="accent">A business reason.</span></h2><p class="intro-statement">Protect your budget.<br>Focus your implementation.</p><p class="lede">Bluzee helps businesses avoid the cost and delay of implementing ERP features they do not need. We assess your workflows and business continuity priorities, then shape a phased roadmap around the capabilities that matter.</p><div class="actions">{button('Find the right ERP scope',contact(O[2]))}</div>{ns['odoo']()}</div><div class="erp-visual scene-card reveal" data-depth><div class="depth-inner">{scene('erp-purpose-v3','Conceptual modular enterprise system illustrating purposeful ERP scope')}<span class="visual-label scope-now"><i></i>PHASE 1 · WHAT MATTERS NOW</span><span class="visual-label scope-next">NEXT · WHEN THE BUSINESS NEEDS IT</span><div class="scene-crosshair" aria-hidden="true"></div></div><div class="scene-caption"><span>RELEVANCE → PRIORITY → CONTINUITY</span><span>Conceptual visual</span></div></div></div><div class="erp-principles"><span><b>01</b> Assess the real need</span><span><b>02</b> Prioritise essential modules</span><span><b>03</b> Plan the next phase</span></div><div class="erp-service-grid">{services}</div></div></section>'''
 def guide():
  return f'''<section class="section guide-section-v3" id="erp-guide"><div class="wrap"><div class="guide-editorial"><div class="guide-visual scene-card reveal" data-depth data-guide-motion><div class="depth-inner">{scene('guide-navigation-v3','Conceptual digital ERP field guide with illuminated pathways')}<div class="guide-orbit" aria-hidden="true"><i></i></div><span class="guide-coordinate coordinate-one">01 / PLAN</span><span class="guide-coordinate coordinate-two">02 / ALIGN</span><span class="guide-coordinate coordinate-three">03 / DELIVER</span><div class="cursor-glow" aria-hidden="true"></div></div><div class="scene-caption"><span>THE ERP IMPLEMENTATION FIELD GUIDE</span><span class="pointer-hint">Move to explore ↗</span></div></div><div class="guide-copy-v3 reveal"><p class="eyebrow">THE BLUZEE ERP GUIDE</p><h2>A clearer path.<br><span class="accent">Before you begin.</span></h2><p class="lede">Navigate the decisions behind an ERP engagement with Bluzee’s implementation methodology guide. A practical reference for planning, alignment and delivery.</p><div class="resource-meta"><span>26 pages</span><span>July 2024 edition</span></div><div class="actions">{button('Download the ERP guide',u('resources/Bluzee_ERP_Implementation_Methodology_Guide_July_2024.pdf'),False,'download')}{link('Discuss your ERP plans',contact(O[2]))}</div></div></div></div></section>'''
 def academy():
  routes=''.join(f'<a class="academy-route" href="{u(href(o))}"><span>0{i+1} / EXPERIENCE PATHWAY</span><h3>{o["name"]}</h3><p>{"Connect ERP workflows with business understanding and delivery practice." if i==0 else "Build practical AI solutions or complete applications through two focused streams."}</p>{A}</a>' for i,o in enumerate(O[6:8]))
  return f'''<div class="academy-introduction"><div class="academy-heading reveal"><div><p class="eyebrow">BLUZEE ACADEMY OF EXPERIENCE</p><h2>Build the experience.<br><span class="accent">Show what you can deliver.</span></h2></div><div class="six-months"><strong>6</strong><span>MONTHS<br>OF PURPOSEFUL EXPERIENCE</span></div></div><div class="academy-editorial"><div class="academy-visual scene-card reveal" data-depth><div class="depth-inner">{scene('academy-delivery-v3','Illustrative professional team reviewing a software project; not actual Bluzee participants')}<div class="academy-visual-shade"></div><div class="project-proof"><small>EXPERIENCE YOU CAN EXPLAIN</small><strong>The task.<br>Your contribution.<br>The outcome.</strong></div></div><span class="illustration-note">Illustrative project scene</span></div><div class="academy-story reveal"><p class="intro-statement">Give employers evidence<br>of your ability to contribute.</p><p>Employers and clients look for evidence that you can deliver: understand a brief, complete a task, solve problems and explain your contribution.</p><p>Build that evidence through Bluzee Academy of Experience’s six-month pathway. Apply your skills to scoped, reviewed assignments and develop a portfolio grounded in practical work.</p><p>On successful completion of the applicable programme requirements, receive a Bluzee experience certificate supported by documented contributions. Approach suitable early-career opportunities with a stronger story than training alone.</p><div class="experience-evidence"><span>Reviewed work</span><span>Project evidence</span><span>Experience certificate</span></div><p class="academy-qualification">Programme duration, assignment access and certification requirements are confirmed at enrolment. Employer acceptance, experience classification and job eligibility depend on each role; employment is not guaranteed.</p></div></div><div class="academy-pathway" aria-label="Experience pathway"><span><b>01</b> Understand the brief</span><span><b>02</b> Deliver the work</span><span><b>03</b> Review &amp; improve</span><span><b>04</b> Demonstrate your contribution</span></div><div class="academy-route-grid">{routes}</div></div>'''
 oldhome=ns['homepage']
 def homepage():
  out=oldhome()
  a=out.index('<section class="section light"><div class="wrap services-layout">');b=out.index('<section class="section-sm resource-section">',a)
  out=out[:a]+erp_intro()+out[b:]
  a=out.index('<section class="section-sm resource-section">');b=out.index('<section class="section"><div class="wrap"><div class="academy-block">',a)
  out=out[:a]+guide()+out[b:]
  a=out.index('<div class="academy-block">');b=out.index('<div class="workshop-band',a)
  out=out[:a]+academy()+out[b:]
  out=out.replace('<section class="section"><div class="wrap"><div class="academy-introduction">','<section class="section academy-section" id="academy"><div class="wrap"><div class="academy-introduction">')
  out=out.replace('<section class="home-hero">','<section class="home-hero immersive-hero human-hero">')
  out=re.sub(r'<div class="hero-motion" aria-hidden="true">.*?</svg></div>','',out,flags=re.S)
  out=out.replace('<div class="hero-scene" role="presentation"></div>','<div class="hero-scene" role="img" aria-label="Illustrative team collaborating in a calm, sunlit workspace; not actual Bluzee staff or clients"></div>')
  out=out.replace('<div class="hero-shade"></div>','<div class="hero-shade"></div><div class="human-daylight" aria-hidden="true"></div><span class="human-scene-caption">Illustrative collaboration scene</span>')
  out=re.sub(r'<div class="hero-signal" aria-hidden="true">(.*?)</div></div>',lambda m:f'<a class="hero-signal" href="{u("products/dimaq/index.html")}" aria-label="Explore Bluzee Dimaq™">{m[1]}</div></a>',out)
  out=re.sub(r'<div class="hero-signal second" aria-hidden="true">(.*?)</div></div>',lambda m:f'<a class="hero-signal second" href="{u("products/dealtailor/index.html")}" aria-label="Explore Bluzee DealTailor™">{m[1]}</div></a>',out)
  out=out.replace(u('stories/index.html'),u('events/index.html'))
  return out
 ns['homepage']=homepage
 oldhead=ns['header']
 def header(active):
  out=oldhead(active)
  nav=''.join(f'<a class="nav-link" href="{u(path)}" '+('aria-current="page"' if active==key else '')+f'>{title}</a>' for title,path,key in [('Events','events/index.html','events'),('Testimonials','testimonials/index.html','testimonials')])
  out=out.replace(f'<a href="{u("stories/index.html")}">Stories &amp; Sessions</a>',f'<a href="{u("events/index.html")}">Events</a><a href="{u("testimonials/index.html")}">Testimonials</a>')
  return out.replace('</details>', '</details>'+nav,1)
 ns['header']=header
 oldfoot=ns['footer']
 def footer():return oldfoot().replace(f'<a href="{u("stories/index.html")}">Stories &amp; Sessions</a>',f'<a href="{u("events/index.html")}">Events</a><a href="{u("testimonials/index.html")}">Testimonials</a><a href="{u("stories/index.html")}">Full media archive</a>')
 ns['footer']=footer
 oldproof=ns['proof_section']
 def proof_section(ids,title='Experience. In their own words.',students=False):
  if students and 'adheena' not in ids: ids=list(ids)+['adheena']
  out=oldproof(ids,title,students)
  return out.replace('Explore Stories &amp; Sessions','Explore Testimonials' if students else 'Explore Events').replace('Explore Stories & Sessions','Explore Testimonials' if students else 'Explore Events').replace(u('stories/index.html'),u('testimonials/index.html' if students else 'events/index.html'))
 ns['proof_section']=proof_section
 def additions():
  f=ROOT/'content-source/events-partners-v3.json'
  return json.loads(f.read_text()) if f.exists() else {'posts':[],'partners':[]}
 def events():
  cards=''
  for key in ['erp-hub-launch','iim-kozhikode-session','volvo-session','iit-madras-session','nit-calicut-session','mindfulness-session','erp-hub-overview','barry-interview']:
   card=ns['proof_card'](key)
   cats='Launch Academy' if key=='erp-hub-launch' else 'Academy' if key=='erp-hub-overview' else 'Leadership IIM' if key=='mindfulness-session' else 'Leadership' if key=='barry-interview' else 'DYPC'+(' IIM' if 'iim' in key else '')
   card=re.sub(r'data-category="[^"]+"',f'data-category="{cats}"',card)
   summary=additions().get('event_summaries',{}).get(key,'')
   card=card.replace('</h3>',f'</h3><p class="event-card-summary">{E(summary)}</p>',1)
   cards+=card
  posts=''
  for p in additions().get('posts',[]):
   media=''.join(f'<a href="{u(i["asset"])}" target="_blank" rel="noopener"><img src="{u(i["asset"])}" alt="{E(i["alt"])}" loading="lazy"></a>' for i in p.get('images',[]))
   posts+=f'<article class="event-journal-card reveal"><span>{E(p["date"])}</span><h3>{E(p["title"])}</h3><p>{E(p["summary"])}</p><div class="news-images">{media}</div>{link("Read the original story",p["url"],'target="_blank" rel="noopener"')}</article>'
  galleries=''
  for g in sorted(additions().get('galleries',[]),key=lambda g:g['id']):
   media=''.join(f'<a href="{E(i["original_url"])}" target="_blank" rel="noopener" aria-label="Open {E(i["alt"])}"><img src="{u(i["asset"])}" alt="{E(i["alt"])}" loading="lazy" width="700" height="467"></a>' for i in g['images'])
   extras=R2_CONFIG['extra_gallery_photos'].get(g['id'],[])
   extra_links='<div class="gallery-original-links">'+''.join(link('Additional photograph ↗',media_url(key),'target="_blank" rel="noopener"') for key in extras)+'</div>' if extras else ''
   galleries+=f'<div class="event-gallery-section"><h3>{E(g["title"])}</h3><p class="event-gallery-caption">{E(g["caption"])}</p><div class="event-gallery">{media}</div>{extra_links}</div>'
  return f'''<section class="standard-hero archive-hero"><div class="wrap"><p class="eyebrow">BLUZEE / EVENTS</p><h1>Ideas in the room.<br><span class="accent">Impact beyond it.</span></h1><p class="lede">Revisit Bluzee’s launch moments, Design Your Professional Character™ workshops, leadership conversations and Academy sessions.</p><div class="actions">{button('Explore the recordings','#event-recordings')}{button('Hear participant feedback',u('testimonials/index.html'),True)}</div><div class="archive-orbits" aria-hidden="true"><i></i><i></i><i></i></div></div></section><section class="section-sm" id="event-recordings"><div class="wrap" data-filter-list><div class="section-head"><div><p class="eyebrow">ORIGINAL RECORDINGS</p><h2>Watch. Reflect.<br>Take an idea forward.</h2></div><p class="lede">Explore our workshops, launch moments and leadership conversations.</p></div>{ns['filters'](['All','Launch','DYPC','IIM','Leadership','Academy'],'Events')}<div class="proof-grid">{cards}</div><p class="empty-state">No events match. Try another category or clear your search.</p><p class="archive-note">The launch recording is the Bluzee ERP Experience Hub™ launch. The ERP Hub introduction is retained as programme content. The mindfulness session took place in Dubai in 2023, with Professor Debashis Chatterjee, IIM Kozhikode Director at the time.</p></div></section><section class="section"><div class="wrap"><p class="eyebrow">EVENT GALLERIES</p><h2>Moments from the room.</h2>{galleries}</div></section><section class="section light"><div class="wrap"><div class="section-head"><div><p class="eyebrow">EVENT JOURNAL</p><h2>Milestones worth revisiting.</h2></div>{link('All original news & events','https://www.bluzee.xyz/blog','target="_blank" rel="noopener"')}</div><div class="event-journal-grid">{posts}</div><div class="source-gallery">{link('Original workshop gallery','https://www.bluzee.xyz/workshop','target="_blank" rel="noopener"')}{link('Original Experience Hub gallery','https://www.bluzee.xyz/experiencehub','target="_blank" rel="noopener"')}</div></div></section>{ns['cta']()}'''
 ns['events']=events
 def testimonials():
  students=[k for k,v in P.items() if 'original_player_url' in v]
  partners=''.join(f'<div class="partner-logo"><img src="{u(p["local_asset"])}" alt="{E(p["name"])}" loading="lazy"><span>{E(p["name"])}</span></div>' for p in additions().get('partners',[]))
  return f'''<section class="standard-hero archive-hero testimonial-hero"><div class="wrap"><p class="eyebrow">BLUZEE / TESTIMONIALS</p><h1>The work matters.<br><span class="accent">Their words matter.</span></h1><p class="lede">Hear from participants, read original feedback and meet our network of partners.</p><div class="actions">{button('Hear the participant voices','#participant-voices')}{button('Explore our events',u('events/index.html'),True)}</div><div class="quote-art" aria-hidden="true">“</div></div></section><section class="section light" id="participant-voices"><div class="wrap"><div class="section-head"><div><p class="eyebrow">EXPERIENCE, IN THEIR OWN WORDS</p><h2>Meet the people<br>behind the feedback.</h2></div><p class="lede">Original participant videos open in Bluzee’s existing video gallery.</p></div><div class="proof-grid students">{''.join(ns['proof_card'](k) for k in students)}</div></div></section><section class="section feedback-section"><div class="wrap feedback-layout"><div><p class="eyebrow">ORIGINAL WRITTEN APPRECIATION</p><h2>Feedback that<br>stays with us.</h2><p class="lede">Read the original Volvo appreciation letter, preserved in its original form.</p>{link('View the original letter',u('assets/volvo-feedback-original.png'),'target="_blank" rel="noopener"')}</div><div class="feedback-original">{ns['proof_card']('volvo-feedback')}</div></div></section><section class="section light" id="partners"><div class="wrap"><div class="section-head"><div><p class="eyebrow">OUR PARTNERS</p><h2>Connections that<br>expand perspectives.</h2></div><p class="lede">Explore our network of partners.</p></div><div class="partner-logo-grid">{partners}</div></div></section>{ns['cta']()}'''
 ns['testimonials']=testimonials
 oldstories=ns['stories']
 def stories():
  s=oldstories();return s.replace('<section class="section-sm">',f'<div class="wrap archive-routes"><a href="{u("events/index.html")}">Events &amp; session recordings {A}</a><a href="{u("testimonials/index.html")}">Testimonials &amp; partners {A}</a></div><section class="section-sm">',1)
 ns['stories']=stories
 oldnotes=ns['notes']
 def notes():
  s=oldnotes();s=s.replace('with white lettering and a deep maroon U on navy, and navy lettering with the same maroon U on pale blue','with white lettering and a bright red U on navy, and navy lettering with the same red U on pale blue').replace('the U is deep maroon','the U is bright red')
  update=f'''<h3>Dynamic homepage &amp; media destinations</h3><p>The latest direction uses a calm, people-centred collaboration scene, modular ERP architecture, a cursor-responsive digital field guide and an illustrative project-delivery scene. Darker navy backgrounds and red brand accents increase contrast. ERP copy focuses on avoiding irrelevant scope and prioritising business continuity. Academy copy introduces six months of purposeful experience, reviewed work and completion documentation, with employer acceptance and eligibility qualifications.</p><p>{link('Events',u('events/index.html'))}{link('Testimonials',u('testimonials/index.html'))}</p><p>Events and Testimonials are separate primary menu pages. Events preserves the launch, workshop and leadership recordings and original event stories. Testimonials preserves participant feedback, Volvo appreciation and source-verified partner logos. The old Stories route remains as a complete archive.</p><p>The homepage uses slow camera-style movement and soft daylight. The guide and editorial images respond to fine-pointer movement. Native Wix entrance/hover effects can reproduce the simple transitions. Exact pointer depth and background motion need a small custom element or scoped code. Content remains native and all motion supports pause and reduced-motion preferences.</p>'''
  return s.replace('<h3>Official implementation references</h3>',update+'<h3>Official implementation references</h3>')
 ns['notes']=notes

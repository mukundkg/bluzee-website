"""Unique editorial imagery and product-specific motion for Bluzee v10."""
from html import escape as E
from pathlib import Path
import hashlib,re

HERO={
 'dealtailor':'dealtailor','dimaq':'dimaq','qsrpro':'qsrpro',
 'tradesphere':'tradesphere','nexus':'nexus',
 'odoo-erp-consulting':'consulting','odoo-erp-implementation':'implementation',
 'erp-talent-outsourcing':'talent','erp-support':'support',
 'erp-experience-hub':'erp-hub','ai-experience-hub':'ai-hub',
 'professional-character':'character'}
CARD={
 **{k:'v10/card-'+k for k in ['dealtailor','dimaq','qsrpro','tradesphere','nexus']},
 'odoo-erp-consulting':'consulting','odoo-erp-implementation':'implementation',
 'erp-talent-outsourcing':'talent','erp-support':'support',
 'erp-experience-hub':'erp-hub','ai-experience-hub':'ai-hub',
 'professional-character':'dypc'}

def install(ns):
    u=ns['u']
    def picture(asset,eager=False):
        small=asset+'-mobile' if asset.startswith(('v8/','v9/','v10/')) else None
        if not (Path(__file__).parent/'dist/assets'/((small or '')+'.webp')).exists():small=None
        source=f'<source media="(max-width:700px)" srcset="{u("assets/"+small+".webp")}">' if small else ''
        return f'<picture>{source}<img data-v10-art="{asset}" src="{u("assets/"+asset+".webp")}" alt="" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'></picture>'
    def replace_scene(block,asset):
        return re.sub(r'(<div class="v8-scene"[^>]*>).*?(</div>)',lambda m:m[1]+picture(asset,True)+m[2],block,count=1,flags=re.S)
    def section_transform(html,marker,fn):
        start=html.find(marker)
        if start<0:raise ValueError('Missing v10 section: '+marker)
        depth=0
        for m in re.finditer(r'</?section\b[^>]*>',html[start:]):
            depth+=-1 if m.group().startswith('</') else 1
            if depth==0:
                end=start+m.end();return html[:start]+fn(html[start:end])+html[end:]
        raise ValueError('Unclosed v10 section')
    def signature(slug):
        paths={
          'dealtailor':['M40 55 C130 55 130 140 240 140 S350 80 460 80','M40 215 C130 215 140 140 240 140','M90 135 L240 140'],
          'dimaq':['M55 50 L200 50 L275 140 L440 140','M55 220 L200 220 L275 140','M275 35 L275 245','M160 140 L440 140'],
          'qsrpro':['M30 180 L470 180','M90 70 L90 180 M220 90 L220 180 M350 50 L350 180'],
          'tradesphere':['M40 210 L125 210 L125 70 L305 70 L305 175 L460 175','M125 140 L220 140 L220 230 L400 230'],
          'nexus':['M35 50 L140 50 Q175 50 175 100 L175 140 L315 140 L315 65 L465 65','M35 230 L140 230 Q175 230 175 185 L175 140','M315 140 L315 225 L465 225']}
        lines=paths[slug]
        shapes=''.join(f'<path class="v10-track" d="{p}"/><path class="v10-packet" style="--packet-delay:{i*-.8}s" d="{p}"/>' for i,p in enumerate(lines))
        if slug=='dimaq':shapes+='<circle class="v10-target" cx="275" cy="140" r="42"/><circle cx="275" cy="140" r="7" class="v10-red-node"/>'
        elif slug=='qsrpro':shapes+=''.join(f'<rect class="v10-order" x="{x}" y="140" width="35" height="25" rx="3" style="--packet-delay:{i*-.7}s"/>' for i,x in enumerate([70,200,330]))
        elif slug=='tradesphere':shapes+='<rect class="v10-cargo" x="289" y="52" width="32" height="32" rx="2"/>'
        elif slug=='nexus':shapes+=''.join(f'<rect class="v10-system" x="{x}" y="{y}" width="30" height="30" rx="5"/>' for x,y in [(20,35),(20,215),(450,50),(450,210)])
        else:shapes+='<circle class="v10-target" cx="460" cy="80" r="24"/><circle class="v10-red-node" cx="460" cy="80" r="8"/>'
        return f'<div class="v10-product-motion v10-motion-{slug}" aria-hidden="true"><svg viewBox="0 0 500 280">{shapes}</svg></div>'
    def red_scene(seed):
        return f'<div class="v10-red-scene" data-red-scene="{seed%5}" aria-hidden="true"><div class="v10-red-orbit"><i></i><i></i></div><div class="v10-ball-track"><div class="v10-ruby v10-ruby-large"><span></span><i></i></div></div><div class="v10-small-track"><div class="v10-ruby v10-ruby-small"><span></span></div></div><div class="v10-red-dot"></div></div>'
    old_decorate=ns['decorate_html']
    def decorate(html,path):
        html=old_decorate(html,path)
        path=str(path).replace('\\','/')
        html=html.replace('v8-design v9-design','v8-design v9-design v10-design')
        html=html.replace('</head>',f'<link rel="stylesheet" href="{u("assets/distinct-v10.css")}"><script src="{u("assets/distinct-v10.js")}" defer></script></head>')
        # Repeated closing photographs are replaced by procedural sculpture.
        marker='<section class="section cta-section v8-cinema"'
        if marker in html:
            def cta(block):
                block=re.sub(r'<div class="v8-scene"[^>]*>.*?</div><div class="v8-shade"[^>]*></div><div class="v8-glow"[^>]*></div>','',block,flags=re.S)
                seed=int(hashlib.sha256(path.encode()).hexdigest()[:4],16)%360
                return block.replace('cta-section v8-cinema','cta-section v8-cinema v10-cta').replace('data-v8-scene>',f'data-v8-scene><div class="v10-cta-sculpture" style="--sculpture-start:{seed}deg" aria-hidden="true"><i></i><i></i><i></i><b></b></div>',1)
            html=section_transform(html,marker,cta)
        slug=path.split('/')[-2] if '/' in path else ''
        if slug in HERO and path.startswith(('products/','services/')):
            def offering(block):
                block=replace_scene(block,'v10/'+HERO[slug])
                block=block.replace('v8-pale','').replace('v8-hero v8-cinema','v8-hero v8-cinema v8-pale v10-offering-hero')
                block=block.replace('data-v8-scene',f'data-v8-scene data-v10-offering="{slug}"',1)
                if slug in ['dealtailor','dimaq','qsrpro','tradesphere','nexus']:block=block.replace('</section>',signature(slug)+'</section>')
                return block
            html=section_transform(html,'<section class="v8-hero',offering)
        if path=='index.html':
            for key in ['ai-conversation','ai-intelligence']:
                html=html.replace('assets/v9/'+key,'assets/v10/'+key)
            for key,asset in [('ai-conversation','v8/private-ai'),('ascent','v8/academy-future')]:
                pattern=r'(<div class="v9-hero-scene[^>]*data-hero-image="'+key+r'">).*?(</div>)'
                html=re.sub(pattern,lambda m:m[1]+picture(asset)+m[2],html,count=1,flags=re.S)
        elif path=='about/index.html':
            html=section_transform(html,'<section class="v8-hero',lambda b:replace_scene(b,'v8/home-horizon'))
            html=section_transform(html,'<section class="v8-purpose ',lambda b:replace_scene(b,'v10/shared-direction'))
        elif path=='offerings/index.html':
            html=section_transform(html,'<section class="v8-hero',lambda b:replace_scene(b,'v8/erp-world').replace('v8-pale',''))
            def card(m):
                opening,link,img=m[1],m[2],m[3]
                key=link.rstrip('/').split('/')[-2]
                if key not in CARD:raise ValueError('Unmapped portfolio image '+key)
                return opening+'<div class="v10-card-media" data-card-motion>'+picture(CARD[key])+'<span class="v10-card-shine" aria-hidden="true"></span><i class="v10-card-signal" aria-hidden="true"></i></div>'
            html=re.sub(r'(<a class="offering-card[^>]*href="([^"]+)"[^>]*>)(<img[^>]+>)',card,html)
        elif path=='contact/index.html':
            html=section_transform(html,'<section class="v8-hero',lambda b:replace_scene(b,'v8/dealtailor-human'))
        elif path=='events/index.html':
            html=section_transform(html,'<section class="v8-hero',lambda b:replace_scene(b,'events-stage-v5'))
        elif path=='testimonials/index.html':
            html=re.sub(r'<div class="v8-voice-wall".*?</div></div>',lambda m:'<div class="v8-scene" aria-hidden="true">'+picture('testimonials-resonance-v5',True)+'</div>',html,count=1,flags=re.S)
            # The wall has four nested portraits: remove the remaining decorative copies.
            html=re.sub(r'<div class="v8-voice-portrait">.*?</div>','',html,flags=re.S)
            html=html.replace('</picture></div></div><div class="v8-shade"','</picture></div><div class="v8-shade"',1)
        elif path=='stories/index.html':
            html=section_transform(html,'<section class="v8-hero',lambda b:replace_scene(b,'v8/workshop-human'))
        elif path=='design-notes/index.html':
            def noteshero(b):
                b=re.sub(r'<div class="v8-scene"[^>]*>.*?</div>','<div class="v10-notes-orbits" aria-hidden="true"><i></i><i></i><i></i></div>',b,count=1,flags=re.S)
                return b.replace('CONCEPT V9','CONCEPT V10').replace('A wider perspective for','A distinct perspective for')
            html=section_transform(html,'<section class="v8-hero',noteshero)
            html=html.replace('Designed to feel open.','A visual identity for every offering.')
            html=html.replace('Full-width imagery replaces isolated decorative image boxes.','Each offering has its own editorial image, with lighter blue daylight and distinct subjects. Decorative photographs are assigned to one location across the website; the original media archive and brand marks retain their source identities. Morphing contours, layered parallax, flowing signals and hover depth bring the imagery to life. Red sculptural spheres roll, bounce and rotate behind pale sections in response to scrolling, with a pause control and reduced-motion support.')
        if slug=='ai-experience-hub':
            index=[0]
            def stream(m):
                asset=['ai-application','full-stack'][index[0]];index[0]+=1
                return m[1]+picture(asset)
            html=re.sub(r'(<article class="split-panel"><p class="eyebrow">STREAM 0?[12]</p>)<img[^>]+>',stream,html)
        # Decorative red sculptures are different arrangements, never over controls.
        counter=[0]
        def light(m):
            opening=m.group();counter[0]+=1
            return opening[:-1]+' data-v10-light>'+red_scene(counter[0]+len(path))
        html=re.sub(r'<section\b[^>]*class="[^"]*\b(?:light|tinted|v8-pale)\b[^"]*"[^>]*>',light,html)
        return html
    ns['decorate_html']=decorate

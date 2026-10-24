"""Cinematic, source-preserving Vision and Mission presentation."""
from html import escape as E

PRINCIPLES = [
    ('Trust', 'Build lasting relationships based on trust.'),
    ('Insight', 'Uncover hidden insights.'),
    ('Exploration', 'Explore beyond boundaries.'),
    ('Diversity', 'Leverage the power of diversity.'),
    ('Resourcefulness', 'Optimize resources.'),
]

def render_purpose(u, source):
    def artwork(name, alt, caption, number):
        return f'''<figure class="purpose-art" data-purpose-art><div class="purpose-art-window"><div class="purpose-art-drift"><picture><source media="(max-width:600px)" srcset="{u('assets/'+name+'-small.webp')}"><img src="{u('assets/'+name+'.webp')}" alt="{E(alt)}" width="1536" height="1024" loading="lazy" decoding="async"></picture></div><div class="purpose-art-light" aria-hidden="true"></div><span class="purpose-art-number" aria-hidden="true">{number}</span></div><figcaption><span>{caption}</span><span>BLUZEE™ / PURPOSE</span></figcaption></figure>'''
    vision=''.join(f'<p>{E(p)}</p>' for p in source['vision']['paragraphs'])
    buttons=''.join(f'<button type="button" id="purpose-tab-{i}" role="tab" aria-selected="{str(i==0).lower()}" aria-controls="purpose-panel-{i}" tabindex="{0 if i==0 else -1}"><span>0{i+1}</span>{E(label)}<i aria-hidden="true">↗</i></button>' for i,(label,_) in enumerate(PRINCIPLES))
    panels=''.join(f'<div role="tabpanel" id="purpose-panel-{i}" aria-labelledby="purpose-tab-{i}" tabindex="0" {"hidden" if i else ""}><span class="principle-counter" aria-hidden="true">0{i+1} / 05</span><p>{E(text)}</p></div>' for i,(_,text) in enumerate(PRINCIPLES))
    return f'''<section class="purpose-cinematic" id="purpose" aria-labelledby="purpose-title">
      <div class="wrap purpose-opening"><div><p class="eyebrow">OUR NORTH STAR</p><h2 id="purpose-title">Where we’re going.<br><span>What drives us.</span></h2></div><nav class="purpose-chapters" aria-label="Explore our purpose"><a href="#vision"><span>01</span> Our vision <i aria-hidden="true">↘</i></a><a href="#mission"><span>02</span> Our mission <i aria-hidden="true">↘</i></a></nav></div>
      <article class="purpose-chapter purpose-vision" id="vision" aria-labelledby="vision-title"><div class="wrap purpose-chapter-grid"><div class="purpose-editorial"><p class="purpose-kicker"><span>01 /</span> OUR VISION</p><h3 id="vision-title">Opportunity,<br><span>without limits.</span></h3><div class="purpose-statement">{vision}</div><a class="purpose-next" href="#mission">Discover what drives us <span aria-hidden="true">↓</span></a></div>{artwork('vision-horizon-v4','Conceptual architectural gateway opening toward a blue ocean horizon','A BLUE OCEAN OF POSSIBILITIES','01')}</div></article>
      <div class="wrap purpose-bridge" aria-hidden="true"><span></span><b>AMBITION, WITH DIRECTION.</b><span></span></div>
      <article class="purpose-chapter purpose-mission" id="mission" aria-labelledby="mission-title"><div class="wrap purpose-chapter-grid"><div class="purpose-editorial"><p class="purpose-kicker"><span>02 /</span> OUR MISSION</p><h3 id="mission-title">Shared principles.<br><span>Lasting purpose.</span></h3><div class="purpose-statement"><p>{E(source['mission']['exact_text'])}</p></div><div class="purpose-principles" data-tabs><p class="purpose-principles-label">FIVE PRINCIPLES. ONE SHARED DIRECTION.</p><div class="purpose-principle-tabs" role="tablist" aria-label="Explore our mission principles">{buttons}</div><div class="purpose-principle-panels">{panels}</div></div></div>{artwork('mission-unity-v4','Conceptual blue glass and burgundy sculpture expressing shared purpose','DISTINCT STRENGTHS. SHARED PURPOSE.','02')}</div></article>
      <div class="wrap purpose-closing"><p>From shared purpose<br><span>to meaningful progress.</span></p><a class="text-link" href="#leadership">Meet the people behind Bluzee <span aria-hidden="true">↗</span></a></div>
    </section>'''

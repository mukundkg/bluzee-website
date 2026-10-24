"""Events and Testimonials: original evidence in a cinematic editorial setting."""
from html import escape as E
from r2_media import poster as media_poster
import re

def install(ns):
    u,button,link=(ns[k] for k in ['u','button','link'])
    proof=ns['PROOF']

    def background(stem):
        return f'<div class="media-scene" aria-hidden="true"><picture><source media="(max-width:600px)" srcset="{u("assets/"+stem+"-small.webp")}"><img src="{u("assets/"+stem+".webp")}" alt="" width="1672" height="941" fetchpriority="high"></picture></div><div class="media-shade" aria-hidden="true"></div><div class="media-lightpass" aria-hidden="true"></div>'

    def chapter_nav(items):
        return '<nav class="media-chapter-nav" aria-label="Explore this page"><div class="wrap">'+''.join(f'<a href="#{anchor}"><span>0{i+1}</span><strong>{title}</strong><i aria-hidden="true">↘</i></a>' for i,(anchor,title) in enumerate(items))+'</div></nav>'

    def video_button(key,classes,label,visual):
        x=proof[key]
        return f'<button type="button" class="{classes}" data-video="{E(x["original_video_url"])}" data-title="{E(x["title"])}" data-source="{E(x["source_pages"][0])}" aria-label="{E(label)}">{visual}</button>'

    def events_hero():
        photo=f'<img src="{u("assets/events/erp-hub-launch-gallery-01.webp")}" alt="Original photograph from the Bluzee ERP Experience Hub inauguration" width="700" height="467"><span class="media-film-caption"><b>ERP EXPERIENCE HUB™</b><span>THE INAUGURATION <i aria-hidden="true">▶</i></span></span>'
        launch=video_button('erp-hub-launch','event-film event-film-main','Watch the ERP Experience Hub launch',photo)
        detail=f'<a class="event-film event-film-detail" href="#event-gallery"><img src="{u("assets/events/mindfulness-gallery-06.webp")}" alt="Original photograph of the mindfulness leadership session" width="700" height="467"><span>LEADERSHIP IN CONVERSATION <i aria-hidden="true">↗</i></span></a>'
        return f'''<section class="media-hero events-hero" data-media-motion>{background('events-stage-v5')}<div class="wrap media-hero-grid"><div class="media-hero-copy"><p class="eyebrow">BLUZEE / EVENTS</p><h1>In the room.<br>Beyond the<br><span>moment.</span></h1><p class="lede">Ideas shared. Perspectives expanded. Revisit Bluzee’s launch moments, professional character workshops and leadership conversations.</p><div class="actions">{button('Explore the recordings','#event-recordings')}{link('The moments in pictures','#event-gallery')}</div></div><div class="event-film-composition"><span class="film-overline">EXPERIENCE, IN MOTION.</span>{detail}{launch}<div class="film-base"><span class="film-line"></span><p>REAL MOMENTS.<br>ORIGINAL RECORDINGS.</p></div></div></div><div class="wrap media-hero-footer"><span>LAUNCHES <b>·</b> WORKSHOPS <b>·</b> CONVERSATIONS</span><span>SCROLL TO EXPLORE <i aria-hidden="true">↓</i></span></div></section>'''

    def feature():
        visual=f'<img src="{u("assets/proof-erp-hub-launch.webp")}" alt="Original Bluzee ERP Experience Hub launch recording poster" width="1400" height="788" loading="lazy"><span class="spotlight-play"><i aria-hidden="true">▶</i><b>PLAY THE ORIGINAL RECORDING</b></span>'
        control=video_button('erp-hub-launch','event-spotlight-player','Play the featured ERP Experience Hub launch',visual)
        return f'''<section class="section media-spotlight"><div class="wrap spotlight-grid"><div class="spotlight-copy reveal"><p class="eyebrow">IN FOCUS / A BLUZEE MILESTONE</p><h2>A beginning.<br><span>A shared ambition.</span></h2><p class="lede">The inauguration of Bluzee ERP Experience Hub™ brought people together around a shared commitment to practical experience.</p><div class="spotlight-meta"><div><small>WHEN</small><strong>22 May 2025</strong></div><div><small>WHERE</small><strong>Kochi Marriott Hotel</strong></div></div>{link('Explore Bluzee ERP Experience Hub™',u('services/erp-experience-hub/index.html'))}</div><div class="spotlight-visual reveal">{control}<div class="spotlight-foot"><span>BLUZEE ERP EXPERIENCE HUB™ / INAUGURATION</span><span>ORIGINAL FILM ↗</span></div></div></div></section>'''

    old_events=ns['events']
    def events():
        out=old_events()
        out=out[out.index('</section>')+10:]
        out=out.replace('<section class="section-sm" id="event-recordings">','<section class="section-sm event-library" id="event-recordings">',1)
        out=out.replace('<section class="section"><div class="wrap"><p class="eyebrow">EVENT GALLERIES</p>','<section class="section event-gallery-editorial" id="event-gallery"><div class="wrap"><p class="eyebrow">EVENT GALLERIES</p>',1)
        out=out.replace('<section class="section light"><div class="wrap"><div class="section-head"><div><p class="eyebrow">EVENT JOURNAL</p>','<section class="section light event-journal-editorial" id="event-journal"><div class="wrap"><div class="section-head"><div><p class="eyebrow">EVENT JOURNAL</p>',1)
        out=out.replace('Moments from the room.','The people.<br>The atmosphere.<br><span class="accent">The moments.</span>')
        return '<div class="media-destination events-destination">'+events_hero()+chapter_nav([('event-recordings','Watch the recordings'),('event-gallery','Explore the photographs'),('event-journal','Revisit the milestones')])+feature()+out+'</div>'
    ns['events']=events

    def voices_hero():
        ids=['manas-aravind','muhammed-ansil-pa','anirudh-vk','vaishnav-pm']
        faces=''.join(f'<img src="{u("assets/proof-"+key+".webp")}" alt="" width="64" height="64">' for key in ids)
        return f'''<section class="media-hero voices-hero" data-media-motion>{background('testimonials-resonance-v5')}<div class="wrap media-hero-grid"><div class="media-hero-copy"><p class="eyebrow">BLUZEE / TESTIMONIALS</p><h1>Real voices.<br><span>Human stories.</span></h1><p class="lede">Experience is personal. Hear from the people who have participated, read original appreciation and discover Bluzee’s partner network.</p><div class="actions">{button('Hear the participant voices','#participant-voices')}{link('Explore our partners','#partners')}</div><a class="voices-proof-link" href="#participant-voices"><span class="voice-portraits" aria-hidden="true">{faces}</span><span><b>Every voice has a perspective.</b><small>Explore the original participant videos <i aria-hidden="true">↗</i></small></span></a></div><div class="voice-art-caption" aria-hidden="true"><span class="resonance-bars">{''.join(f'<i style="--bar:{i}"></i>' for i in range(17))}</span><p>EXPERIENCE.<br>IN THEIR OWN WORDS.</p></div></div><div class="wrap media-hero-footer"><span>PEOPLE <b>·</b> PERSPECTIVES <b>·</b> CONNECTIONS</span><span>SCROLL TO HEAR THEIR STORIES <i aria-hidden="true">↓</i></span></div></section>'''

    def participant_cards():
        cards=[]
        for index,key in enumerate(['manas-aravind','muhammed-ansil-pa','anirudh-vk','vaishnav-pm','adheena']):
            x=proof[key]
            visual=media_poster(key,x['title'],u)
            cards.append(f'''<article class="voice-story reveal"><button type="button" class="voice-story-visual" data-video="{E(x['original_video_url'])}" data-title="{E(x['title'])}" data-source="{u('testimonials/index.html#participant-voices')}" data-source-label="View testimonials ↗" aria-label="Play {E(x['title'])} testimonial">{visual}<span class="voice-play" aria-hidden="true">▶</span><span class="voice-story-watch">WATCH THEIR STORY <i aria-hidden="true">↗</i></span></button><div class="voice-story-info"><span class="voice-story-number">0{index+1}</span><div><p>PARTICIPANT PERSPECTIVE</p><h3>{E(x['title'])}</h3></div><a href="{E(x['original_video_url'])}" target="_blank" rel="noopener" aria-label="Open {E(x['title'])}'s recording">↗</a></div></article>''')
        return '<div class="voice-story-grid">'+''.join(cards)+'</div>'

    old_testimonials=ns['testimonials']
    def testimonials():
        out=old_testimonials()
        out=out[out.index('</section>')+10:]
        out=out.replace('<section class="section light" id="participant-voices">','<section class="section voices-editorial" id="participant-voices">',1)
        start=out.index('<div class="proof-grid students">')
        end=out.index('</section>',start)
        out=out[:start]+participant_cards()+'</div>'+out[end:]
        out=out.replace('Meet the people<br>behind the feedback.','A face. A voice.<br><span class="accent">A personal perspective.</span>')
        out=out.replace('<section class="section feedback-section">','<section class="section feedback-section appreciation-editorial" id="written-appreciation">',1)
        out=out.replace('Feedback that<br>stays with us.','Appreciation.<br><span>In its original words.</span>')
        out=out.replace('<section class="section light" id="partners">','<section class="section light partner-editorial" id="partners">',1)
        out=out.replace('Connections that<br>expand perspectives.','Connected by possibility.<br><span>Our partner network.</span>')
        return '<div class="media-destination voices-destination">'+voices_hero()+chapter_nav([('participant-voices','Participant voices'),('written-appreciation','Written appreciation'),('partners','Our partner network')])+out+'</div>'
    ns['testimonials']=testimonials

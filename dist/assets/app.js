'use strict';
(() => {
  document.body.classList.add('js');
  const $ = (q, root=document) => root.querySelector(q);
  const $$ = (q, root=document) => [...root.querySelectorAll(q)];
  const motion = $('.motion-button');
  const motionQuick=$('.motion-quick');
  let paused=false;
  try { paused=localStorage.getItem('bluzee-motion')==='paused'; } catch (_) {}
  const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
  const setMotion=()=>{ document.body.classList.toggle('motion-paused',paused); document.documentElement.classList.toggle('motion-paused',paused); if(motion){motion.textContent=reduced.matches?'Reduced motion enabled':paused?'Resume motion':'Pause motion';motion.setAttribute('aria-pressed',String(paused||reduced.matches));motion.disabled=reduced.matches;} if(motionQuick){motionQuick.setAttribute('aria-pressed',String(paused||reduced.matches));motionQuick.setAttribute('aria-label',reduced.matches?'Reduced motion enabled':paused?'Resume animation':'Pause animation');motionQuick.disabled=reduced.matches;$('.motion-label',motionQuick).textContent=paused?'Resume motion':'Pause motion';$('span',motionQuick).textContent=paused?'▷':'Ⅱ';} document.dispatchEvent(new Event('bluzee:motion')); };
  setMotion(); reduced.addEventListener('change',setMotion);
  const toggleMotion=()=>{paused=!paused;setMotion();try{localStorage.setItem('bluzee-motion',paused?'paused':'active');}catch(_){} };
  motion?.addEventListener('click',toggleMotion);motionQuick?.addEventListener('click',toggleMotion);
  if('IntersectionObserver' in window){const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}}),{threshold:.07});$$('.reveal').forEach(e=>obs.observe(e));}else $$('.reveal').forEach(e=>e.classList.add('visible'));
  const menu=$('.menu-toggle'),nav=$('.site-nav'),offerings=$('.nav-offerings');
  const closeMenu=()=>{nav?.classList.remove('mobile-open');menu?.setAttribute('aria-expanded','false');if(offerings)offerings.open=false;};
  menu?.addEventListener('click',()=>{let open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('mobile-open',open);if(!open)offerings.open=false;});
  document.addEventListener('click',e=>{if(offerings&&!offerings.contains(e.target))offerings.open=false;if(nav&&menu&&!nav.contains(e.target)&&!menu.contains(e.target))closeMenu();});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('dialog[open]')){if(nav?.classList.contains('mobile-open')){closeMenu();menu.focus();}else if(offerings?.open){offerings.open=false;$('summary',offerings).focus();}}});
  $$('.site-nav a').forEach(a=>a.addEventListener('click',closeMenu));
  window.matchMedia('(max-width:800px)').addEventListener('change',closeMenu);
  $$('[data-tabs]').forEach(group=>{
    const tabs=$$('[role=tab]',group); const panels=$$('[role=tabpanel]',group);
    function choose(tab){tabs.forEach(t=>{const yes=t===tab;t.setAttribute('aria-selected',String(yes));t.tabIndex=yes?0:-1;});panels.forEach(p=>p.hidden=p.id!==tab.getAttribute('aria-controls'));}
    tabs.forEach((t,i)=>{t.addEventListener('click',()=>choose(t));t.addEventListener('keydown',e=>{let next;if(e.key==='ArrowRight')next=(i+1)%tabs.length;else if(e.key==='ArrowLeft')next=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')next=0;else if(e.key==='End')next=tabs.length-1;if(next!==undefined){e.preventDefault();choose(tabs[next]);tabs[next].focus();}});});
  });
  $$('[data-filter-list]').forEach(list=>{
    const controls=$$('[data-filter]',list),items=$$('[data-item]',list),search=$('[data-search-input]',list),count=$('.filters-count',list),empty=$('.empty-state',list);
    const requested=new URLSearchParams(location.search).get('category');let filter=controls.some(c=>c.dataset.filter===requested)?requested:'All';
    function update(){let n=0;const term=(search?.value||'').trim().toLowerCase();items.forEach(item=>{let yes=(filter==='All'||item.dataset.category.split(' ').includes(filter))&&item.dataset.search.includes(term);item.hidden=!yes;if(yes){n++;item.classList.add('visible');}});controls.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.filter===filter)));count.textContent=`${n} ${n===1?'result':'results'}`;empty.style.display=n?'none':'block';}
    controls.forEach(c=>c.addEventListener('click',()=>{filter=c.dataset.filter;update();}));search?.addEventListener('input',update);update();
  });
  const dialog=$('.video-dialog'), video=dialog?$('video',dialog):null;let trigger=null;
  $$('[data-video]').forEach(btn=>btn.addEventListener('click',()=>{trigger=btn;$('#video-title').textContent=btn.dataset.title;$('.original-source',dialog).href=btn.dataset.source;$('.direct-video',dialog).href=btn.dataset.video;$('.video-status',dialog).textContent='';video.src=btn.dataset.video;video.poster=$('img',btn)?.src||'';dialog.showModal();document.body.classList.add('modal-open');video.play().catch(()=>{$('.video-status',dialog).textContent='Press play to start the original recording.';});}));
  video?.addEventListener('error',()=>{$('.video-status',dialog).textContent='The original recording could not load here. Open the original page or recording using the links below.';});
  $('.dialog-close')?.addEventListener('click',()=>dialog.close());
  dialog?.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
  dialog?.addEventListener('close',()=>{video.pause();video.removeAttribute('src');video.load();document.body.classList.remove('modal-open');trigger?.focus();});
  const form=$('#enquiry-form');
  if(form){const selected=new URLSearchParams(location.search).get('offering');const match=[...form.offering.options].find(o=>o.value.replaceAll('™','')===(selected||'').replaceAll('™',''));if(match)form.offering.value=match.value;let draft='';
    const recipient=()=>/DealTailor|Dimaq|AI Products/i.test(form.offering.value)?'ai@bluzee.xyz':'inbox@bluzee.xyz';
    const updateRecipient=()=>{const target=recipient();$('.recipient-note').innerHTML=(target==='ai@bluzee.xyz'?'AI product enquiries: ':'General enquiries: ')+'<strong>'+target+'</strong>'+(target==='ai@bluzee.xyz'?' · copy to inbox@bluzee.xyz':'');$('.draft-output').hidden=true;};
    form.offering.addEventListener('change',updateRecipient);updateRecipient();
    form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const f=new FormData(form);const subject='Bluzee enquiry: '+f.get('offering');draft=`Hello Bluzee,\n\nI would like to discuss ${f.get('offering')}.\n\n${String(f.get('message')).trim()}\n\nName: ${String(f.get('name')).trim()}\nEmail: ${String(f.get('email')).trim()}\nOrganisation: ${String(f.get('organisation')).trim()||'Not specified'}`;$('.draft-text').textContent=draft;const target=recipient();$('.draft-link').href='mailto:'+target+'?'+(target==='ai@bluzee.xyz'?'cc=inbox%40bluzee.xyz&':'')+'subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(draft);$('.draft-recipient').textContent='To: '+target+(target==='ai@bluzee.xyz'?' · Copy: inbox@bluzee.xyz':'');$('.draft-output').hidden=false;$('.copy-status').textContent='';$('.draft-output').scrollIntoView({behavior:reduced.matches||paused?'instant':'smooth',block:'center'});});
    $('.copy-draft').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(draft);$('.copy-status').textContent='Message copied. Paste it into your email app.';}catch(_){$('.copy-status').textContent='Please select and copy the message above.';}});
  }
})();
/* Motion layer: event-driven, offscreen-aware and removable by the visitor. */
(() => {
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const fine=matchMedia('(hover:hover) and (pointer:fine)');
  const allowed=()=>!reduced.matches&&!document.body.classList.contains('motion-paused')&&!document.hidden;
  const animated=[...document.querySelectorAll('.home-hero,.capability-marquee,.ocean-art,.mission-emblem,.detail-art')];
  if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(e=>e.target.classList.toggle('offstage',!e.isIntersecting)),{rootMargin:'80px'});animated.forEach(e=>observer.observe(e));}
  document.addEventListener('visibilitychange',()=>document.body.classList.toggle('tab-hidden',document.hidden));
  let scrollFrame=0;
  const progress=()=>{scrollFrame=0;const max=document.documentElement.scrollHeight-innerHeight;document.documentElement.style.setProperty('--read-progress',max?Math.min(1,scrollY/max):0);document.querySelector('.site-header')?.classList.toggle('scrolled',scrollY>30);};
  window.addEventListener('scroll',()=>{if(!scrollFrame)scrollFrame=requestAnimationFrame(progress);},{passive:true});progress();
  const hero=document.querySelector('.home-hero');
  if(hero){let frame=0;hero.addEventListener('pointermove',event=>{if(!allowed()||!fine.matches||frame)return;const x=event.clientX,y=event.clientY;frame=requestAnimationFrame(()=>{frame=0;const r=hero.getBoundingClientRect();hero.style.setProperty('--hero-x',((x-r.left)/r.width-.5)*18+'px');hero.style.setProperty('--hero-y',((y-r.top)/r.height-.5)*12+'px');});},{passive:true});hero.addEventListener('pointerleave',()=>{hero.style.setProperty('--hero-x','0px');hero.style.setProperty('--hero-y','0px');});}
  document.querySelectorAll('.product-panel,[data-tilt]').forEach(card=>{let frame=0;card.addEventListener('pointermove',event=>{if(!allowed()||!fine.matches||frame)return;const x=event.clientX,y=event.clientY;frame=requestAnimationFrame(()=>{frame=0;const r=card.getBoundingClientRect(),px=(x-r.left)/r.width,py=(y-r.top)/r.height;card.style.setProperty('--pointer-x',px*100+'%');card.style.setProperty('--pointer-y',py*100+'%');card.style.setProperty('--portrait-x',(px-.5)*5+'px');card.style.setProperty('--portrait-y',(py-.5)*5+'px');});},{passive:true});});
  document.querySelectorAll('.stagger,.product-grid,.feature-list,.journey-grid').forEach(group=>[...group.children].forEach((el,i)=>el.style.setProperty('--i',i%4)));
})();
/* Fine-pointer depth: visual-only, bounded and responsive to motion preferences. */
(() => {
  const reduced=matchMedia('(prefers-reduced-motion: reduce)'), fine=matchMedia('(hover:hover) and (pointer:fine)');
  const cards=[...document.querySelectorAll('[data-depth]')];
  const enabled=()=>!reduced.matches&&fine.matches&&!document.body.classList.contains('motion-paused')&&!document.hidden;
  const reset=card=>['--depth-rx','--depth-ry','--depth-x','--depth-y','--depth-px','--depth-py'].forEach(p=>card.style.removeProperty(p));
  cards.forEach(card=>{
    let frame=0;
    card.addEventListener('pointermove',e=>{
      if(!enabled()||frame)return;
      const x=e.clientX,y=e.clientY;
      frame=requestAnimationFrame(()=>{frame=0;if(!enabled()){reset(card);return;}const r=card.getBoundingClientRect(),px=(x-r.left)/r.width,py=(y-r.top)/r.height;
        card.style.setProperty('--depth-rx',(0.5-py)*9+'deg');card.style.setProperty('--depth-ry',(px-.5)*11+'deg');
        card.style.setProperty('--depth-x',(px-.5)*16+'px');card.style.setProperty('--depth-y',(py-.5)*12+'px');
        card.style.setProperty('--depth-px',px*100+'%');card.style.setProperty('--depth-py',py*100+'%');
      });
    },{passive:true});
    card.addEventListener('pointerleave',()=>{if(frame){cancelAnimationFrame(frame);frame=0;}reset(card);});
  });
  const clear=()=>cards.forEach(reset);
  reduced.addEventListener('change',clear);fine.addEventListener('change',clear);document.addEventListener('bluzee:motion',clear);document.addEventListener('visibilitychange',()=>{if(document.hidden)clear();});
  if('IntersectionObserver'in window){const io=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('offstage',!e.isIntersecting)),{rootMargin:'80px'});document.querySelectorAll('.guide-visual,.archive-hero').forEach(e=>io.observe(e));}
})();

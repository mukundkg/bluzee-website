'use strict';
(() => {
  const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
  const root=document.documentElement, reduced=matchMedia('(prefers-reduced-motion: reduce)'), fine=matchMedia('(hover:hover) and (pointer:fine)');
  const enabled=()=>!reduced.matches&&!document.body.classList.contains('motion-paused')&&!document.hidden;
  const interactive=()=>enabled()&&fine.matches;
  const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
  root.classList.add('v9-js');
  if(enabled()){root.classList.add('v9-arriving');setTimeout(()=>root.classList.remove('v9-arriving'),1000);}
  const active=new Set(), landscapes=$$('[data-v9-landscape],[data-v8-scene]');
  let scrollFrame=0;
  const home=$('.v9-home-hero'), stage=$('.v9-hero-stage');
  function scrollUpdate(){scrollFrame=0;if(!enabled())return;
    for(const el of active){const r=el.getBoundingClientRect();const p=clamp((innerHeight*.5-r.top-r.height*.5)/(innerHeight+r.height),-.5,.5);el.style.setProperty('--v9-scroll',(p*(fine.matches?120:25)).toFixed(2)+'px');}
    if(home){const r=home.getBoundingClientRect();home.style.setProperty('--hero-progress',clamp((88-r.top)/Math.max(1,r.height*.65),0,1).toFixed(3));}
  }
  const requestScroll=()=>{if(!scrollFrame&&enabled())scrollFrame=requestAnimationFrame(scrollUpdate);};
  if('IntersectionObserver' in window){
    const observer=new IntersectionObserver(es=>{es.forEach(e=>{e.target.classList.toggle('v9-offstage',!e.isIntersecting);if(e.isIntersecting)active.add(e.target);else active.delete(e.target);});requestScroll();},{rootMargin:'100px'});
    landscapes.forEach(el=>observer.observe(el));
    const reveal=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');reveal.unobserve(e.target);}}),{threshold:.1});
    $$('.v8-reveal').forEach(el=>reveal.observe(el));
  }else{landscapes.forEach(el=>active.add(el));$$('.v8-reveal').forEach(el=>el.classList.add('visible'));}
  addEventListener('scroll',requestScroll,{passive:true});addEventListener('resize',requestScroll,{passive:true});requestScroll();
  landscapes.forEach(el=>{let frame=0;el.addEventListener('pointermove',e=>{if(!interactive()||frame)return;const x=e.clientX,y=e.clientY;frame=requestAnimationFrame(()=>{frame=0;if(!interactive())return;const r=el.getBoundingClientRect(),px=(x-r.left)/r.width-.5,py=(y-r.top)/r.height-.5;el.style.setProperty('--v9-x',(px*-30).toFixed(2)+'px');el.style.setProperty('--v9-y',(py*-18).toFixed(2)+'px');el.style.setProperty('--landscape-x',(px*-24).toFixed(2)+'px');el.style.setProperty('--landscape-y',(py*-15).toFixed(2)+'px');el.style.setProperty('--tilt-x',(-py*15).toFixed(2)+'deg');el.style.setProperty('--tilt-y',(px*18).toFixed(2)+'deg');});},{passive:true});el.addEventListener('pointerleave',()=>['--v9-x','--v9-y','--landscape-x','--landscape-y','--tilt-x','--tilt-y'].forEach(p=>el.style.removeProperty(p)));});

  /* Deliberate visual choices work with pointer, touch and keyboard. */
  let currentHero='arrival';
  const heroChoices=$$('[data-hero-choice]');
  function chooseHero(button){const key=button.dataset.heroChoice;if(key===currentHero)return;currentHero=key;heroChoices.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));$$('[data-hero-image]').forEach(e=>e.classList.toggle('selected',e.dataset.heroImage===key));prepareLens();}
  heroChoices.forEach(b=>{b.addEventListener('click',()=>chooseHero(b));let timer;b.addEventListener('pointerenter',()=>{if(interactive())timer=setTimeout(()=>chooseHero(b),120);});b.addEventListener('pointerleave',()=>clearTimeout(timer));b.addEventListener('focus',()=>chooseHero(b));});
  let aiMode=0;
  const aiButtons=$$('[data-ai-choice]');
  function chooseAI(button){const key=button.dataset.aiChoice;aiMode=key==='dimaq'?1:0;aiButtons.forEach(b=>{const yes=b===button;b.setAttribute('aria-selected',String(yes));b.tabIndex=yes?0:-1;});$$('.v9-ai-panel').forEach(p=>p.hidden=p.id!==button.getAttribute('aria-controls'));$$('[data-ai-image]').forEach(e=>e.classList.toggle('selected',e.dataset.aiImage===key));const words=aiMode?['AUTHORISED DATA','BUSINESS CONTEXT','INFORMED ACTION']:['ENQUIRY','UNDERSTANDING','NEXT ACTION'];$$('.v9-network-label').forEach((el,i)=>el.textContent=words[i]);wakeNetwork();}
  function tabKeyboard(buttons,activate){buttons.forEach((b,i)=>b.addEventListener('keydown',e=>{let next;if(e.key==='ArrowRight'||e.key==='ArrowDown')next=(i+1)%buttons.length;else if(e.key==='ArrowLeft'||e.key==='ArrowUp')next=(i+buttons.length-1)%buttons.length;else if(e.key==='Home')next=0;else if(e.key==='End')next=buttons.length-1;if(next!==undefined){e.preventDefault();activate(buttons[next]);buttons[next].focus();}}));}
  aiButtons.forEach(b=>{b.addEventListener('click',()=>chooseAI(b));let timer;b.addEventListener('pointerenter',()=>{if(interactive())timer=setTimeout(()=>chooseAI(b),160);});b.addEventListener('pointerleave',()=>clearTimeout(timer));});tabKeyboard(aiButtons,chooseAI);
  $$('[data-erp-focus]').forEach(a=>{const select=()=>{const erp=a.closest('.v9-erp');if(!erp)return;erp.style.setProperty('--erp-focus',a.dataset.erpFocus);$('.v9-erp-position p',erp).textContent=a.dataset.erpLabel;};a.addEventListener('pointerenter',select);a.addEventListener('focus',select);});

  /* The guide uses real source pages. The cover is a visual preview wrapper. */
  const folio=$('.v9-folio'),cover=$('.v9-folio-cover'),closeFolio=$('.v9-close-folio'),guideButtons=$$('[data-guide-page]');
  function setFolio(open,returnFocus=false){if(!folio)return;folio.classList.toggle('open',open);cover.setAttribute('aria-expanded',String(open));cover.tabIndex=open?-1:0;closeFolio.hidden=!open;const pageLink=$('.v9-folio-page');pageLink.tabIndex=open?0:-1;pageLink.setAttribute('aria-hidden',String(!open));if(returnFocus)cover.focus();}
  function chooseGuide(button){const page=button.dataset.guidePage;guideButtons.forEach(b=>{const yes=b===button;b.setAttribute('aria-selected',String(yes));b.tabIndex=yes?0:-1;});$$('.v9-guide-topic [role=tabpanel]').forEach(p=>p.hidden=p.id!==button.getAttribute('aria-controls'));$$('[data-guide-image]').forEach(im=>im.hidden=im.dataset.guideImage!==page);const pageLink=$('.v9-folio-page');pageLink.href=pageLink.href.split('#')[0]+'#page='+Number(page);pageLink.setAttribute('aria-label','Read original ERP guide page '+Number(page));setFolio(true);}
  guideButtons.forEach(b=>b.addEventListener('click',()=>chooseGuide(b)));tabKeyboard(guideButtons,chooseGuide);
  setFolio(false);
  cover?.addEventListener('click',()=>{setFolio(true);closeFolio.focus();});closeFolio?.addEventListener('click',()=>setFolio(false,true));
  $('.v9-folio-stage')?.addEventListener('keydown',e=>{if(e.key==='Escape'&&folio?.classList.contains('open')){e.preventDefault();setFolio(false,true);}});
  $$('[data-v9-tilt]').forEach(el=>{let frame=0;el.addEventListener('pointermove',e=>{if(!interactive()||frame)return;const x=e.clientX,y=e.clientY;frame=requestAnimationFrame(()=>{frame=0;const r=el.getBoundingClientRect();el.style.setProperty('--folio-x',((.5-(y-r.top)/r.height)*18).toFixed(2)+'deg');el.style.setProperty('--folio-y',(((x-r.left)/r.width-.5)*22).toFixed(2)+'deg');});},{passive:true});el.addEventListener('pointerleave',()=>{el.style.removeProperty('--folio-x');el.style.removeProperty('--folio-y');});});

  /* Optical refraction: a small, pointer-local 2D treatment, no WebGL dependency. */
  const lens=$('.v9-water-lens'),lensContext=lens?.getContext('2d',{alpha:true}),lensBuffer=document.createElement('canvas'),bufferContext=lensBuffer.getContext('2d');
  let lensWidth=0,lensHeight=0,lensX=0,lensY=0,lensTargetX=0,lensTargetY=0,lensActive=false,lensFrame=0,lensReady=false,lastLens=0;
  function prepareLens(){if(!lens||!stage||!lensContext||!bufferContext)return;lensReady=false;const img=$('.v9-hero-scene.selected img');if(!img)return;const draw=()=>{if(!img.complete||!img.naturalWidth)return;const r=stage.getBoundingClientRect();lensWidth=Math.round(r.width);lensHeight=Math.round(r.height);lens.width=lensBuffer.width=lensWidth;lens.height=lensBuffer.height=lensHeight;const scale=Math.max(lensWidth/img.naturalWidth,lensHeight/img.naturalHeight)*1.035;const w=img.naturalWidth*scale,h=img.naturalHeight*scale;bufferContext.clearRect(0,0,lensWidth,lensHeight);bufferContext.drawImage(img,(lensWidth-w)*.8,(lensHeight-h)/2,w,h);lensReady=true;};if(img.complete)draw();else img.addEventListener('load',draw,{once:true});}
  function drawLens(time){lensFrame=0;if(!lensActive||!interactive()||!lensReady||!active.has(home))return;if(time-lastLens<32){lensFrame=requestAnimationFrame(drawLens);return;}lastLens=time;lensX+=(lensTargetX-lensX)*.15;lensY+=(lensTargetY-lensY)*.15;const c=lensContext,radius=Math.min(200,lensWidth*.16);c.clearRect(0,0,lensWidth,lensHeight);c.save();c.beginPath();c.arc(lensX,lensY,radius,0,Math.PI*2);c.clip();for(let y=Math.max(0,Math.floor(lensY-radius));y<Math.min(lensHeight,lensY+radius);y+=8){const offset=Math.sin((y-lensY)*.045-time*.0027)*5+Math.sin(y*.014+time*.0014)*3;c.drawImage(lensBuffer,0,y,lensWidth,Math.min(8,lensHeight-y),offset,y,lensWidth,Math.min(8,lensHeight-y));}c.globalCompositeOperation='destination-in';const gradient=c.createRadialGradient(lensX,lensY,radius*.2,lensX,lensY,radius);gradient.addColorStop(0,'#fff');gradient.addColorStop(.65,'#ffffffb0');gradient.addColorStop(1,'#ffffff00');c.fillStyle=gradient;c.fillRect(0,0,lensWidth,lensHeight);c.restore();lensFrame=requestAnimationFrame(drawLens);}
  if(stage&&lensContext){prepareLens();stage.addEventListener('pointermove',e=>{if(!interactive())return;const r=stage.getBoundingClientRect();lensTargetX=e.clientX-r.left;lensTargetY=e.clientY-r.top;if(!lensActive){lensX=lensTargetX;lensY=lensTargetY;}lensActive=true;lens.classList.add('engaged');if(!lensFrame)lensFrame=requestAnimationFrame(drawLens);},{passive:true});stage.addEventListener('pointerleave',()=>{lensActive=false;lens.classList.remove('engaged');});addEventListener('resize',prepareLens,{passive:true});}

  /* A rotating, morphing data sculpture. Each AI product has a distinct topology. */
  const network=$('.v9-morph-network'),nc=network?.getContext('2d',{alpha:true});
  let networkFrame=0,networkVisible=false,lastNetwork=0,morph=0,netW=0,netH=0,netPointerX=0,netPointerY=0;
  const points=Array.from({length:84},(_,i)=>{const a=(i%28)/28*Math.PI*2,ring=Math.floor(i/28)-1;return {ring:[Math.cos(a)*(135+ring*20),Math.sin(a)*(135+ring*20),ring*70],grid:[((i%7)-3)*45,(Math.floor(i/7)%4-1.5)*65,(Math.floor(i/28)-1)*90]};});
  function sizeNetwork(){if(!network||!nc)return;const r=network.getBoundingClientRect();netW=r.width;netH=r.height;const d=Math.min(devicePixelRatio||1,1.5);network.width=Math.round(netW*d);network.height=Math.round(netH*d);nc.setTransform(d,0,0,d,0,0);}
  function drawNetwork(time,still=false){networkFrame=0;if(!nc||!networkVisible)return;if(!still&&!enabled())return;if(!still&&time-lastNetwork<33){networkFrame=requestAnimationFrame(drawNetwork);return;}lastNetwork=time;morph+=(aiMode-morph)*.065;if(still)morph=aiMode;const t=still?0:time*.00016,ry=t+netPointerX*.6,rx=.3+netPointerY*.35,scale=Math.min(netW/420,netH/410);nc.clearRect(0,0,netW,netH);const projected=points.map((p,i)=>{let [x,y,z]=p.ring.map((v,j)=>v*(1-morph)+p.grid[j]*morph);const nx=x*Math.cos(ry)+z*Math.sin(ry),nz=-x*Math.sin(ry)+z*Math.cos(ry);const ny=y*Math.cos(rx)-nz*Math.sin(rx),zz=y*Math.sin(rx)+nz*Math.cos(rx),perspective=520/(520+zz);return {x:netW*.5+nx*scale*perspective,y:netH*.47+ny*scale*perspective,z:zz,i};});
    for(let i=0;i<projected.length;i++){const a=projected[i];for(let j=i+1;j<projected.length;j++){const b=projected[j],d=Math.hypot(a.x-b.x,a.y-b.y);if(d<62*scale&&Math.abs(a.z-b.z)<110){nc.strokeStyle='rgba(164,220,244,'+((1-d/(62*scale))*.28)+')';nc.lineWidth=.6;nc.beginPath();nc.moveTo(a.x,a.y);nc.lineTo(b.x,b.y);nc.stroke();}}}
    projected.sort((a,b)=>b.z-a.z).forEach(p=>{const pulse=.6+Math.sin((still?0:time*.002)+p.i*.47)*.4;nc.fillStyle=p.i%13===0?'rgba(234,164,146,.9)':'rgba(195,234,250,'+(.45+pulse*.45)+')';nc.shadowBlur=p.i%13===0?14:5;nc.shadowColor=p.i%13===0?'#d88c81':'#9dddf5';const size=(p.i%13===0?2.8:1.5)*scale;if(morph>.6)nc.fillRect(p.x-size,p.y-size,size*2,size*2);else{nc.beginPath();nc.arc(p.x,p.y,size,0,Math.PI*2);nc.fill();}});nc.shadowBlur=0;
    if(!still)networkFrame=requestAnimationFrame(drawNetwork);
  }
  function wakeNetwork(){if(!nc||!networkVisible)return;if(enabled()){if(!networkFrame)networkFrame=requestAnimationFrame(drawNetwork);}else drawNetwork(0,true);}
  if(network&&nc){sizeNetwork();if('IntersectionObserver'in window)new IntersectionObserver(es=>{networkVisible=es[0].isIntersecting;if(networkVisible)wakeNetwork();else if(networkFrame){cancelAnimationFrame(networkFrame);networkFrame=0;}},{threshold:.05}).observe(network);else{networkVisible=true;wakeNetwork();}network.closest('.v9-ai-stage')?.addEventListener('pointermove',e=>{if(!interactive())return;const r=network.getBoundingClientRect();netPointerX=clamp((e.clientX-r.left)/r.width-.5,-.8,.8);netPointerY=clamp((e.clientY-r.top)/r.height-.5,-.8,.8);},{passive:true});addEventListener('resize',()=>{sizeNetwork();wakeNetwork();},{passive:true});}

  /* Real human movement uses short, silent windows from the existing recordings. */
  const films=$$('[data-motion-film]').map(el=>{const video=$('video',el),toggle=$('.v9-film-toggle',el);let visible=false,manualPaused=false,requested=false;video.muted=true;
    const update=()=>{toggle.setAttribute('aria-pressed',String(!video.paused));toggle.textContent=video.paused?'Play silent preview ▷':'Pause silent preview Ⅱ';el.classList.toggle('is-playing',!video.paused);};
    const play=async(manual=false)=>{if(!visible||!manual&&!enabled()||manualPaused&&!manual)return;if(!manual&&(!fine.matches||innerWidth<800||navigator.connection?.saveData))return;if(!video.getAttribute('src')){video.src=video.dataset.previewSrc;video.load();}requested=true;try{await video.play();}catch(_){update();}};
    video.addEventListener('loadedmetadata',()=>{const start=Math.min(Number(video.dataset.loopStart)||0,Math.max(0,video.duration-4));if(Number.isFinite(start))video.currentTime=start;});
    video.addEventListener('timeupdate',()=>{const end=Math.min(Number(video.dataset.loopEnd)||26,video.duration);if(video.currentTime>=end-.08){video.currentTime=Math.min(Number(video.dataset.loopStart)||0,Math.max(0,end-4));}});
    video.addEventListener('ended',()=>{if(requested&&enabled()&&!manualPaused){video.currentTime=Math.min(Number(video.dataset.loopStart)||0,Math.max(0,video.duration-4));play();}});
    video.addEventListener('play',update);video.addEventListener('pause',update);video.addEventListener('error',()=>{requested=false;video.pause();toggle.textContent='Watch the original recording ↗';toggle.setAttribute('aria-pressed','false');el.classList.add('preview-unavailable');});
    toggle.addEventListener('click',()=>{if(el.classList.contains('preview-unavailable')){location.href=$('a',el).href;return;}if(video.paused){manualPaused=false;play(true);}else{manualPaused=true;video.pause();}});
    if('IntersectionObserver'in window)new IntersectionObserver(es=>{visible=es[0].isIntersecting;if(visible)play();else video.pause();},{threshold:.25}).observe(el);else visible=true;
    return {pause:()=>video.pause(),resume:()=>{if(visible)play();}};
  });

  /* Cursor echo keeps the native cursor and never covers a control. */
  const cursor=$('.v9-pointer-orbit');let cursorFrame=0,cx=-200,cy=-200,tx=-200,ty=-200;
  function followCursor(){cursorFrame=0;if(!interactive()||!cursor)return;cx+=(tx-cx)*.22;cy+=(ty-cy)*.22;cursor.style.transform=`translate3d(${cx-33}px,${cy-33}px,0)`;if(Math.abs(tx-cx)+Math.abs(ty-cy)>.3)cursorFrame=requestAnimationFrame(followCursor);}
  document.addEventListener('pointermove',e=>{if(!interactive()||!cursor)return;tx=e.clientX;ty=e.clientY;const scene=e.target.closest('[data-v9-landscape],.v8-cinema,.proof-visual,.offering-card');cursor.classList.toggle('visible',!!scene);const action=e.target.closest('a,button');cursor.classList.toggle('action',!!action);if(!cursorFrame)cursorFrame=requestAnimationFrame(followCursor);},{passive:true});document.addEventListener('pointerleave',()=>cursor?.classList.remove('visible'));
  /* A bounded curtain transition between local HTML pages; downloads stay direct. */
  let navigating=false;
  document.addEventListener('click',e=>{if(!enabled()||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||navigating)return;const a=e.target.closest('a[href]');if(!a||a.target&&a.target!=='_self'||a.hasAttribute('download'))return;let url;try{url=new URL(a.href,location.href);}catch(_){return;}if(url.origin!==location.origin||!url.pathname.endsWith('.html')&& !url.pathname.endsWith('/')||url.pathname===location.pathname)return;e.preventDefault();navigating=true;root.classList.remove('v9-arriving');root.classList.add('v9-leaving');setTimeout(()=>location.assign(url.href),520);});
  addEventListener('pageshow',()=>{navigating=false;root.classList.remove('v9-leaving');});
  function motionChanged(){if(!enabled()){lensActive=false;lens?.classList.remove('engaged');cursor?.classList.remove('visible');if(lensFrame){cancelAnimationFrame(lensFrame);lensFrame=0;}if(networkFrame){cancelAnimationFrame(networkFrame);networkFrame=0;}landscapes.forEach(el=>['--v9-x','--v9-y','--v9-scroll','--landscape-x','--landscape-y'].forEach(p=>el.style.removeProperty(p)));films.forEach(f=>f.pause());root.classList.remove('v9-arriving');}else{requestScroll();films.forEach(f=>f.resume());}wakeNetwork();}
  reduced.addEventListener('change',motionChanged);fine.addEventListener('change',motionChanged);document.addEventListener('bluzee:motion',motionChanged);document.addEventListener('visibilitychange',motionChanged);
})();

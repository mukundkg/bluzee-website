'use strict';
(() => {
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const fine=matchMedia('(hover:hover) and (pointer:fine)');
  const allowed=()=>!reduced.matches&&!document.body.classList.contains('motion-paused')&&!document.hidden;
  const clamp=(n,a,b)=>Math.max(a,Math.min(b,n));
  // Independent, shape-morphing layers keep photograph subjects undistorted.
  const flowHosts=[...document.querySelectorAll('.v8-cinema:not(.v10-cta),.v9-hero-stage,.v9-ai-stage,.v9-guide,.v10-card-media')];
  flowHosts.forEach((el,i)=>{
    el.classList.add('v10-flow-host');el.style.setProperty('--flow-delay',(-i*2.7)+'s');
    const layer=document.createElement('div');layer.className='v10-flow-layer';layer.setAttribute('aria-hidden','true');
    for(let n=0;n<3;n++)layer.appendChild(document.createElement('i'));
    el.appendChild(layer);
  });
  const visualFrames=[...document.querySelectorAll('.v10-card-media,.proof-visual,.leader-card,.event-gallery>a,.voice-story,.split-panel')];
  visualFrames.forEach((el,i)=>{el.classList.add('v10-visual-frame');el.style.setProperty('--frame-delay',((i%3)*.11)+'s');});
  if('IntersectionObserver'in window){
    const reveal=new IntersectionObserver(entries=>{for(const e of entries){e.target.classList.toggle('v10-visual-in',e.isIntersecting);e.target.classList.toggle('v10-visual-rest',!e.isIntersecting);}},{threshold:.08,rootMargin:'0px 0px 35px'});
    [...flowHosts,...visualFrames].forEach(el=>reveal.observe(el));
  }else visualFrames.forEach(el=>el.classList.add('v10-visual-in'));
  const scenes=[...document.querySelectorAll('[data-v10-light]')];
  const live=new Set();let frame=0;
  const phase=new WeakMap();
  function update(){
    frame=0;if(!allowed())return;let moving=false;
    for(const el of live){
      const r=el.getBoundingClientRect(),target=clamp((innerHeight-r.top)/(innerHeight+r.height),0,1);
      let p=phase.get(el)??target;p+=(target-p)*.16;phase.set(el,p);
      const range=innerWidth<700?35:125;
      el.style.setProperty('--ruby-y',((p-.5)*range*2).toFixed(2)+'px');
      el.style.setProperty('--ruby-roll',((p-.5)*410).toFixed(2)+'deg');
      el.style.setProperty('--ruby-side',(Math.sin(p*Math.PI*2)*20).toFixed(2)+'px');
      if(Math.abs(target-p)>.001)moving=true;
    }
    if(moving)frame=requestAnimationFrame(update);
  }
  function wake(){if(!frame&&allowed())frame=requestAnimationFrame(update);}
  const animated=[...document.querySelectorAll('[data-v10-light],.v10-offering-hero,.v10-cta,.v10-notes-orbits,.v10-flow-host')];
  if('IntersectionObserver'in window){
    const observer=new IntersectionObserver(entries=>{for(const e of entries){e.target.classList.toggle('v10-offscreen',!e.isIntersecting);if(e.target.matches('[data-v10-light]')){if(e.isIntersecting)live.add(e.target);else live.delete(e.target);}}wake();},{rootMargin:'80px'});
    animated.forEach(el=>observer.observe(el));
  }else scenes.forEach(el=>live.add(el));
  addEventListener('scroll',wake,{passive:true});addEventListener('resize',wake,{passive:true});wake();
  document.querySelectorAll('[data-card-motion],.v10-flow-host,.v10-visual-frame').forEach(el=>{
    let pending=0;
    el.addEventListener('pointermove',e=>{
      if(!allowed()||!fine.matches||pending)return;const x=e.clientX,y=e.clientY;
      pending=requestAnimationFrame(()=>{pending=0;if(!allowed())return;const r=el.getBoundingClientRect(),px=(x-r.left)/r.width-.5,py=(y-r.top)/r.height-.5;
        el.style.setProperty('--card-x',(px*-14).toFixed(2)+'px');el.style.setProperty('--card-y',(py*-10).toFixed(2)+'px');
        el.style.setProperty('--motion-x',(px*20).toFixed(2)+'px');el.style.setProperty('--motion-y',(py*12).toFixed(2)+'px');
        el.style.setProperty('--visual-rx',(py*-3).toFixed(2)+'deg');el.style.setProperty('--visual-ry',(px*4).toFixed(2)+'deg');
      });
    },{passive:true});
    el.addEventListener('pointerleave',()=>['--card-x','--card-y','--motion-x','--motion-y','--visual-rx','--visual-ry'].forEach(p=>el.style.removeProperty(p)));
  });
  function preference(){if(!allowed()){if(frame)cancelAnimationFrame(frame);frame=0;}else wake();}
  reduced.addEventListener('change',preference);document.addEventListener('bluzee:motion',preference);document.addEventListener('visibilitychange',preference);
})();

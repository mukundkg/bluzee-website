'use strict';
(()=>{
 const root=document.documentElement;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const fine=matchMedia('(hover:hover) and (pointer:fine)');
 const scenes=[...document.querySelectorAll('[data-v8-scene]')];
 const active=new Set();
 let frame=0;
 const allowed=()=>!reduced.matches&&!document.body.classList.contains('motion-paused')&&!document.hidden;
 const update=()=>{
  frame=0;
  if(!allowed())return;
  for(const el of active){
   const r=el.getBoundingClientRect();
   const amount=Math.max(-1,Math.min(1,(innerHeight*.5-(r.top+r.height*.5))/(innerHeight+r.height)*2));
   el.style.setProperty('--scene-y',(amount*(fine.matches?35:13)).toFixed(2)+'px');
  }
 };
 const request=()=>{if(!frame&&allowed())frame=requestAnimationFrame(update);};
 if('IntersectionObserver' in window){
  const sceneObserver=new IntersectionObserver(entries=>{for(const e of entries){e.target.classList.toggle('v8-offstage',!e.isIntersecting);if(e.isIntersecting)active.add(e.target);else active.delete(e.target);}request();},{rootMargin:'80px'});
  scenes.forEach(el=>sceneObserver.observe(el));
  root.classList.add('v8-js');
  const reveal=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');reveal.unobserve(e.target);}}),{threshold:.12});
  document.querySelectorAll('.v8-reveal').forEach(el=>reveal.observe(el));
 }else{scenes.forEach(el=>active.add(el));}
 addEventListener('scroll',request,{passive:true});addEventListener('resize',request,{passive:true});
 scenes.forEach(el=>{
  let pointerFrame=0;
  el.addEventListener('pointermove',e=>{
   if(!allowed()||!fine.matches||pointerFrame)return;
   const x=e.clientX,y=e.clientY;
   pointerFrame=requestAnimationFrame(()=>{pointerFrame=0;if(!allowed())return;const r=el.getBoundingClientRect();const px=(x-r.left)/r.width,py=(y-r.top)/r.height;el.style.setProperty('--scene-x',((px-.5)*13).toFixed(2)+'px');el.style.setProperty('--pointer-x',(px*100).toFixed(1)+'%');el.style.setProperty('--pointer-y',(py*100).toFixed(1)+'%');});
  },{passive:true});
  el.addEventListener('pointerleave',()=>el.style.setProperty('--scene-x','0px'));
 });
 document.querySelectorAll('[data-v8-depth]').forEach(el=>{
  let tick=0;
  el.addEventListener('pointermove',e=>{if(!allowed()||!fine.matches||tick)return;const x=e.clientX,y=e.clientY;tick=requestAnimationFrame(()=>{tick=0;if(!allowed())return;const r=el.getBoundingClientRect();el.style.setProperty('--book-x',((x-r.left)/r.width-.5)*22+'deg');el.style.setProperty('--book-y',(.5-(y-r.top)/r.height)*15+'deg');});},{passive:true});
  el.addEventListener('pointerleave',()=>{el.style.setProperty('--book-x','0deg');el.style.setProperty('--book-y','0deg');});
 });
 const reset=()=>{if(!allowed()){scenes.forEach(el=>{el.style.removeProperty('--scene-x');el.style.removeProperty('--scene-y');});}else request();};
 reduced.addEventListener('change',reset);document.addEventListener('bluzee:motion',reset);document.addEventListener('visibilitychange',reset);request();
})();

/* Event-driven depth; imagery animates without moving text or rotating stories. */
(() => {
  const scenes=[...document.querySelectorAll('[data-media-motion]')];
  if(!scenes.length)return;
  const reduced=matchMedia('(prefers-reduced-motion:reduce)'),fine=matchMedia('(hover:hover) and (pointer:fine)');
  const allowed=()=>!reduced.matches&&fine.matches&&!document.hidden&&!document.body.classList.contains('motion-paused');
  scenes.forEach(scene=>{
    let frame=0;
    const reset=()=>{if(frame)cancelAnimationFrame(frame);frame=0;scene.style.removeProperty('--media-x');scene.style.removeProperty('--media-y');};
    scene.addEventListener('pointermove',e=>{
      if(!allowed()||frame)return;const x=e.clientX,y=e.clientY;
      frame=requestAnimationFrame(()=>{frame=0;if(!allowed())return reset();const r=scene.getBoundingClientRect();scene.style.setProperty('--media-x',((x-r.left)/r.width-.5)*16+'px');scene.style.setProperty('--media-y',((y-r.top)/r.height-.5)*12+'px');});
    },{passive:true});
    scene.addEventListener('pointerleave',reset);
    document.addEventListener('bluzee:motion',reset);document.addEventListener('visibilitychange',reset);reduced.addEventListener('change',reset);fine.addEventListener('change',reset);
  });
  if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('offstage',!e.isIntersecting)),{rootMargin:'50px'});scenes.forEach(s=>io.observe(s));}
})();

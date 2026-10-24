/* Visual-only motion. No scroll interception or automatic content switching. */
(() => {
  const root=document.querySelector('.purpose-cinematic');
  if(!root)return;
  const art=[...root.querySelectorAll('[data-purpose-art]')];
  const reduced=matchMedia('(prefers-reduced-motion:reduce)');
  const fine=matchMedia('(hover:hover) and (pointer:fine)');
  const enabled=()=>!reduced.matches&&fine.matches&&!document.hidden&&!document.body.classList.contains('motion-paused');
  if('IntersectionObserver' in window){
    root.classList.add('purpose-ready');
    const observer=new IntersectionObserver(entries=>entries.forEach(({target,isIntersecting})=>{
      target.classList.toggle('offstage',!isIntersecting);
      if(isIntersecting)target.classList.add('in-view');
    }),{threshold:.12});
    art.forEach(el=>observer.observe(el));
  }
  art.forEach(el=>{
    let frame=0;
    const reset=()=>{if(frame)cancelAnimationFrame(frame);frame=0;el.style.removeProperty('--purpose-x');el.style.removeProperty('--purpose-y');};
    el.addEventListener('pointermove',event=>{
      if(!enabled()||frame)return;
      const x=event.clientX,y=event.clientY;
      frame=requestAnimationFrame(()=>{
        frame=0;if(!enabled())return reset();
        const r=el.getBoundingClientRect();
        el.style.setProperty('--purpose-x',((x-r.left)/r.width-.5)*12+'px');
        el.style.setProperty('--purpose-y',((y-r.top)/r.height-.5)*10+'px');
      });
    },{passive:true});
    el.addEventListener('pointerleave',reset);
    document.addEventListener('bluzee:motion',reset);
    document.addEventListener('visibilitychange',reset);
    reduced.addEventListener('change',reset);fine.addEventListener('change',reset);
  });
})();

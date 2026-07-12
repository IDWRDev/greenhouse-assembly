const header=document.querySelector('[data-header]');
const menu=document.querySelector('.menu-toggle');
const nav=document.querySelector('nav');
addEventListener('scroll',()=>header.classList.toggle('scrolled',scrollY>24),{passive:true});
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',open)});
document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}));
const counters=document.querySelectorAll('[data-count]');
const observer=new IntersectionObserver(entries=>entries.forEach(({isIntersecting,target})=>{if(!isIntersecting||target.dataset.done)return;target.dataset.done='true';const end=+target.dataset.count,start=performance.now();const render=now=>{const p=Math.min((now-start)/1400,1);target.textContent=Math.floor(end*(1-Math.pow(1-p,3))).toLocaleString()+(target.dataset.suffix||'');if(p<1)requestAnimationFrame(render)};requestAnimationFrame(render)}),{threshold:.5});counters.forEach(c=>observer.observe(c));
document.querySelector('.newsletter form').addEventListener('submit',e=>{e.preventDefault();const b=e.currentTarget.querySelector('button');b.textContent='You’re on the list ✓';b.disabled=true});

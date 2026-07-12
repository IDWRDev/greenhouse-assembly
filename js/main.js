const toggle=document.querySelector('.menu-toggle'),links=document.querySelector('.nav-links');
toggle?.addEventListener('click',()=>{const open=links.classList.toggle('open');toggle.setAttribute('aria-expanded',open)});
links?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{links.classList.remove('open');toggle.setAttribute('aria-expanded','false')}));
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.13});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
document.querySelector('#year').textContent=new Date().getFullYear();
document.querySelector('form')?.addEventListener('submit',e=>{e.preventDefault();const button=e.currentTarget.querySelector('button');button.textContent='✓';button.setAttribute('aria-label','Subscribed')});

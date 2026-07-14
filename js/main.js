const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
const mobileBreakpoint = window.matchMedia('(max-width: 640px)');

function setMenuState(isOpen, { returnFocus = false } = {}) {
  if (!menuToggle || !navLinks) return;

  navLinks.classList.toggle('open', isOpen);
  document.body.classList.toggle('menu-is-open', isOpen);
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');

  if (!isOpen && returnFocus) menuToggle.focus();
}

menuToggle?.addEventListener('click', () => setMenuState(!navLinks?.classList.contains('open')));
navLinks?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenuState(false)));

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && navLinks?.classList.contains('open')) {
    setMenuState(false, { returnFocus: true });
  }
});

mobileBreakpoint.addEventListener('change', (event) => {
  if (!event.matches) setMenuState(false);
});

if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  }), { threshold: 0.13 });
  document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
} else {
  document.querySelectorAll('.reveal').forEach((element) => element.classList.add('visible'));
}

document.querySelector('#year').textContent = new Date().getFullYear();

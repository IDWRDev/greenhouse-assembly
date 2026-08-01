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

const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();

if (!window.__greenhouseOperationsLoading) {
  window.__greenhouseOperationsLoading = true;
  const operations = document.createElement('script');
  operations.src = 'js/site-operations.js';
  operations.defer = true;
  const config = document.createElement('script');
  config.src = 'js/site-config.js';
  config.onload = () => document.head.append(operations);
  document.head.append(config);
}

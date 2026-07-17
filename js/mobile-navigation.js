(() => {
  if (window.__greenhouseSmartHeaderInitialized) return;
  window.__greenhouseSmartHeaderInitialized = true;

  const nestedRoute = /\/(pages|documents)\//.test(window.location.pathname);
  const root = nestedRoute ? '../' : '';
  let header = document.querySelector('.site-header');
  if (!header) {
    if (!document.querySelector('link[href$="css/pages.css"]')) {
      const styles = document.createElement('link');
      styles.rel = 'stylesheet';
      styles.href = `${root}css/pages.css`;
      document.head.append(styles);
    }
    header = document.createElement('header');
    header.className = 'site-header';
    header.innerHTML = `<div class="nav-wrap"><a class="brand" href="${root}index.html"><img src="${root}assets/logos/navigation-mark.png" alt="The GreenHouse Assembly Ministries"><span>The GreenHouse<small>Assembly Ministries</small></span></a><nav class="site-nav" aria-label="Primary navigation"><a href="${root}index.html">Home</a><a href="${root}pages/about.html">About</a><a href="${root}pages/ministries.html">Ministries</a><a href="${root}pages/teaching.html">Teaching</a><a href="${root}pages/resources.html">Resources</a><a href="${root}pages/events.html">Events</a><a href="${root}pages/contact.html">Contact</a><a class="nav-give" href="${root}pages/donations.html">Give</a></nav></div>`;
    document.body.insertBefore(header, document.body.firstChild);
  }
  const nav = header.querySelector('.site-nav');

  const breadcrumb = document.querySelector('.breadcrumb');
  if (breadcrumb && !breadcrumb.closest('nav')) {
    const home = breadcrumb.querySelector('a');
    const current = breadcrumb.querySelector('[aria-current="page"]');
    if (home && current) {
      const trail = document.createElement('nav');
      trail.className = 'breadcrumb-nav';
      trail.setAttribute('aria-label', 'Breadcrumb');
      trail.innerHTML = `<ol class="breadcrumb-list"><li><a href="${home.getAttribute('href')}">${home.textContent}</a></li><li aria-current="page">${current.textContent}</li></ol>`;
      breadcrumb.replaceWith(trail);
    }
  }

  if (nav && !header.querySelector('.mobile-menu-toggle')) {
    const button = document.createElement('button');
    button.className = 'mobile-menu-toggle';
    button.type = 'button';
    button.setAttribute('aria-controls', 'mobile-navigation');
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', 'Open navigation');
    button.innerHTML = '<span aria-hidden="true">&#9776;</span>';
    nav.id = 'mobile-navigation';
    header.querySelector('.nav-wrap').insertBefore(button, nav);

    const close = (restoreFocus = false) => {
      nav.classList.remove('is-open');
      document.body.classList.remove('menu-is-open');
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', 'Open navigation');
      button.innerHTML = '<span aria-hidden="true">&#9776;</span>';
      if (restoreFocus) button.focus();
    };

    button.addEventListener('click', () => {
      const opening = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', opening);
      document.body.classList.toggle('menu-is-open', opening);
      button.setAttribute('aria-expanded', String(opening));
      button.setAttribute('aria-label', opening ? 'Close navigation' : 'Open navigation');
      button.innerHTML = `<span aria-hidden="true">${opening ? '&times;' : '&#9776;'}</span>`;
    });

    nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => close()));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) close(true);
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', (event) => {
      if (event.matches) close();
    });
  }

  const mobileViewport = window.matchMedia('(max-width: 900px)');
  const inactivityDelay = 3000;
  const hideGraceDelay = 120;
  let inactivityTimer;
  let lastScrollY = window.scrollY;
  let framePending = false;
  let headerHidden = header.classList.contains('is-hidden');
  let headerHiding = header.classList.contains('is-hiding');

  const menuIsOpen = () => {
    const toggle = header.querySelector('.mobile-menu-toggle, .menu-toggle');
    return toggle?.getAttribute('aria-expanded') === 'true'
      || header.querySelector('.site-nav.is-open, .nav-links.open') !== null;
  };

  const focusIsInHeader = () => header.contains(document.activeElement);

  const stopTimer = () => {
    window.clearTimeout(inactivityTimer);
    inactivityTimer = undefined;
  };

  const showHeader = () => {
    stopTimer();
    if (!headerHidden && !headerHiding) return;
    header.classList.remove('is-hidden', 'is-hiding');
    headerHidden = false;
    headerHiding = false;
  };

  const beginHide = () => {
    if (headerHidden || headerHiding) return;
    header.classList.add('is-hiding');
    headerHiding = true;
    inactivityTimer = window.setTimeout(() => {
      if (mobileViewport.matches && window.scrollY > 10 && !menuIsOpen() && !focusIsInHeader()) {
        header.classList.add('is-hidden');
        headerHidden = true;
      } else {
        showHeader();
      }
    }, hideGraceDelay);
  };

  const scheduleHide = () => {
    stopTimer();
    showHeader();
    if (!mobileViewport.matches || window.scrollY <= 10 || menuIsOpen() || focusIsInHeader()) return;
    inactivityTimer = window.setTimeout(() => {
      if (mobileViewport.matches && window.scrollY > 10 && !menuIsOpen() && !focusIsInHeader()) {
        beginHide();
      }
    }, inactivityDelay);
  };

  const reveal = () => scheduleHide();

  const handleScroll = () => {
    if (framePending) return;
    framePending = true;
    window.requestAnimationFrame(() => {
      const currentScrollY = window.scrollY;
      if (currentScrollY <= 10 || currentScrollY < lastScrollY) showHeader();
      lastScrollY = currentScrollY;
      scheduleHide();
      framePending = false;
    });
  };

  ['touchstart', 'pointerdown'].forEach((eventName) => {
    document.addEventListener(eventName, reveal, { passive: true });
  });
  ['pointermove', 'mousemove'].forEach((eventName) => {
    document.addEventListener(eventName, () => {
      if (framePending) return;
      framePending = true;
      window.requestAnimationFrame(() => {
        reveal();
        framePending = false;
      });
    }, { passive: true });
  });
  document.addEventListener('keydown', reveal);
  document.addEventListener('focusin', reveal);
  window.addEventListener('scroll', handleScroll, { passive: true });
  window.addEventListener('hashchange', reveal);
  window.addEventListener('pageshow', reveal);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) reveal();
  });
  mobileViewport.addEventListener('change', () => {
    showHeader();
    scheduleHide();
  });

  const menuStateObserver = new MutationObserver(() => {
    showHeader();
    if (menuIsOpen()) stopTimer();
    else scheduleHide();
  });
  header.querySelectorAll('.mobile-menu-toggle, .menu-toggle').forEach((toggle) => {
    menuStateObserver.observe(toggle, { attributes: true, attributeFilter: ['aria-expanded'] });
  });

  showHeader();
  scheduleHide();

  const loadOperations = () => {
    if (window.__greenhouseOperationsLoading) return;
    window.__greenhouseOperationsLoading = true;
    const operations = document.createElement('script');
    operations.src = `${root}js/site-operations.js`;
    operations.defer = true;
    const config = document.createElement('script');
    config.src = `${root}js/site-config.js`;
    config.onload = () => document.head.append(operations);
    document.head.append(config);
  };
  loadOperations();
})();

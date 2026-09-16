(() => {
  const config = window.GREENHOUSE_CONFIG || {};
  const validHttps = value => /^https:\/\/[^\s]+$/i.test(value || '');
  const validEmail = value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value || '');
  const setStatus = (element, message, state = '') => {
    if (!element) return;
    element.textContent = message;
    element.dataset.state = state;
  };

  const contactForm = document.querySelector('form.contact-form.form-grid');
  if (contactForm) {
    const status = contactForm.querySelector('#form-status');
    const button = contactForm.querySelector('button');
    const acknowledgement = contactForm.querySelector('input[type="checkbox"]')?.closest('.field');
    const endpointReady = validHttps(config.contactEndpoint);
    const emailReady = validEmail(config.contactEmail);
    const category = contactForm.querySelector('[name="category"]');
    const requestedCategory = new URLSearchParams(window.location.search).get('category');
    if (category && requestedCategory && [...category.options].some(option => option.value === requestedCategory)) {
      category.value = requestedCategory;
    }

    document.querySelectorAll('[data-category-link]').forEach(link => {
      link.addEventListener('click', () => {
        if (!category) return;
        const value = link.dataset.categoryLink;
        if ([...category.options].some(option => option.value === value)) category.value = value;
      });
    });

    if (endpointReady || emailReady) {
      acknowledgement?.remove();
      document.querySelector('.contact-notice')?.remove();
      button.type = 'submit';
      button.removeAttribute('aria-disabled');
      button.textContent = 'Send enquiry';
      setStatus(status, 'Required fields are marked.');

      contactForm.addEventListener('submit', async event => {
        event.preventDefault();
        if (!contactForm.reportValidity()) return;
        button.disabled = true;
        setStatus(status, 'Preparing your enquiry…', 'working');
        const data = new FormData(contactForm);

        if (endpointReady) {
          try {
            const response = await fetch(config.contactEndpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
            const result = await response.json().catch(() => ({}));
            if (!response.ok || result.success === false) throw new Error(result.message || 'Submission endpoint rejected the request.');
            contactForm.reset();
            setStatus(status, 'Thank you. Your enquiry has been sent.', 'success');
          } catch (error) {
            setStatus(status, 'Your enquiry could not be sent. Please try again later or use the published contact details.', 'error');
          } finally {
            button.disabled = false;
          }
          return;
        }

        const subject = encodeURIComponent(`[Website enquiry] ${data.get('category') || 'General enquiry'}`);
        const body = encodeURIComponent(`Name: ${data.get('name')}\nEmail: ${data.get('email')}\nPhone: ${data.get('phone') || 'Not provided'}\n\n${data.get('message')}`);
        window.location.href = `mailto:${config.contactEmail}?subject=${subject}&body=${body}`;
        setStatus(status, 'Your email application has been opened. Please review and send the prepared message.', 'success');
        button.disabled = false;
      });
    }
  }

  if (validHttps(config.givingUrl)) {
    document.querySelectorAll('[data-giving-link], .is-disabled.button-gold').forEach(link => {
      const replacement = document.createElement('a');
      replacement.className = link.className.replace('is-disabled', '').trim();
      replacement.href = config.givingUrl;
      replacement.rel = 'noopener';
      replacement.textContent = 'Give securely';
      replacement.dataset.givingLink = '';
      link.replaceWith(replacement);
    });
  }

  document.querySelectorAll('[data-config="address"]').forEach(node => {
    if (config.publicAddress) node.textContent = config.publicAddress;
  });
  document.querySelectorAll('[data-config="schedule"]').forEach(node => {
    if (config.gatheringSchedule) node.textContent = config.gatheringSchedule;
  });

  const social = config.social || {};
  document.querySelectorAll('.social-presence__item--listed').forEach(listed => {
    if (!validHttps(social.facebook) || listed.tagName === 'A') return;
    const facebook = document.createElement('a');
    facebook.className = listed.className.replace('social-presence__item--listed', '').trim();
    facebook.href = social.facebook;
    facebook.target = '_blank';
    facebook.rel = 'noopener noreferrer';
    facebook.setAttribute('aria-label', `${social.facebookName || 'Facebook'} (opens in a new tab)`);
    facebook.innerHTML = listed.innerHTML;
    listed.replaceWith(facebook);
  });
  document.querySelectorAll('.social-presence').forEach(grid => {
    if (!validHttps(social.youtube) || grid.querySelector(`[href="${social.youtube}"]`)) return;
    const youtube = document.createElement('a');
    youtube.className = 'social-presence__item';
    youtube.href = social.youtube;
    youtube.target = '_blank';
    youtube.rel = 'noopener noreferrer';
    youtube.innerHTML = `<span>YouTube</span><strong>${social.youtubeHandle || '@GreenHouseAssembly'}</strong>`;
    grid.append(youtube);
  });
  document.querySelectorAll('.footer-brand').forEach(brand => {
    if (brand.querySelector('.footer-socials')) return;
    const links = [
      ['Facebook', social.facebook, social.facebookName],
      ['Instagram', social.instagram, social.instagramHandle],
      ['TikTok', social.tiktok, social.tiktokHandle],
      ['YouTube', social.youtube, social.youtubeHandle],
      ['X', social.x, social.xHandle]
    ].filter(([, url]) => validHttps(url));
    if (!links.length) return;
    const nav = document.createElement('nav');
    nav.className = 'footer-socials';
    nav.setAttribute('aria-label', 'Social media');
    links.forEach(([platform, url, handle]) => {
      const link = document.createElement('a');
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.setAttribute('aria-label', `${platform}: ${handle || platform} (opens in a new tab)`);
      link.textContent = platform;
      nav.append(link);
    });
    brand.append(nav);
  });
})();

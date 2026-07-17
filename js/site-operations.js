(() => {
  const config = window.GREENHOUSE_CONFIG || {};
  const validHttps = value => /^https:\/\/[^\s]+$/i.test(value || '');
  const validEmail = value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value || '');
  const setStatus = (element, message, state = '') => {
    if (!element) return;
    element.textContent = message;
    element.dataset.state = state;
  };

  const contactForm = document.querySelector('form.form-grid');
  if (contactForm) {
    const status = contactForm.querySelector('#form-status');
    const button = contactForm.querySelector('button');
    const acknowledgement = contactForm.querySelector('input[type="checkbox"]')?.closest('.field');
    const endpointReady = validHttps(config.contactEndpoint);
    const emailReady = validEmail(config.contactEmail);

    if (endpointReady || emailReady) {
      acknowledgement?.remove();
      button.type = 'submit';
      button.removeAttribute('aria-disabled');
      button.textContent = 'Send enquiry';
      setStatus(status, 'Required fields are marked. Please do not include passwords, financial details or urgent medical information.');

      contactForm.addEventListener('submit', async event => {
        event.preventDefault();
        if (!contactForm.reportValidity()) return;
        button.disabled = true;
        setStatus(status, 'Preparing your enquiry…', 'working');
        const data = new FormData(contactForm);

        if (endpointReady) {
          try {
            const response = await fetch(config.contactEndpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
            if (!response.ok) throw new Error('Submission endpoint rejected the request.');
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
})();

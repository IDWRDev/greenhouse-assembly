(() => {
  const config = window.GREENHOUSE_CONFIG || {};
  const apiBase = String(config.givingApiBase || '').replace(/\/$/, '');
  const form = document.querySelector('#giving-form');
  if (!form) return;

  const status = document.querySelector('#giving-status');
  const submit = document.querySelector('#giving-submit');
  const mode = document.querySelector('#giving-mode');
  const isApiReady = /^https:\/\/[^\s]+$/i.test(apiBase) && config.givingEnabled === true;
  const setStatus = (message, state = '') => {
    status.textContent = message;
    status.dataset.state = state;
  };

  if (isApiReady) {
    mode.textContent = 'Secure giving available';
    setStatus('Choose your amount and payment method. You will be redirected to the provider’s secure checkout.', 'ready');
  } else {
    mode.textContent = 'Giving setup in progress';
    setStatus('Online giving is not active yet. Please use the official contact page for giving questions.', 'pending');
    submit.disabled = true;
  }

  const currency = form.querySelector('[name="currency"]');
  const cryptoMethod = form.querySelector('[value="cryptomus"]');
  const cardMethod = form.querySelector('[value="paystack"]');
  const syncCurrency = () => {
    if (cryptoMethod.checked) {
      currency.value = 'USD';
      currency.disabled = true;
    } else {
      currency.disabled = false;
    }
  };
  cryptoMethod.addEventListener('change', syncCurrency);
  cardMethod.addEventListener('change', syncCurrency);
  syncCurrency();

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!isApiReady || !form.reportValidity()) return;
    const data = Object.fromEntries(new FormData(form));
    const endpoint = data.method === 'cryptomus' ? '/api/giving/cryptomus' : '/api/giving/paystack';
    submit.disabled = true;
    setStatus('Creating your secure payment session…', 'working');
    try {
      const response = await fetch(`${apiBase}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ name: data.name, email: data.email, amount: data.amount, currency: data.currency, purpose: data.purpose })
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || !result.checkoutUrl) throw new Error(result.message || 'The payment service could not create a checkout session.');
      setStatus('Redirecting you to secure checkout…', 'working');
      window.location.assign(result.checkoutUrl);
    } catch (error) {
      setStatus(error.message || 'Your payment session could not be created. Please try again later or contact the ministry.', 'error');
      submit.disabled = false;
    }
  });
})();

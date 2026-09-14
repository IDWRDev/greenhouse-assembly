import { configuredCurrencies, cors, enabled, parseGift, reference, send, siteUrl } from '../_lib/giving.js';

export default async function handler(req, res) {
  if (cors(req, res)) return;
  if (req.method !== 'POST') return send(res, 405, { message: 'Method not allowed.' });
  if (!enabled() || !process.env.PAYSTACK_SECRET_KEY) return send(res, 503, { message: 'Online giving is not available yet.' });
  try {
    const gift = parseGift(req.body);
    if (!configuredCurrencies('GIVING_PAYSTACK_CURRENCIES').has(gift.currency)) return send(res, 422, { message: 'This currency is not enabled for card and bank payments.' });
    const paymentReference = reference('gh');
    const response = await fetch('https://api.paystack.co/transaction/initialize', {
      method: 'POST',
      headers: { Authorization: `Bearer ${process.env.PAYSTACK_SECRET_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: gift.email,
        amount: String(Math.round(Number(gift.amount) * 100)),
        currency: gift.currency,
        reference: paymentReference,
        callback_url: `${siteUrl()}?provider=paystack&reference=${encodeURIComponent(paymentReference)}`,
        metadata: { giver_name: gift.name, giving_purpose: gift.purpose, source: 'greenhouseassembly.org' }
      })
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok || !result.status || !result.data?.authorization_url) throw new Error(result.message || 'Paystack could not create a checkout session.');
    return send(res, 200, { checkoutUrl: result.data.authorization_url, reference: result.data.reference });
  } catch (error) {
    return send(res, 400, { message: error.message || 'Unable to create a payment session.' });
  }
}

import crypto from 'node:crypto';
import { cors, enabled, parseGift, reference, send, siteUrl } from '../_lib/giving.js';

export default async function handler(req, res) {
  if (cors(req, res)) return;
  if (req.method !== 'POST') return send(res, 405, { message: 'Method not allowed.' });
  if (!enabled() || !process.env.CRYPTOMUS_MERCHANT_ID || !process.env.CRYPTOMUS_API_KEY) return send(res, 503, { message: 'Crypto giving is not available yet.' });
  if (!/^https:\/\/[^\s]+$/i.test(process.env.GIVING_API_ORIGIN || '')) return send(res, 503, { message: 'Crypto giving is being configured.' });
  try {
    const gift = parseGift(req.body);
    if (gift.currency !== 'USD') return send(res, 422, { message: 'Crypto gifts are currently quoted in USD.' });
    const invoice = {
      amount: gift.amount,
      currency: 'USD',
      order_id: reference('ghcrypto'),
      url_return: siteUrl(),
      url_success: siteUrl('?provider=cryptomus'),
      url_callback: new URL('/api/webhooks/cryptomus', process.env.GIVING_API_ORIGIN).toString(),
      additional_data: JSON.stringify({ giver_name: gift.name, giver_email: gift.email, giving_purpose: gift.purpose })
    };
    const body = JSON.stringify(invoice);
    const sign = crypto.createHash('md5').update(Buffer.from(body).toString('base64') + process.env.CRYPTOMUS_API_KEY).digest('hex');
    const response = await fetch('https://api.cryptomus.com/v1/payment', {
      method: 'POST',
      headers: { merchant: process.env.CRYPTOMUS_MERCHANT_ID, sign, 'Content-Type': 'application/json' },
      body
    });
    const result = await response.json().catch(() => ({}));
    if (!response.ok || result.state !== 0 || !result.result?.url) throw new Error(result.message || 'Cryptomus could not create an invoice.');
    return send(res, 200, { checkoutUrl: result.result.url, reference: invoice.order_id });
  } catch (error) {
    return send(res, 400, { message: error.message || 'Unable to create a crypto invoice.' });
  }
}

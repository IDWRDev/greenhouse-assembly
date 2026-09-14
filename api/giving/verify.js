import { cors, enabled, send } from '../_lib/giving.js';

export default async function handler(req, res) {
  if (cors(req, res)) return;
  if (req.method !== 'POST') return send(res, 405, { message: 'Method not allowed.' });
  if (!enabled() || !process.env.PAYSTACK_SECRET_KEY) return send(res, 503, { message: 'Online giving is not available yet.' });
  const reference = String((req.body || {}).reference || '');
  if (!/^[A-Za-z0-9.=\-]{8,150}$/.test(reference)) return send(res, 400, { message: 'Invalid payment reference.' });
  const response = await fetch(`https://api.paystack.co/transaction/verify/${encodeURIComponent(reference)}`, { headers: { Authorization: `Bearer ${process.env.PAYSTACK_SECRET_KEY}` } });
  const result = await response.json().catch(() => ({}));
  if (!response.ok || !result.status) return send(res, 502, { message: 'Payment verification is temporarily unavailable.' });
  return send(res, 200, { verified: result.data?.status === 'success', reference: result.data?.reference || reference, amount: result.data?.amount, currency: result.data?.currency });
}

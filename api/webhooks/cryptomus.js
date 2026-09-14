import crypto from 'node:crypto';

export default function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ message: 'Method not allowed.' });
  if (!process.env.CRYPTOMUS_API_KEY) return res.status(503).json({ message: 'Not configured.' });
  const payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body || {};
  const suppliedSign = String(payload.sign || '');
  delete payload.sign;
  const signedBody = JSON.stringify(payload).replaceAll('/', '\\/');
  const expectedSign = crypto.createHash('md5').update(Buffer.from(signedBody).toString('base64') + process.env.CRYPTOMUS_API_KEY).digest('hex');
  if (!suppliedSign || suppliedSign.length !== expectedSign.length || !crypto.timingSafeEqual(Buffer.from(expectedSign), Buffer.from(suppliedSign))) return res.status(401).json({ message: 'Invalid signature.' });
  // A valid notification is acknowledged. The merchant dashboard remains the
  // settlement record until a dedicated accounting store is approved and added.
  return res.status(200).json({ received: true });
}

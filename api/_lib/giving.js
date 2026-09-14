const ALLOWED_PURPOSES = new Set([
  'General giving',
  'Teaching and resources',
  'Children and youth',
  'Community care and service'
]);

export function cors(req, res) {
  const origin = process.env.GIVING_SITE_ORIGIN || 'https://greenhouseassembly.org';
  if (req.headers.origin === origin) res.setHeader('Access-Control-Allow-Origin', origin);
  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') {
    res.status(204).end();
    return true;
  }
  return false;
}

export function send(res, status, payload) {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.status(status).json(payload);
}

export function enabled() {
  return process.env.GIVING_ENABLED === 'true';
}

export function parseGift(body) {
  const data = typeof body === 'string' ? JSON.parse(body) : body || {};
  const name = String(data.name || '').trim().slice(0, 100);
  const email = String(data.email || '').trim().toLowerCase();
  const amount = Number(data.amount);
  const currency = String(data.currency || '').trim().toUpperCase();
  const purpose = ALLOWED_PURPOSES.has(data.purpose) ? data.purpose : 'General giving';
  if (name.length < 2 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new Error('Please provide your name and a valid email address.');
  if (!Number.isFinite(amount) || amount < 1 || amount > 10000000) throw new Error('Please enter a valid gift amount.');
  if (!['NGN', 'USD'].includes(currency)) throw new Error('Please select a supported currency.');
  return { name, email, amount: amount.toFixed(2), currency, purpose };
}

export function siteUrl(path = '/giving/') {
  return new URL(path, process.env.GIVING_SITE_ORIGIN || 'https://greenhouseassembly.org').toString();
}

export function reference(prefix) {
  return `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
}

export function configuredCurrencies(name) {
  return new Set(String(process.env[name] || 'NGN,USD').split(',').map(value => value.trim().toUpperCase()).filter(Boolean));
}

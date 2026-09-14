# GreenHouse giving platform setup

The donor page and serverless handlers are intentionally safe by default: `givingEnabled` is `false`, the public API base is blank, and no provider secret is stored in this repository.

## Architecture

- `greenhouseassembly.org/giving/` is the donor-facing page.
- A Vercel deployment of this repository provides the `/api/giving/*` serverless routes.
- Paystack creates hosted card, bank-transfer and USSD checkout sessions.
- Cryptomus creates a one-time USD crypto invoice and sends a signed status webhook.
- GreenHouse does not collect or store card details.

## Before enabling live giving

1. Complete the ministry’s Paystack and Cryptomus merchant onboarding using the approved legal recipient details.
2. In Vercel, create a project from `IDWRDev/greenhouse-assembly` and deploy it. Do not replace the existing GitHub Pages site or alter its Namecheap DNS records during this step.
3. In that Vercel project, add these environment variables as encrypted secrets:

   - `GIVING_ENABLED=true`
   - `GIVING_SITE_ORIGIN=https://greenhouseassembly.org`
   - `GIVING_API_ORIGIN=https://YOUR-VERCEL-PROJECT.vercel.app`
   - `PAYSTACK_SECRET_KEY=...`
   - `GIVING_PAYSTACK_CURRENCIES=NGN,USD` (enable only currencies approved for the merchant account)
   - `CRYPTOMUS_MERCHANT_ID=...`
   - `CRYPTOMUS_API_KEY=...`

4. Configure the Cryptomus webhook URL as `https://YOUR-VERCEL-PROJECT.vercel.app/api/webhooks/cryptomus`.
5. In `js/site-config.js`, set:

   ```js
   givingEnabled: true,
   givingApiBase: 'https://YOUR-VERCEL-PROJECT.vercel.app',
   ```

6. Deploy the static site through the existing GitHub Pages workflow.
7. Perform one test payment in each provider’s test or sandbox mode. Confirm the correct amount, currency, purpose and provider reference before enabling live keys.

## Operating rules

- Never paste provider keys into chat, HTML, JavaScript committed to Git, or GitHub repository settings.
- Do not enable a currency that the merchant account has not approved.
- The provider dashboards are the settlement records for this initial version. Add a dedicated accounting system only after the ministry’s receipt, privacy and retention requirements are approved.
- A redirected donor is not proof of payment. Paystack payments must be verified through the provider API; Cryptomus notifications are signature-checked.

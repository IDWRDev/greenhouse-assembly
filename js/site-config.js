window.GREENHOUSE_CONFIG = Object.freeze({
  ministryName: 'The GreenHouse Assembly Ministries',
  contactEmail: 'info@greenhouseassembly.org',
  contactEndpoint: 'https://formsubmit.co/ajax/info@greenhouseassembly.org',
  publicPhone: '',
  publicAddress: '',
  mapUrl: '',
  gatheringSchedule: '',
  officeHours: '',
  givingUrl: '',
  // This branch is deployed only as a Vercel Preview for Paystack testing.
  // Using the current preview origin keeps test payment requests isolated
  // from the public GreenHouse site on the main branch.
  givingEnabled: true,
  givingApiBase: window.location.origin,
  newsletterAction: '',
  eventRegistrationUrl: '',
  social: Object.freeze({
    facebook: 'https://www.facebook.com/profile.php?id=61591869475590&mibextid=ZbWKwL',
    facebookName: 'The GreenHouse Assembly Ministries',
    instagram: 'https://www.instagram.com/greenhouseassembly/',
    instagramHandle: '@greenhouseassembly',
    tiktok: 'https://www.tiktok.com/@greenhouseassembly',
    tiktokHandle: '@greenhouseassembly',
    youtube: 'https://www.youtube.com/@GreenHouseAssembly',
    youtubeHandle: '@GreenHouseAssembly',
    linkedin: '',
    x: 'https://x.com/greenhouseassembly',
    xHandle: '@greenhouseassembly'
  })
});

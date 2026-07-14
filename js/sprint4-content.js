(() => {
  const page = location.pathname.split('/').pop() || 'index.html';
  const escape = value => String(value).replace(/[&<>"']/g, character => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' })[character]);
  const block = (eyebrow, title, content, soft = false) => `<section class="section${soft ? ' section--soft' : ''} sprint4-section"><div class="container"><p class="eyebrow">${eyebrow}</p><h2>${title}</h2>${content}</div></section>`;
  const cards = (items, className = 'grid grid--3 mobile-card-slider') => `<div class="${className}">${items.map(item => `<article class="card sprint4-card">${item.status ? `<span class="status-label">${escape(item.status)}</span>` : ''}<h3>${escape(item.title)}</h3>${item.meta ? `<p class="media-meta">${escape(item.meta)}</p>` : ''}<p>${escape(item.text)}</p>${item.action ? `<button class="preview-launch" type="button" data-preview="${escape(item.title)}">View preview</button>` : ''}</article>`).join('')}</div>`;
  const mediaCards = items => `<div class="grid grid--3 mobile-card-slider">${items.map((item, index) => `<article class="card sprint4-card teaching-preview-card"><div class="teaching-poster teaching-poster--${index % 5}" role="img" aria-label="Editorial visual preview for ${escape(item.title)}"><span class="teaching-poster__series">${escape(item.meta.split(' · ')[0])}</span><span class="teaching-poster__play" aria-hidden="true">▶</span><span class="teaching-poster__state">${escape(item.status)}</span></div><span class="status-label">${escape(item.status)}</span><h3>${escape(item.title)}</h3><p class="media-meta">${escape(item.meta)}</p><p>${escape(item.text)}</p><button class="preview-launch" type="button" data-preview="${escape(item.title)}">Open teaching preview</button></article>`).join('')}</div>`;
  const series = [
    ['The Architecture of Redemption','A long-form study of promise, covenant, Christ and the coherence of the Gospel.'],
    ['The World That Created the Tithe','A historical and theological preview of land, produce, Levites, worship and covenant responsibility.'],
    ['Covenant and Kingdom','A pathway through promise, law, nationhood, kingship and Gospel fulfilment.'],
    ['Spiritual Formation','Prayer, Scripture, worship, discipline, character and community as a patient life with God.'],
    ['Spirit · Mind · Body Under Christ','An integrated GreenHouse framework for whole-person Christian maturity.'],
    ['Christian Leadership','Character, stewardship, responsibility and service before visibility.'],
    ['Gospel Foundations','A clear starting place for people exploring Christian faith and practice.'],
    ['Faith, Culture, and Public Life','Biblical wisdom for work, family, creativity, technology and public responsibility.'],
    ['Wisdom for Ordinary Days','A thoughtful approach to decision-making, habits, relationships and vocation.'],
    ['Prayer and Communion','Prayer as attentiveness, Scripture-shaped communion and shared dependence on God.']
  ].map(([title,text]) => ({ title, text, status:'Editorial series preview' }));
  const messages = [
    ['Promise and the Shape of Redemption','The Architecture of Redemption','Genesis 12–22'],['Covenant Before Calculation','The World That Created the Tithe','Deuteronomy 14'],['Land, Levites, and Shared Worship','The World That Created the Tithe','Numbers 18'],['The King and the Kingdom','Covenant and Kingdom','2 Samuel 7'],['Prayer That Forms Desire','Spiritual Formation','Matthew 6'],['Reading Scripture With Patience','Spiritual Formation','Psalm 1'],['A Whole Life Under Christ','Spirit · Mind · Body Under Christ','Romans 12'],['Leadership Before Visibility','Christian Leadership','Mark 10'],['The Gospel as Good News','Gospel Foundations','1 Corinthians 15'],['Grace, Truth, and Christian Character','Gospel Foundations','Titus 2'],['Work as Faithful Presence','Faith, Culture, and Public Life','Colossians 3'],['Wisdom in an Age of Distraction','Faith, Culture, and Public Life','Proverbs 4'],['The Practice of Communion','Prayer and Communion','John 15'],['Family as a Place of Formation','Wisdom for Ordinary Days','Deuteronomy 6'],['Serving Without Self-Importance','Christian Leadership','Philippians 2'],['The People of God and Public Hope','Covenant and Kingdom','Jeremiah 29'],['A Rule of Life for Growing Faith','Spiritual Formation','Galatians 5'],['Purpose, Calling, and Faithfulness','Wisdom for Ordinary Days','Ephesians 2']
  ].map(([title,seriesName,scripture], index) => ({ title, text:`A derived editorial preview exploring ${seriesName.toLowerCase()} with clarity, care and a practical next step.`, meta:`${seriesName} · ${scripture} · Duration preview`, status:index < 10 ? 'Video preview' : 'Audio preview', action:true }));
  const append = html => document.querySelector('main')?.insertAdjacentHTML('beforeend', html);
  if (page === 'teaching.html') {
    append(block('Series library','Teaching built for study, prayer and maturity.', cards(series), true));
    append(block('Message previews','A growing theological library.', mediaCards(messages), false));
    append(block('Study collections','Structured pathways for different seasons.', cards([
      ...['Covenant foundations','Reading the Gospel','Prayer and communion','Whole-person formation','Wisdom and vocation','Church, family and community'].map(title => ({title,text:'Six-session study pathway; Scripture selection and downloadable notes require owner review.',status:'Study guide preview'})),
      ...['Servant leadership','Stewardship and responsibility','Character under pressure','Leading with wisdom','Creative service','Accountability and care'].map(title => ({title,text:'Leadership-session preview for formation before visibility.',status:'Leadership preview'})),
      ...['Learning to pray','Prayer and Scripture','Worship as attention','Rest and renewal','Practices of gratitude','Interceding with hope'].map(title => ({title,text:'Prayer-and-formation lesson preview; final Scripture selection and study notes require approval.',status:'Formation lesson preview'})),
      ...['Faith at the family table','Listening and repair','Marriage and mutual service','Raising questions with grace','Hospitality at home','Community care in practice'].map(title => ({title,text:'Family-and-community lesson preview for thoughtful shared discipleship.',status:'Family lesson preview'}))
    ]), true));
  }
  if (page === 'resources.html') {
    const resources = [
      ['The Divine Art of Violence','Book framework','A substantive book feature awaiting manuscript, author details, cover rights and publication approval.'],
      ['Architecture of Redemption Study Guide','Study guide','Six guided sessions exploring covenant, Gospel and mature Christian understanding.'],
      ['Prayer as Formation, Not Performance','Article preview','An original editorial outline on prayer as communion rather than display.'],
      ['Reading Scripture Architecturally','Article preview','A preview of careful reading that attends to covenant, story and fulfilment.'],
      ['The Practice of a Steady Life','Devotional preview','A six-part devotional rhythm of Scripture, prayer, rest, work and service.'],
      ['Gospel Foundations Reading Plan','Reading plan','Four weeks of accessible Scripture readings and reflection prompts.'],
      ['Family Table Conversations','Family resource','A future guide for faith, questions, listening and hospitality at home.'],
      ['Leadership Before Visibility','Leadership resource','A practical reflection framework for character, responsibility and service.'],
      ['Faithful Digital Habits','Youth resource','A conversation starter for attention, identity, creativity and online wisdom.'],
      ['Teaching Transcript Companion','Media companion','A replacement-ready format for approved teaching notes and transcripts.']
    ].map(([title,status,text])=>({title,status,text,action:true}));
    append(block('The GreenHouse publishing table','Books, articles and guides in development.', cards(resources), true));
    append(block('Featured book','The Divine Art of Violence', `<div class="feature sprint4-book"><p>This editorial framework prepares a future book page without claiming a finished manuscript, author biography, date, price, ISBN, endorsement or availability. Its proposed focus is the difficult work of reading Scripture faithfully where power, judgment, covenant, mercy and the way of Christ are in view.</p><div class="grid grid--3"><article><h3>Core question</h3><p>How should Christians read demanding biblical texts with theological care, moral seriousness and attention to the Gospel?</p></article><article><h3>Intended readers</h3><p>Thoughtful Christians, students, leaders and readers seeking patient biblical interpretation.</p></article><article><h3>Proposed movement</h3><p>Text, covenant world, redemption, Christ, ethics and faithful public life.</p></article></div><p class="media-meta">Publication status · Pending owner review</p><span class="preview-action">Purchase and download information not available</span></div>`, false));
    const articles = ['Why Spiritual Formation Must Shape the Whole Person','The Covenant World Behind Biblical Giving','What Modern Readers Miss About Ancient Israel','Why Scripture Must Be Read Architecturally','Prayer as Formation, Not Performance','Leadership Before Visibility'].map((title,index)=>({title,status:'Article preview',meta:`${[6,8,7,9,6,7][index]} min read · Editorial draft`,text:'A source-aware editorial outline prepared for owner and doctrinal review; no article is presented as published.',action:true}));
    append(block('Journal','Questions worth reading slowly.', cards(articles), true));
    const practices = ['Abiding in Christ','Rest and renewal','A rule of prayer','Wisdom in ordinary decisions','Gratitude and attention','Serving with humility'].map(title=>({title,status:'Devotional preview',text:'A guided reflection format with Scripture, prayer, practice and journal prompts awaiting final review.',action:true}));
    append(block('Devotional practices','Small rhythms for a steady life with God.', cards(practices), false));
    const pathways = ['Gospel Foundations · 4 weeks','Prayer and Communion · 21 days','Wisdom for Work and Life · 4 weeks','Scripture and Formation · 6 weeks'].map(title=>({title,status:'Reading-plan preview',text:'A replacement-ready pathway for approved readings, reflection prompts and group discussion notes.',action:true}));
    append(block('Reading pathways','A deliberate route through Scripture and reflection.', cards(pathways), true));
    const collections = ['Prayer resources','New-believer foundations','Family and marriage','Leadership and stewardship','Youth and digital wisdom','Audio and video companions'].map(title=>({title,status:'Collection preview',text:'A clearly organised resource collection that will receive real files, media and guidance only after review.',action:true}));
    append(block('Resource collections','Support for faith at home, work and in community.', cards(collections), false));
  }
  if (page === 'events.html') {
    const events = ['Sunday Worship Gathering','Midweek Bible Formation','Corporate Prayer Gathering','Young Adults Forum','Leadership Formation Intensive','Family and Marriage Forum','Community Outreach Day','Media and Creative Workshop','Scripture and Theology Seminar','New Believers Foundation Class'].map((title,index)=>({title,status:index < 4?'Weekly-rhythm concept':'Programme concept',text:'A thoughtful gathering model with purpose, welcome, Scripture, prayer, community and a clear next step. Date, venue and registration are awaiting confirmation.',action:true}));
    append(block('Gathering concepts','A living rhythm, without invented dates.', cards(events), true));
    append(block('What a gathering is for','More than attendance.', cards([
      {title:'Worship and attention',status:'Programme principle',text:'Space to turn toward God with reverence, gratitude, Scripture and song.'},
      {title:'Teaching and conversation',status:'Programme principle',text:'Clear biblical learning with room for thoughtful questions, reflection and practice.'},
      {title:'Prayer and care',status:'Programme principle',text:'Prayerful support and mutual care offered responsibly, without replacing professional services.'},
      {title:'Welcome and participation',status:'Programme principle',text:'A first-visit experience designed to be calm, hospitable and respectful of different stages of faith.'}
    ]), false));
  }
  if (page === 'ministries.html') {
    const names = ['Children','Youth','Young Adults','Men','Women','Marriage and Family','Prayer','Worship','Care and Hospitality','Discipleship Groups','Leadership Development','Outreach and Community Care','Media and Creative','The GreenHouse Academy','New Believers','Serving Teams'];
    append(block('Ministry pathways','Distinct places to grow, belong and serve.', cards(names.map(title=>({title,status:'Pathway preview',text:'A clear participation pathway for people seeking community, formation, practical service and a faithful next step. Leadership, schedule and availability are pending confirmation.',action:true}))), true));
    append(block('How ministry grows','A shared life, not a catalogue.', cards([
      {title:'Begin by belonging',status:'Participation pathway',text:'Start by listening, meeting people and taking one uncomplicated next step.'},
      {title:'Learn with others',status:'Participation pathway',text:'Grow through Scripture, conversation, prayer, practice and constructive feedback.'},
      {title:'Serve with care',status:'Participation pathway',text:'Offer gifts and time in ways that are accountable, sustainable and attentive to people.'},
      {title:'Lead as you are formed',status:'Participation pathway',text:'Leadership is approached as character, responsibility and service before visibility.'}
    ]), false));
  }
  if (page === 'about.html') {
    append(block('A life of formation','Why cultivation matters.', `<div class="section-copy"><p>GreenHouse uses the language of cultivation because Christian maturity is rarely instant. It is formed through Scripture, prayer, worship, wise relationships, patient practice and practical service. We want a life with God that reaches the mind, the body, the home, work, community and public responsibility.</p><p>Our aim is not religious performance. It is a rooted, thoughtful and generous people whose faith becomes visible in character, hospitality, learning, creativity and care for others.</p></div>`, true));
    append(block('The GreenHouse way','Know, become, belong, serve, influence.', cards([
      {title:'Know',status:'Formation movement',text:'Receive Scripture with attention: learn the Gospel, ask better questions and grow in biblical understanding.'},
      {title:'Become',status:'Formation movement',text:'Let prayer, worship, wisdom and discipline shape character over time.'},
      {title:'Belong',status:'Formation movement',text:'Practise hospitality, mutual care and honest community across generations and backgrounds.'},
      {title:'Serve and influence',status:'Formation movement',text:'Carry faith into work, family, creativity, leadership and the common good.'}
    ]), false));
  }
  if (page === 'contact.html') append(block('Ways to connect','Start with the conversation that fits your need.', cards(['First visit','Prayer support','Ministry interest','Volunteering','Partnership','Media enquiry','Publishing enquiry','Speaking invitation','Event question','Giving question'].map(title=>({title,status:'Contact route pending',text:'This pathway is being prepared with responsible handling and a verified contact route. Please do not submit personal or sensitive information through an inactive form.'}))), true));
  if (page === 'index.html') {
    append(block('Discover the next step','A connected life of faith.', cards([
    {title:'Know',text:'Explore teaching, study guides and biblical foundations.',status:'Learning pathway'},
    {title:'Become',text:'Practise prayer, wisdom, character and whole-person formation.',status:'Formation pathway'},
    {title:'Belong',text:'Find worship, welcome, care and community.',status:'Community pathway'},
    {title:'Serve',text:'Discover practical service, creativity and leadership.',status:'Ministry pathway'},
    {title:'Influence',text:'Bring Christian wisdom to work, family, culture and public life.',status:'Vocation pathway'}
    ]), true));
    append(block('Begin where you are','A gentle first step is still a step.', cards([
      {title:'Explore a teaching',status:'Discovery',text:'Use the teaching library to begin with Scripture, Gospel foundations or formation.'},
      {title:'Read a resource',status:'Discovery',text:'Find draft guides, articles and reading pathways that can support steady reflection.'},
      {title:'Plan a future visit',status:'Visitor guidance',text:'Gathering details will appear only after the ministry confirms time, place and accessibility information.'},
      {title:'Ask for a connection',status:'Visitor guidance',text:'Contact routes are being prepared for ministry interest, prayer, partnership and practical questions.'}
    ]), false));
  }
  if (page === 'contact.html') append(block('For your first visit','What a thoughtful welcome can include.', cards([
    {title:'Before you arrive',status:'Visitor guide',text:'Confirmed location, arrival, accessibility and family information will be published in one clear place.'},
    {title:'When you arrive',status:'Visitor guide',text:'Expect space to settle in, join at your own pace and ask a question without pressure.'},
    {title:'After the gathering',status:'Visitor guide',text:'Future next steps may include teaching, community, prayer or a ministry conversation when verified routes are available.'}
  ]), false));
  document.addEventListener('click', event => { const button = event.target.closest('.preview-launch'); if (!button) return; const status = document.createElement('p'); status.className = 'form-status'; status.setAttribute('role','status'); status.textContent = `“${button.dataset.preview}” is an editorial media preview. A final video, audio file or resource will be connected after production and approval.`; button.replaceWith(status); });
})();

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"

DEEP = HexColor("#062f27")
FOREST = HexColor("#0b4d3b")
GOLD = HexColor("#d7b853")
CREAM = HexColor("#f7f4ea")
MIST = HexColor("#edf3ee")
INK = HexColor("#19382f")
MUTED = HexColor("#60766c")
LINE = HexColor("#d8e1da")


GUIDES = [
    {
        "file": "gospel-foundations-guide.pdf",
        "kicker": "FOUNDATIONS SERIES  /  GUIDE 01",
        "title": "Gospel\nFoundations",
        "subtitle": "A six-part guide for understanding grace, new life, faith and the shared life of a people reconciled to God.",
        "accent": HexColor("#47765b"),
        "intro": "The Gospel is not a private improvement plan or a religious escape from the world. It is the good news that God has acted in Jesus Christ to reconcile, restore and form a people for His life. Move through these sessions slowly. The aim is not to collect correct phrases, but to receive the truth of Christ in ways that change allegiance, attention and practice.",
        "sessions": [
            ("01", "The good news begins with God", "Creation, gift and the purpose of human life", "Genesis 1:26-31; Psalm 8; John 1:1-5", "The biblical story begins with a generous God, not with a human problem. Before sin fractures trust, people are created to receive life from God and to bear His image in the world. This means identity is received before it is achieved, and vocation is rooted in relationship before it becomes a question of performance.", "Where have you made achievement carry the weight of identity? What would it mean to receive life, ability and opportunity as gifts? Where might ordinary work become a way to represent God's good care?", "Begin each morning this week by naming three gifts before naming three tasks. Let gratitude set the order of your attention."),
            ("02", "Sin names a real rupture", "Worship, desire and the loss of true communion", "Genesis 3:1-13; Romans 1:18-25; Ephesians 2:1-5", "Sin is more than isolated mistakes. It is a turning of trust away from God that bends worship, desire, relationship and the use of power. It disorders life from the inside out. Naming this truth is not an invitation to shame; it is the beginning of honesty about why self-repair is never enough.", "What forms of self-protection become automatic when you feel exposed? How does misplaced worship affect the way you use people, time or success? What is the difference between conviction and condemnation?", "Write one sentence that names a pattern without excuse. Follow it with a prayer that asks for mercy, courage and a truthful next step."),
            ("03", "Grace meets us truthfully", "The cross, mercy and reconciliation", "Romans 3:21-26; Romans 5:6-11; 2 Corinthians 5:17-21", "In Jesus, God does not minimise the rupture. Christ enters it, bears its cost and opens reconciliation. Grace is therefore neither denial nor indulgence. It is mercy with substance: God acts where we cannot save ourselves, then draws us into the life His mercy makes possible.", "Which part of the Gospel feels hardest to receive: need, forgiveness, surrender or change? How does the cross challenge both pride and despair? What reconciliation may need a faithful beginning in your life?", "Read Romans 5:6-11 aloud. Write a short prayer of gratitude that names what you cannot achieve for yourself and what Christ has freely given."),
            ("04", "Faith becomes allegiance", "Repentance, trust and a new centre", "Mark 1:14-15; Romans 6:1-14; Galatians 2:19-20", "Faith is more than agreement with a set of claims. To trust Christ is to receive His grace and to allow that gift to change direction. Repentance is not merely regret; it is the turning of a life toward a new Lord. The Gospel frees people from the old master so they can learn the life of Christ with others.", "Which old allegiance most competes with trust in Christ? What would repentance look like beyond regret? How can grace become visible without making truth optional?", "Choose one concrete response that expresses new allegiance: a repair, a boundary, a confession or a practice of truthfulness."),
            ("05", "New life is learned in community", "Belonging, gifts and the body of Christ", "Acts 2:42-47; Ephesians 4:1-16; Colossians 3:12-17", "The Gospel does not create isolated spiritual consumers. It gathers people into a reconciled body where gifts become service, truth is spoken in love and maturity is shared. Community does not remove difference or difficulty. It gives people a place to practise forgiveness, responsibility and durable love.", "Where do you tend to treat faith as private? What gift or responsibility could strengthen another person? What habits make a community safer for truth and repair?", "Offer one quiet act of service this week. Notice whether you are seeking visibility or genuinely seeking another person's good."),
            ("06", "Grace sends people into real life", "Witness, work and faithful presence", "Matthew 5:13-16; 1 Peter 2:9-12; Titus 2:11-14", "Grace forms people for the places they already inhabit. The purpose is not to withdraw from the world, but to carry the character of Christ into homes, work, leadership, creativity and public responsibility. A formed life becomes a credible witness when its truth is joined to mercy, courage and usefulness.", "Where has God already placed you to carry life? What would faithful influence look like without self-promotion? Which ordinary responsibility can become a form of witness?", "Identify one place you influence. Pray for the courage to make it more truthful, more generous and more life-giving this week."),
        ],
    },
    {
        "file": "life-of-prayer-7-day-guide.pdf",
        "kicker": "FORMATION SERIES  /  GUIDE 02",
        "title": "A Life\nof Prayer",
        "subtitle": "Seven days of Scripture-shaped attention, honest communion and intercession that enters ordinary life.",
        "accent": HexColor("#8a7130"),
        "intro": "Prayer is not a performance and it is not only a last resort. It is a returning: fear, desire, gratitude, decisions and relationships are brought back under the care of God. Give each day fifteen to twenty unhurried minutes. Read the Scripture aloud, stay with one question and keep the practice small enough to carry honestly.",
        "sessions": [
            ("DAY 01", "Arrive", "Prayer begins with the God who is already present", "Psalm 46; Matthew 11:28-30", "Prayer begins by becoming present to the God who is already present. We do not bring a polished version of ourselves. We bring the life we actually have: noise, gratitude, fatigue, confusion and need. Honest arrival is the first act of trust.", "What noise are you carrying into prayer? What would it mean to stop performing competence before God? What burden are you being invited to name rather than manage alone?", "Sit in silence for three minutes. Name what is present without trying to solve it. End with: God, I arrive as I am."),
            ("DAY 02", "Listen", "Attention shaped by Scripture and humility", "1 Samuel 3:1-10; John 10:1-5", "Listening is not passivity. It is trained attention shaped by Scripture, humility and a willingness to obey what is good. We learn to distinguish God's voice not by chasing novelty, but by returning to the character of Christ, the witness of Scripture and wise community.", "What competes most strongly for your attention? How can Scripture test what you think you hear? Where do you need to listen before you react or decide?", "Read one short passage aloud twice. Write down one phrase that calls you toward faithfulness, then carry that phrase through the day."),
            ("DAY 03", "Ask", "Petition that reorders desire", "Matthew 6:5-13; Philippians 4:4-7", "Jesus teaches prayer that is direct about need while remaining rooted in God's name, Kingdom and will. Petition is not a way to control outcomes. It is a way to bring desire into relationship with the Father, who knows what is needed and teaches us to receive with trust.", "Which request in the Lord's Prayer do you avoid? What need can you name plainly today? How might surrender change the way you ask?", "Write five simple requests. Leave space beneath each one to record not only what happens, but how your perspective is being formed."),
            ("DAY 04", "Confess", "Truthful return without hiding or despair", "Psalm 51:1-12; 1 John 1:5-9", "Confession refuses both hiding and self-condemnation. It tells the truth in the presence of mercy. Because God meets us in Christ, we can name what has been distorted without defending ourselves or losing hope that repair is possible.", "What are you tempted to minimise? What repair may need to follow your confession? What helps you distinguish remorse from a willingness to change?", "Name one specific failure without excuse. Identify one practical movement of repair: an apology, a boundary, a conversation or a changed pattern."),
            ("DAY 05", "Give thanks", "Attention trained to recognise grace", "Psalm 103:1-5; Luke 17:11-19", "Gratitude trains attention to recognise gift, sustaining mercy and ordinary goodness. It does not deny grief or complexity. It keeps grief from becoming the only story we can see, and it returns what we have received to worship rather than entitlement.", "Which ordinary gift have you stopped noticing? How can gratitude coexist with lament? Who has carried good into your life without being recognised?", "Record ten concrete gifts from the last twenty-four hours. Thank one person directly and specifically."),
            ("DAY 06", "Intercede", "Love that carries people and places before God", "1 Timothy 2:1-6; Ephesians 3:14-21", "Intercession expands prayer beyond private concerns. We learn to carry people, communities and public places before God with patience rather than anxiety. This is not a way to avoid action. It is a way to let action grow from a deeper love and a wider hope.", "Who is easy for you to forget? Which public concern needs sustained rather than reactive prayer? How can prayer make your care more practical?", "Pray through five circles: household, community, leaders, those under pressure and the Church. Choose one circle for sustained prayer this month."),
            ("DAY 07", "Remain", "A rule of life that makes communion durable", "John 15:1-11; Colossians 4:2-6", "A life of prayer is built through return. Faithfulness grows through small rhythms that connect communion to speech, work and relationships. The aim is not intensity for its own sake. It is a life that can turn toward God before reacting, deciding or withdrawing.", "Which practice from this week is truly sustainable? What time and place will help you return? Who can help you review your rhythm with wisdom?", "Design one daily moment, one weekly longer space and one shared prayer practice. Keep each one simple, clear and reviewable for thirty days."),
        ],
    },
    {
        "file": "leadership-before-visibility-guide.pdf",
        "kicker": "LEADERSHIP SERIES  /  GUIDE 03",
        "title": "Leadership\nBefore Visibility",
        "subtitle": "Six sessions on character, service, wisdom, stewardship and the responsibility of influence.",
        "accent": HexColor("#3c5d58"),
        "intro": "Leadership is not first a platform, title or public role. It is stewardship: the care of people, trust, gifts, time and responsibility. These sessions are for anyone carrying influence in a home, team, church, workplace or creative setting. Move slowly enough to let hidden habits become visible and to let practical repair follow insight.",
        "sessions": [
            ("01", "Character before platform", "The unseen life that carries public responsibility", "1 Samuel 16:1-13; Luke 16:10-12", "Public usefulness cannot outrun private formation indefinitely. Faithfulness in unseen places creates the capacity to carry visible responsibility without being ruled by recognition, fear or image-management. God attends to the heart, not because outward work is unimportant, but because the heart eventually gives outward work its character.", "Which unseen habits currently shape your leadership? Where are you seeking recognition before readiness? Who has permission to ask you questions you would rather avoid?", "Choose one hidden responsibility and practise it consistently for thirty days without announcing it."),
            ("02", "Service before status", "Authority used for the flourishing of others", "Mark 10:35-45; John 13:1-17", "Jesus reframes greatness through service. This does not make leadership passive or vague. It gives leadership its purpose: strength is used to protect, equip, clarify and serve rather than to make others carry the leader's image. Authority becomes safer when it is accountable to the good of people.", "Who benefits most from the way you currently lead? Which task feels beneath you? How can you make another person's contribution more fruitful?", "Complete one necessary, low-visibility task that removes friction for a person, team or household."),
            ("03", "Wisdom before speed", "Counsel, patience and decisions that protect people", "Proverbs 15:22; James 1:19-20; Luke 14:28-30", "Urgency can mimic importance. Wise leadership listens, seeks counsel, counts cost and knows when a slower decision protects people and purpose. Pace is not a neutral choice: a rushed leader can create confusion, silence needed voices and make repair harder than it needed to be.", "What decision are you rushing? Whose perspective is missing? What cost has not yet been named?", "Before one meaningful decision, write what you know, what you assume, who is affected and who should be consulted."),
            ("04", "Truth before image", "Correction, repair and responsible communication", "Proverbs 27:5-6; Ephesians 4:25-32; James 3:13-18", "Influence can tempt a person to protect appearance at the expense of truth. Mature leaders receive correction without retaliation, speak plainly without cruelty and repair harm without making others manage their discomfort. Truthfulness is not bluntness. It is love joined to courage, timing and responsibility.", "How do you respond when corrected? Where has image-management made communication less honest? What does a complete repair require beyond an apology?", "Invite one trusted person to name a blind spot. Listen without defending yourself. Write the first step you will take in response."),
            ("05", "Stewardship before scale", "Tending what is already entrusted", "Matthew 25:14-30; 1 Peter 4:8-11", "Scale is not the same as fruitfulness. Stewardship asks whether people, gifts, trust, time and resources are being handled faithfully at the size they are now. Growth that outruns care creates strain. Faithful leaders learn to honour limits, strengthen foundations and make responsibility clear.", "What has already been entrusted to you? Where is growth creating strain or neglect? Which boundary would protect long-term faithfulness?", "Create an inventory of time, relationships, money, gifts and responsibility. Choose one small repair that protects what has been entrusted."),
            ("06", "Formation before legacy", "The kind of people our influence is producing", "2 Timothy 2:1-2; 1 Peter 5:1-4; Philippians 2:1-11", "A leader's deepest legacy is not personal recognition. It is the kind of people and practices that remain when the leader is not present. Healthy influence equips others, shares credit, creates room for truth and leaves people more secure, more capable and more able to serve.", "If your influence grows, will people around you become more secure and more truthful? Who are you equipping rather than using? What practice would make your leadership more life-giving?", "Choose one person to encourage, equip or share meaningful responsibility with. Make the next step clear and offer support without control."),
        ],
    },
]


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=7, leading=10, textColor=GOLD, tracking=1.4, spaceAfter=7))
styles.add(ParagraphStyle(name="GuideTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=DEEP, spaceAfter=11))
styles.add(ParagraphStyle(name="Deck", parent=styles["BodyText"], fontName="Helvetica", fontSize=11, leading=16, textColor=MUTED, spaceAfter=14))
styles.add(ParagraphStyle(name="Heading", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=DEEP, spaceAfter=7))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.3, leading=13.6, textColor=INK, spaceAfter=8))
styles.add(ParagraphStyle(name="Question", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.8, leading=12.6, textColor=INK, leftIndent=9, firstLineIndent=-9, spaceAfter=4))
styles.add(ParagraphStyle(name="Small", parent=styles["Normal"], fontName="Helvetica", fontSize=7.5, leading=10.2, textColor=MUTED))
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=31, leading=33, textColor=white, spaceAfter=10))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["BodyText"], fontName="Helvetica", fontSize=11, leading=16, textColor=HexColor("#d0e0d7")))


def cover(canvas, doc, guide):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(DEEP)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(.8)
    canvas.circle(width * .85, height * .83, 100 * mm, fill=0, stroke=1)
    canvas.setStrokeColor(guide["accent"])
    canvas.circle(width * .85, height * .83, 76 * mm, fill=0, stroke=1)
    canvas.setFillColor(guide["accent"])
    canvas.circle(width * .9, height * .18, 42 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawString(22 * mm, height - 27 * mm, "THE GREENHOUSE ASSEMBLY MINISTRIES")
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 30)
    y = height - 67 * mm
    for line in guide["title"].split("\n"):
        canvas.drawString(22 * mm, y, line.upper())
        y -= 15 * mm
    canvas.setFillColor(HexColor("#d0e0d7"))
    words = guide["subtitle"].split()
    lines, line = [], ""
    for word in words:
        candidate = (line + " " + word).strip()
        if canvas.stringWidth(candidate, "Helvetica", 11) > width - 44 * mm and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    canvas.setFont("Helvetica", 11)
    for index, line in enumerate(lines):
        canvas.drawString(22 * mm, y - 5 * mm - (index * 7 * mm), line)
    canvas.setFillColor(GOLD)
    canvas.rect(22 * mm, 42 * mm, 26 * mm, 1.6 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 7.6)
    canvas.drawString(22 * mm, 32 * mm, "SCRIPTURE  /  REFLECTION  /  PRACTICE  /  CONVERSATION")
    canvas.restoreState()


def on_page(guide):
    def render(canvas, doc):
        if doc.page == 1:
            cover(canvas, doc, guide)
            return
        width, height = A4
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.line(18 * mm, height - 15 * mm, width - 18 * mm, height - 15 * mm)
        canvas.setFillColor(FOREST)
        canvas.setFont("Helvetica-Bold", 6.8)
        canvas.drawString(18 * mm, height - 11 * mm, "THE GREENHOUSE ASSEMBLY  /  " + guide["kicker"])
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7)
        canvas.drawRightString(width - 18 * mm, 12 * mm, str(doc.page - 1))
        canvas.restoreState()
    return render


def practice_box(text):
    table = Table([[Paragraph("PRACTISE THIS WEEK", styles["Eyebrow"]), Paragraph(text, styles["Body"])]], colWidths=[43 * mm, 117 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), MIST), ("BOX", (0, 0), (-1, -1), .5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return table


def build(guide):
    target = OUT / guide["file"]
    doc = BaseDocTemplate(str(target), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=24 * mm, bottomMargin=20 * mm)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=on_page(guide))])
    story = [Spacer(1, 1), PageBreak()]
    story += [
        Paragraph("WELCOME", styles["Eyebrow"]), Paragraph("How to use this guide", styles["GuideTitle"]), Paragraph(guide["intro"], styles["Deck"]),
        Paragraph("A steady rhythm", styles["Heading"]),
        Paragraph("Read the passages in your preferred Bible translation. Notice what they reveal about God, people and faithful response. Read the teaching slowly. Journal or discuss the questions without rushing for a polished answer. Finally, take the weekly practice into real life and return to share what you noticed.", styles["Body"]),
        Paragraph("A note on care", styles["Heading"]),
        Paragraph("These guides are designed for formation, not for bypassing pain, complexity or the need for responsible care. If a session raises significant personal, relational or safeguarding concerns, bring them to an appropriate pastoral, professional or emergency support route.", styles["Body"]),
        Paragraph("Contents", styles["Heading"]),
    ]
    for number, title, focus, *_ in guide["sessions"]:
        story.append(Paragraph(f"{number}  {title}  -  {focus}", styles["Body"]))
    story.append(PageBreak())
    for number, title, focus, reading, teaching, questions, practice in guide["sessions"]:
        story += [
            Paragraph(f"SESSION {number}", styles["Eyebrow"]), Paragraph(title, styles["GuideTitle"]), Paragraph(focus, styles["Deck"]),
            Paragraph("READ", styles["Eyebrow"]), Paragraph(reading, styles["Body"]),
            Paragraph("TEACHING", styles["Eyebrow"]), Paragraph(teaching, styles["Body"]),
            Paragraph("REFLECT OR DISCUSS", styles["Eyebrow"]),
        ]
        for index, question in enumerate(questions.split("? "), 1):
            story.append(Paragraph(f"{index}. {question.strip().rstrip('?')}?", styles["Question"]))
        story += [Spacer(1, 4), practice_box(practice), PageBreak()]
    story += [
        Paragraph("CONTINUE THE JOURNEY", styles["Eyebrow"]), Paragraph("A thirty-day response", styles["GuideTitle"]),
        Paragraph("Choose one daily practice, one weekly practice and one relationship in which you will make room for truth, prayer and accountable growth. Keep the rule modest enough to be honest. Review it after thirty days with a trusted person, and adjust it in the direction of greater love, clarity and faithfulness.", styles["Deck"]),
        Paragraph("Closing prayer", styles["Heading"]),
        Paragraph("Lord Jesus, centre us in Your life. Give us patient attention to Your word, courage to name what is true and grace to practise the next faithful step. Form us into people whose love becomes useful in homes, work, communities and every place entrusted to us. Amen.", styles["Body"]),
        Paragraph("THE GREENHOUSE ASSEMBLY  /  KNOW. BECOME. BELONG. SERVE. INFLUENCE.", styles["Small"]),
    ]
    doc.build(story)
    print(target)


OUT.mkdir(parents=True, exist_ok=True)
for guide in GUIDES:
    build(guide)

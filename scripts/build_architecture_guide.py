from pathlib import Path
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import BaseDocTemplate, Frame, PageBreak, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "architecture-of-redemption-study-guide.pdf"

FOREST = HexColor("#083f31")
DEEP = HexColor("#052e24")
GOLD = HexColor("#d7b853")
CREAM = HexColor("#f7f4ea")
MIST = HexColor("#edf4ef")
INK = HexColor("#15352b")
MUTED = HexColor("#586f65")
LINE = HexColor("#d8e2db")

sessions = [
    {
        "number": "01", "title": "The story we enter", "focus": "Creation, image and vocation",
        "reading": "Genesis 1:26-28; Psalm 8; Colossians 1:15-17",
        "core": "Scripture opens with a world that belongs to God. Human beings are not accidents in a hostile universe; they are image-bearers, created to receive life from God and represent His wise care within creation.",
        "teaching": [
            "The Bible does not begin with our failure. It begins with God's goodness, His word and His purpose. That matters because the Gospel is not an escape from the created world; it is God's work of restoring people and creation toward the life He intended.",
            "Vocation is therefore not merely a career question. It is the call to carry God's character into real places - homes, work, culture, relationships and responsibility. Before we ask what we can achieve, we ask what faithful image-bearing requires here."
        ],
        "questions": ["What does it mean to receive life as a gift rather than a possession?", "Where has your view of purpose become smaller than God's good creation?", "What ordinary responsibility could become an act of image-bearing this week?"],
        "practice": "Name one place you influence each day. Pray for wisdom to make that place more truthful, more ordered and more life-giving."
    },
    {
        "number": "02", "title": "Promise creates a people", "focus": "Abraham, blessing and covenant",
        "reading": "Genesis 12:1-3; Genesis 15:1-6; Galatians 3:6-14",
        "core": "God's promise to Abraham is personal, but never private. God calls one family so that blessing may reach the nations. Covenant teaches us that belonging is a gift with a direction.",
        "teaching": [
            "God's covenant faithfulness is not earned by human achievement. Abraham receives a promise before he has built a record that could purchase it. Grace precedes and creates the response of faith.",
            "Yet covenant also forms a people who live differently. The blessing they receive is meant to move outward. A covenant people learn hospitality, justice, truthfulness and trust because they belong to the God who has committed Himself to them."
        ],
        "questions": ["What is the difference between receiving blessing and consuming blessing?", "How does God's faithfulness change the way you approach obedience?", "Where might your life become a channel of good rather than a container of comfort?"],
        "practice": "Choose one act of generosity, welcome or reconciliation that makes God's promise tangible to another person."
    },
    {
        "number": "03", "title": "Freedom needs a way of life", "focus": "Exodus, worship and holiness",
        "reading": "Exodus 19:3-6; Deuteronomy 6:4-9; Micah 6:6-8",
        "core": "God does not rescue Israel from slavery only to leave them without shape. Freedom is protected by worship, truth and a communal way of life that resists the patterns of bondage.",
        "teaching": [
            "The law is not a ladder by which people climb into God's favour. It is instruction for a people who have already been rescued. It reveals what life under God's good rule looks like in worship, work, relationships, rest and justice.",
            "Every person is formed by a liturgy - a repeated pattern of attention and desire. Israel is taught to remember because forgetting produces imitation of the powers that once held them. We also need practices that keep freedom from becoming another name for self-rule."
        ],
        "questions": ["What old pattern still speaks like a master in your life?", "How do repeated practices shape desire, not just behaviour?", "What does faithful freedom require of a community?"],
        "practice": "Create one daily reminder of God's care: a short Scripture, a prayer before work or a shared practice at home. Keep it for seven days."
    },
    {
        "number": "04", "title": "Christ is the centre", "focus": "Fulfilment, reconciliation and new creation",
        "reading": "Luke 24:25-27; 2 Corinthians 5:17-21; Ephesians 1:7-10",
        "core": "Jesus is not a late answer added to the story. In Him, promise, covenant, sacrifice, kingship and new creation become visible and complete.",
        "teaching": [
            "To read Scripture through Christ is not to flatten every passage into a slogan. It is to recognise that the story is moving somewhere: toward the Son who reveals the Father, bears sin, defeats death and gathers all things under His rule.",
            "Reconciliation changes more than private guilt. It opens a new humanity. People once separated by hostility are called into one body, and the old habits of self-protection, pride and contempt are brought under the cross."
        ],
        "questions": ["What changes when Christ is the centre rather than an addition to your plans?", "Where has reconciliation become an idea instead of a practice?", "What part of your life needs to be brought under Christ's rule with greater honesty?"],
        "practice": "Read one Gospel passage this week and ask: What does this show me about the character and authority of Jesus?"
    },
    {
        "number": "05", "title": "Grace begins a new allegiance", "focus": "Repentance, faith and belonging",
        "reading": "Romans 5:6-11; Romans 6:1-14; Titus 2:11-14",
        "core": "Grace does not excuse a life from transformation. It frees people to leave the old master and learn the life of Christ in community.",
        "teaching": [
            "The Gospel announces what God has done in Christ before it asks what we should do. That order protects us from performance and despair. We do not change in order to become loved; we change because the love of God has met us truthfully.",
            "Faith therefore carries allegiance. We receive mercy, confess what is false, learn obedience and enter the life of the people of God. This is not self-salvation. It is grace becoming visible through a willing, dependent response."
        ],
        "questions": ["What does repentance look like beyond regret?", "Which old allegiance still competes with trust in Christ?", "How can a community make grace visible without making truth optional?"],
        "practice": "Write a brief prayer of honest confession. End it with one concrete response you will take, not to earn love but to live in it."
    },
    {
        "number": "06", "title": "The life within", "focus": "Mind, desire, habit and formation",
        "reading": "Romans 12:1-2; Proverbs 4:20-27; Philippians 4:8-9",
        "core": "Visible choices begin in deeper places: interpretation, desire, memory, fear and habit. Formation brings those places under the light of Christ.",
        "teaching": [
            "Not every strong reaction tells the truth about the present moment. Sometimes it reveals an old wound, a rehearsed fear or a story that has been granted too much authority. Naming that is not condemnation; it is a beginning of freedom.",
            "Renewal is patient. It happens as Scripture, prayer, worship, rest, confession and wise relationships make another way of life more familiar. Small practices are not attempts to earn God's nearness. They are ways of receiving it with greater attention."
        ],
        "questions": ["What story do you begin telling when you feel threatened or unseen?", "Which repeated practice is already forming you?", "What would it mean to bring one inner pattern into the light without shame?"],
        "practice": "When a strong reaction arrives, pause and write: What happened? What story did I tell? What would love require next?"
    },
    {
        "number": "07", "title": "A people who carry the Kingdom", "focus": "Church, gifts and public life",
        "reading": "1 Peter 2:9-12; Ephesians 4:1-16; Jeremiah 29:4-7",
        "core": "The Kingdom becomes visible in a reconciled people who carry truth, mercy, courage and useful responsibility into ordinary places.",
        "teaching": [
            "The church is not an audience gathered around a religious idea. It is a body receiving life from Christ and learning to give that life away. Different gifts do not create competing platforms; they serve the maturity of the whole people.",
            "Public faith is more than opinion. It asks how our work, speech, creativity, leadership and exchange affect the places we inhabit. Christians are not formed merely to survive their environment. They are formed to carry a different kind of presence within it."
        ],
        "questions": ["What gift or responsibility could serve the maturity of others?", "Where does your faith need to become more useful in public?", "How can a community practise conviction without contempt?"],
        "practice": "Identify one place - work, home, neighbourhood or team - where you can bring clarity, service or reconciliation this week."
    },
    {
        "number": "08", "title": "A rule of life for the next step", "focus": "Prayer, practice and durable faithfulness",
        "reading": "John 15:1-11; Colossians 3:12-17; James 1:22-25",
        "core": "A mature life is rarely built by one dramatic moment. It is built through repeated returns to Christ, truth, community and the next obedient step.",
        "teaching": [
            "A rule of life is not a rigid system for controlling God or proving spiritual seriousness. It is a simple, honest pattern that makes room for what we say matters: Scripture, prayer, rest, worship, relationships, work and service.",
            "Start smaller than your ambition. A practice that can be kept with humility is more valuable than a heroic routine abandoned in two weeks. Let your pattern serve love, not self-display. Review it with someone who can help you remain truthful."
        ],
        "questions": ["What practice would help you return to Christ before reacting?", "What limit do you need to accept in order to live more truthfully?", "Who can help you review your next step with wisdom?"],
        "practice": "Choose one daily, one weekly and one relational practice for the next thirty days. Keep them simple, specific and reviewable."
    },
]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=GOLD, tracking=1.2, spaceAfter=8))
styles.add(ParagraphStyle(name="GuideTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=29, leading=32, textColor=DEEP, spaceAfter=12))
styles.add(ParagraphStyle(name="Deck", parent=styles["Normal"], fontName="Helvetica", fontSize=12, leading=17, textColor=MUTED, spaceAfter=14))
styles.add(ParagraphStyle(name="SessionTitle", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=DEEP, spaceAfter=8))
styles.add(ParagraphStyle(name="SessionFocus", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=FOREST, spaceAfter=14))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=14, textColor=INK, spaceAfter=9))
styles.add(ParagraphStyle(name="Label", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=FOREST, spaceBefore=8, spaceAfter=4, tracking=.6))
styles.add(ParagraphStyle(name="Question", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=13, textColor=INK, leftIndent=9, firstLineIndent=-9, spaceAfter=4))
styles.add(ParagraphStyle(name="Small", parent=styles["Normal"], fontName="Helvetica", fontSize=7.8, leading=10.5, textColor=MUTED))

def cover(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(DEEP)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setStrokeColor(HexColor("#d7b853"))
    canvas.setLineWidth(.8)
    canvas.circle(w * .84, h * .82, 104 * mm, stroke=1, fill=0)
    canvas.setStrokeColor(HexColor("#376d5a"))
    canvas.circle(w * .84, h * .82, 82 * mm, stroke=1, fill=0)
    canvas.setFillColor(HexColor("#0f5844"))
    canvas.circle(w * .88, h * .18, 52 * mm, stroke=0, fill=1)
    canvas.setFillColor(GOLD)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawString(23 * mm, h - 28 * mm, "THE GREENHOUSE ASSEMBLY MINISTRIES")
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 31)
    canvas.drawString(23 * mm, h - 66 * mm, "THE")
    canvas.drawString(23 * mm, h - 80 * mm, "ARCHITECTURE")
    canvas.drawString(23 * mm, h - 94 * mm, "OF REDEMPTION")
    canvas.setFillColor(HexColor("#c8ddd3"))
    canvas.setFont("Helvetica", 11)
    canvas.drawString(23 * mm, h - 111 * mm, "A formation guide for reading Scripture as one story")
    canvas.drawString(23 * mm, h - 118 * mm, "and carrying its truth into everyday life.")
    canvas.setFillColor(GOLD)
    canvas.rect(23 * mm, 43 * mm, 23 * mm, 1.6 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(23 * mm, 33 * mm, "8 SESSIONS  /  SCRIPTURE  /  REFLECTION  /  PRACTICE")
    canvas.restoreState()

def running_page(canvas, doc):
    if doc.page == 1:
        cover(canvas, doc)
        return
    w, h = A4
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(.4)
    canvas.line(18 * mm, h - 15 * mm, w - 18 * mm, h - 15 * mm)
    canvas.setFillColor(FOREST)
    canvas.setFont("Helvetica-Bold", 7)
    canvas.drawString(18 * mm, h - 11 * mm, "THE GREENHOUSE ASSEMBLY  /  THE ARCHITECTURE OF REDEMPTION")
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawRightString(w - 18 * mm, 12 * mm, f"{doc.page - 1}")
    canvas.restoreState()

doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=24 * mm, bottomMargin=20 * mm)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([])
from reportlab.platypus import PageTemplate
doc.addPageTemplates([PageTemplate(id="Guide", frames=[frame], onPage=running_page)])

story = [Spacer(1, 1), PageBreak()]
story.extend([
    Paragraph("WELCOME", styles["Eyebrow"]),
    Paragraph("How to use this guide", styles["GuideTitle"]),
    Paragraph("This guide is designed for personal study, small groups or a teaching environment. It does not ask you to rush through Scripture. It asks you to read carefully, notice what is being formed and choose one response that can enter real life.", styles["Deck"]),
    Paragraph("A simple rhythm", styles["SessionTitle"]),
    Paragraph("1. Read the assigned passages in their own context.  2. Read the teaching section without trying to solve every question at once.  3. Discuss or journal the questions honestly.  4. Keep the practice small enough to carry for a week.  5. Return and notice what became clearer.", styles["Body"]),
    Paragraph("A note on pace", styles["Label"]),
    Paragraph("Formation is not a race for religious information. Give each session enough time to become prayer, conversation and action. If a passage exposes pain, confusion or a need for care, bring it into a trusted pastoral or professional conversation rather than carrying it alone.", styles["Body"]),
    Paragraph("Contents", styles["SessionTitle"]),
])
for s in sessions:
    story.append(Paragraph(f"{s['number']}  {s['title']} - {s['focus']}", styles["Body"]))
story.append(PageBreak())

for s in sessions:
    story.append(Paragraph(f"SESSION {s['number']}", styles["Eyebrow"]))
    story.append(Paragraph(s["title"], styles["SessionTitle"]))
    story.append(Paragraph(s["focus"], styles["SessionFocus"]))
    story.append(Paragraph("READ", styles["Label"]))
    story.append(Paragraph(s["reading"], styles["Body"]))
    story.append(Paragraph("CORE IDEA", styles["Label"]))
    story.append(Paragraph(s["core"], styles["Body"]))
    story.append(Paragraph("TEACHING", styles["Label"]))
    for para in s["teaching"]:
        story.append(Paragraph(para, styles["Body"]))
    story.append(Paragraph("REFLECT OR DISCUSS", styles["Label"]))
    for i, question in enumerate(s["questions"], 1):
        story.append(Paragraph(f"{i}. {question}", styles["Question"]))
    practice_table = Table([[Paragraph("PRACTICE FOR THE WEEK", styles["Label"]), Paragraph(s["practice"], styles["Body"])]], colWidths=[42 * mm, 118 * mm])
    practice_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), MIST), ("BOX", (0, 0), (-1, -1), .4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story.append(Spacer(1, 4))
    story.append(practice_table)
    story.append(PageBreak())

story.extend([
    Paragraph("NEXT THIRTY DAYS", styles["Eyebrow"]),
    Paragraph("A simple rule of life", styles["GuideTitle"]),
    Paragraph("Choose practices that are small enough to be honest and clear enough to be reviewed. This is not a way to earn God's favour. It is a way to make room for the life you have received in Christ.", styles["Deck"]),
    Paragraph("Daily", styles["Label"]),
    Paragraph("One short Scripture passage. One honest prayer. One moment of attention before reacting.", styles["Body"]),
    Paragraph("Weekly", styles["Label"]),
    Paragraph("One period of rest. One act of service. One conversation in which you listen before you teach or defend yourself.", styles["Body"]),
    Paragraph("Relational", styles["Label"]),
    Paragraph("Choose one trusted person to ask: What is becoming more visible in my life? What am I avoiding? What could faithfulness require next?", styles["Body"]),
    Paragraph("Closing prayer", styles["Label"]),
    Paragraph("Lord Jesus, centre us in Your life. Teach us to receive Your grace, to read Your word with patience and to carry Your truth into the places You have entrusted to us. Form in us a faithful love that becomes visible in worship, work, relationships and service. Amen.", styles["Body"]),
])

OUT.parent.mkdir(parents=True, exist_ok=True)
doc.build(story)
print(OUT)

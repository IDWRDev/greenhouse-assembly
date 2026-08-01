from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)

FOREST = colors.HexColor("#083f31")
DEEP = colors.HexColor("#052e24")
GOLD = colors.HexColor("#b79735")
CREAM = colors.HexColor("#f7f4ea")
INK = colors.HexColor("#15352b")
MUTED = colors.HexColor("#586f65")
LINE = colors.HexColor("#d8e2db")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverEyebrow", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=GOLD, alignment=TA_CENTER, spaceAfter=14, tracking=2))
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Times-Roman", fontSize=34, leading=37, textColor=colors.white, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=17, textColor=colors.HexColor("#dce9e2"), alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Times-Roman", fontSize=25, leading=29, textColor=FOREST, spaceAfter=13))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Times-Roman", fontSize=17, leading=21, textColor=FOREST, spaceBefore=9, spaceAfter=7))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=15, textColor=INK, spaceAfter=9))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.5, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="Prompt", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=14, textColor=INK, leftIndent=10, borderColor=LINE, borderWidth=0.5, borderPadding=8, backColor=CREAM, spaceAfter=8))
styles.add(ParagraphStyle(name="Quote", parent=styles["BodyText"], fontName="Times-Italic", fontSize=14, leading=20, textColor=FOREST, leftIndent=14, rightIndent=14, spaceBefore=8, spaceAfter=12))

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm, 17*mm, w-20*mm, 17*mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(20*mm, 11*mm, "THE GREENHOUSE ASSEMBLY MINISTRIES - FORMATION LIBRARY")
    canvas.drawRightString(w-20*mm, 11*mm, str(doc.page))
    canvas.restoreState()

def cover(title, subtitle, label):
    block = Table([[Paragraph(label.upper(), styles["CoverEyebrow"])], [Paragraph(title, styles["CoverTitle"])], [Paragraph(subtitle, styles["CoverSub"])]], colWidths=[160*mm], rowHeights=[35*mm, 65*mm, 42*mm])
    block.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),DEEP),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("BOX",(0,0),(-1,-1),1,GOLD),("LEFTPADDING",(0,0),(-1,-1),17*mm),("RIGHTPADDING",(0,0),(-1,-1),17*mm)]))
    return [Spacer(1, 25*mm), block, Spacer(1, 10*mm), Paragraph("Editorial preview edition - prepared for ministry review", styles["Smallx"]), PageBreak()]

def section(title, scripture, idea, prompts, practice, prayer):
    story = [Paragraph(title, styles["H1x"]), Paragraph(f"Scripture pathway: {scripture}", styles["Smallx"]), Spacer(1, 4*mm), Paragraph("Core idea", styles["H2x"]), Paragraph(idea, styles["Bodyx"]), Paragraph("Reflect together", styles["H2x"])]
    story += [Paragraph(f"{i}. {p}", styles["Prompt"]) for i, p in enumerate(prompts, 1)]
    story += [Paragraph("Practise this", styles["H2x"]), Paragraph(practice, styles["Bodyx"]), Paragraph("Prayer direction", styles["H2x"]), Paragraph(prayer, styles["Quote"]), PageBreak()]
    return story

def build(filename, title, subtitle, label, intro, sessions):
    story = cover(title, subtitle, label)
    story += [Paragraph("How to use this guide", styles["H1x"]), Paragraph(intro, styles["Bodyx"]), Paragraph("A simple rhythm", styles["H2x"]), Paragraph("Read the listed passages in your preferred Bible translation. Notice what the text reveals about God, people and faithful response. Discuss without rushing. Choose one practice for the week. Return to the next session ready to share what changed.", styles["Bodyx"]), Paragraph("Important note", styles["H2x"]), Paragraph("This is an original editorial formation guide, not a substitute for pastoral care or a final doctrinal statement. Scripture references are provided without reproduced translation text so readers can use an approved translation.", styles["Prompt"]), PageBreak()]
    for item in sessions:
        story += section(*item)
    story += [Paragraph("Continue the journey", styles["H1x"]), Paragraph("Growth becomes durable when reflection turns into repeated practice. Revisit the session that most challenged you, share one insight with a trusted person and choose one faithful action to continue for the next thirty days.", styles["Bodyx"]), Paragraph("Know. Become. Belong. Serve. Influence.", styles["Quote"]), Paragraph("greenhouseassembly.org", styles["Smallx"])]
    doc = SimpleDocTemplate(str(OUT / filename), pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=20*mm, bottomMargin=23*mm, title=title, author="The GreenHouse Assembly Ministries")
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

build("gospel-foundations-guide.pdf", "Gospel Foundations", "A four-session guide for understanding grace, new life and faithful response.", "Study guide", "Use this guide personally, with a friend or in a small group. Each session is designed for 45-60 minutes and moves from observation to reflection and practice.", [
    ("Session 1 - The good news begins with God", "Genesis 1:26-31; Psalm 8; John 1:1-5", "The Christian story begins with the goodness, wisdom and initiative of God. Identity is received before it is performed, and creation is a gift before it becomes a task.", ["What do these passages reveal about God as Creator?", "Where are you tempted to build identity only from achievement?", "What would it mean to receive life as gift this week?"], "Begin each morning by naming three gifts you have received before naming three tasks you must complete.", "God of life, teach us to receive before we strive, to worship before we work and to carry your goodness into what we build."),
    ("Session 2 - Grace meets us truthfully", "Romans 3:21-26; Luke 15:11-24; Ephesians 2:1-10", "Grace does not deny what is broken. It tells the truth about sin, restores relationship and creates a new way of living that cannot be purchased by performance.", ["How is grace different from avoidance or indulgence?", "Which part of the returning son's story is hardest for you to receive?", "How can gratitude reshape your response to God?"], "Write a short account of where grace has met you truthfully. End with one concrete expression of gratitude.", "Merciful God, free us from hiding and self-salvation. Help us receive grace with humility and live from gratitude."),
    ("Session 3 - New life has a new centre", "John 15:1-11; Galatians 2:19-20; Colossians 3:1-17", "Christian formation is not cosmetic improvement. Life is re-centred in Christ so that attention, desire, relationships and action can be reordered over time.", ["What does abiding suggest about the pace of growth?", "Which old pattern most competes for the centre of your life?", "What practice helps you remain attentive to Christ?"], "Choose one daily cue - waking, commuting or eating - and attach a two-minute prayer of attention to it.", "Christ our life, become the centre of our attention, choices and relationships. Form in us what effort alone cannot produce."),
    ("Session 4 - Formed people become sent people", "Matthew 5:13-16; 2 Corinthians 5:14-20; 1 Peter 4:8-11", "The Gospel gathers and restores people so their lives can become signs of God's reconciling love. Gifts mature through service, and influence becomes stewardship.", ["Where has God already placed you to carry life?", "Which gift can you offer without needing visibility?", "What would faithful influence look like in one relationship?"], "Perform one quiet act of service this week. Do not post about it. Pay attention to what the act reveals about your motives.", "God of mission, make our growth useful to others. Give us courage to serve, wisdom to speak and humility to remain faithful."),
])

build("life-of-prayer-7-day-guide.pdf", "A Life of Prayer", "Seven days of Scripture-shaped attention, communion and intercession.", "Devotional guide", "Set aside 15-20 quiet minutes each day. Read slowly, sit with one question and complete the practice. The goal is not volume but a more attentive life with God.", [
    ("Day 1 - Arrive", "Psalm 46; Matthew 11:28-30", "Prayer begins by becoming present to the God who is already present. We bring the life we actually have, not the life we wish we could display.", ["What noise are you carrying into prayer?", "What would honest arrival sound like today?"], "Sit in silence for three minutes. Name what is present without trying to solve it.", "God, I arrive as I am. Quiet what is false and awaken me to your presence."),
    ("Day 2 - Listen", "1 Samuel 3:1-10; John 10:1-5", "Listening is not passivity. It is trained attention shaped by Scripture, humility and a willingness to obey what is good.", ["What competes most strongly for your attention?", "How can Scripture test what you think you hear?"], "Read one passage aloud twice. Record the phrase that invites faithful response.", "Speak, Lord. Give me humility to listen and wisdom to recognise your truth."),
    ("Day 3 - Ask", "Matthew 6:5-13; Philippians 4:4-7", "Petition brings real need before God without performance. Jesus teaches prayer that reorders desire around God's name, Kingdom, provision, mercy and protection.", ["Which request in the Lord's Prayer do you avoid?", "What need can you name plainly today?"], "Write five requests in one sentence each. Leave space beneath them to record perspective, not only outcomes.", "Father, give what is needed, reorder what is wanted and keep me faithful while I wait."),
    ("Day 4 - Confess", "Psalm 51:1-12; 1 John 1:5-9", "Confession is truthful return. It refuses both hiding and despair because mercy makes honest change possible.", ["What are you tempted to minimise?", "What repair may need to follow confession?"], "Name one specific failure without excuse. Identify one person or practice involved in repair.", "Merciful God, bring me into the light. Clean what is distorted and restore a willing spirit."),
    ("Day 5 - Give thanks", "Psalm 103:1-5; Luke 17:11-19", "Gratitude trains attention to recognise gift, grace and sustaining mercy. It resists entitlement without denying grief.", ["Which ordinary gift have you stopped noticing?", "How can gratitude coexist with lament?"], "Record ten concrete gifts from the last twenty-four hours. Thank one person directly.", "Giver of every good gift, keep my heart awake to grace and generous in response."),
    ("Day 6 - Intercede", "1 Timothy 2:1-6; Ephesians 3:14-21", "Intercession carries people and places before God with love. It expands prayer beyond private concerns and teaches patient solidarity.", ["Who is easy for you to forget?", "Which public concern needs sustained rather than reactive prayer?"], "Pray through five circles: household, community, leaders, those suffering and the Church.", "God of all people, widen my concern and teach me to carry others with hope."),
    ("Day 7 - Remain", "John 15:4-11; Colossians 4:2-6", "A life of prayer is built through return. Faithfulness grows through small rhythms that keep communion connected to speech, work and relationships.", ["Which practice from this week is sustainable?", "What time and place will help you return?"], "Design a simple weekly rhythm: a daily moment, a weekly longer space and one shared prayer practice.", "Christ, teach me to remain. Let prayer become attention, obedience and love throughout ordinary life."),
])

build("leadership-before-visibility-guide.pdf", "Leadership Before Visibility", "A four-session reflection guide for character, stewardship and service.", "Leadership guide", "This guide is for emerging leaders, volunteers, creative teams and anyone carrying responsibility. It prioritises inner formation and healthy service over platform-building.", [
    ("Session 1 - Character before platform", "1 Samuel 16:1-13; Luke 16:10-12", "Public usefulness cannot outrun private formation indefinitely. Faithfulness in unseen places creates the capacity to carry visible responsibility without being consumed by it.", ["Which unseen habits currently shape your leadership?", "Where are you seeking recognition before readiness?", "Who has permission to ask you honest questions?"], "Choose one hidden responsibility and practise it consistently for thirty days without announcing it.", "God, form in secret what can remain faithful in public. Make integrity stronger than appetite for recognition."),
    ("Session 2 - Service before status", "Mark 10:35-45; John 13:1-17", "Jesus reframes greatness through service. Authority becomes responsibility for the good of others, not permission to make others serve the leader's image.", ["Who benefits most from the way you currently lead?", "Which task feels beneath you?", "How can you make another person's contribution more fruitful?"], "Complete one necessary, low-visibility task that removes friction for your team or household.", "Servant King, free us from status-seeking. Teach us to use strength for the flourishing of others."),
    ("Session 3 - Wisdom before speed", "Proverbs 15:22; James 1:19-20; Luke 14:28-30", "Urgency can mimic importance. Wise leadership listens, seeks counsel, counts cost and knows when a slower decision protects people and purpose.", ["What decision are you rushing?", "Whose perspective is missing?", "What cost has not yet been named?"], "Before one meaningful decision, write what you know, what you assume, who is affected and who should be consulted.", "God of wisdom, slow what is impulsive, clarify what is confused and give us courage to wait for what is true."),
    ("Session 4 - Stewardship before scale", "Matthew 25:14-30; 1 Peter 4:8-11", "Scale is not the same as fruitfulness. Stewardship asks whether people, gifts, trust, time and resources are being handled faithfully at the size they are now.", ["What has already been entrusted to you?", "Where is growth creating strain or neglect?", "Which boundary would protect long-term faithfulness?"], "Create a stewardship inventory for time, relationships, money, gifts and responsibility. Choose one repair.", "Faithful God, teach us to tend what is entrusted before asking for more. Make our influence responsible, generous and sustainable."),
])

print(f"Built PDFs in {OUT}")

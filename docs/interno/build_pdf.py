# -*- coding: utf-8 -*-
import re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

SRC, OUT = sys.argv[1], sys.argv[2]

BRAND  = colors.HexColor("#1F4435")
ACCENT = colors.HexColor("#D96A2B")
INK    = colors.HexColor("#16211B")
INK2   = colors.HexColor("#3D4B43")
MUTED  = colors.HexColor("#6D7A71")
LINE   = colors.HexColor("#DDE4D8")
SOFT   = colors.HexColor("#EFF3EA")
BSOFT  = colors.HexColor("#E4EDE4")
WARNBG = colors.HexColor("#F8EED6")
WARN   = colors.HexColor("#9A6A08")

BODY, BOLD, ITAL = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
MONO = "Courier"

S = {
 "h1": ParagraphStyle("h1", fontName=BOLD, fontSize=23, leading=27, textColor=BRAND,
                      spaceBefore=0, spaceAfter=4),
 "sub": ParagraphStyle("sub", fontName=BODY, fontSize=13, leading=17, textColor=INK2, spaceAfter=14),
 "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=13.5, leading=17, textColor=BRAND,
                      spaceBefore=17, spaceAfter=7),
 "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=11, leading=14, textColor=INK,
                      spaceBefore=11, spaceAfter=4),
 "p": ParagraphStyle("p", fontName=BODY, fontSize=9.6, leading=14.2, textColor=INK2,
                     spaceAfter=7, alignment=TA_LEFT),
 "li": ParagraphStyle("li", fontName=BODY, fontSize=9.6, leading=14.2, textColor=INK2,
                      leftIndent=13, bulletIndent=3, spaceAfter=4),
 "quote": ParagraphStyle("quote", fontName=BODY, fontSize=9.4, leading=13.6, textColor=INK2,
                         leftIndent=9, rightIndent=7, spaceBefore=3, spaceAfter=3),
 "th": ParagraphStyle("th", fontName=BOLD, fontSize=8.1, leading=10.6, textColor=MUTED),
 "thr": ParagraphStyle("thr", fontName=BOLD, fontSize=8.1, leading=10.6, textColor=MUTED, alignment=TA_RIGHT),
 "td": ParagraphStyle("td", fontName=BODY, fontSize=8.9, leading=12.2, textColor=INK2),
 "tdr": ParagraphStyle("tdr", fontName=BODY, fontSize=8.9, leading=12.2, textColor=INK2, alignment=TA_RIGHT),
 "meta": ParagraphStyle("meta", fontName=BODY, fontSize=9, leading=13, textColor=MUTED, spaceAfter=3),
}

def inline(t):
    t = t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    t = re.sub(r'\*\*(.+?)\*\*', r'<font name="%s" color="#16211B">\1</font>' % BOLD, t)
    t = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', r'<font name="%s">\1</font>' % MONO, t)
    t = re.sub(r'\[(.+?)\]\((.+?)\)', r'<link href="\2" color="#1F4435">\1</link>', t)
    return t

def split_row(r):
    return [c.strip() for c in r.strip().strip("|").split("|")]

def build_table(rows, width):
    head, body = rows[0], rows[1:]
    n = len(head)
    sin_encabezado = not any(c.strip() for c in head)
    if sin_encabezado:
        head, body = body[0], body[1:]
        rows = rows[1:]
    right = [False]*n
    data = []
    data.append([Paragraph(inline(c), S["th"]) for c in head])
    for r in body:
        cells = (r + [""]*n)[:n]
        for i,c in enumerate(cells):
            if re.match(r'^\**\$?[\d,\.]+\s*%?\**$', c.strip()) or c.strip().endswith("%"):
                right[i] = right[i] or (i > 0)
        data.append(cells)
    for i in range(n):
        data[0][i] = Paragraph(inline(head[i]),
                               (S["tdr"] if right[i] else S["td"]) if sin_encabezado
                               else (S["thr"] if right[i] else S["th"]))
    for ri in range(1, len(data)):
        data[ri] = [Paragraph(inline(c), S["tdr"] if right[i] else S["td"])
                    for i,c in enumerate(data[ri])]
    if n == 1:   first = 1.0
    elif n == 2: first = 0.60
    elif n == 3: first = 0.60
    else:        first = max(0.30, 1.0 - 0.15*(n-1))
    rest = (1.0-first)/(n-1) if n > 1 else 0
    cw = [width*first] + [width*rest]*(n-1)
    t = Table(data, colWidths=cw, repeatRows=0 if sin_encabezado else 1, hAlign="LEFT")
    st = [("VALIGN",(0,0),(-1,-1),"TOP"),
          ("TOPPADDING",(0,0),(-1,0),7 if sin_encabezado else 5.5),
          ("TOPPADDING",(0,0),(-1,-1),5.5),("BOTTOMPADDING",(0,0),(-1,-1),5.5),
          ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7)]
    if not sin_encabezado:
        st.append(("BACKGROUND",(0,0),(-1,0),SOFT))
        st.append(("LINEBELOW",(0,0),(-1,0),0.7,LINE))
    for ri in range((0 if sin_encabezado else 1), len(data)):
        st.append(("LINEBELOW",(0,ri),(-1,ri),0.35,LINE))
    return Table([[t]], colWidths=[width], hAlign="LEFT",
                 style=[("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),4)])

def callout(lines, width, bg, border):
    inner = [Paragraph(inline(l), S["quote"]) for l in lines]
    t = Table([[inner]], colWidths=[width])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),
                           ("LINEBEFORE",(0,0),(0,-1),2.2,border),
                           ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                           ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
    return t

raw = open(SRC, encoding="utf-8").read()
# fuera la nota interna
raw = re.sub(r'^> \*\*NOTA INTERNA.*?\n---\n', '', raw, flags=re.S)
lines = raw.split("\n")

W = letter[0] - 2*20*mm
story, i = [], 0
while i < len(lines):
    ln = lines[i]
    st = ln.strip()
    if not st:
        i += 1; continue
    if st.startswith("|") and i+1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
        rows = [split_row(st)]
        i += 2
        while i < len(lines) and lines[i].strip().startswith("|"):
            rows.append(split_row(lines[i].strip())); i += 1
        story.append(build_table(rows, W)); continue
    if st.startswith(">"):
        blk = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            blk.append(lines[i].strip().lstrip(">").strip()); i += 1
        story.append(Spacer(1,3))
        story.append(callout([" ".join(blk)], W, WARNBG, WARN))
        story.append(Spacer(1,7)); continue
    if st == "---":
        story.append(Spacer(1,4))
        story.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=2, spaceAfter=8))
        i += 1; continue
    if st.startswith("# "):
        story.append(Paragraph(inline(st[2:]), S["h1"])); i += 1; continue
    if st.startswith("### "):
        story.append(Paragraph(inline(st[4:]), S["sub"] if len(story)<4 else S["h3"])); i += 1; continue
    if st.startswith("## "):
        story.append(Paragraph(inline(st[3:]), S["h2"])); i += 1; continue
    if re.match(r'^[-*] ', st):
        while i < len(lines) and re.match(r'^[-*] ', lines[i].strip()):
            txt = lines[i].strip()[2:]
            i += 1
            while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() and not re.match(r'^[-*] |^\d+\. ', lines[i].strip()):
                txt += " " + lines[i].strip(); i += 1
            story.append(Paragraph(inline(txt), S["li"], bulletText="•"))
        story.append(Spacer(1,4)); continue
    if re.match(r'^\d+\. ', st):
        while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
            m = re.match(r'^(\d+)\. (.*)$', lines[i].strip())
            num, txt = m.group(1), m.group(2)
            i += 1
            while i < len(lines) and lines[i].startswith("   ") and lines[i].strip() and not re.match(r'^\d+\. ', lines[i].strip()):
                txt += " " + lines[i].strip(); i += 1
            story.append(Paragraph(inline(txt), S["li"], bulletText=num+"."))
        story.append(Spacer(1,4)); continue
    para = [st]; i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|-|\*|\d+\.|---)', lines[i].strip()):
        para.append(lines[i].strip()); i += 1
    sty = S["meta"] if len(story) < 5 and para[0].startswith("**Preparada") else S["p"]
    story.append(Paragraph(inline(" ".join(para)), sty))

def deco(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BRAND)
    canvas.rect(0, letter[1]-6*mm, letter[0], 6*mm, stroke=0, fill=1)
    canvas.setFont(BODY, 7.4); canvas.setFillColor(MUTED)
    canvas.drawString(20*mm, 12*mm, "monclair  ·  Propuesta para Healthy Tummies")
    canvas.drawRightString(letter[0]-20*mm, 12*mm, "%d" % doc.page)
    canvas.setStrokeColor(LINE); canvas.setLineWidth(0.5)
    canvas.line(20*mm, 16*mm, letter[0]-20*mm, 16*mm)
    canvas.restoreState()

doc = BaseDocTemplate(OUT, pagesize=letter,
                      leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=22*mm,
                      title="Propuesta · Plataforma de inscripción y cobro · Healthy Tummies",
                      author="monclair", subject="Propuesta comercial")
doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(doc.leftMargin, doc.bottomMargin,
                      doc.width, doc.height, id="f")], onPage=deco)])
doc.build(story)
print("PDF generado:", OUT)

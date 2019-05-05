from copy import copy

from reportlab.lib.enums import TA_RIGHT, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Table

document = SimpleDocTemplate("file.pdf")
flowables = []

style_sheet = getSampleStyleSheet()

flowables.append(Image("logojs.png", hAlign="LEFT", width=200, height=50, kind="proportional"))

custom_body_text_style_sheet = copy(style_sheet["BodyText"])
custom_body_text_style_sheet.textColor = "grey"
flowables.append(
    Paragraph(
        "<br/>Jestocke.com<br/>12 rue Théodore Ducos<br/>33000 Bordeaux<br/>01.76.42.00.1<br/>contact@jestocke.com",
        custom_body_text_style_sheet,
    )
)

custom_body_text_style_sheet = copy(style_sheet["BodyText"])
print(custom_body_text_style_sheet.listAttrs())
custom_body_text_style_sheet.alignment = TA_RIGHT
flowables.append(Paragraph("M. Firstname LASTNAME<br/>42 rue aléatoire<br/>75000 Paris", custom_body_text_style_sheet))

custom_body_text_style_sheet = copy(style_sheet["BodyText"])
custom_body_text_style_sheet.alignment = TA_RIGHT
flowables.append(
    Paragraph(
        "<br/><br/><br/><br/><br/><br/>Bordeaux, le 01/04/2042<br/>Facture n° BS-2019-01-001<br/><br/><br/><br/><br/>",
        custom_body_text_style_sheet,
    )
)

flowables.append(
    Table(
        (
            ("Désignation", "Montant HT"),
            ("Mise à disposition d'un nouveau bip d'accès et d'une nouvelle clé suite à perte", "91.67€"),
        ),
        hAlign="LEFT",
    )
)

document.build(flowables)

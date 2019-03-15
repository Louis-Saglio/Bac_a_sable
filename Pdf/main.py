import PyPDF2
import io
import reportlab.pdfgen.canvas
import reportlab.lib.pagesizes

# Nom complet locataire     l: 175, h: 715
# Nom complet propriétaire  l: 375, h: 715
# Né le                        175     700
# Né le                        375     700
# Telephone                    175     685
# Telephone                    375     685
# Address1                     175     670
# Address1                     375     670
# Address2                     175     656.5
# Address2                     375     656.5


packet = io.BytesIO()
canvas = reportlab.pdfgen.canvas.Canvas(packet, reportlab.lib.pagesizes.letter)
canvas.drawString(175, 715, "000000000")
canvas.drawString(375, 715, "000000000")
canvas.drawString(175, 700, "111111111")
canvas.drawString(375, 700, "111111111")
canvas.drawString(175, 685, "222222222")
canvas.drawString(375, 685, "222222222")
canvas.drawString(175, 670, "333333333")
canvas.drawString(375, 670, "333333333")
canvas.drawString(175, 656.5, "444444444")
canvas.drawString(375, 656.5, "444444444")
canvas.drawString(175, 640, "555555555")
canvas.drawString(375, 640, "555555555")
canvas.drawString(175, 625, "666666666")
canvas.drawString(375, 625, "666666666")

canvas.drawString(175, 564, "777777777")
canvas.drawString(175, 549, "888888888")
canvas.drawString(175, 535, "999999999")
canvas.drawString(175, 519.6, "000000000")
canvas.drawString(175, 504, "111111111")
canvas.drawString(175, 491, "222222222")

canvas.drawString(175, 430, "333333333")
canvas.drawString(175, 414, "444444444")
canvas.drawString(175, 399, "555555555")
canvas.drawString(175, 384, "666666666")
canvas.drawString(175, 370, "777777777")

canvas.drawString(108, 329, "888888888")

canvas.drawString(49, 208.5, "x")
canvas.drawString(49.2, 193, "x")
canvas.drawString(49.2, 179, "x")

canvas.drawString(110, 181, "99999999")

canvas.drawString(49, 81, "00")
canvas.drawString(73, 81, "11")
canvas.drawString(100, 81, "2222")

canvas.save()

packet.seek(0)
new_pdf = PyPDF2.PdfFileReader(packet)

output = PyPDF2.PdfFileWriter()

with open("contrat.pdf", "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    page0, page1, page2 = reader.getPage(0), reader.getPage(1), reader.getPage(2)
    page0.mergePage(new_pdf.getPage(0))

    output.addPage(page0)
    output.addPage(page1)
    output.addPage(page2)

    with open("final.pdf", "wb") as final:
        output.write(final)

__author__ = "https://stackoverflow.com/users/705945/david-dehghan"
__source__ = "https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python"


from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()
packet.seek(0)
watermark = PdfFileReader(packet)

original = open("contrat.pdf", "rb")
existing_pdf = PdfFileReader(original)

output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(watermark.getPage(0))
output.addPage(page)

output.addPage(existing_pdf.getPage(1))
output.addPage(existing_pdf.getPage(2))

outputStream = open("destination.pdf", "wb")
output.write(outputStream)

outputStream.close()
original.close()

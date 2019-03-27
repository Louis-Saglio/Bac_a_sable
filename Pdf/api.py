import io
from collections import namedtuple
from typing import Dict, Any, Tuple

import PyPDF2
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas
from PyPDF2.pdf import PageObject

PdfTemplateVariable = namedtuple("PdfTemplateVariable", ("name", "line_size"))


PageData = Dict[Tuple[int, int], PdfTemplateVariable]


def build_filled_pdf_page(page_data: PageData, values: Dict[str, Any]) -> PageObject:
    packet = io.BytesIO()
    canvas = reportlab.pdfgen.canvas.Canvas(
        packet, reportlab.lib.pagesizes.letter, initialFontName="Times-Roman", initialFontSize=14
    )
    for position, emplacement_data in page_data.items():
        canvas.drawString(*position, str(values.get(emplacement_data.name, ""))[: emplacement_data.line_size])
    canvas.showPage()
    canvas.save()
    packet.seek(0)
    return PyPDF2.PdfFileReader(packet).getPage(0)


class PdfTemplate:
    def __init__(self, base_file_path: str, emplacements: Dict[int, PageData]):
        self.base_file_path = base_file_path
        self.emplacements = emplacements

    def render(self, **values: Any) -> PyPDF2.PdfFileWriter:
        output = PyPDF2.PdfFileWriter()

        reader = PyPDF2.PdfFileReader(self.base_file_path)

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            # Intersection of the possible variable names and the actual given ones
            if set(values).intersection({line.name for line in self.emplacements.get(page_num, {}).values()}):
                page.mergePage(build_filled_pdf_page(self.emplacements[page_num], values))
            output.addPage(page)

        return output

import io
from typing import Set, Dict, Any, Tuple

import PyPDF2
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas


class PdfTemplateVariable:
    def __init__(self, name: str, line_size: int):
        self.name = name
        self.line_size = line_size


PageData = Dict[Tuple[int, int], PdfTemplateVariable]


def build_filled_pdf_page(page_data: PageData, values: Dict[str, Any]) -> PyPDF2.PdfFileReader:
    packet = io.BytesIO()
    canvas = reportlab.pdfgen.canvas.Canvas(
        packet, reportlab.lib.pagesizes.letter, initialFontName="Times-Roman", initialFontSize=14
    )
    for position, emplacement_data in page_data.items():
        canvas.drawString(*position, str(values[emplacement_data.name])[:emplacement_data.line_size])
    canvas.save()
    packet.seek(0)
    return PyPDF2.PdfFileReader(packet)


class PdfTemplate:
    def __init__(self, base_file_path: str, emplacements: Dict[int, PageData]):
        self.base_file_path = base_file_path
        self.emplacements = emplacements

    def get_pages_to_fill_numbers(self, values: Dict[str, Any]) -> Set[int]:
        """
        Returns a set containing the numbers of the pages having to be filled by at least one value of values
        """
        pages_to_fill = set()
        for page_num, page_data in self.emplacements.items():
            for emplacement_data in page_data.values():
                if emplacement_data.name in values:
                    pages_to_fill.add(page_num)
                    break
        return pages_to_fill

    def render(self, **values: Any) -> PyPDF2.PdfFileWriter:
        pages_to_fill = self.get_pages_to_fill_numbers(values)

        output = PyPDF2.PdfFileWriter()

        with open(self.base_file_path, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)

            for page_num in range(reader.getNumPages()):
                page = reader.getPage(page_num)
                if page_num in pages_to_fill:
                    page.mergePage(build_filled_pdf_page(self.emplacements[page_num], values).getPage(0))
                output.addPage(page)

            # For debug purposes. Remove in production.
            with open("out.pdf", "wb") as final:
                output.write(final)

        return output

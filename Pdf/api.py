import io

import PyPDF2
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas


class PdfException(Exception):
    pass


class PdfTemplate:
    def __init__(self, base_file_path, emplacements):
        self.base_file_path = base_file_path
        self.emplacements_available = emplacements
        self.pages_to_fill = set()

    def __setitem__(self, key, value):
        # Comment stocker la valeur donnée pour remplir un emplacement ? Stocker dans le dictionnaire emplacements ?
        # Mais alors, comment savoir s'il faut modifier une page ?
        variable_exists = False
        for page_num, page_data in self.emplacements_available.items():
            for emplacement_data in page_data.values():
                for variable_data in emplacement_data:
                    if variable_data["name"] == key:
                        if not variable_exists:
                            variable_exists = True
                        variable_data["value"] = value
                        self.pages_to_fill.add(page_num)
        if not variable_exists:
            raise PdfException("There is no emplacement named '{}' in this PDF template".format(key))

    def _fill_emplacements_of_page(self, canvas, page_num):
        for position, emplacement_data in self.emplacements_available[page_num].items():
            for variable_data in emplacement_data:
                if "value" in variable_data:
                    canvas.drawString(*position, variable_data["value"])

    def _build_watermark_pdf_filled_with_values_for_page(self, page_num):
        packet = io.BytesIO()
        canvas = reportlab.pdfgen.canvas.Canvas(
            packet, reportlab.lib.pagesizes.letter, initialFontName="Times-Roman", initialFontSize=14
        )
        for position, emplacement_data in self.emplacements_available[page_num].items():
            for variable_data in emplacement_data:
                if "value" in variable_data:
                    canvas.drawString(*position, variable_data["value"])
        canvas.save()
        packet.seek(0)
        return PyPDF2.PdfFileReader(packet)

    def render(self):
        output = PyPDF2.PdfFileWriter()

        with open(self.base_file_path, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)

            for page_num in range(reader.getNumPages()):
                page = reader.getPage(page_num)
                if page_num in self.pages_to_fill:
                    page.mergePage(self._build_watermark_pdf_filled_with_values_for_page(page_num).getPage(0))
                output.addPage(page)

            # For debug purposes. Remove in production.
            with open("out.pdf", "wb") as final:
                output.write(final)

        return output

import io

import PyPDF2
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas


class PdfException(Exception):
    pass


class PdfTemplate:
    def __init__(self, base_file_path, output_file_path, emplacements):
        self.base_file_path = base_file_path
        self.output_file_path = output_file_path
        self.emplacements = emplacements
        self.values = {name: None for name in self.emplacements}

    def __setitem__(self, key, value):
        if key in self.emplacements:
            self.values[key] = value
        else:
            raise PdfException("There is no emplacement named {} in this PDF template".format(key))

    def _fill_emplacements(self, canvas, page_num):
        for name, value in self.values.items():
            if value is None:
                continue
            emplacement_data = self.emplacements[name]
            line_nbr = len(emplacement_data)
            for line_num in range(line_nbr):
                if emplacement_data[line_num][0] != page_num:
                    continue
                line_size = emplacement_data[line_num][3]
                chunk = value[line_size * line_num: (line_size * line_num + line_size)]
                if chunk:
                    canvas.drawString(*emplacement_data[line_num][1:3], chunk)
        canvas.save()

    def _build_watermark_pdf_filled_with_values_for_page(self, page_num):
        packet = io.BytesIO()
        canvas = reportlab.pdfgen.canvas.Canvas(packet, reportlab.lib.pagesizes.letter)
        self._fill_emplacements(canvas, page_num)
        packet.seek(0)
        return PyPDF2.PdfFileReader(packet)

    def render(self):
        output = PyPDF2.PdfFileWriter()

        with open(self.base_file_path, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)

            for page_num in range(reader.getNumPages()):
                page = reader.getPage(page_num)
                watermark = self._build_watermark_pdf_filled_with_values_for_page(page_num)
                if watermark.getNumPages() > 0:
                    # A strange behaviour of PyPDF makes PdfFileReader built with a blank canvas contains no page at all
                    # It is useful to check if there is anything we need to add to the actual pdf page
                    page.mergePage(watermark.getPage(0))
                output.addPage(page)

            with open(self.output_file_path, "wb") as final:
                output.write(final)

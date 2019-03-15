import PyPDF2
import io
import reportlab.pdfgen.canvas
import reportlab.lib.pagesizes


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

    def _fill_emplacements(self, canvas):
        for name, value in self.values.items():
            emplacement_data = self.emplacements[name]
            line_nbr = len(emplacement_data)
            for line_num in range(line_nbr):
                line_size = emplacement_data[line_num][2]
                if value is not None:
                    chunk = value[line_size*line_num:(line_size*line_num+line_size)]
                    if chunk:
                        canvas.drawString(*emplacement_data[line_num][:2], chunk)
        canvas.save()

    def render(self):
        packet = io.BytesIO()
        canvas = reportlab.pdfgen.canvas.Canvas(packet, reportlab.lib.pagesizes.letter)
        self._fill_emplacements(canvas)

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        output = PyPDF2.PdfFileWriter()

        with open(self.base_file_path, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)
            page0, page1, page2 = reader.getPage(0), reader.getPage(1), reader.getPage(2)
            page0.mergePage(new_pdf.getPage(0))

            output.addPage(page0)
            output.addPage(page1)
            output.addPage(page2)

            with open(self.output_file_path, "wb") as final:
                output.write(final)

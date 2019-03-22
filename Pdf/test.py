import unittest

from Pdf import api


class TestPdfTemplate(unittest.TestCase):
    def test_simple_template(self):
        template = api.PdfTemplate(
            base_file_path="contrat.pdf",
            emplacements={
                0: {
                    (175, 715): {"name": "tenant_full_name", "line_size": 30},
                    (175, 600): {"name": "tenant_address", "line_size": 30},
                },
                1: {(175, 600): {"name": "owner_full_name", "line_size": 10}},
            },
        )
        template.render(
            tenant_full_name="Louis Saglio", tenant_address="lorem ipsum address", owner_full_name="Jean Dupont"
        )

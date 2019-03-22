import Pdf.api as api
from Pdf.api import PdfTemplateVariable

template = api.PdfTemplate(
    base_file_path="contrat.pdf",
    emplacements={
        0: {
            (175, 715): PdfTemplateVariable(name="tenant_full_name", line_size=30),
            (175, 600): PdfTemplateVariable(name="tenant_address", line_size=30),
            (175, 400): PdfTemplateVariable(name="owner_full_name", line_size=30),
        },
        1: {(175, 600): PdfTemplateVariable(name="owner_full_name", line_size=10)},
    },
)

template.render(tenant_full_name="Louis Saglio", tenant_address="lorem ipsum address", owner_full_name=None)

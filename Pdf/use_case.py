import Pdf.api as api
from Pdf.api import PdfTemplateVariable

template = api.PdfTemplate(
    base_file_path="contrat.pdf",
    emplacements={
        0: {
            (175, 715): PdfTemplateVariable(name="tenant_full_name", line_size=30),
            (375, 715): PdfTemplateVariable(name="owner_full_name", line_size=30),
            (175, 700): PdfTemplateVariable(name="tenant_phone_number", line_size=30),
            (375, 700): PdfTemplateVariable(name="owner_phone_number", line_size=30),
            (175, 685): PdfTemplateVariable(name="tenant_address_1", line_size=30),
            (175, 656.5): PdfTemplateVariable(name="tenant_address_2", line_size=30),
            (375, 685): PdfTemplateVariable(name="owner_address_1", line_size=30),
            (375, 656.5): PdfTemplateVariable(name="owner_address_2", line_size=30),
            (175, 640): PdfTemplateVariable(name="tenant_postal_code", line_size=30),
            (375, 640): PdfTemplateVariable(name="owner_postal_code", line_size=30),
            (175, 625): PdfTemplateVariable(name="tenant_city", line_size=30),
            (375, 625): PdfTemplateVariable(name="owner_city", line_size=30),
            (175, 564): PdfTemplateVariable(name="storage_type", line_size=60),
            (175, 549): PdfTemplateVariable(name="storage_dimensions", line_size=60),
            (175, 535): PdfTemplateVariable(name="storage_address_1", line_size=60),
            (175, 519.6): PdfTemplateVariable(name="storage_address_2", line_size=60),
            (175, 504): PdfTemplateVariable(name="storage_address_3", line_size=60),
            (175, 491): PdfTemplateVariable(name="access_conditions", line_size=60),
            (175, 430): PdfTemplateVariable(name="start_date", line_size=60),
            (175, 414): PdfTemplateVariable(name="end_date", line_size=60),
            (175, 378): PdfTemplateVariable(name="owner_rent_control", line_size=60),
            (108, 329): PdfTemplateVariable(name="owner_full_name", line_size=30),
        }
    },
)

with open("out.pdf", "wb") as f:
    out = template.render(
        tenant_full_name="Louis Saglio",
        tenant_address_1="lorem ipsum address",
        owner_full_name="Jean Dupont",
        tenant_address_2="210 cours Victor Hugo",
        tenant_city="Langon"
    )
    out.write(f)

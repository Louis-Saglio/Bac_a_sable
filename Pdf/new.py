import Pdf.api as api


template = api.PdfTemplate(
    base_file_path="contrat.pdf",
    output_file_path="out.pdf",
    emplacements={
        # emplacement_name": ((page_num, x, y, max_size), (same but for line 2), (same but for line x))
        "tenant_full_name": ((0, 175, 715, 27),),
        "owner_full_name": ((0, 375, 715, 27),),
        "tenant_birthday": ((0, 175, 700, 27),),
        "owner_birthday": ((0, 375, 700, 27),),
        "tenant_phone": ((0, 175, 685, 27),),
        "owner_phone": ((0, 375, 685, 27),),
        "tenant_address": ((0, 175, 670, 27), (0, 175, 656.5, 27)),
        "owner_address": ((0, 374, 670, 26), (0, 374, 656.5, 26)),
        "tenant_postal_code": ((0, 175, 640, 27),),
        "owner_postal_code": ((0, 375, 640, 27),),
        "tenant_city": ((0, 175, 625, 27),),
        "owner_city": ((0, 375, 625, 27),),
        "storage_type": ((0, 175, 564, 60),),
        "storage_size": ((0, 175, 549, 60),),
        "storage_address": ((0, 175, 535, 5), (1, 175, 519.6, 6), (2, 175, 504, 60)),
        "access_conditions": ((175, 491, 60),),
        "start_date": ((0, 175, 430, 60),),
        "end_date": ((0, 175, 414, 60),),
        "booked_surface": ((0, 175, 399, 60),),
        "owner_share": ((0, 175, 378, 60),),
        "undersigned_tenant": ((0, 108, 329, 25),),
        "has_photocopy": ((0, 49, 208.5, 1),),
        "has_proof of residence": ((0, 49, 193, 1),),
        "surety bond": ((0, 49, 179, 1),),
        "signature date_day": ((0, 49, 81, 2),),
        "signature date_month": ((0, 73, 81, 2),),
        "signature date_year": ((0, 100, 81, 4),),
    },
)

template["tenant_full_name"] = "Louis Saglio"
template["owner_full_name"] = "Jean Dupont"
template["tenant_birthday"] = "07/09/1998"
template["tenant_address"] = "lorem ipsum dolor sit amet donec adipiscing consequetur etiam"
template["owner_address"] = "smerjognf  ojsfdngvo osdij fôsijfdôsrigjôijsfog ijpij insdfunv usdf"
template["storage_address"] = "smerjognf  ojsfdngvo osdij fôsijfdôsrigjôijsfog ijpij insdfunv usdf"

template.render()

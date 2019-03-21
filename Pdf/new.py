import Pdf.api as api


template = api.PdfTemplate(
    "contrat.pdf",
    "out.pdf",
    {
        "tenant_full_name": ((175, 715, 27),),
        "owner_full_name": ((375, 715, 27),),
        "tenant_birthday": ((175, 700, 27),),
        "owner_birthday": ((375, 700, 27),),
        "tenant_phone": ((175, 685, 27),),
        "owner_phone": ((375, 685, 27),),
        "tenant_address": ((175, 670, 27), (175, 656.5, 27)),
        "owner_address": ((374, 670, 26), (374, 656.5, 26)),
        "tenant_postal_code": ((175, 640, 27),),
        "owner_postal_code": ((375, 640, 27),),
        "tenant_city": ((175, 625, 27),),
        "owner_city": ((375, 625, 27),),
        "storage_type": ((175, 564, 60),),
        "storage_size": ((175, 549, 60),),
        "storage_address": ((175, 535, 60), (175, 519.6, 60), (175, 504, 60)),
        "access_conditions": ((175, 491, 60),),
        "start_date": ((175, 430, 60),),
        "end_date": ((175, 414, 60),),
        "booked_surface": ((175, 399, 60),),
        "owner_share": ((175, 378, 60),),
        "undersigned_tenant": ((108, 329, 25),),
        "has_photocopy": ((49, 208.5, 1),),
        "has_proof of residence": ((49, 193, 1),),
        "surety bond": ((49, 179, 1),),
        "signature date_day": ((49, 81, 2),),
        "signature date_month": ((73, 81, 2),),
        "signature date_year": ((100, 81, 4),),
    },
)

template["tenant_full_name"] = "Louis Saglio"
template["owner_full_name"] = "Laure Courty"
template["tenant_birthday"] = "07/09/1998"
template["tenant_address"] = "lorem ipsum dolor sit amet donec adipiscing consequetur etiam"
template["owner_address"] = "smerjognf  ojsfdngvo osdij fôsijfdôsrigjôijsfog ijpij insdfunv usdf"

template.render()

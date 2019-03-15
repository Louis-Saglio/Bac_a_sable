import Pdf.api as api


template = api.PdfTemplate(
    "contrat.pdf",
    "final.pdf",
    {
        "tenant_full_name": ((175, 715, 27),),
        "owner_full_name": ((375, 715, 27),),
        "tenant_birthday": ((175, 700, 27),),
        "owner_birthday": ((375, 700, 27),),
        "tenant_phone": ((175, 685, 27),),
        "owner_phone": ((375, 685, 27),),
        "tenant_address": ((175, 670, 27), (175, 656.5, 27)),
        "owner_address": ((374, 670, 26), (374, 656.5, 26)),
    },
)

template["tenant_full_name"] = "Louis Saglio"
template["owner_full_name"] = "Laure Courty"
template["tenant_birthday"] = "07/09/1998"
template["tenant_address"] = "111111111111111111111111111111111111111111111111111111111111111111111111"
template["owner_address"] = "111111111111111111111111111111111111111111111111111111111111111111111111"

template.render()

"""FHIR Immunization site_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_site_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "site.coding",
            "column": [
                {
                    "name": "site_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "site_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "site_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationSiteCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "site_coding", VIEW_DEFINITION)

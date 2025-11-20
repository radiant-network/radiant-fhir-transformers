"""FHIR Procedure body_site transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_body_site",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "bodySite",
            "column": [
                {
                    "name": "body_site_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "body_site_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "body_site_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "body_site_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProcedureBodySiteTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "body_site", VIEW_DEFINITION)

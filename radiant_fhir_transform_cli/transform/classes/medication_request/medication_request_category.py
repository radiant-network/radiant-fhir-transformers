"""FHIR MedicationRequest category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_category",
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
                    "name": "medication_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "category",
            "column": [
                {
                    "name": "category_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "category_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "category_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "category_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class MedicationRequestCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationRequest", "category", VIEW_DEFINITION)

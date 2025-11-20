"""FHIR Medication form_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Medication",
    "name": "medication_form_coding",
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
                    "name": "medication_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "form.coding",
            "column": [
                {
                    "name": "form_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "form_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "form_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationFormCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Medication", "form_coding", VIEW_DEFINITION)

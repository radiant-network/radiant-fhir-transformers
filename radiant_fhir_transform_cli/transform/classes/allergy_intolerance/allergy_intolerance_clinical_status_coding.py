"""FHIR AllergyIntolerance clinical_status_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "AllergyIntolerance",
    "name": "allergy_intolerance_clinical_status_coding",
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
                    "name": "allergy_intolerance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "clinicalStatus.coding",
            "column": [
                {
                    "name": "clinical_status_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "clinical_status_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "clinical_status_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AllergyIntoleranceClinicalStatusCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "AllergyIntolerance", "clinical_status_coding", VIEW_DEFINITION
        )

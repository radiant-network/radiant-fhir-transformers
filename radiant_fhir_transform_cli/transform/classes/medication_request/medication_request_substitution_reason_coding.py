"""FHIR MedicationRequest substitution_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_substitution_reason_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "medication_request_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "substitution.reason.coding",
            "column": [
                {
                    "name": "substitution_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "substitution_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "substitution_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestSubstitutionReasonCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationRequest", "substitution_reason_coding", VIEW_DEFINITION
        )

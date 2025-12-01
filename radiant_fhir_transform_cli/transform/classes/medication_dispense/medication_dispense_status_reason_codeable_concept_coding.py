"""FHIR MedicationDispense status_reason_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_status_reason_codeable_concept_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "medication_dispense_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "statusReasonCodeableConcept.coding",
            "column": [
                {
                    "name": "status_reason_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "status_reason_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "status_reason_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseStatusReasonCodeableConceptCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationDispense",
            "status_reason_codeable_concept_coding",
            VIEW_DEFINITION,
        )

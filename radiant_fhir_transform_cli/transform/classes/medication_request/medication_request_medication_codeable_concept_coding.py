"""FHIR MedicationRequest medication_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_medication_codeable_concept_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
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
            "forEachOrNull": "medicationCodeableConcept.coding",
            "column": [
                {
                    "name": "medication_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "medication_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "medication_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestMedicationCodeableConceptCodingTransformer(FhirResourceTransformer):
    resource_type = "MedicationRequest"
    resource_component = "medication_codeable_concept_coding"
    view_definition = VIEW_DEFINITION

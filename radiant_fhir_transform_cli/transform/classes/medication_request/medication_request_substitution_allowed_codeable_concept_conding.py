"""FHIR MedicationRequest substitution_allowed_codeable_concept_conding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_substitution_allowed_codeable_concept_conding",
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
            "forEachOrNull": "substitution.allowedCodeableConcept.coding",
            "column": [
                {
                    "name": "substitution_allowed_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "substitution_allowed_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "substitution_allowed_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestSubstitutionAllowedCodeableConceptCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationRequest",
            "substitution_allowed_codeable_concept_coding",
            VIEW_DEFINITION,
        )

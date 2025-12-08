"""FHIR MedicationRequest instantiates_canonical transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_instantiates_canonical",
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
            "forEachOrNull": "instantiatesCanonical",
            "column": [
                {
                    "name": "instantiates_canonical",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestInstantiatesCanonicalTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationRequest", "instantiates_canonical", VIEW_DEFINITION
        )

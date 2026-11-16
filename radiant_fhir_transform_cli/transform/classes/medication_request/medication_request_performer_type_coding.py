"""FHIR MedicationRequest performer_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_performer_type_coding",
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
            "forEachOrNull": "performerType.coding",
            "column": [
                {
                    "name": "performer_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "performer_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "performer_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestPerformerTypeCodingTransformer(FhirResourceTransformer):
    resource_type = "MedicationRequest"
    resource_component = "performer_type_coding"
    view_definition = VIEW_DEFINITION

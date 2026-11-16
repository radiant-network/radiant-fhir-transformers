"""FHIR MedicationRequest insurance transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_insurance",
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
            "forEachOrNull": "insurance",
            "column": [
                {
                    "name": "insurance_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "insurance_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "insurance_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestInsuranceTransformer(FhirResourceTransformer):
    resource_type = "MedicationRequest"
    resource_component = "insurance"
    view_definition = VIEW_DEFINITION

"""FHIR Immunization subpotent_reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_subpotent_reason",
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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "subpotentReason",
            "column": [
                {
                    "name": "subpotent_reason_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "subpotent_reason_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationSubpotentReasonTransformer(FhirResourceTransformer):
    resource_type = "Immunization"
    resource_component = "subpotent_reason"
    view_definition = VIEW_DEFINITION

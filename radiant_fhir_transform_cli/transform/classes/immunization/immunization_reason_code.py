"""FHIR Immunization reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_reason_code",
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
            "forEachOrNull": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "reason_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationReasonCodeTransformer(FhirResourceTransformer):
    resource_type = "Immunization"
    resource_component = "reason_code"
    view_definition = VIEW_DEFINITION

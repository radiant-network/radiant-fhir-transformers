"""FHIR Immunization subpotent_reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_subpotent_reason",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "immunization_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "subpotentReason",
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
    def __init__(self):
        super().__init__("Immunization", "subpotent_reason", VIEW_DEFINITION)

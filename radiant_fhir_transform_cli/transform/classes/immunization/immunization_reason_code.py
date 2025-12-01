"""FHIR Immunization reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_reason_code",
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
            "forEach": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "reason_code_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class ImmunizationReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "reason_code", VIEW_DEFINITION)

"""FHIR Immunization status_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_status_reason_coding",
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
            "forEach": "statusReason.coding",
            "column": [
                {
                    "name": "status_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "status_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "status_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationStatusReasonCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Immunization", "status_reason_coding", VIEW_DEFINITION
        )

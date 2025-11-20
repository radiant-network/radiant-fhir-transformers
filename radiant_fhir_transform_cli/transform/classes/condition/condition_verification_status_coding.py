"""FHIR Condition verification_status_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_verification_status_coding",
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
                    "name": "condition_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "verificationStatus.coding",
            "column": [
                {
                    "name": "verification_status_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "verification_status_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "verification_status_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConditionVerificationStatusCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Condition", "verification_status_coding", VIEW_DEFINITION
        )

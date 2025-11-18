"""FHIR ServiceRequest performer_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_performer_type_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "service_request_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "performerType.coding",
            "column": [
                {
                    "name": "performer_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "performer_type_coding_version",
                    "path": "version",
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
                {
                    "name": "performer_type_coding_user_selected",
                    "path": "userSelected",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestPerformerTypeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "ServiceRequest", "performer_type_coding", VIEW_DEFINITION
        )

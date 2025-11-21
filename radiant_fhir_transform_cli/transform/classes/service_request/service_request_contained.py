"""FHIR ServiceRequest contained transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_contained",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "contained",
            "column": [
                {
                    "name": "contained_resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "contained_id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "contained_status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "contained_code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "contained_subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "contained_subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "contained_subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "contained_collection_collected_date_time",
                    "path": "collection.collectedDateTime",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestContainedTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "contained", VIEW_DEFINITION)

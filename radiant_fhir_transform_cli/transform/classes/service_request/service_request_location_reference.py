"""FHIR ServiceRequest location_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_location_reference",
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
            "forEach": "locationReference",
            "column": [
                {
                    "name": "location_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "location_reference_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "location_reference_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestLocationReferenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "ServiceRequest", "location_reference", VIEW_DEFINITION
        )

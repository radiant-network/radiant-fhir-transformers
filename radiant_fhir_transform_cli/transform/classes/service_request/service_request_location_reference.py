"""FHIR ServiceRequest location_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_location_reference",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "locationReference",
            "column": [
                {
                    "name": "location_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "location_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "location_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestLocationReferenceTransformer(FhirResourceTransformer):
    resource_type = "ServiceRequest"
    resource_component = "location_reference"
    view_definition = VIEW_DEFINITION

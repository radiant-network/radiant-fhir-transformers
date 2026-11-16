"""FHIR Observation body_site_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_body_site_coding",
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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "bodySite.coding",
            "column": [
                {
                    "name": "body_site_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "body_site_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "body_site_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationBodySiteCodingTransformer(FhirResourceTransformer):
    resource_type = "Observation"
    resource_component = "body_site_coding"
    view_definition = VIEW_DEFINITION

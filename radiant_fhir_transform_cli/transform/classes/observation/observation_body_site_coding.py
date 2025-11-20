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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "bodySite.coding",
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
    def __init__(self):
        super().__init__("Observation", "body_site_coding", VIEW_DEFINITION)

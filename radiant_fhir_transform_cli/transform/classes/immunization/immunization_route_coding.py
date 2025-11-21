"""FHIR Immunization route_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_route_coding",
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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "route.coding",
            "column": [
                {
                    "name": "route_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "route_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "route_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationRouteCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "route_coding", VIEW_DEFINITION)

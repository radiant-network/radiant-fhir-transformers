"""FHIR Observation method_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_method_coding",
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
            "forEachOrNull": "method.coding",
            "column": [
                {
                    "name": "method_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "method_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "method_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationMethodCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "method_coding", VIEW_DEFINITION)

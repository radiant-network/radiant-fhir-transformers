"""FHIR Observation extension transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_extension",
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
            "forEach": "extension",
            "column": [
                {
                    "name": "extension_url",
                    "path": "url",
                    "type": "string",
                },
                {
                    "name": "extension_value_identifier_system",
                    "path": "valueIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "extension_value_identifier_value",
                    "path": "valueIdentifier.value",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationExtensionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "extension", VIEW_DEFINITION)

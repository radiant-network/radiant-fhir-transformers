"""FHIR Encounter service_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_service_type_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "encounter_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "serviceType.coding",
            "column": [
                {
                    "name": "service_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "service_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "service_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterServiceTypeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "service_type_coding", VIEW_DEFINITION)

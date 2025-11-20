"""FHIR Encounter location transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_location",
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
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "location",
            "column": [
                {
                    "name": "location_location_reference",
                    "path": "location.reference",
                    "type": "string",
                },
                {
                    "name": "location_location_type",
                    "path": "location.type",
                    "type": "string",
                },
                {
                    "name": "location_location_display",
                    "path": "location.display",
                    "type": "string",
                },
                {
                    "name": "location_status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "location_physical_type_coding_code",
                    "path": "physicalType.coding.code",
                    "type": "string",
                },
                {
                    "name": "location_physical_type_coding_system",
                    "path": "physicalType.coding.system",
                    "type": "string",
                },
                {
                    "name": "location_physical_type_coding_display",
                    "path": "physicalType.coding.display",
                    "type": "string",
                },
                {
                    "name": "location_physical_type_text",
                    "path": "physicalType.text",
                    "type": "string",
                },
                {
                    "name": "location_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "location_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class EncounterLocationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "location", VIEW_DEFINITION)

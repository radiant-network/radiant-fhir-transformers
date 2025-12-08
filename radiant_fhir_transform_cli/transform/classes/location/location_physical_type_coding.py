"""FHIR Location physical_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location_physical_type_coding",
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
                    "name": "location_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "physicalType.coding",
            "column": [
                {
                    "name": "physical_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "physical_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "physical_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class LocationPhysicalTypeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", "physical_type_coding", VIEW_DEFINITION)

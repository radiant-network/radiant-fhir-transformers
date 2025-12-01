"""FHIR MedicationDispense part_of transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_part_of",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "medication_dispense_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "partOf",
            "column": [
                {
                    "name": "part_of_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "part_of_type", "path": "type", "type": "string"},
                {
                    "name": "part_of_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispensePartOfTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "part_of", VIEW_DEFINITION)

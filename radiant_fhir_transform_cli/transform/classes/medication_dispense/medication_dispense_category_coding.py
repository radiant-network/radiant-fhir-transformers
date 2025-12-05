"""FHIR MedicationDispense category_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_category_coding",
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
            "forEach": "category.coding",
            "column": [
                {
                    "name": "category_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "category_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "category_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseCategoryCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "MedicationDispense", "category_coding", VIEW_DEFINITION
        )

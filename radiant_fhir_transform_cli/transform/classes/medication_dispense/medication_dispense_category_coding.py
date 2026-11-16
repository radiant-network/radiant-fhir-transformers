"""FHIR MedicationDispense category_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_category_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        }
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
    resource_type = "MedicationDispense"
    resource_component = "category_coding"
    view_definition = VIEW_DEFINITION

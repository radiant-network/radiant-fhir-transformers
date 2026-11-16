"""FHIR Specimen condition transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_condition",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "condition",
            "column": [
                {
                    "name": "condition_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "condition_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenConditionTransformer(FhirResourceTransformer):
    resource_type = "Specimen"
    resource_component = "condition"
    view_definition = VIEW_DEFINITION

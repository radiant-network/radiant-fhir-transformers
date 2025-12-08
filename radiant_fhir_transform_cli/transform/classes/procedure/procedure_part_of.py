"""FHIR Procedure part_of transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_part_of",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "partOf",
            "column": [
                {
                    "name": "part_of_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "part_of_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "part_of_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedurePartOfTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "part_of", VIEW_DEFINITION)

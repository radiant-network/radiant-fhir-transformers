"""FHIR Procedure used_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_used_reference",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "procedure_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "usedReference",
            "column": [
                {
                    "name": "used_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "used_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "used_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureUsedReferenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "used_reference", VIEW_DEFINITION)

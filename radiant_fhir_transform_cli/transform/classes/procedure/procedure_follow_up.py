"""FHIR Procedure follow_up transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_follow_up",
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
            "forEach": "followUp",
            "column": [
                {
                    "name": "follow_up_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "follow_up_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class ProcedureFollowUpTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "follow_up", VIEW_DEFINITION)

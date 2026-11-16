"""FHIR Procedure complication transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_complication",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "complication",
            "column": [
                {
                    "name": "complication_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "complication_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureComplicationTransformer(FhirResourceTransformer):
    resource_type = "Procedure"
    resource_component = "complication"
    view_definition = VIEW_DEFINITION

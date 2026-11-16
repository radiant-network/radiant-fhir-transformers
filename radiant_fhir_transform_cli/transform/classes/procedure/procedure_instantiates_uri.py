"""FHIR Procedure instantiates_uri transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_instantiates_uri",
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
            "forEachOrNull": "instantiatesUri",
            "column": [
                {
                    "name": "instantiates_uri",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureInstantiatesUriTransformer(FhirResourceTransformer):
    resource_type = "Procedure"
    resource_component = "instantiates_uri"
    view_definition = VIEW_DEFINITION

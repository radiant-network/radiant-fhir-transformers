"""FHIR Procedure instantiates_uri transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_instantiates_uri",
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
            "forEach": "instantiatesUri",
            "column": [
                {"name": "instantiates_uri", "path": "$this", "type": "string"}
            ],
        },
    ],
}


class ProcedureInstantiatesUriTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "instantiates_uri", VIEW_DEFINITION)

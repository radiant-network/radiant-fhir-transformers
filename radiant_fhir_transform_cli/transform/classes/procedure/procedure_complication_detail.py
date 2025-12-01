"""FHIR Procedure complication_detail transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_complication_detail",
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
            "forEach": "complicationDetail",
            "column": [
                {
                    "name": "complication_detail_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "complication_detail_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "complication_detail_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureComplicationDetailTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "complication_detail", VIEW_DEFINITION)

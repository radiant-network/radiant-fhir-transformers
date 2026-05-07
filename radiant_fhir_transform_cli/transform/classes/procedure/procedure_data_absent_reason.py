"""FHIR Procedure data_absent_reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_data_absent_reason",
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
            "forEachOrNull": "extension",
            "column": [
                {
                    "name": "value_code",
                    "path": "$this.where(url = 'http://hl7.org/fhir/StructureDefinition/data-absent-reason').valueCode",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureDataAbsentReasonTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "data_absent_reason", VIEW_DEFINITION)

"""FHIR Procedure status_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_status_reason_coding",
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
            "forEachOrNull": "statusReason.coding",
            "column": [
                {
                    "name": "status_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "status_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "status_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureStatusReasonCodingTransformer(FhirResourceTransformer):
    resource_type = "Procedure"
    resource_component = "status_reason_coding"
    view_definition = VIEW_DEFINITION

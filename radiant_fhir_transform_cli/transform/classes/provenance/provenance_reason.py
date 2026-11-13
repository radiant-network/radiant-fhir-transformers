"""FHIR Provenance reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_reason",
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
                    "name": "provenance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "reason",
            "column": [
                {
                    "name": "reason_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "reason_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceReasonTransformer(FhirResourceTransformer):
    resource_type = "Provenance"
    resource_component = "reason"
    view_definition = VIEW_DEFINITION

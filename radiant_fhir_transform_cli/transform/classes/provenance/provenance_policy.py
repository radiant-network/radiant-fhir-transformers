"""FHIR Provenance policy transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_policy",
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
            "forEachOrNull": "policy",
            "column": [
                {
                    "name": "policy",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenancePolicyTransformer(FhirResourceTransformer):
    resource_type = "Provenance"
    resource_component = "policy"
    view_definition = VIEW_DEFINITION

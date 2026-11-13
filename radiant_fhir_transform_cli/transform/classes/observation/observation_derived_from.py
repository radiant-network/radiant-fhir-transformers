"""FHIR Observation derived_from transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_derived_from",
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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "derivedFrom",
            "column": [
                {
                    "name": "derived_from_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "derived_from_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "derived_from_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationDerivedFromTransformer(FhirResourceTransformer):
    resource_type = "Observation"
    resource_component = "derived_from"
    view_definition = VIEW_DEFINITION

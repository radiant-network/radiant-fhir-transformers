"""FHIR DocumentReference context_encounter transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_encounter",
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
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "context.encounter",
            "column": [
                {
                    "name": "context_encounter_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "context_encounter_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "context_encounter_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContextEncounterTransformer(FhirResourceTransformer):
    resource_type = "DocumentReference"
    resource_component = "context_encounter"
    view_definition = VIEW_DEFINITION

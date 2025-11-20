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
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
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
            "forEach": "context.encounter",
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
    def __init__(self):
        super().__init__(
            "DocumentReference", "context_encounter", VIEW_DEFINITION
        )

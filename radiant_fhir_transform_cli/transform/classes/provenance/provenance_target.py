"""FHIR Provenance target transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_target",
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
                    "name": "provenance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "target",
            "column": [
                {
                    "name": "target_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "target_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "target_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceTargetTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "target", VIEW_DEFINITION)

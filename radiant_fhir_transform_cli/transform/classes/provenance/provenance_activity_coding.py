"""FHIR Provenance activity_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_activity_coding",
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
            "forEach": "activity.coding",
            "column": [
                {
                    "name": "activity_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "activity_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "activity_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceActivityCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "activity_coding", VIEW_DEFINITION)

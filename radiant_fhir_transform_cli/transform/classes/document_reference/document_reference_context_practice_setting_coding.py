"""FHIR DocumentReference context_practice_setting_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_practice_setting_coding",
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
            "forEach": "context.practiceSetting.coding",
            "column": [
                {
                    "name": "context_practice_setting_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "context_practice_setting_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "context_practice_setting_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContextPracticeSettingCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "DocumentReference",
            "context_practice_setting_coding",
            VIEW_DEFINITION,
        )

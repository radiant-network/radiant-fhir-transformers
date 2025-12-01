"""FHIR Consent category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_category",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "consent_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "category",
            "column": [
                {
                    "name": "category_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "category_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class ConsentCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "category", VIEW_DEFINITION)

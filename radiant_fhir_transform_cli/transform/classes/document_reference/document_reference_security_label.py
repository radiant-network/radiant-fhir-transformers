"""FHIR DocumentReference security_label transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_security_label",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "securityLabel",
            "column": [
                {
                    "name": "security_label_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "security_label_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceSecurityLabelTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DocumentReference", "security_label", VIEW_DEFINITION)

"""FHIR DocumentReference security_label transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_security_label",
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
            "forEachOrNull": "securityLabel",
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
    resource_type = "DocumentReference"
    resource_component = "security_label"
    view_definition = VIEW_DEFINITION

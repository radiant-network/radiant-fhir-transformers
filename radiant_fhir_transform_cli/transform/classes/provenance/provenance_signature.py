"""FHIR Provenance signature transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_signature",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "provenance_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "signature",
            "column": [
                {
                    "name": "signature_type",
                    "path": "type",
                    "type": "string",
                    "collection": True,
                },
                {"name": "signature_when", "path": "when", "type": "dateTime"},
                {
                    "name": "signature_who_reference",
                    "path": "who.reference",
                    "type": "string",
                },
                {
                    "name": "signature_who_type",
                    "path": "who.type",
                    "type": "string",
                },
                {
                    "name": "signature_who_display",
                    "path": "who.display",
                    "type": "string",
                },
                {
                    "name": "signature_on_behalf_of_reference",
                    "path": "onBehalfOf.reference",
                    "type": "string",
                },
                {
                    "name": "signature_on_behalf_of_type",
                    "path": "onBehalfOf.type",
                    "type": "string",
                },
                {
                    "name": "signature_on_behalf_of_display",
                    "path": "onBehalfOf.display",
                    "type": "string",
                },
                {
                    "name": "signature_target_format",
                    "path": "targetFormat",
                    "type": "string",
                },
                {
                    "name": "signature_sig_format",
                    "path": "sigFormat",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceSignatureTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "signature", VIEW_DEFINITION)

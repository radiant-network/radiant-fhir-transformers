"""FHIR Consent verification transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_verification",
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
                    "name": "consent_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "verification",
            "column": [
                {
                    "name": "verification_verified",
                    "path": "verified",
                    "type": "string",
                },
                {
                    "name": "verification_verified_with_reference",
                    "path": "verifiedWith.reference",
                    "type": "string",
                },
                {
                    "name": "verification_verified_with_type",
                    "path": "verifiedWith.type",
                    "type": "string",
                },
                {
                    "name": "verification_verified_with_display",
                    "path": "verifiedWith.display",
                    "type": "string",
                },
                {
                    "name": "verification_verification_date",
                    "path": "verificationDate",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class ConsentVerificationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "verification", VIEW_DEFINITION)

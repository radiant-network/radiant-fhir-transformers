"""FHIR Immunization funding_source_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_funding_source_coding",
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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "fundingSource.coding",
            "column": [
                {
                    "name": "funding_source_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "funding_source_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "funding_source_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationFundingSourceCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Immunization", "funding_source_coding", VIEW_DEFINITION
        )

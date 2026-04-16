"""FHIR Immunization report_origin_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_report_origin_coding",
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
            "forEachOrNull": "reportOrigin.coding",
            "column": [
                {
                    "name": "report_origin_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "report_origin_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "report_origin_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationReportOriginCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Immunization", "report_origin_coding", VIEW_DEFINITION
        )

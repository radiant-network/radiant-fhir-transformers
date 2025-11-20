"""FHIR Immunization protocol_applied transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_protocol_applied",
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
            "forEach": "protocolApplied",
            "column": [
                {
                    "name": "protocol_applied_series",
                    "path": "series",
                    "type": "string",
                },
                {
                    "name": "protocol_applied_authority_reference",
                    "path": "authority.reference",
                    "type": "string",
                },
                {
                    "name": "protocol_applied_authority_type",
                    "path": "authority.type",
                    "type": "string",
                },
                {
                    "name": "protocol_applied_authority_display",
                    "path": "authority.display",
                    "type": "string",
                },
                {
                    "name": "protocol_applied_dose_number_positive_int",
                    "path": "doseNumberPositiveInt",
                    "type": "integer",
                },
                {
                    "name": "protocol_applied_dose_number_string",
                    "path": "doseNumberString",
                    "type": "string",
                },
                {
                    "name": "protocol_applied_series_doses_positive_int",
                    "path": "seriesDosesPositiveInt",
                    "type": "integer",
                },
                {
                    "name": "protocol_applied_series_doses_string",
                    "path": "seriesDosesString",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "targetDisease",
                    "column": [
                        {
                            "name": "protocol_applied_target_disease_coding",
                            "path": "coding",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ImmunizationProtocolAppliedTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "protocol_applied", VIEW_DEFINITION)

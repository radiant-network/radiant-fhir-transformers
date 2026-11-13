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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "protocolApplied",
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
                    "name": "protocol_applied_target_disease",
                    "path": "targetDisease",
                    "type": "string",
                    "collection": True,
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
        },
    ],
}


class ImmunizationProtocolAppliedTransformer(FhirResourceTransformer):
    resource_type = "Immunization"
    resource_component = "protocol_applied"
    view_definition = VIEW_DEFINITION

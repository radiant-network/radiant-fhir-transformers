"""
FHIR Immunization ProtocolApplied transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "immunization_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "protocolApplied",
        "columns": {
            "protocol_applied_series": {"fhir_key": "series", "type": "str"},
            "protocol_applied_authority_reference": {
                "fhir_key": "authority.reference",
                "type": "str",
            },
            "protocol_applied_authority_type": {
                "fhir_key": "authority.type",
                "type": "str",
            },
            "protocol_applied_authority_display": {
                "fhir_key": "authority.display",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "protocol_applied_target_disease": {
                "fhir_key": "targetDisease",
                "type": "str",
            },
            "protocol_applied_dose_number_positive_int": {
                "fhir_key": "doseNumberPositiveInt",
                "type": "int",
            },
            "protocol_applied_dose_number_string": {
                "fhir_key": "doseNumberString",
                "type": "str",
            },
            "protocol_applied_series_doses_positive_int": {
                "fhir_key": "seriesDosesPositiveInt",
                "type": "int",
            },
            "protocol_applied_series_doses_string": {
                "fhir_key": "seriesDosesString",
                "type": "str",
            },
        },
    },
]


class ImmunizationProtocolAppliedTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'protocolApplied' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'protocolApplied' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('protocol_applied').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationProtocolAppliedTransformer instance with the resource type 'Immunization',
            subtype 'protocol_applied', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "protocol_applied", TRANSFORM_SCHEMA)

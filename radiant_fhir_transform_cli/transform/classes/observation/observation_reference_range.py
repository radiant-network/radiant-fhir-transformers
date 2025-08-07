"""
FHIR Observation ReferenceRange transformer
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
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "referenceRange",
        "columns": {
            "reference_range_low_value": {
                "fhir_key": "low.value",
                "type": "str",
            },
            "reference_range_low_unit": {"fhir_key": "low.unit", "type": "str"},
            "reference_range_low_system": {
                "fhir_key": "low.system",
                "type": "str",
            },
            "reference_range_low_code": {"fhir_key": "low.code", "type": "str"},
            "reference_range_high_value": {
                "fhir_key": "high.value",
                "type": "str",
            },
            "reference_range_high_unit": {
                "fhir_key": "high.unit",
                "type": "str",
            },
            "reference_range_high_system": {
                "fhir_key": "high.system",
                "type": "str",
            },
            "reference_range_high_code": {
                "fhir_key": "high.code",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "reference_range_type_coding": {
                "fhir_key": "type.coding",
                "type": "str",
            },
            "reference_range_type_text": {
                "fhir_key": "type.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "reference_range_applies_to": {
                "fhir_key": "appliesTo",
                "type": "str",
            },
            "reference_range_age_low_value": {
                "fhir_key": "age.low.value",
                "type": "str",
            },
            "reference_range_age_low_unit": {
                "fhir_key": "age.low.unit",
                "type": "str",
            },
            "reference_range_age_low_system": {
                "fhir_key": "age.low.system",
                "type": "str",
            },
            "reference_range_age_low_code": {
                "fhir_key": "age.low.code",
                "type": "str",
            },
            "reference_range_age_high_value": {
                "fhir_key": "age.high.value",
                "type": "str",
            },
            "reference_range_age_high_unit": {
                "fhir_key": "age.high.unit",
                "type": "str",
            },
            "reference_range_age_high_system": {
                "fhir_key": "age.high.system",
                "type": "str",
            },
            "reference_range_age_high_code": {
                "fhir_key": "age.high.code",
                "type": "str",
            },
            "reference_range_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ObservationReferenceRangeTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'referenceRange' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'referenceRange' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('reference_range').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationReferenceRangeTransformer instance with the resource type 'Observation',
            subtype 'reference_range', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "reference_range", TRANSFORM_SCHEMA)

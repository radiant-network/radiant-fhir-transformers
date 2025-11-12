"""
FHIR MedicationDispense Substitution Reason transformer
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
            "medication_dispense_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "substitution.reason",
        "columns": {
            "substitution_reason_text": {"fhir_key": "text", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "substitution_reason_coding": {"fhir_key": "coding", "type": "str"},
        },
    },
]


class MedicationDispenseSubstitutionReasonTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'substitution.reason' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'substitution.reason' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('substitution_reason').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseSubstitutionReasonTransformer instance with the resource type 'MedicationDispense',
            subtype 'substitution_reason', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationDispense", "substitution_reason", TRANSFORM_SCHEMA
        )

"""
FHIR Immunization ProgramEligibility transformer
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
        "fhir_path": "programEligibility",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "program_eligibility_coding": {"fhir_key": "coding", "type": "str"},
            "program_eligibility_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ImmunizationProgramEligibilityTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'programEligibility' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'programEligibility' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('program_eligibility').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationProgramEligibilityTransformer instance with the resource type 'Immunization',
            subtype 'program_eligibility', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Immunization", "program_eligibility", TRANSFORM_SCHEMA
        )

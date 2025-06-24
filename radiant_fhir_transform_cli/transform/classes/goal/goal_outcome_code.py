"""
FHIR Goal OutcomeCode transformer
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
            "goal_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "outcomeCode",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "outcome_code_coding": {"fhir_key": "coding", "type": "str"},
            "outcome_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class GoalOutcomeCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'outcomeCode' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'outcomeCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('outcome_code').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalOutcomeCodeTransformer instance with the resource type 'Goal',
            subtype 'outcome_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "outcome_code", TRANSFORM_SCHEMA)

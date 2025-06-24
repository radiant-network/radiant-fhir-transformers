"""
FHIR Goal OutcomeReference transformer
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
        "fhir_path": "outcomeReference",
        "fhir_reference": "outcome_reference_reference",
        "columns": {
            "outcome_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "outcome_reference_type": {"fhir_key": "type", "type": "str"},
            "outcome_reference_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class GoalOutcomeReferenceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'outcomeReference' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'outcomeReference' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('outcome_reference').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalOutcomeReferenceTransformer instance with the resource type 'Goal',
            subtype 'outcome_reference', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "outcome_reference", TRANSFORM_SCHEMA)

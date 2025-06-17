"""
FHIR Goal Priority Coding transformer
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
        "fhir_path": "priority.coding",
        "columns": {
            "priority_coding_system": {"fhir_key": "system", "type": "str"},
            "priority_coding_code": {"fhir_key": "code", "type": "str"},
            "priority_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class GoalPriorityCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'priority.coding' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'priority.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('priority_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalPriorityCodingTransformer instance with the resource type 'Goal',
            subtype 'priority_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "priority_coding", TRANSFORM_SCHEMA)

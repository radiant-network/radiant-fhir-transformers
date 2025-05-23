"""
FHIR Condition Stage transformer
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
            "condition_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "stage",
        "columns": {
            "stage_summary_coding": {"fhir_key": "summary.coding", "type": "str"},
            "stage_summary_text": {"fhir_key": "summary.text", "type": "str"},
            "stage_assessment": {"fhir_key": "assessment", "type": "str"},
            "stage_type_coding": {"fhir_key": "type.coding", "type": "str"},
            "stage_type_text": {"fhir_key": "type.text", "type": "str"},
        },
    },
]


class ConditionStageTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'stage' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'stage' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('stage').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionStageTransformer instance with the resource type 'Condition',
            subtype 'stage', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", "stage", TRANSFORM_SCHEMA)

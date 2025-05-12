"""
FHIR Condition Severity Coding transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "condition_id": { "type": "str"},
        },
    },
    {
        "fhir_path": "severity.coding",
        "columns": {
            "severity_coding_system": {"fhir_key": "system", "type": "str"},
            "severity_coding_code": {"fhir_key": "code", "type": "str"},
            "severity_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]

class ConditionSeverityCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'severity.coding' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'severity.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('severity_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionSeverityCodingTransformer instance with the resource type 'Condition',
            subtype 'severity_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", "severity_coding", TRANSFORM_SCHEMA)

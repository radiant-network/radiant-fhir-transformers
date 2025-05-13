"""
FHIR Condition Evidence transformer
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
        "fhir_path": "evidence.code.coding",
        "columns": {
            "evidence_system": {"fhir_key": "system", "type": "str"},
            "evidence_code": {"fhir_key": "code", "type": "str"},
            "evidence_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "evidence.detail",
        "fhir_reference": "evidence_detail_reference",
        "columns": {
            "evidence_detail_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "evidence_detail_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ConditionEvidenceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'Evidence' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'Evidence' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('Evidence').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionEvidenceTransformer instance with the resource type 'Condition',
            subtype 'Evidence', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", "Evidence", TRANSFORM_SCHEMA)

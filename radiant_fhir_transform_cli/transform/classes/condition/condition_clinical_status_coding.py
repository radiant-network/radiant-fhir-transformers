"""
FHIR Condition Clinical Status Coding transformer
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
            "condition_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "clinicalStatus.coding",
        "columns": {
            "clinical_status_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "clinical_status_coding_code": {"fhir_key": "code", "type": "str"},

            "clinical_status_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ConditionClinicalStatusCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'clinicalStatus.coding' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'clinicalStatus.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('clinical_status_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionClinicalStatusCodingTransformer instance with the resource type 'Condition',
            subtype 'clinical_status_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Condition", "clinical_status_coding", TRANSFORM_SCHEMA
        )

"""
FHIR Medication Code Coding transformer
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
            "medication_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "code.coding",
        "columns": {
            "code_coding_system": {"fhir_key": "system", "type": "str"},
            "code_coding_code": {"fhir_key": "code", "type": "str"},
            "code_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationCodeCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR, focusing on the 'code.coding' element.

    This class transforms FHIR Medication JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'code.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Medication').
        subtype (str): Specifies the sub-element of the resource to focus on ('code_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationCodeCodingTransformer instance with the resource type 'Medication',
            subtype 'code_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Medication", "code_coding", TRANSFORM_SCHEMA)

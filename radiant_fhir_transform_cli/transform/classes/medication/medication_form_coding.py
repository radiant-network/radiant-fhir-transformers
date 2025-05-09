"""
FHIR Medication Form Coding transformer
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
        "fhir_path": "form.coding",
        "columns": {
            "form_coding_system": {"fhir_key": "system", "type": "str"},
            "form_coding_code": {"fhir_key": "code", "type": "str"},
            "form_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationFormCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR, focusing on the 'form.coding' element.

    This class transforms FHIR Medication JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'form.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Medication').
        subtype (str): Specifies the sub-element of the resource to focus on ('form_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationFormCodingTransformer instance with the resource type 'Medication',
            subtype 'form_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Medication", "form_coding", TRANSFORM_SCHEMA)

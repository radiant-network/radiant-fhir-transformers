"""
FHIR MedicationDispense PartOf transformer
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
            "medication_dispense_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "partOf",
        "columns": {
            "part_of_reference": {"fhir_key": "reference", "type": "str"},
            "part_of_type": {"fhir_key": "type", "type": "str"},
            "part_of_display": {"fhir_key": "display", "type": "str"},
        },
    },
]

class MedicationDispensePartOfTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'partOf' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'partOf' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('part_of').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispensePartOfTransformer instance with the resource type 'MedicationDispense',
            subtype 'part_of', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationDispense", "part_of", TRANSFORM_SCHEMA)
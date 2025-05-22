"""
FHIR Location PhysicalType Coding transformer
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
            "location_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "physicalType.coding",
        "columns": {
            "physical_type_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "physical_type_coding_code": {"fhir_key": "code", "type": "str"},
            "physical_type_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class LocationPhysicalTypeCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR, focusing on the 'physicalType.coding' element.

    This class transforms FHIR Location JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'physicalType.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Location').
        subtype (str): Specifies the sub-element of the resource to focus on ('physical_type_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the LocationPhysicalTypeCodingTransformer instance with the resource type 'Location',
            subtype 'physical_type_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", "physical_type_coding", TRANSFORM_SCHEMA)

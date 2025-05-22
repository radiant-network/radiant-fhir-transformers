"""
FHIR Location Address Line transformer
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
        "fhir_path": "address.line",
        "columns": {
            "address_line": {"fhir_key": "line", "type": "str"},
        },
    },
]


class LocationAddressLineTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR, focusing on the 'address.line' element.
    This class transforms FHIR Location JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'address.line' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Location').
        subtype (str): Specifies the sub-element of the resource to focus on ('address_line').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the LocationAddressLineTransformer instance with the resource type 'Location',
            subtype 'address_line', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", "address_line", TRANSFORM_SCHEMA)

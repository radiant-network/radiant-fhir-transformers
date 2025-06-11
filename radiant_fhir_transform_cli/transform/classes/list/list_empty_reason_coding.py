"""
FHIR List EmptyReason Coding transformer
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
            "list_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "emptyReason.coding",
        "columns": {
            "empty_reason_coding_system": {"fhir_key": "system", "type": "str"},
            "empty_reason_coding_code": {"fhir_key": "code", "type": "str"},
            "empty_reason_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ListEmptyReasonCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'List' resource in FHIR, focusing on the 'emptyReason.coding' element.

    This class transforms FHIR List JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'emptyReason.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('List').
        subtype (str): Specifies the sub-element of the resource to focus on ('empty_reason_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ListEmptyReasonCodingTransformer instance with the resource type 'List',
            subtype 'empty_reason_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("List", "empty_reason_coding", TRANSFORM_SCHEMA)

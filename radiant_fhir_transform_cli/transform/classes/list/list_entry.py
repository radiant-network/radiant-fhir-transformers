"""
FHIR List Entry transformer
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
        "fhir_path": "entry",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "entry_flag_coding": {"fhir_key": "flag.coding", "type": "str"},
            "entry_flag_text": {"fhir_key": "flag.text", "type": "str"},
            "entry_deleted": {"fhir_key": "deleted", "type": "bool"},
            "entry_date": {"fhir_key": "date", "type": "datetime"},
            "entry_item_reference": {
                "fhir_key": "item.reference",
                "type": "str",
            },
            "entry_item_type": {"fhir_key": "item.type", "type": "str"},
            "entry_item_display": {"fhir_key": "item.display", "type": "str"},
        },
    },
]


class ListEntryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'List' resource in FHIR, focusing on the 'entry' element.

    This class transforms FHIR List JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'entry' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('List').
        subtype (str): Specifies the sub-element of the resource to focus on ('entry').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ListEntryTransformer instance with the resource type 'List',
            subtype 'entry', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("List", "entry", TRANSFORM_SCHEMA)

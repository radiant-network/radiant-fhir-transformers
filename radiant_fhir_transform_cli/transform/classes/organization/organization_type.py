"""
FHIR Organization Type transformer
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
            "organization_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "type",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "type_coding": {"fhir_key": "coding", "type": "str"},
            "type_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class OrganizationTypeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Organization' resource in FHIR, focusing on the 'type' element.

    This class transforms FHIR Organization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'type' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Organization').
        subtype (str): Specifies the sub-element of the resource to focus on ('type').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the OrganizationTypeTransformer instance with the resource type 'Organization',
            subtype 'type', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Organization", "type", TRANSFORM_SCHEMA)

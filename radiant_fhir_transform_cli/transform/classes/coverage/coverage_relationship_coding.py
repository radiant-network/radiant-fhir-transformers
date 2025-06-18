"""
FHIR Coverage Relationship Coding transformer
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
            "coverage_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "relationship.coding",
        "columns": {
            "relationship_coding_system": {"fhir_key": "system", "type": "str"},
            "relationship_coding_code": {"fhir_key": "code", "type": "str"},
            "relationship_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class CoverageRelationshipCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR, focusing on the 'relationship.coding' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'relationship.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Coverage').
        subtype (str): Specifies the sub-element of the resource to focus on ('relationship_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CoverageRelationshipCodingTransformer instance with the resource type 'Coverage',
            subtype 'relationship_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", "relationship_coding", TRANSFORM_SCHEMA)

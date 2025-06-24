"""
FHIR Coverage Type Coding transformer
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
        "fhir_path": "type.coding",
        "columns": {
            "type_coding_system": {"fhir_key": "system", "type": "str"},
            "type_coding_code": {"fhir_key": "code", "type": "str"},
            "type_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class CoverageTypeCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR, focusing on the 'type.coding' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'type.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Coverage').
        subtype (str): Specifies the sub-element of the resource to focus on ('type_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CoverageTypeCodingTransformer instance with the resource type 'Coverage',
            subtype 'type_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", "type_coding", TRANSFORM_SCHEMA)

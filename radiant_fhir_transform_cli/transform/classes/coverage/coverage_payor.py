"""
FHIR Coverage Payor transformer
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
        "fhir_path": "payor",
        "fhir_reference": "payor_reference",
        "columns": {
            "payor_reference": {"fhir_key": "reference", "type": "str"},
            "payor_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class CoveragePayorTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR, focusing on the 'payor' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'payor' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Coverage').
        subtype (str): Specifies the sub-element of the resource to focus on ('payor').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CoveragePayorTransformer instance with the resource type 'Coverage',
            subtype 'payor', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", "payor", TRANSFORM_SCHEMA)

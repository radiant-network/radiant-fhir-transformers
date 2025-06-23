"""
FHIR Immunization Site Coding transformer
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
            "immunization_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "site.coding",
        "columns": {
            "site_coding_system": {"fhir_key": "system", "type": "str"},
            "site_coding_code": {"fhir_key": "code", "type": "str"},
            "site_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ImmunizationSiteCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'site.coding' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'site.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('site_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationSiteCodingTransformer instance with the resource type 'Immunization',
            subtype 'site_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "site_coding", TRANSFORM_SCHEMA)

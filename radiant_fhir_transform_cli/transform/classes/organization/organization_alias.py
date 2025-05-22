"""
FHIR Organization Alias transformer
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
        "fhir_path": "alias",
        "columns": {"alias": {"fhir_key": "alias", "type": "str"}},
    },
]


class OrganizationAliasTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Organization' resource in FHIR, focusing on the 'alias' element.

    This class transforms FHIR Organization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'alias' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Organization').
        subtype (str): Specifies the sub-element of the resource to focus on ('alias').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the OrganizationAliasTransformer instance with the resource type 'Organization',
            subtype 'alias', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Organization", "alias", TRANSFORM_SCHEMA)

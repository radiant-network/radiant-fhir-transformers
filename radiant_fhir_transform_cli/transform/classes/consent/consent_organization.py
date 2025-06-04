"""
FHIR Consent Organization transformer
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
            "consent_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "organization",
        "fhir_reference": "organization_reference",
        "columns": {
            "organization_reference": {"fhir_key": "reference", "type": "str"},
            "organization_type": {"fhir_key": "type", "type": "str"},
            "organization_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ConsentOrganizationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'organization' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'organization' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('organization').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentOrganizationTransformer instance with the resource type 'Consent',
            subtype 'organization', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "organization", TRANSFORM_SCHEMA)

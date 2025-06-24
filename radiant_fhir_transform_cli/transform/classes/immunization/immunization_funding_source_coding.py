"""
FHIR Immunization FundingSource Coding transformer
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
        "fhir_path": "fundingSource.coding",
        "columns": {
            "funding_source_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "funding_source_coding_code": {"fhir_key": "code", "type": "str"},
            "funding_source_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ImmunizationFundingSourceCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'fundingSource.coding' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'fundingSource.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('funding_source_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationFundingSourceCodingTransformer instance with the resource type 'Immunization',
            subtype 'funding_source_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Immunization", "funding_source_coding", TRANSFORM_SCHEMA
        )

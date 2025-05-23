"""
FHIR Condition Body Site transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "condition_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "bodySite",
        "columns": {
            "body_site_coding": {"fhir_key": "coding", "type": "str"},
            "body_site_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ConditionBodySiteTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'body_site' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'body_site' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('body_site').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionBodySiteTransformer instance with the resource type 'Condition',
            subtype 'body_site', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", "body_site", TRANSFORM_SCHEMA)

"""
FHIR Observation BodySite Coding transformer
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
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "bodySite.coding",
        "columns": {
            "body_site_coding_system": {"fhir_key": "system", "type": "str"},
            "body_site_coding_code": {"fhir_key": "code", "type": "str"},
            "body_site_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationBodySiteCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'bodySite.coding' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'bodySite.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('body_site_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationBodySiteCodingTransformer instance with the resource type 'Observation',
            subtype 'body_site_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "body_site_coding", TRANSFORM_SCHEMA)

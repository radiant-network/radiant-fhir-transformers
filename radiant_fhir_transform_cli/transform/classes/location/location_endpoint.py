"""
FHIR Location Endpoint transformer
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
            "location_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "endpoint",
        "fhir_reference": "endpoint_reference",
        "columns": {
            "endpoint_reference": {"fhir_key": "reference", "type": "str"},
            "endpoint_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class LocationEndpointTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR, focusing on the 'endpoint' element.
    This class transforms FHIR Location JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'endpoint' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Location').
        subtype (str): Specifies the sub-element of the resource to focus on ('endpoint').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the LocationEndpointTransformer instance with the resource type 'Location',
            subtype 'endpoint', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", "endpoint", TRANSFORM_SCHEMA)

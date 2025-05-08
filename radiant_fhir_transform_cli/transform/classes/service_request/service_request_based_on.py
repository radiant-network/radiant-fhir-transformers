"""
FHIR ServiceRequest Based On transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
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
        "fhir_path": "basedOn",
        "fhir_reference": "based_on_reference",
        "columns": {
            "based_on_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "based_on_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ServiceRequestBasedOnTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'basedOn' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'basedOn' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('basedOn').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestBasedOnTransformer instance with the resource type 'ServiceRequest',
            subtype 'basedOn', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "based_on", TRANSFORM_SCHEMA)

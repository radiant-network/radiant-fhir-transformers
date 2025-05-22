"""
FHIR ServiceRequest Location Reference transformer
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
            "service_request_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "locationReference",
        "columns": {
            "location_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "location_reference_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "location_reference_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class ServiceRequestLocationReferenceTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'locationReference' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'locationReference' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('location_reference').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestLocationReferenceTransformer instance with the resource type 'ServiceRequest',
            subtype 'location_reference', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "ServiceRequest", "location_reference", TRANSFORM_SCHEMA
        )

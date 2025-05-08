"""
FHIR ServiceRequest Insurance transformer
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
        "fhir_path": "insurance",
        "columns": {
            "insurance_reference": {"fhir_key": "reference", "type": "str"},
            "insurance_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ServiceRequestInsuranceTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'insurance' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'insurance' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('insurance').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestInsuranceTransformer instance with the resource type 'ServiceRequest',
            subtype 'insurance', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "insurance", TRANSFORM_SCHEMA)

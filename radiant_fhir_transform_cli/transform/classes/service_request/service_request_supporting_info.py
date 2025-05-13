"""
FHIR ServiceRequest Supporting Info transformer
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
        "fhir_path": "supportingInfo",
        "columns": {
            "supporting_info_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "supporting_info_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ServiceRequestSupportingInfoTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'supportingInfo' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'supportingInfo' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('supportingInfo').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestPerformerTransformer instance with the resource type 'ServiceRequest',
            subtype 'supportingInfo', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "supporting_info", TRANSFORM_SCHEMA)

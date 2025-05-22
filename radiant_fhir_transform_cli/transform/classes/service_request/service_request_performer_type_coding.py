"""
FHIR ServiceRequest Performer Type Coding transformer
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
        "fhir_path": "performerType.coding",
        "columns": {
            "performer_type_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "performer_type_coding_version": {
                "fhir_key": "version",
                "type": "str",
            },
            "performer_type_coding_code": {"fhir_key": "code", "type": "str"},
            "performer_type_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "performer_type_coding_user_selected": {
                "fhir_key": "userSelected",
                "type": "str",
            },
        },
    },
]


class ServiceRequestPerformerTypeCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'performerTypeCoding' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'performerTypeCoding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('performer_type_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestPerformerTypeTransformer instance with the resource type 'ServiceRequest',
            subtype 'performer_type_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "ServiceRequest", "performer_type_coding", TRANSFORM_SCHEMA
        )

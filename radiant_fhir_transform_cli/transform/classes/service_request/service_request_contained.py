"""
FHIR ServiceRequest Contained transformer
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
        "fhir_path": "contained",
        "columns": {
            "contained_resource_type": {
                "fhir_key": "resourceType",
                "type": "str",
            },
            "contained_id": {"fhir_key": "id", "type": "str"},
            "contained_status": {"fhir_key": "status", "type": "str"},
            "contained_code_text": {"fhir_key": "code.text", "type": "str"},
            "contained_subject_reference": {
                "fhir_key": "subject.reference",
                "type": "str",
            },
            "contained_subject_display": {
                "fhir_key": "subject.display",
                "type": "str",
            },
            "contained_collection_collected_date_time": {
                "fhir_key": "collection.collectedDateTime",
                "type": "str",
            },
        },
    },
]


class ServiceRequestContainedTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'contained' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'contained' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('contained').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestContainedTransformer instance with the resource type 'ServiceRequest',
            subtype 'contained', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "contained", TRANSFORM_SCHEMA)

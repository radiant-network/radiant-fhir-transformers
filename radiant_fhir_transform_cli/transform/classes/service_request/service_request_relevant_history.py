"""
FHIR ServiceRequest Relevant History transformer
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
        "fhir_path": "relevantHistory",
        "columns": {
            "relevant_history_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "relevant_history_display": {"fhir_key": "display", "type": "str"},
            "relevant_history_type": {"fhir_key": "type", "type": "str"},
        },
    },
]


class ServiceRequestRelevantHistoryTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'relevantHistory' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'relevantHistory' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('relevant_history').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestRelevantHistoryTransformer instance with the resource type 'ServiceRequest',
            subtype 'relevant_history', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "relevant_history", TRANSFORM_SCHEMA)

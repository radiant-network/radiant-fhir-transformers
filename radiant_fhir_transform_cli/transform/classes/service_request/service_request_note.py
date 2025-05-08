"""
FHIR ServiceRequest Note transformer
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
        "fhir_path": "note",
        "columns": {
            "note_text": {"fhir_key": "text", "type": "str"},
            "note_author_string": {"fhir_key": "authorString", "type": "str"},
            "note_author_reference_reference": {"fhir_key": "authorReference.reference", "type": "str"},
            "note_author_reference_display": {"fhir_key": "authorReference.display", "type": "str"},  
            "note_time": {"fhir_key": "time", "type": "str"},                                  
        },
    },
]


class ServiceRequestNoteTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'ServiceRequest' resource in FHIR, focusing on the 'note' element.

    This class transforms FHIR ServiceRequest JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'note' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('ServiceRequest').
        subtype (str): Specifies the sub-element of the resource to focus on ('note').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ServiceRequestNoteTransformer instance with the resource type 'ServiceRequest',
            subtype 'note', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", "note", TRANSFORM_SCHEMA)

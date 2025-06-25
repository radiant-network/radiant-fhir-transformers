"""
FHIR Document Reference subtype Content transformer
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
            "document_reference_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "content",
        "columns": {
            "content_attachment_content_type": {
                "fhir_key": "attachment.contentType",
                "type": "str",
            },
            "content_attachment_language": {
                "fhir_key": "attachment.language",
                "type": "str",
            },
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "content_attachment_data": {"fhir_key": "attachment.data", "type": "str"},
            "content_attachment_url": {
                "fhir_key": "attachment.url",
                "type": "str",
            },
            "content_attachment_size": {
                "fhir_key": "attachment.size",
                "type": "int",
            },
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "content_attachment_hash": {"fhir_key": "attachment.hash", "type": "str"},
            "content_attachment_title": {
                "fhir_key": "attachment.title",
                "type": "str",
            },
            "content_attachment_creation": {
                "fhir_key": "attachment.creation",
                "type": "datetime",
            },
            "content_format_system": {
                "fhir_key": "format.system",
                "type": "str",
            },
            "content_format_code": {"fhir_key": "format.code", "type": "str"},
            "content_format_display": {
                "fhir_key": "format.display",
                "type": "str",
            },
        },
    },
]


class DocumentReferenceContentTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DocumentReference' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "content", TRANSFORM_SCHEMA)

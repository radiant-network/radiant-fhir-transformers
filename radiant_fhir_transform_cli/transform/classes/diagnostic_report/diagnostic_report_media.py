"""
FHIR DiagnosticReport media transformer
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
            "diagnostic_report_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "media.comment",
        "columns": {
            "media_comment": {"type": "str"},
        },
    },
    {
        "fhir_path": "media.link",
        "fhir_reference": "media_link_reference",
        "columns": {
            "media_link_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "media_link_display": {"fhir_key": "display", "type": "str"},
            "media_link_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class DiagnosticReportMediaTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'media' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'media' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('media').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportCodeCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'media', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DiagnosticReport", "media", TRANSFORM_SCHEMA)

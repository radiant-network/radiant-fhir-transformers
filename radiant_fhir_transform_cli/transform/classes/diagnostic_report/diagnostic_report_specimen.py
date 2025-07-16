"""
FHIR DiagnosticReport specimen transformer
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
            "diagnostic_report_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "specimen",
        "fhir_reference": "specimen_reference",
        "columns": {
            "specimen_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "specimen_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class DiagnosticReportSpecimenTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'specimen' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'specimen' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('specimen').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportCodeCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'specimen', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DiagnosticReport", "specimen", TRANSFORM_SCHEMA)

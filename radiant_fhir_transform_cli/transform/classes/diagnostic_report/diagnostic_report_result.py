"""
FHIR DiagnosticReport result transformer
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
        "fhir_path": "result",
        "fhir_reference": "result_reference",
        "columns": {
            "result_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "result_display": {"fhir_key": "display", "type": "str"},
            "result_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class DiagnosticReportResultTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'result' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'result' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('result').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportCodeCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'result', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DiagnosticReport", "result", TRANSFORM_SCHEMA)

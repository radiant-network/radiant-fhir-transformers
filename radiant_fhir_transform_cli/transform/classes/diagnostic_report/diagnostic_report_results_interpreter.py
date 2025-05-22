"""
FHIR DiagnosticReport resultsInterpreter transformer
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
        "fhir_path": "resultsInterpreter",
        "fhir_reference": "results_interpreter_reference",
        "columns": {
            "results_interpreter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "results_interpreter_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "results_interpreter_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class DiagnosticReportResultsInterpreterTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'resultsInterpreter' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'resultsInterpreter' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('results_interpreter').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportCodeCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'results_interpreter', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "DiagnosticReport", "results_interpreter", TRANSFORM_SCHEMA
        )

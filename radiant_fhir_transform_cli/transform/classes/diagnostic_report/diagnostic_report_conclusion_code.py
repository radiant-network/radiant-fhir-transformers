"""
FHIR DiagnosticReport conclusionCode transformer
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
        "fhir_path": "conclusionCode",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "conclusion_code_coding": {"fhir_key": "coding", "type": "str"},
            "conclusion_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class DiagnosticReportConclusionCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'conclusionCode' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'conclusionCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('conclusion_code').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportStatusReasonCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'conclusion_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "DiagnosticReport", "conclusion_code", TRANSFORM_SCHEMA
        )

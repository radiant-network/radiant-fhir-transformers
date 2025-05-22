"""
FHIR DiagnosticReport presentedForm transformer
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
        "fhir_path": "presentedForm",
        "columns": {
            "presented_form_content_type": {
                "fhir_key": "contentType",
                "type": "str",
            },
            "presented_form_language": {"fhir_key": "language", "type": "str"},
            # note: per natasha, the presentedForm.data field is an actual binary attachment and we need to handle it differently
            # "presented_form_data": {"fhir_key": "type","type": "str",},
            "presented_form_url": {"fhir_key": "url", "type": "str"},
            "presented_form_size": {"fhir_key": "size", "type": "int"},
            "presented_form_hash": {"fhir_key": "hash", "type": "str"},
            "presented_form_title": {"fhir_key": "title", "type": "str"},
            "presented_form_creation": {"fhir_key": "url", "type": "datetime"},
        },
    },
]


class DiagnosticReportPresentedFormTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR, focusing on the 'presentedForm' element.

    This class transforms FHIR DiagnosticReport JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'presentedForm' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DiagnosticReport').
        subtype (str): Specifies the sub-element of the resource to focus on ('presented_form').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DiagnosticReportCodeCodingTransformer instance with the resource type 'DiagnosticReport',
            subtype 'presented_form', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DiagnosticReport", "presented_form", TRANSFORM_SCHEMA)

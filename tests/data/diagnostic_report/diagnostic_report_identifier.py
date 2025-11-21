"""
Test helper class for FHIR resource type DiagnosticReport subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_system": "http://acme.com/lab/reports",
        "identifier_value": "5234342",
        "identifier_type_text": None,
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "bfcb29ed-33c3-41fd-bf1e-5bb4a1afa951",
        "diagnostic_report_id": "101",
    },
]


class DiagnosticReportIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'DiagnosticReport' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'DiagnosticReport' resource.

    It predefines the resource type as 'DiagnosticReport'
    and initializes the resource with the specific 'DiagnosticReport' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'DiagnosticReport'.

        resource (dict): The raw FHIR 'DiagnosticReport' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'DiagnosticReport' resource payload.
    """

    resource_type = "DiagnosticReport"
    resource_subtype = "identifier"
    transformer = DiagnosticReportIdentifierTransformer
    expected_table_name = "diagnostic_report_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

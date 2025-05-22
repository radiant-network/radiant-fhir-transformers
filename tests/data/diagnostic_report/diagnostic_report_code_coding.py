"""
Test helper class for FHIR resource type DiagnosticReport subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "diagnostic_report_id": "101",
        "code_coding_system": "http://loinc.org",
        "code_coding_code": "58410-2",
        "code_coding_display": "Complete blood count (hemogram) panel - Blood by Automated count",
    },
    {
        "diagnostic_report_id": "101",
        "code_coding_system": None,
        "code_coding_code": "CBC",
        "code_coding_display": "MASTER FULL BLOOD COUNT",
    },
]


class DiagnosticReportCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = DiagnosticReportCodeCodingTransformer
    expected_table_name = "diagnostic_report_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

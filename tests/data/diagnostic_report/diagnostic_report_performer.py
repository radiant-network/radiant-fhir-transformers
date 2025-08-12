"""
Test helper class for FHIR resource type DiagnosticReport subtype performer
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportPerformerTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "diagnostic_report_id": "101",
        "performer_reference": "1832473e-2fe0-452d-abe9-3cdb9879522f",
        "performer_reference_type": "Organization",
        "performer_display": "Acme Laboratory, Inc",
    }
]


class DiagnosticReportPerformerTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "performer"
    transformer = DiagnosticReportPerformerTransformer
    expected_table_name = "diagnostic_report_performer"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

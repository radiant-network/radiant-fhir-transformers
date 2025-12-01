"""
Test helper class for FHIR resource type DiagnosticReport subtype presentedForm
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportPresentedFormTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "presented_form_content_type": "application/pdf",
        "presented_form_language": "en-AU",
        "presented_form_url": None,
        "presented_form_size": None,
        "presented_form_hash": "L9ThxnotKPzthJ7hu3bnORuT6xI=",
        "presented_form_title": "HTML Report",
        "presented_form_creation": None,
        "id": "30734c3e-ed3d-49ee-b4b8-818d28165c01",
        "diagnostic_report_id": "101",
    },
]


class DiagnosticReportPresentedFormTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "presented_form"
    transformer = DiagnosticReportPresentedFormTransformer
    expected_table_name = "diagnostic_report_presented_form"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

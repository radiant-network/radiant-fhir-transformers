"""
Test helper class for FHIR resource type DiagnosticReport subtype media
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportMediaTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "media_comment": "some comment",
        "media_link_reference": "Media/123",
        "media_link_display": "a slide image",
        "media_link_type": None,
        "id": "979b2d9e-7bd1-4fd7-ab05-53fcf6b5b0f7",
        "diagnostic_report_id": "101",
    },
]


class DiagnosticReportMediaTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "media"
    transformer = DiagnosticReportMediaTransformer
    expected_table_name = "diagnostic_report_media"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

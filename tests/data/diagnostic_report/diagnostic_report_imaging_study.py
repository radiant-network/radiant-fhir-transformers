"""
Test helper class for FHIR resource type DiagnosticReport subtype imagingStudy
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportImagingStudyTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "imaging_study_reference": "ImagingStudy/myimage",
        "imaging_study_display": "some Mri image",
        "imaging_study_type": None,
        "id": "2e70c29c-7258-48fe-b410-ef129bc87941",
        "diagnostic_report_id": "101",
    },
]


class DiagnosticReportImagingStudyTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "imaging_study"
    transformer = DiagnosticReportImagingStudyTransformer
    expected_table_name = "diagnostic_report_imaging_study"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

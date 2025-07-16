"""
Test helper class for FHIR resource type DiagnosticReport subtype result
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportResultTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "diagnostic_report_id": "101",
        "result_reference": "r1",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r2",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r3",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r4",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r5",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r6",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r7",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r8",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r9",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r10",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r11",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r12",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r13",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r14",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r15",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r16",
        "result_reference_type": "Observation",
        "result_display": None,
    },
    {
        "diagnostic_report_id": "101",
        "result_reference": "r17",
        "result_reference_type": "Observation",
        "result_display": None,
    },
]


class DiagnosticReportResultTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "result"
    transformer = DiagnosticReportResultTransformer
    expected_table_name = "diagnostic_report_result"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

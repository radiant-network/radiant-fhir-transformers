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
        "result_reference": "Observation/r1",
        "result_display": None,
        "result_type": None,
        "id": "4045b480-3155-43de-91e0-aaf501136fe7",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r2",
        "result_display": None,
        "result_type": None,
        "id": "9f2c0ec9-45af-4eb0-a029-add0a5fe2537",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r3",
        "result_display": None,
        "result_type": None,
        "id": "4b0e465a-d9ab-4e5f-a75b-c93d9f78b88e",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r4",
        "result_display": None,
        "result_type": None,
        "id": "58bb3f57-6ef2-41ef-b264-2dabcd1f19d3",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r5",
        "result_display": None,
        "result_type": None,
        "id": "746b4afd-bb39-4c64-a9e5-65d59140f767",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r6",
        "result_display": None,
        "result_type": None,
        "id": "5557e160-5fa9-4eae-ab01-1395ba6b7340",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r7",
        "result_display": None,
        "result_type": None,
        "id": "ee74450e-4933-4109-aa3b-e53070e0d0f7",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r8",
        "result_display": None,
        "result_type": None,
        "id": "5d465c99-acff-4a4d-88a1-ace5f1dcbbef",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r9",
        "result_display": None,
        "result_type": None,
        "id": "419f9cbd-5f04-45e5-867f-a342836c7e22",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r10",
        "result_display": None,
        "result_type": None,
        "id": "6a20ccdd-2362-4fb3-8bfc-0c3aa3577d76",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r11",
        "result_display": None,
        "result_type": None,
        "id": "2b632351-7023-4dc1-a5ff-08274c669cab",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r12",
        "result_display": None,
        "result_type": None,
        "id": "2c3e08e8-f7bf-4109-8292-caf817557530",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r13",
        "result_display": None,
        "result_type": None,
        "id": "3d55bd27-7654-4bd4-9ea1-f23fdebd4b26",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r14",
        "result_display": None,
        "result_type": None,
        "id": "323e5f08-7c8e-4f39-b9ad-904b2841bf47",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r15",
        "result_display": None,
        "result_type": None,
        "id": "1f26922d-342b-4f9b-b95e-d229dd1d7d19",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r16",
        "result_display": None,
        "result_type": None,
        "id": "61766b01-ba8e-485d-bf86-0553f7f2e317",
        "diagnostic_report_id": "101",
    },
    {
        "result_reference": "Observation/r17",
        "result_display": None,
        "result_type": None,
        "id": "4d6272b8-feae-4aef-bddd-d468d5124f79",
        "diagnostic_report_id": "101",
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

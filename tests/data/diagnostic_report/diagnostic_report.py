"""
Test helper class for FHIR resource type DiagnosticReport
"""

import json

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "101",
        "resource_type": "DiagnosticReport",
        "code_text": "Complete Blood Count",
        "status": "final",
        "subject_reference": "pat2",
        "subject_type": None,
        "subject_display": "Patient Two",
        "encounter_reference": "example",
        "encounter_type": None,
        "encounter_display": None,
        "effective_date_time": "2011-03-04T08:30:00+11:00",
        "effective_period_start": None,
        "effective_period_stop": None,
        "issued": "2011-03-04T11:45:33+11:00",
        "conclusion": "Core lab",
        "diagnostic_report_raw_json": json.dumps(RESOURCE),
    }
]


class DiagnosticReportTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = DiagnosticReportTransformer
    expected_table_name = "diagnostic_report"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

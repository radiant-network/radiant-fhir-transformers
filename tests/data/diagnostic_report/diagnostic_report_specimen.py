"""
Test helper class for FHIR resource type DiagnosticReport subtype Specimen
"""

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportSpecimenTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .diagnostic_report_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specimen_reference": "Specimen/rtt",
        "specimen_display": "Red Top Tube",
        "specimen_type": None,
        "id": "4c1649c2-88ac-4380-9157-2f257f820fdb",
        "diagnostic_report_id": "101",
    },
    {
        "specimen_reference": "Specimen/ltt",
        "specimen_display": "Lavender Top Tube",
        "specimen_type": None,
        "id": "39862b66-045d-4280-8c31-a33073397f9e",
        "diagnostic_report_id": "101",
    },
    {
        "specimen_reference": "Specimen/urine",
        "specimen_display": "Urine Sample",
        "specimen_type": None,
        "id": "d4862c6b-5011-459a-a8a3-6012b474fca9",
        "diagnostic_report_id": "101",
    },
]


class DiagnosticReportSpecimenTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "specimen"
    transformer = DiagnosticReportSpecimenTransformer
    expected_table_name = "diagnostic_report_specimen"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

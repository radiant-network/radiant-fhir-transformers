"""
Test helper class for FHIR resource type Immunization subtype ReportOrigin Coding
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationReportOriginCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "report_origin_coding_system": "http://terminology.hl7.org/CodeSystem/immunization-origin",
        "report_origin_coding_code": "record",
        "report_origin_coding_display": None,
        "id": "53517dcd-bdfd-43de-998a-64d92f9c71ad",
        "immunization_id": "example",
    },
]


class ImmunizationReportOriginCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Immunization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Immunization' resource.

    It predefines the resource type as 'Immunization'
    and initializes the resource with the specific 'Immunization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Immunization'.
        resource (dict): The raw FHIR 'Immunization' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Immunization' resource payload.
    """

    resource_type = "Immunization"
    resource_subtype = "report_origin_coding"
    transformer = ImmunizationReportOriginCodingTransformer
    expected_table_name = "immunization_report_origin_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

"""
Test helper class for FHIR resource type DocumentReference subtype Context FacilityType Coding
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceContextFacilityTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "context_facility_type_coding_system": "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes",
        "context_facility_type_coding_code": "Outpatient",
        "context_facility_type_coding_display": "Outpatient",
    },
]


class DocumentReferenceContextFacilityTypeCodingTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'DocumentReference' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'DocumentReference' resource.

    It predefines the resource type as 'DocumentReference'
    and initializes the resource with the specific 'DocumentReference' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'DocumentReference'.
        resource (dict): The raw FHIR 'DocumentReference' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'DocumentReference' resource payload.
    """

    resource_type = "DocumentReference"
    resource_subtype = "context_facility_type_coding"
    transformer = DocumentReferenceContextFacilityTypeCodingTransformer
    expected_table_name = "document_reference_context_facility_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

"""
Test helper class for FHIR resource type DocumentReference
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "resource_type": "DocumentReference",
        "master_identifier_use": None,
        "master_identifier_type_text": None,
        "master_identifier_system": "urn:ietf:rfc:3986",
        "master_identifier_value": "urn:oid:129.6.58.92.88336",
        "master_identifier_period_start": None,
        "master_identifier_period_end": None,
        "status": "current",
        "doc_status": "preliminary",
        "type_text": "Progress Notes",
        "subject_reference": "Patient/eiCbDCEzFk6wR6UNlcWziySVQrlN47NTRvxPwgT4P3883",
        "subject_type": None,
        "subject_display": None,
        "date": "2004-12-23",
        "authenticator_reference": "Organization/f001",
        "authenticator_type": None,
        "authenticator_display": None,
        "custodian_reference": "Organization/custodian",
        "custodian_type": None,
        "custodian_display": None,
        "description": None,
        "context_period_start": "2004-12-23",
        "context_period_end": "2004-12-23",
        "context_facility_type_text": None,
        "context_practice_setting_text": None,
        "context_source_patient_info_reference": "Patient/xcda",
        "context_source_patient_info_type": None,
        "context_source_patient_info_display": None,
    },
]


class DocumentReferenceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = DocumentReferenceTransformer
    expected_table_name = "document_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

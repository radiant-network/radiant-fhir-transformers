"""
Test helper class for FHIR resource type DocumentReference subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category_coding": {
            "system": "http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category",
            "code": "clinical-note",
            "display": "Clinical Note",
        },
        "category_text": "Clinical Note",
        "id": "d9ccbc5b-659e-451e-ac05-bc2cb02aea39",
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
    },
]


class DocumentReferenceCategoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category"
    transformer = DocumentReferenceCategoryTransformer
    expected_table_name = "document_reference_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

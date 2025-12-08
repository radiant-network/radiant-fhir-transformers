"""
Test helper class for FHIR resource type DocumentReference subtype Context Encounter
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceContextEncounterTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "context_encounter_reference": "Encounter/xcda",
        "context_encounter_type": None,
        "context_encounter_display": None,
        "id": "c418b629-6db2-471f-9cc8-952e886c0b60",
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
    },
]


class DocumentReferenceContextEncounterTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "context_encounter"
    transformer = DocumentReferenceContextEncounterTransformer
    expected_table_name = "document_reference_context_encounter"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

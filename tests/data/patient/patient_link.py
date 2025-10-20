"""
Test helper class for FHIR resource type Organization subtype Link
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientLinkTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "link_other_reference": "pat2",
        "link_other_type": None,
        "link_other_identifier": None,
        "link_other_display": None,
        "link_type": "seealso",
    },
    {
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "link_other_reference": "pat3",
        "link_other_type": None,
        "link_other_identifier": None,
        "link_other_display": None,
        "link_type": "seealso1",
    },
]


class PatientLinkTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Patient' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Patient' resource.

    It predefines the resource type as 'Patient'
    and initializes the resource with the specific 'Patient' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Patient'.

        resource (dict): The raw FHIR 'Patient' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Patient' resource payload.
    """

    resource_type = "Patient"
    resource_subtype = "link"
    transformer = PatientLinkTransformer
    expected_table_name = "patient_link"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

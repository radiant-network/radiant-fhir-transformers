"""
Test helper class for FHIR resource type Organization subtype GeneralPractitioner
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientGeneralPractitionerTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "general_practitioner_reference": "Practitioner/eGHJaqroQFAsUO8lEm-zIFw3",
        "general_practitioner_type": "Practitioner",
        "general_practitioner_identifier": None,
        "general_practitioner_display": "Kathleen O Crocker, MD",
        "id": "6322fdca-01b5-4d30-8ca1-44cde78d02b0",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
]


class PatientGeneralPractitionerTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "general_practitioner"
    transformer = PatientGeneralPractitionerTransformer
    expected_table_name = "patient_general_practitioner"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

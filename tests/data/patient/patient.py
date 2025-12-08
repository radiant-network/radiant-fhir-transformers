"""
Test helper class for FHIR resource type Patient
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "identifier_mrn": "82001496",
        "race": "Unknown",
        "ethnicity": "Unknown",
        "given_name": "Betty",
        "family_name": "MyChart",
        "active": True,
        "birth_date": "2010-02-03",
        "gender": "Female",
        "deceased_boolean": False,
        "deceased_date_time": None,
        "address_line": "1234 Administration Blvd",
        "address_city": "SOUTHAMPTON",
        "address_state": "PA",
        "address_postal_code": "18966",
        "address_country": "US",
        "communication_language": "English",
    },
]


class PatientTestHelper(FhirResourceTestHelper):
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
    transformer = PatientTransformer
    expected_table_name = "patient"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

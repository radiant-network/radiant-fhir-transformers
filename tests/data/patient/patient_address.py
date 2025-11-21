"""
Test helper class for FHIR resource type Patient subtype Address
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientAddressTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "address_line": "1234 Administration Blvd",
        "address_use": "home",
        "address_type": None,
        "address_text": None,
        "address_city": "SOUTHAMPTON",
        "address_district": "Bucks",
        "address_state": "PA",
        "address_postal_code": "18966",
        "address_country": "US",
        "address_period_start": None,
        "address_period_end": None,
        "id": "082f17d3-d7a8-4e0c-abde-bfa9fa628d8f",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "address_line": "1234 Adminsutration Blvd",
        "address_use": "old",
        "address_type": None,
        "address_text": None,
        "address_city": "SOUTHAMPTON",
        "address_district": "Bucks",
        "address_state": "PA",
        "address_postal_code": "18966",
        "address_country": "US",
        "address_period_start": None,
        "address_period_end": None,
        "id": "b84a1962-7057-4dcf-8fed-914b7f81b998",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "address_line": "1234 Administration Blvd",
        "address_use": "old",
        "address_type": None,
        "address_text": None,
        "address_city": "SOUTHAMPTON",
        "address_district": "Bucks",
        "address_state": "PA",
        "address_postal_code": "18966",
        "address_country": "US",
        "address_period_start": None,
        "address_period_end": None,
        "id": "5f7da6be-5f4f-4e02-aee7-8c26501be2b4",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
]


class PatientAddressTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "address"
    transformer = PatientAddressTransformer
    expected_table_name = "patient_address"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

"""
Test helper class for FHIR resource type Organization subtype Contact
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientContactTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "contact_address_line": "1234 Administration Blvd",
        "contact_telecom_system": "phone",
        "contact_telecom_value": "215-777-7777",
        "contact_telecom_use": "home",
        "contact_relationship_coding": {
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
            "code": "3",
            "display": "Father",
        },
        "contact_relationship_text": "Father",
        "contact_name_use": "usual",
        "contact_name_text": "Dad1stName LastName",
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_address_use": "home",
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_city": "SOUTHAMPTON",
        "contact_address_district": "Bucks",
        "contact_address_state": "PA",
        "contact_address_postal_code": "18966",
        "contact_address_country": "US",
        "contact_address_period_start": None,
        "contact_address_period_end": None,
        "contact_gender": None,
        "contact_organization_reference": None,
        "contact_organization_type": None,
        "contact_organization_identifier": None,
        "contact_organization_display": None,
        "contact_period_start": "2022-03-09",
        "contact_period_end": None,
        "id": "665daf1d-27d3-4467-a85e-b7f61f2d6d2e",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "contact_address_line": "1234 Administration Blvd",
        "contact_telecom_system": "phone",
        "contact_telecom_value": "215-888-8888",
        "contact_telecom_use": "work",
        "contact_relationship_coding": {
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
            "code": "3",
            "display": "Father",
        },
        "contact_relationship_text": "Father",
        "contact_name_use": "usual",
        "contact_name_text": "Dad1stName LastName",
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_address_use": "home",
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_city": "SOUTHAMPTON",
        "contact_address_district": "Bucks",
        "contact_address_state": "PA",
        "contact_address_postal_code": "18966",
        "contact_address_country": "US",
        "contact_address_period_start": None,
        "contact_address_period_end": None,
        "contact_gender": None,
        "contact_organization_reference": None,
        "contact_organization_type": None,
        "contact_organization_identifier": None,
        "contact_organization_display": None,
        "contact_period_start": "2022-03-09",
        "contact_period_end": None,
        "id": "4b389899-ac85-4b82-9717-5afa87ed6958",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "contact_address_line": "1234 Administration Blvd",
        "contact_telecom_system": "phone",
        "contact_telecom_value": "215-444-4444",
        "contact_telecom_use": "mobile",
        "contact_relationship_coding": {
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
            "code": "3",
            "display": "Father",
        },
        "contact_relationship_text": "Father",
        "contact_name_use": "usual",
        "contact_name_text": "Dad1stName LastName",
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_address_use": "home",
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_city": "SOUTHAMPTON",
        "contact_address_district": "Bucks",
        "contact_address_state": "PA",
        "contact_address_postal_code": "18966",
        "contact_address_country": "US",
        "contact_address_period_start": None,
        "contact_address_period_end": None,
        "contact_gender": None,
        "contact_organization_reference": None,
        "contact_organization_type": None,
        "contact_organization_identifier": None,
        "contact_organization_display": None,
        "contact_period_start": "2022-03-09",
        "contact_period_end": None,
        "id": "532bebc5-3c30-41df-aa70-423899d5744e",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "contact_address_line": "1234 Administration Blvd",
        "contact_telecom_system": "email",
        "contact_telecom_value": "mychart@yahoo.com",
        "contact_telecom_use": None,
        "contact_relationship_coding": {
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
            "code": "3",
            "display": "Father",
        },
        "contact_relationship_text": "Father",
        "contact_name_use": "usual",
        "contact_name_text": "Dad1stName LastName",
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_address_use": "home",
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_city": "SOUTHAMPTON",
        "contact_address_district": "Bucks",
        "contact_address_state": "PA",
        "contact_address_postal_code": "18966",
        "contact_address_country": "US",
        "contact_address_period_start": None,
        "contact_address_period_end": None,
        "contact_gender": None,
        "contact_organization_reference": None,
        "contact_organization_type": None,
        "contact_organization_identifier": None,
        "contact_organization_display": None,
        "contact_period_start": "2022-03-09",
        "contact_period_end": None,
        "id": "1a29e5ed-a852-4b8a-ba88-a16233aefea0",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
]


class PatientContactTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "contact"
    transformer = PatientContactTransformer
    expected_table_name = "patient_contact"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

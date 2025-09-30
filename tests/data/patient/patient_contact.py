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
        "patient_id":"e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "contact_relationship": [{
                    "coding": [
                        {
                            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
                            "code": "3",
                            "display": "Father",
                        }
                    ],
                    "text": "Father",
                }],
        "contact_name_use": "usual",
        "contact_name_text":"Dad1stName LastName",
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_telecom": [
                {"system": "phone", "value": "215-777-7777", "use": "home"},
                {"system": "phone", "value": "215-888-8888", "use": "work"},
                {"system": "phone", "value": "215-444-4444", "use": "mobile"},
                {"system": "email", "value": "mychart@yahoo.com"},
            ],
        "contact_address_use": "home",
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_line": ["1234 Administration Blvd"],
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

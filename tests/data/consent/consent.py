"""
Test helper class for FHIR resource type Consent
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provision_provision_type": "permit",
        "provision_provision_actor": [
            {
                "role": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            "code": "AUT",
                        },
                    ],
                },
                "reference": {
                    "reference": "Practitioner/xcda-author",
                },
            },
        ],
        "provision_provision_class": [
            {
                "system": "urn:ietf:bcp:13",
                "code": "application/hl7-cda+xml",
            },
        ],
        "provision_provision_code": [
            {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "34133-9",
                    },
                ],
            },
            {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "18842-5",
                    },
                ],
            },
        ],
        "id": "consent-example-basic",
        "resource_type": "Consent",
        "status": "active",
        "scope_text": None,
        "patient_reference": "Patient/f001",
        "patient_type": None,
        "patient_display": "P. van de Heuvel",
        "date_time": "2016-05-11",
        "source_attachment_content_type": None,
        "source_attachment_language": None,
        "source_attachment_url": None,
        "source_attachment_size": None,
        "source_attachment_title": "The terms of the consent in lawyer speak.",
        "source_attachment_creation": None,
        "source_reference_reference": None,
        "source_reference_type": None,
        "source_reference_display": None,
        "policy_rule_text": None,
        "provision_type": None,
        "provision_period_start": "2015-10-10",
        "provision_period_end": "2016-10-10",
        "provision_data_period_start": None,
        "provision_data_period_end": None,
    },
]


class ConsentTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Consent' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Consent' resource.

    It predefines the resource type as 'Consent'
    and initializes the resource with the specific 'Consent' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Consent'.

        resource (dict): The raw FHIR 'Consent' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Consent' resource payload.
    """

    resource_type = "Consent"
    resource_subtype = None
    transformer = ConsentTransformer
    expected_table_name = "consent"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

"""
Test helper class for FHIR resource type Consent subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": "urn:oid:2.16.840.1.113883.3.72.5.9.1",
        "identifier_value": "494e0c7a-a69e-4fb4-9d02-6aae747790d7",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "077721c4-0ca9-46c7-8ca6-484a9a88ee9b",
        "consent_id": "consent-example-basic",
    },
]


class ConsentIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = ConsentIdentifierTransformer
    expected_table_name = "consent_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

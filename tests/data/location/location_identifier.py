"""
Test helper class for FHIR resource type Location subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.location import (
    LocationIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .location_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "location_id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
        "identifier_use": "usual",
        "identifier_type_text": "NPI",
        "identifier_system": "http://hl7.org/fhir/sid/us-npi",
        "identifier_value": "1215921457",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
    {
        "location_id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
        "identifier_use": "usual",
        "identifier_type_text": None,
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.686980",
        "identifier_value": "84275011",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class LocationIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Location' resource.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Location' resource.
    It predefines the resource type as 'Location'
    and initializes the resource with the specific 'Location' resource payload
    and its expected transformation output.
    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Location'.
        resource (dict): The raw FHIR 'Location' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Location' resource payload.
    """

    resource_type = "Location"
    resource_subtype = "identifier"
    transformer = LocationIdentifierTransformer
    expected_table_name = "location_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

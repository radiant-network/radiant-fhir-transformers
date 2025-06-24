"""
Test helper class for FHIR resource type Immunization subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "immunization_id": "example",
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": "urn:ietf:rfc:3986",
        "identifier_value": "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class ImmunizationIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Immunization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Immunization' resource.

    It predefines the resource type as 'Immunization'
    and initializes the resource with the specific 'Immunization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Immunization'.
        resource (dict): The raw FHIR 'Immunization' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Immunization' resource payload.
    """

    resource_type = "Immunization"
    resource_subtype = "identifier"
    transformer = ImmunizationIdentifierTransformer
    expected_table_name = "immunization_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

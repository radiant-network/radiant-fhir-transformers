"""
Test helper class for FHIR resource type Specimen subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specimen_id": "101",
        "identifier_use": None,
        "identifier_system": "http://ehr.acme.org/identifiers/collections",
        "identifier_value": "23234352356",
        "identifier_type_text": None,
        "identifier_period_start": None,
        "identifier_period_end": None,
    }
]


class SpecimenIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Specimen' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Specimen' resource.

    It predefines the resource type as 'Specimen'
    and initializes the resource with the specific 'Specimen' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Specimen'.

        resource (dict): The raw FHIR 'Specimen' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Specimen' resource payload.
    """

    resource_type = "Specimen"
    resource_subtype = "identifier"
    transformer = SpecimenIdentifierTransformer
    expected_table_name = "specimen_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

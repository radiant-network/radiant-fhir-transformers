"""
Test helper class for FHIR resource type Medication subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f201",
        "identifier_use": "temp",
        "identifier_system": None,
        "identifier_value": "Encounter_Roel_20130404",
    }
]


class EncounterIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource.

    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.

        resource (dict): The raw FHIR 'Encounter' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Encounter' resource payload.
    """

    resource_type = "Encounter"
    resource_subtype = "identifier"
    transformer = EncounterIdentifierTransformer
    expected_table_name = "encounter_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

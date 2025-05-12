"""
Test helper class for FHIR resource type Medication subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_id": "med0301",
        "identifier_use": "usual",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698288",
        "identifier_value": "21279",
    }
]


class MedicationIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Medication' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Medication' resource.

    It predefines the resource type as 'Medication'
    and initializes the resource with the specific 'Medication' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Medication'.

        resource (dict): The raw FHIR 'Medication' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Medication' resource payload.
    """

    resource_type = "Medication"
    resource_subtype = "identifier"
    transformer = MedicationIdentifierTransformer
    expected_table_name = "medication_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

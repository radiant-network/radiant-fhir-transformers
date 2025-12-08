"""
Test helper class for FHIR resource type MedicationDispense subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": None,
        "medication_dispense_id": "meddisp001",
        "identifier_use": "official",
        "identifier_type_text": None,
        "identifier_system": "http://www.bmc.nl/portal/prescriptions",
        "identifier_value": "12345689",
        "identifier_period_end": None,
        "identifier_period_start": None,
    }
]


class MedicationDispenseIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationDispense' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationDispense' resource.
    It predefines the resource type as 'MedicationDispense'
    and initializes the resource with the specific 'MedicationDispense' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationDispense'.

        resource (dict): The raw FHIR 'MedicationDispense' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationDispense' resource payload.
    """

    resource_type = "MedicationDispense"
    resource_subtype = "identifier"
    transformer = MedicationDispenseIdentifierTransformer
    expected_table_name = "medication_dispense_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

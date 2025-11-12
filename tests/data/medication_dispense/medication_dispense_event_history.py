"""
Test helper class for FHIR resource type MedicationDispense eventHistory
"""
from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseEventHistoryTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_dispense_id": "meddisp001",
        "event_history_reference": "#signature",
        "event_history_type": None,
        "event_history_display": "Author's Signature",
    }
]
    
class MedicationDispenseEventHistoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "event_history"
    transformer = MedicationDispenseEventHistoryTransformer
    expected_table_name = "medication_dispense_event_history"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
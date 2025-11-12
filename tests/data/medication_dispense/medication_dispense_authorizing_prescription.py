"""
Test helper class for FHIR resource type MedicationDispense authorizingPrescription
"""
from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseAuthorizingPrescriptionTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_dispense_id": "meddisp001",
        "authorizing_prescription_reference": "MedicationRequest/medrx0318",
        "authorizing_prescription_type": None,
        "authorizing_prescription_display": None,
    }
]
    
class MedicationDispenseAuthorizingPrescriptionTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "authorizing_prescription"
    transformer = MedicationDispenseAuthorizingPrescriptionTransformer
    expected_table_name = "medication_dispense_authorizing_prescription"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
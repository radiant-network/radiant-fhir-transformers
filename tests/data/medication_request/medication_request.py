"""
Test helper class for FHIR resource type MedicationRequest
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "euHtu0fIBKsu8UhaYJaWMfg3",
        "resource_type": "MedicationRequest",
        "status": "active",
        "intent": "order",
        "reported_reference_reference": None,
        "reported_reference_type": None,
        "reported_reference_identifier_use": None,
        "reported_reference_identifier_system": None,
        "reported_reference_identifier_value": None,
        "reported_reference_display": None,
        "reported_boolean": True,
        "medication_reference_reference": "uscore-med2",
        "medication_reference_type": None,
        "medication_reference_identifier_use": None,
        "medication_reference_identifier_system": None,
        "medication_reference_identifier_value": None,
        "medication_reference_display": "Nizatidine 15 MG/ML Oral Solution [Axid]",
        "subject_reference": "example",
        "subject_display": "Amy Shaw",
        "subject_type": None,
        "subject_identifier_use": None,
        "subject_identifier_system": None,
        "subject_identifier_value": None,
        "encounter_reference": "example-1",
        "encounter_display": "Office Visit",
        "encounter_type": None,
        "encounter_identifier_use": None,
        "encounter_identifier_system": None,
        "encounter_identifier_value": None,
        "authored_on": "2008-04-05",
        "requester_reference": "practitioner-1",
        "requester_display": "Ronald Bone, MD",
        "medication_codeable_concept_text": "Tylenol PM Pill",
        "dispense_request_number_of_repeats_allowed": 1,
        "dispense_request_quantity_value": 480,
        "dispense_request_quantity_unit": "mL",
        "dispense_request_quantity_code": "mL",
        "dispense_request_quantity_system": "http://unitsofmeasure.org",
    }
]


class MedicationRequestTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_subtype = None
    transformer = MedicationRequestTransformer
    expected_table_name = "medication_request"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

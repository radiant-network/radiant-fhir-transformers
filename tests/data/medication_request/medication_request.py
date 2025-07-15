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
        "resource_type": "MedicationRequest",
        "id": "medrx0301",
        "status": "completed",
        "status_reason_text": "This therapy is a backup and will be used only if the preferred therapy fails.",
        "intent": "order",
        "priority": "routine",
        "do_not_perform": False,
        "reported_boolean": True,
        "reported_reference_reference": None,
        "reported_reference_type": None,
        "reported_reference_display": None,
        "medication_codeable_concept_text": None,
        "medication_reference_reference": "med0310",
        "medication_reference_type": None,
        "medication_reference_display": None,
        "subject_reference": "pat1",
        "subject_reference_type": "Patient",
        "subject_display": "Donald Duck",
        "encounter_reference": "f201",
        "encounter_type": None,
        "encounter_display": "encounter who leads to this prescription",
        "authored_on": "2015-01-15",
        "requester_reference": "f007",
        "requester_type": None,
        "requester_display": "Patrick Pump",
        "performer_reference": "f204",
        "performer_type": None,
        "performer_display": "Carla Espinosa",
        "performer_type_text": "Nurse",
        "recorder_reference": "ef81ZrgFqs7ufzYI2X9ixcA3",
        "recorder_type": None,
        "recorder_display": "Epic User",
        "group_identifier_use": None,
        "group_identifier_system": None,
        "group_identifier_value": None,
        "course_of_therapy_type_text": "Short course (acute) therapy",
        "dispense_request_initial_fill_quantity_value": None,
        "dispense_request_initial_fill_quantity_unit": None,
        "dispense_request_initial_fill_quantity_system": None,
        "dispense_request_initial_fill_quantity_code": None,
        "dispense_request_initial_fill_duration_value": None,
        "dispense_request_initial_fill_duration_unit": None,
        "dispense_request_initial_fill_duration_system": None,
        "dispense_request_initial_fill_duration_code": None,
        "dispense_request_dispense_interval_value": None,
        "dispense_request_dispense_interval_unit": None,
        "dispense_request_dispense_interval_system": None,
        "dispense_request_dispense_interval_code": None,
        "dispense_request_validity_period_start": "2015-01-15",
        "dispense_request_validity_period_end": "2016-01-15",
        "dispense_request_number_of_repeats_allowed": 0,
        "dispense_request_quantity_value": 30,
        "dispense_request_quantity_unit": "TAB",
        "dispense_request_quantity_system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
        "dispense_request_quantity_code": "TAB",
        "dispense_request_expected_supply_duration_value": 10,
        "dispense_request_expected_supply_duration_unit": "days",
        "dispense_request_expected_supply_duration_system": "http://unitsofmeasure.org",
        "dispense_request_expected_supply_duration_code": "d",
        "dispense_request_performer_reference": "Practitioner/f001",
        "dispense_request_performer_type": None,
        "dispense_request_performer_display": None,
        "substitution_allowed_boolean": True,
        "substitution_allowed_codeable_concept_text": None,
        "substitution_reason_text": None,
        "prior_prescription_reference": None,
        "prior_prescription_type": None,
        "prior_prescription_display": None,
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

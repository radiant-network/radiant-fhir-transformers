"""
Test helper class for FHIR resource type MedicationDispense
"""

from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "meddisp001",
        "resource_type": "MedicationDispense",
        "status": "in-progress",
        "status_reason_codeable_concept_text": None,
        "status_reason_reference": None,
        "status_reason_reference_type": None,
        "status_reason_reference_display": None,
        "category_text": None,
        "medication_codeable_concept_text": None,
        "medication_reference_reference": "#med0301",
        "medication_reference_type": None,
        "medication_reference_display": "Vancomycin Hydrochloride",
        "subject_reference": "pat1",
        "subject_type": None,
        "subject_display": "Donald Duck",
        "context_reference": None,
        "context_type": None,
        "context_display": None,
        "location_reference": "ukp",
        "location_type": None,
        "location_display": "Pharmacy",
        "type_text": None,
        "quantity_value": 12,
        "quantity_unit": "Vial",
        "quantity_system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
        "quantity_code": "Vial",
        "days_supply_value": 3,
        "days_supply_unit": "Day",
        "days_supply_system": "http://unitsofmeasure.org",
        "days_supply_code": "d",
        "when_prepared": "2015-01-15T10:20:00Z",
        "when_handed_over": None,
        "destination_reference": "ph",
        "destination_type": None,
        "destination_display": None,
        "receiver_reference": "pat1",
        "receiver_type": None,
        "receiver_display": "Donald Duck",
        "substitution_was_substituted": None,
        "substitution_type_text": None,
    }

]


class MedicationDispenseTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = MedicationDispenseTransformer
    expected_table_name = "medication_dispense"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
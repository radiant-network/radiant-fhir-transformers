"""
Test helper class for FHIR resource type AllergyIntolerance
"""

from radiant_fhir_transform_cli.transform.classes.allergy_intolerance import (
    AllergyIntoleranceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "example_ai",
        "resource_type": "AllergyIntolerance",
        "clinical_status_text": "active",
        "verification_status_text": "confirmed",
        "type": "allergy",
        "criticality": "high",
        "code_text": "cashews",
        "patient_reference": "example",
        "patient_type": None,
        "patient_display": None,
        "encounter_reference": None,
        "encounter_type": None,
        "encounter_display": None,
        "onset_date_time": "2004",
        "onset_age_value": None,
        "onset_age_unit": None,
        "onset_age_system": None,
        "onset_age_code": None,
        "onset_period_start": None,
        "onset_period_end": None,
        "onset_range_low_value": None,
        "onset_range_low_unit": None,
        "onset_range_low_system": None,
        "onset_range_low_code": None,
        "onset_range_high_value": None,
        "onset_range_high_unit": None,
        "onset_range_high_system": None,
        "onset_range_high_code": None,
        "onset_string": None,
        "recorded_date": "2014-10-09T14:58:00+11:00",
        "recorder_reference": "example_doc",
        "recorder_type": None,
        "recorder_display": None,
        "asserter_reference": "example",
        "asserter_type": None,
        "asserter_display": None,
        "last_occurrence": "2012-06",
    }
]


class AllergyIntoleranceTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'AllergyIntolerance' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'AllergyIntolerance' resource.

    It predefines the resource type as 'AllergyIntolerance'
    and initializes the resource with the specific 'AllergyIntolerance' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'AllergyIntolerance'.

        resource (dict): The raw FHIR 'AllergyIntolerance' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'AllergyIntolerance' resource payload.
    """

    resource_type = "AllergyIntolerance"
    resource_subtype = None
    transformer = AllergyIntoleranceTransformer
    expected_table_name = "allergy_intolerance"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

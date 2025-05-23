"""
Test helper class for FHIR resource type Condition 
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition import (
    ConditionTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "f201",
        "resource_type": "Condition",
        "code_text": None,
        "subject_reference": "f201",
        "subject_display": "Roel",
        "encounter_reference": "f201",
        "encounter_display": None,
        "onsetDateTime": "2013-04-02",
        "onset_age_value": None,
        "onset_age_unit": None,
        "onset_age_system": None,
        "onset_age_code": None,
        "onset_period_start": None,
        "onset_period_end": None,
        "onset_range_low_value": None,
        "onset_range_low_unit": None,
        "onset_range_high_value": None,
        "onset_range_high_unit": None,
        "onsetString": None,
        "abatementDateTime": None,
        "abatement_age_value": None,
        "abatement_age_unit": None,
        "abatement_age_system": None,
        "abatement_age_code": None,
        "abatement_period_start": None,
        "abatement_period_end": None,
        "abatement_range_low_value": None,
        "abatement_range_low_unit": None,
        "abatement_range_high_value": None,
        "abatement_range_high_unit": None,
        "abatementString": "around April 9, 2013",
        "recordedDate": "2013-04-04",
        "recorder_reference": "f201",
        "recorder_display": None,
        "asserter_reference": "f201",
        "asserter_display": None,
        "clinical_status_text": None,
        "verification_status_text": None,
        "severity_text": None,
    }
]


class ConditionTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Condition' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Condition' resource.

    It predefines the resource type as 'Condition'
    and initializes the resource with the specific 'Condition' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Condition'.

        resource (dict): The raw FHIR 'Condition' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Condition' resource payload.
    """

    resource_type = "Condition"
    resource_subtype = None
    transformer = ConditionTransformer
    expected_table_name = "condition"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

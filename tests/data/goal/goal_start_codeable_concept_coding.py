"""
Test helper class for FHIR resource type Goal subtype StartCodeableConcept Coding
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalStartCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "start_codeable_concept_coding_system": "http://snomed.info/sct",
        "start_codeable_concept_coding_code": "414260005",
        "start_codeable_concept_coding_display": "First outpatient appointment date (finding)",
        "id": "ca27f81c-e740-48bb-b89e-362f68996e97",
        "goal_id": "example",
    },
]


class GoalStartCodeableConceptCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Goal' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Goal' resource.

    It predefines the resource type as 'Goal'
    and initializes the resource with the specific 'Goal' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Goal'.
        resource (dict): The raw FHIR 'Goal' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Goal' resource payload.
    """

    resource_type = "Goal"
    resource_subtype = "start_codeable_concept_coding"
    transformer = GoalStartCodeableConceptCodingTransformer
    expected_table_name = "goal_start_codeable_concept_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

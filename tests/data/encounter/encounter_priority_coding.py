"""
Test helper class for FHIR resource type Encounter subtype Priority Coding
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterPriorityCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "priority_coding_system": "http://snomed.info/sct",
        "priority_coding_code": "394849002",
        "priority_coding_display": "High priority",
    }
]


class EncounterPriorityCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource subtype Priority Coding.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource subtype Priority Coding.
    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.
    """

    resource_type = "Encounter"
    resource_subtype = "priority_coding"
    transformer = EncounterPriorityCodingTransformer
    expected_table_name = "encounter_priority_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

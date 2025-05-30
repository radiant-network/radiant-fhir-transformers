"""
Test helper class for FHIR resource type Encounter subtype Type
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterTypeTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "type_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "183807002",
                "display": "Inpatient stay for nine days",
            }
        ],
        "type_text": None,
    }
]


class EncounterTypeTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource subtype Type.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource subtype Type.
    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.
    """

    resource_type = "Encounter"
    resource_subtype = "type"
    transformer = EncounterTypeTransformer
    expected_table_name = "encounter_type"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

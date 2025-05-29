"""
Test helper class for FHIR resource type Encounter subtype ClassHistory
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterClassHistoryTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE
EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "class_history_class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "IMP",
            "display": "inpatient encounter",
        },
        "class_history_period": {
            "start": "2013-03-08T00:00:00Z",
            "end": "2013-03-08T00:00:00Z"
        },
    },
]
class EncounterClassHistoryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource.

    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.

        resource_subtype (str): The subtype of the FHIR resource being tested,
          which is set to 'class_history'.

        transformer: The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The expected name of the table after transformation.
    """

    resource_type = "Encounter"
    resource_subtype = "class_history"
    transformer = EncounterClassHistoryTransformer
    expected_table_name = "encounter_class_history"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
"""
Test helper class for FHIR resource type Encounter subtype Class
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterClassTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "class_code": "IMP",
        "class_display": "inpatient encounter",
        "class_system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    }
]


class EncounterClassTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource being tested, which
          is set to 'class'.

        transformer: The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the expected output table.
    """

    resource_type = "Encounter"
    resource_subtype = "class"
    transformer = EncounterClassTransformer
    expected_table_name = "encounter_class"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

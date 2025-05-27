"""
Test helper class for FHIR resource type Encounter
"""
from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE
EXPECTED_OUTPUT = [
    {
        "id": "enc001",
        "resource_type": "Encounter",
        "status": "in-progress",
        "class_code": "AMB",
        "class_system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "class_display": "ambulatory",
        "subject_reference": "#pat001",
        "subject_type": "Patient",
        "subject_display": "Patient 1",
        "period_start": "2023-01-01T10:00:00Z",
        "period_end": "2023-01-01T11:00:00Z",
        "length_value": 60.0,
        "length_comparator": None,
        "length_unit": "min",
        "length_system": "http://unitsofmeasure.org",
        "length_code": "[min]",
    }
]
class EncounterTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource, which is None
          for this resource.

        transformer (class): The transformer class used for transforming the
          FHIR resource.

        expected_table_name (str): The expected name of the table after transformation.
    """
    resource_type = "Encounter"
    resource_subtype = None
    transformer = EncounterTransformer
    expected_table_name = "encounter"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
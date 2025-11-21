"""
Test helper class for FHIR resource type Medication subtype Ingredient
"""

from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationIngredientTransformer,
)
from tests.data.base import FhirResourceTestHelper

RESOURCE = None

EXPECTED_OUTPUT = None

from .medication_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "ingredient_item_codeable_concept": {
            "coding": [
                {
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                    "code": "66955",
                    "display": "Vancomycin Hydrochloride",
                },
            ],
        },
        "ingredient_item_reference": {
            "reference": "Medication/abcd",
            "display": "potassium phosphate",
        },
        "ingredient_is_active": True,
        "ingredient_strength_numerator_value": 500,
        "ingredient_strength_numerator_unit": None,
        "ingredient_strength_numerator_system": "http://unitsofmeasure.org",
        "ingredient_strength_numerator_code": "mg",
        "ingredient_strength_denominator_value": 10,
        "ingredient_strength_denominator_unit": None,
        "ingredient_strength_denominator_system": "http://unitsofmeasure.org",
        "ingredient_strength_denominator_code": "mL",
        "id": "41adc668-bae6-4d4c-9c1c-58122f927687",
        "medication_id": "med0301",
    },
]


class MedicationIngredientTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Medication' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Medication' resource.

    It predefines the resource type as 'Medication'
    and initializes the resource with the specific 'Medication' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Medication'.

        resource (dict): The raw FHIR 'Medication' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Medication' resource payload.
    """

    resource_type = "Medication"
    resource_subtype = "ingredient"
    transformer = MedicationIngredientTransformer
    expected_table_name = "medication_ingredient"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)

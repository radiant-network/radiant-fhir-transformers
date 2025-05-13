"""
FHIR Medication Ingredient transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "medication_id": {"fhir_key": "id", "type": "str"},
        },
    },
    # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
    # {
    #     "fhir_path": "ingredient.itemCodeableConcept.coding",
    #     "columns": {
    #         "ingredient_item_codeable_concept_coding_system": {
    #             "fhir_key": "system",
    #             "type": "str",
    #         },
    #         "ingredient_item_codeable_concept_coding_code": {
    #             "fhir_key": "code",
    #             "type": "str",
    #         },
    #         "ingredient_item_codeable_concept_coding_display": {
    #             "fhir_key": "display",
    #             "type": "str",
    #         },
    #     },
    # },
    # {
    #     "fhir_path": "ingredient.itemCodeableConcept.text",
    #     "columns": {
    #         "ingredient_item_codeable_concept_text": {
    #             "fhir_key": "text",
    #             "type": "str",
    #         },
    #     },
    # },
    {
        "fhir_path": "ingredient",
        "columns": {
            "ingredient_is_active": {"fhir_key": "isActive", "type": "bool"},
            "ingredient_strength_numerator_value": {
                "fhir_key": "strength.numerator.value",
                "type": "int",
            },
            "ingredient_strength_numerator_unit": {
                "fhir_key": "strength.numerator.unit",
                "type": "str",
            },
            "ingredient_strength_numerator_system": {
                "fhir_key": "strength.numerator.system",
                "type": "str",
            },
            "ingredient_strength_numerator_code": {
                "fhir_key": "strength.numerator.code",
                "type": "str",
            },
            "ingredient_strength_denominator_value": {
                "fhir_key": "strength.denominator.value",
                "type": "int",
            },
            "ingredient_strength_denominator_unit": {
                "fhir_key": "strength.denominator.unit",
                "type": "str",
            },
            "ingredient_strength_denominator_system": {
                "fhir_key": "strength.denominator.system",
                "type": "str",
            },
            "ingredient_strength_denominator_code": {
                "fhir_key": "strength.denominator.code",
                "type": "str",
            },
        },
    },
]


class MedicationIngredientTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Medication' resource in FHIR, focusing on the 'ingredient' element.

    This class transforms FHIR Medication JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'ingredient' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Medication').
        subtype (str): Specifies the sub-element of the resource to focus on ('ingredient').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationIngredientTransformer instance with the resource type 'Medication',
            subtype 'ingredient', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Medication", "ingredient", TRANSFORM_SCHEMA)

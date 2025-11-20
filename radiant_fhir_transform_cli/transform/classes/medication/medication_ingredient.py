"""FHIR Medication ingredient transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Medication",
    "name": "medication_ingredient",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "medication_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "ingredient",
            "column": [
                {
                    "name": "ingredient_item_codeable_concept",
                    "path": "itemCodeableConcept",
                    "type": "string",
                },
                {
                    "name": "ingredient_item_reference",
                    "path": "itemReference",
                    "type": "string",
                },
                {
                    "name": "ingredient_is_active",
                    "path": "isActive",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_numerator_value",
                    "path": "strength.numerator.value",
                    "type": "integer",
                },
                {
                    "name": "ingredient_strength_numerator_unit",
                    "path": "strength.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_numerator_system",
                    "path": "strength.numerator.system",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_numerator_code",
                    "path": "strength.numerator.code",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_denominator_value",
                    "path": "strength.denominator.value",
                    "type": "integer",
                },
                {
                    "name": "ingredient_strength_denominator_unit",
                    "path": "strength.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_denominator_system",
                    "path": "strength.denominator.system",
                    "type": "string",
                },
                {
                    "name": "ingredient_strength_denominator_code",
                    "path": "strength.denominator.code",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationIngredientTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Medication", "ingredient", VIEW_DEFINITION)

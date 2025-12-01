"""FHIR Coverage cost_to_beneficiary transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_cost_to_beneficiary",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "coverage_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "costToBeneficiary",
            "column": [
                {
                    "name": "cost_to_beneficiary_type_coding",
                    "path": "type.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "cost_to_beneficiary_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_quantity_value",
                    "path": "valueQuantity.value",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_quantity_unit",
                    "path": "valueQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_quantity_system",
                    "path": "valueQuantity.system",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_quantity_code",
                    "path": "valueQuantity.code",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_money_value",
                    "path": "valueMoney.value",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_value_money_currency",
                    "path": "valueMoney.currency",
                    "type": "string",
                },
                {
                    "name": "cost_to_beneficiary_exception",
                    "path": "exception",
                    "type": "string",
                    "collection": True,
                },
            ],
        },
    ],
}


class CoverageCostToBeneficiaryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Coverage", "cost_to_beneficiary", VIEW_DEFINITION)

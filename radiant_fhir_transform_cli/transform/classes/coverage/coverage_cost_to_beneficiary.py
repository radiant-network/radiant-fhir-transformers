"""
FHIR Coverage CostToBeneficiary transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
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
            "coverage_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "costToBeneficiary",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "cost_to_beneficiary_type_coding": {
                "fhir_key": "type.coding",
                "type": "str",
            },
            "cost_to_beneficiary_type_text": {
                "fhir_key": "type.text",
                "type": "str",
            },
            "cost_to_beneficiary_value_quantity_value": {
                "fhir_key": "valueQuantity.value",
                "type": "str",
            },
            "cost_to_beneficiary_value_quantity_unit": {
                "fhir_key": "valueQuantity.unit",
                "type": "str",
            },
            "cost_to_beneficiary_value_quantity_system": {
                "fhir_key": "valueQuantity.system",
                "type": "str",
            },
            "cost_to_beneficiary_value_quantity_code": {
                "fhir_key": "valueQuantity.code",
                "type": "str",
            },
            "cost_to_beneficiary_value_money_value": {
                "fhir_key": "valueMoney.value",
                "type": "str",
            },
            "cost_to_beneficiary_value_money_currency": {
                "fhir_key": "valueMoney.currency",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "cost_to_beneficiary_exception": {
                "fhir_key": "exception",
                "type": "str",
            },
        },
    },
]


class CoverageCostToBeneficiaryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR, focusing on the 'costToBeneficiary' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'costToBeneficiary' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Coverage').
        subtype (str): Specifies the sub-element of the resource to focus on ('costToBeneficiary').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CoverageCostToBeneficiaryTransformer instance with the resource type 'Coverage',
            subtype 'costToBeneficiary', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", "costToBeneficiary", TRANSFORM_SCHEMA)

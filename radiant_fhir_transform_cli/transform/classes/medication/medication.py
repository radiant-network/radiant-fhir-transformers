"""FHIR Medication transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Medication",
    "name": "medication",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "manufacturer_reference",
                    "path": "manufacturer.reference",
                    "type": "string",
                },
                {
                    "name": "manufacturer_type",
                    "path": "manufacturer.type",
                    "type": "string",
                },
                {
                    "name": "manufacturer_display",
                    "path": "manufacturer.display",
                    "type": "string",
                },
                {
                    "name": "form_text",
                    "path": "form.text",
                    "type": "string",
                },
                {
                    "name": "amount_numerator_value",
                    "path": "amount.numerator.value",
                    "type": "string",
                },
                {
                    "name": "amount_numerator_unit",
                    "path": "amount.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "amount_numerator_system",
                    "path": "amount.numerator.system",
                    "type": "string",
                },
                {
                    "name": "amount_numerator_code",
                    "path": "amount.numerator.code",
                    "type": "string",
                },
                {
                    "name": "amount_denominator_value",
                    "path": "amount.denominator.value",
                    "type": "string",
                },
                {
                    "name": "amount_denominator_unit",
                    "path": "amount.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "amount_denominator_system",
                    "path": "amount.denominator.system",
                    "type": "string",
                },
                {
                    "name": "amount_denominator_code",
                    "path": "amount.denominator.code",
                    "type": "string",
                },
                {
                    "name": "batch_lot_number",
                    "path": "batch.lotNumber",
                    "type": "string",
                },
                {
                    "name": "batch_expiration_date",
                    "path": "batch.expirationDate",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class MedicationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Medication", None, VIEW_DEFINITION)

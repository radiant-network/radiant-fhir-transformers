"""FHIR MedicationDispense supporting_information transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_supporting_information",
    "status": "active",
    "constant": [{"name": "id_hash", "valueString": "hash_row()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_hash", "type": "string"},
                {
                    "name": "medication_dispense_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "supportingInformation",
            "column": [
                {
                    "name": "supporting_information_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "supporting_information_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "supporting_information_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseSupportingInformationTransformer(FhirResourceTransformer):
    resource_type = "MedicationDispense"
    resource_component = "supporting_information"
    view_definition = VIEW_DEFINITION

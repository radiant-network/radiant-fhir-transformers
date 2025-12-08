"""FHIR MedicationDispense supporting_information transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_supporting_information",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
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


class MedicationDispenseSupportingInformationTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationDispense", "supporting_information", VIEW_DEFINITION
        )

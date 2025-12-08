"""FHIR MedicationRequest supporting_information transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_supporting_information",
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
                    "name": "medication_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "supportingInformation",
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


class MedicationRequestSupportingInformationTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationRequest", "supporting_information", VIEW_DEFINITION
        )

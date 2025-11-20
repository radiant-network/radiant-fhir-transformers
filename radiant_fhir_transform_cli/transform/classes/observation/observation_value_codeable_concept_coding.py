"""FHIR Observation value_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_value_codeable_concept_coding",
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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "valueCodeableConcept.coding",
            "column": [
                {
                    "name": "value_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "value_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "value_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationValueCodeableConceptCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Observation", "value_codeable_concept_coding", VIEW_DEFINITION
        )

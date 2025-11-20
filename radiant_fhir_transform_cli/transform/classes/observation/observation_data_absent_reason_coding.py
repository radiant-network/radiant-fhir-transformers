"""FHIR Observation data_absent_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_data_absent_reason_coding",
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
            "forEach": "dataAbsentReason.coding",
            "column": [
                {
                    "name": "data_absent_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "data_absent_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "data_absent_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationDataAbsentReasonCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Observation", "data_absent_reason_coding", VIEW_DEFINITION
        )

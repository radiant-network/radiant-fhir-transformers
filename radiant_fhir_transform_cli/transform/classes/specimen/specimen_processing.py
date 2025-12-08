"""FHIR Specimen processing transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_processing",
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "processing",
            "column": [
                {
                    "name": "processing_description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "processing_procedure_text",
                    "path": "procedure.text",
                    "type": "string",
                },
                {
                    "name": "processing_time_date_time",
                    "path": "timeDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "processing_time_period_start",
                    "path": "timePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "processing_time_period_end",
                    "path": "timePeriod.end",
                    "type": "dateTime",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "procedure.coding",
                    "column": [
                        {
                            "name": "processing_procedure_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "processing_procedure_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "additive",
                    "column": [
                        {
                            "name": "processing_additive_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class SpecimenProcessingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "processing", VIEW_DEFINITION)

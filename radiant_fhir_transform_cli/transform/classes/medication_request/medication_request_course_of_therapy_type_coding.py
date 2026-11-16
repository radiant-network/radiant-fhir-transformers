"""FHIR MedicationRequest course_of_therapy_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_course_of_therapy_type_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
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
            "forEachOrNull": "courseOfTherapyType.coding",
            "column": [
                {
                    "name": "course_of_therapy_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "course_of_therapy_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "course_of_therapy_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestCourseOfTherapyTypeCodingTransformer(FhirResourceTransformer):
    resource_type = "MedicationRequest"
    resource_component = "course_of_therapy_type_coding"
    view_definition = VIEW_DEFINITION

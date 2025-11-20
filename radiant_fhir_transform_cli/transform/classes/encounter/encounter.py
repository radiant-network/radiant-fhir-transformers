"""FHIR Encounter transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter",
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
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "class_code",
                    "path": "class.code",
                    "type": "string",
                },
                {
                    "name": "class_system",
                    "path": "class.system",
                    "type": "string",
                },
                {
                    "name": "class_display",
                    "path": "class.display",
                    "type": "string",
                },
                {
                    "name": "service_type_text",
                    "path": "serviceType.text",
                    "type": "string",
                },
                {
                    "name": "priority_text",
                    "path": "priority.text",
                    "type": "string",
                },
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
                {
                    "name": "length_value",
                    "path": "length.value",
                    "type": "string",
                },
                {
                    "name": "length_comparator",
                    "path": "length.comparator",
                    "type": "string",
                },
                {
                    "name": "length_unit",
                    "path": "length.unit",
                    "type": "string",
                },
                {
                    "name": "length_system",
                    "path": "length.system",
                    "type": "string",
                },
                {
                    "name": "length_code",
                    "path": "length.code",
                    "type": "string",
                },
                {
                    "name": "service_provider_reference",
                    "path": "serviceProvider.reference",
                    "type": "string",
                },
                {
                    "name": "service_provider_type",
                    "path": "serviceProvider.type",
                    "type": "string",
                },
                {
                    "name": "service_provider_display",
                    "path": "serviceProvider.display",
                    "type": "string",
                },
                {
                    "name": "part_of_reference",
                    "path": "partOf.reference",
                    "type": "string",
                },
                {
                    "name": "part_of_type",
                    "path": "partOf.type",
                    "type": "string",
                },
                {
                    "name": "part_of_display",
                    "path": "partOf.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", None, VIEW_DEFINITION)

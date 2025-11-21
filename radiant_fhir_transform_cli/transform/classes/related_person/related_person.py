"""FHIR RelatedPerson transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RelatedPerson",
    "name": "related_person",
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
                    "name": "active",
                    "path": "active",
                    "type": "string",
                },
                {
                    "name": "patient_reference",
                    "path": "patient.reference",
                    "type": "string",
                },
                {
                    "name": "patient_type",
                    "path": "patient.type",
                    "type": "string",
                },
                {
                    "name": "patient_display",
                    "path": "patient.display",
                    "type": "string",
                },
                {
                    "name": "gender",
                    "path": "gender",
                    "type": "string",
                },
                {
                    "name": "birth_date",
                    "path": "birthDate",
                    "type": "dateTime",
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
            ],
        },
    ],
}


class RelatedPersonTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RelatedPerson", None, VIEW_DEFINITION)

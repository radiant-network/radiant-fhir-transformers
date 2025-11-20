"""FHIR Provenance transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance",
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
                    "name": "occurred_period_start",
                    "path": "occurredPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "occurred_period_end",
                    "path": "occurredPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "occurred_date_time",
                    "path": "occurredDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "recorded",
                    "path": "recorded",
                    "type": "dateTime",
                },
                {
                    "name": "location_reference",
                    "path": "location.reference",
                    "type": "string",
                },
                {
                    "name": "location_type",
                    "path": "location.type",
                    "type": "string",
                },
                {
                    "name": "location_display",
                    "path": "location.display",
                    "type": "string",
                },
                {
                    "name": "activity_text",
                    "path": "activity.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", None, VIEW_DEFINITION)

"""FHIR Coverage transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {"name": "status", "path": "status", "type": "string"},
                {"name": "type_text", "path": "type.text", "type": "string"},
                {
                    "name": "policy_holder_reference",
                    "path": "policyHolder.reference",
                    "type": "string",
                },
                {
                    "name": "policy_holder_type",
                    "path": "policyHolder.type",
                    "type": "string",
                },
                {
                    "name": "policy_holder_display",
                    "path": "policyHolder.display",
                    "type": "string",
                },
                {
                    "name": "subscriber_reference",
                    "path": "subscriber.reference",
                    "type": "string",
                },
                {
                    "name": "subscriber_type",
                    "path": "subscriber.type",
                    "type": "string",
                },
                {
                    "name": "subscriber_display",
                    "path": "subscriber.display",
                    "type": "string",
                },
                {
                    "name": "subscriber_id",
                    "path": "subscriberId",
                    "type": "string",
                },
                {
                    "name": "beneficiary_reference",
                    "path": "beneficiary.reference",
                    "type": "string",
                },
                {
                    "name": "beneficiary_type",
                    "path": "beneficiary.type",
                    "type": "string",
                },
                {
                    "name": "beneficiary_display",
                    "path": "beneficiary.display",
                    "type": "string",
                },
                {"name": "dependent", "path": "dependent", "type": "string"},
                {
                    "name": "relationship_text",
                    "path": "relationship.text",
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
                {"name": "order", "path": "order", "type": "integer"},
                {"name": "network", "path": "network", "type": "string"},
                {
                    "name": "subrogation",
                    "path": "subrogation",
                    "type": "string",
                },
            ]
        }
    ],
}


class CoverageTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Coverage", None, VIEW_DEFINITION)

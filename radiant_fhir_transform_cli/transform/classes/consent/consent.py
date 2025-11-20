"""FHIR Consent transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent",
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
                    "name": "scope_text",
                    "path": "scope.text",
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
                    "name": "date_time",
                    "path": "dateTime",
                    "type": "dateTime",
                },
                {
                    "name": "source_attachment_content_type",
                    "path": "sourceAttachment.contentType",
                    "type": "string",
                },
                {
                    "name": "source_attachment_language",
                    "path": "sourceAttachment.language",
                    "type": "string",
                },
                {
                    "name": "source_attachment_url",
                    "path": "sourceAttachment.url",
                    "type": "string",
                },
                {
                    "name": "source_attachment_size",
                    "path": "sourceAttachment.size",
                    "type": "integer",
                },
                {
                    "name": "source_attachment_title",
                    "path": "sourceAttachment.title",
                    "type": "string",
                },
                {
                    "name": "source_attachment_creation",
                    "path": "sourceAttachment.creation",
                    "type": "dateTime",
                },
                {
                    "name": "source_reference_reference",
                    "path": "sourceReference.reference",
                    "type": "string",
                },
                {
                    "name": "source_reference_type",
                    "path": "sourceReference.type",
                    "type": "string",
                },
                {
                    "name": "source_reference_display",
                    "path": "sourceReference.display",
                    "type": "string",
                },
                {
                    "name": "policy_rule_text",
                    "path": "policyRule.text",
                    "type": "string",
                },
                {
                    "name": "provision_type",
                    "path": "provision.type",
                    "type": "string",
                },
                {
                    "name": "provision_period_start",
                    "path": "provision.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "provision_period_end",
                    "path": "provision.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "provision_data_period_start",
                    "path": "provision.dataPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "provision_data_period_end",
                    "path": "provision.dataPeriod.end",
                    "type": "dateTime",
                },
            ],
            "select": [
                {
                    "forEach": "provision.provision",
                    "column": [
                        {
                            "name": "provision_provision_type",
                            "path": "type",
                            "type": "string",
                        },
                        {
                            "name": "provision_provision_actor",
                            "path": "actor",
                            "type": "string",
                        },
                        {
                            "name": "provision_provision_class",
                            "path": "class",
                            "type": "string",
                        },
                        {
                            "name": "provision_provision_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ConsentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", None, VIEW_DEFINITION)

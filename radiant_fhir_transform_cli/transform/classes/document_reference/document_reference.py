"""FHIR DocumentReference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference",
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
                    "name": "master_identifier_use",
                    "path": "masterIdentifier.use",
                    "type": "string",
                },
                {
                    "name": "master_identifier_type_text",
                    "path": "masterIdentifier.type.text",
                    "type": "string",
                },
                {
                    "name": "master_identifier_system",
                    "path": "masterIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "master_identifier_value",
                    "path": "masterIdentifier.value",
                    "type": "string",
                },
                {
                    "name": "master_identifier_period_start",
                    "path": "masterIdentifier.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "master_identifier_period_end",
                    "path": "masterIdentifier.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "doc_status",
                    "path": "docStatus",
                    "type": "string",
                },
                {
                    "name": "type_text",
                    "path": "type.text",
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
                    "name": "date",
                    "path": "date",
                    "type": "dateTime",
                },
                {
                    "name": "authenticator_reference",
                    "path": "authenticator.reference",
                    "type": "string",
                },
                {
                    "name": "authenticator_type",
                    "path": "authenticator.type",
                    "type": "string",
                },
                {
                    "name": "authenticator_display",
                    "path": "authenticator.display",
                    "type": "string",
                },
                {
                    "name": "custodian_reference",
                    "path": "custodian.reference",
                    "type": "string",
                },
                {
                    "name": "custodian_type",
                    "path": "custodian.type",
                    "type": "string",
                },
                {
                    "name": "custodian_display",
                    "path": "custodian.display",
                    "type": "string",
                },
                {
                    "name": "description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "context_period_start",
                    "path": "context.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "context_period_end",
                    "path": "context.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "context_facility_type_text",
                    "path": "context.facilityType.text",
                    "type": "string",
                },
                {
                    "name": "context_practice_setting_text",
                    "path": "context.practiceSetting.text",
                    "type": "string",
                },
                {
                    "name": "context_source_patient_info_reference",
                    "path": "context.sourcePatientInfo.reference",
                    "type": "string",
                },
                {
                    "name": "context_source_patient_info_type",
                    "path": "context.sourcePatientInfo.type",
                    "type": "string",
                },
                {
                    "name": "context_source_patient_info_display",
                    "path": "context.sourcePatientInfo.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DocumentReference", None, VIEW_DEFINITION)

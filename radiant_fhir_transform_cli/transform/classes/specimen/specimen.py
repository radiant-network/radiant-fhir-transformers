"""FHIR Specimen transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen",
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
                {
                    "name": "accession_identifier_use",
                    "path": "accessionIdentifier.use",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_system",
                    "path": "accessionIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_value",
                    "path": "accessionIdentifier.value",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_period_start",
                    "path": "accessionIdentifier.period.start",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_period_end",
                    "path": "accessionIdentifier.period.end",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_assigner_reference",
                    "path": "accessionIdentifier.assigner.reference",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_assigner_display",
                    "path": "accessionIdentifier.assigner.display",
                    "type": "string",
                },
                {
                    "name": "accession_identifier_assigner_type",
                    "path": "accessionIdentifier.assigner.type",
                    "type": "string",
                },
                {"name": "status", "path": "status", "type": "string"},
                {"name": "type_text", "path": "type.text", "type": "string"},
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "received_time",
                    "path": "receivedTime",
                    "type": "dateTime",
                },
                {
                    "name": "collection_collector_reference",
                    "path": "collection.collector.reference",
                    "type": "string",
                },
                {
                    "name": "collection_collector_display",
                    "path": "collection.collector.display",
                    "type": "string",
                },
                {
                    "name": "collection_collector_type",
                    "path": "collection.collector.type",
                    "type": "string",
                },
                {
                    "name": "collection_collected_date_time",
                    "path": "collection.collectedDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "collection_collected_period_start",
                    "path": "collection.collectedPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "collection_collected_period_end",
                    "path": "collection.collectedPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "collection_duration_value",
                    "path": "collection.duration.value",
                    "type": "string",
                },
                {
                    "name": "collection_duration_comparator",
                    "path": "collection.duration.comparator",
                    "type": "string",
                },
                {
                    "name": "collection_duration_unit",
                    "path": "collection.duration.unit",
                    "type": "string",
                },
                {
                    "name": "collection_duration_system",
                    "path": "collection.duration.system",
                    "type": "string",
                },
                {
                    "name": "collection_duration_code",
                    "path": "collection.duration.code",
                    "type": "string",
                },
                {
                    "name": "collection_quantity_value",
                    "path": "collection.quantity.value",
                    "type": "string",
                },
                {
                    "name": "collection_quantity_unit",
                    "path": "collection.quantity.unit",
                    "type": "string",
                },
                {
                    "name": "collection_quantity_system",
                    "path": "collection.quantity.system",
                    "type": "string",
                },
                {
                    "name": "collection_quantity_code",
                    "path": "collection.quantity.code",
                    "type": "string",
                },
                {
                    "name": "collection_method_text",
                    "path": "collection.method.text",
                    "type": "string",
                },
                {
                    "name": "collection_body_site_text",
                    "path": "collection.bodySite.text",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_duration_value",
                    "path": "collection.fastingStatusDuration.value",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_duration_comparator",
                    "path": "collection.fastingStatusDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_duration_unit",
                    "path": "collection.fastingStatusDuration.unit",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_duration_system",
                    "path": "collection.fastingStatusDuration.system",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_duration_code",
                    "path": "collection.fastingStatusDuration.code",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_codeable_concept_text",
                    "path": "collection.fastingStatusCodeableConcept.text",
                    "type": "string",
                },
            ]
        }
    ],
}


class SpecimenTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", None, VIEW_DEFINITION)

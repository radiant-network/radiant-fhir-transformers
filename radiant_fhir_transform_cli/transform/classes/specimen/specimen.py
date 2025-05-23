"""
FHIR Specimen transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {"resource_type": {"type": "str"}},
    },
    {
        "fhir_path": "accessionIdentifier",
        "columns": {
            "accession_identifier_use": {"fhir_key": "use", "type": "str"},
            "accession_identifier_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "accession_identifier_value": {"fhir_key": "value", "type": "str"},
            "accession_identifier_period_start": {
                "fhir_key": "period.start",
                "type": "str",
            },
            "accession_identifier_period_end": {
                "fhir_key": "period.end",
                "type": "str",
            },
            "accession_identifier_assigner_reference": {
                "fhir_key": "assigner.reference",
                "type": "str",
            },
            "accession_identifier_assigner_display": {
                "fhir_key": "assigner.display",
                "type": "str",
            },
            "accession_identifier_assigner_type": {
                "fhir_key": "assigner.type",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"type": "str"}},
    },
    {
        "fhir_path": "type.text",
        "columns": {"type_text": {"type": "str"}},
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "subject_display": {"fhir_key": "display", "type": "str"},
            "subject_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "receivedTime",
        "columns": {"received_time": {"type": "datetime"}},
    },
    {
        "fhir_path": "collection.collector",
        "fhir_reference": "collection_collector_reference",
        "columns": {
            "collection_collector_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "collection_collector_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "collection_collector_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "collection.collectedDateTime",
        "columns": {"collection_collected_date_time": {"type": "datetime"}},
    },
    {
        "fhir_path": "collection.collectedPeriod",
        "columns": {
            "collection_collected_period_start": {
                "fhir_key": "start",
                "type": "datetime",
            },
            "collection_collected_period_end": {
                "fhir_key": "end",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "collection.duration",
        "columns": {
            "collection_duration_value": {
                "fhir_key": "value",
                "type": "str",
            },
            "collection_duration_comparator": {
                "fhir_key": "comparator",
                "type": "str",
            },
            "collection_duration_unit": {
                "fhir_key": "unit",
                "type": "str",
            },
            "collection_duration_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "collection_duration_code": {
                "fhir_key": "code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "collection.quantity",
        "columns": {
            "collection_quantity_value": {
                "fhir_key": "value",
                "type": "str",
            },
            "collection_quantity_unit": {
                "fhir_key": "unit",
                "type": "str",
            },
            "collection_quantity_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "collection_quantity_code": {
                "fhir_key": "code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "collection.method.text",
        "columns": {
            "collection_method_text": {"type": "str"},
        },
    },
    {
        "fhir_path": "collection.bodySite.text",
        "columns": {
            "collection_body_site_text": {"type": "str"},
        },
    },
    {
        "fhir_path": "collection.fastingStatusDuration",
        "columns": {
            "collection_fasting_status_duration_value": {
                "fhir_key": "value",
                "type": "str",
            },
            "collection_fasting_status_duration_comparator": {
                "fhir_key": "comparator",
                "type": "str",
            },
            "collection_fasting_status_duration_unit": {
                "fhir_key": "unit",
                "type": "str",
            },
            "collection_fasting_status_duration_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "collection_fasting_status_duration_code": {
                "fhir_key": "code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "collection.fastingStatusCodeableConcept.text",
        "columns": {
            "collection_fasting_status_codeable_concept_text": {"type": "str"},
        },
    },
]


class SpecimenTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Specimen' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the SpecimenTransformer instance with the resource
            type 'Specimen' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", None, TRANSFORM_SCHEMA)

"""
FHIR DocumentReference transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"},
        },
    },
    {
        "fhir_path": "masterIdentifier",
        "columns": {
            "master_identifier_use": {"fhir_key": "use", "type": "str"},
            "master_identifier_type_text": {
                "fhir_key": "type.text",
                "type": "str",
            },
            "master_identifier_system": {"fhir_key": "system", "type": "str"},
            "master_identifier_value": {"fhir_key": "value", "type": "str"},
            "master_identifier_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "master_identifier_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "docStatus",
        "columns": {
            "doc_status": {"fhir_key": "docStatus", "type": "str"},
        },
    },
    {
        "fhir_path": "type.text",
        "columns": {
            "type_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {"fhir_key": "reference", "type": "str"},
            "subject_type": {"fhir_key": "type", "type": "str"},
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "date",
        "columns": {
            "date": {"fhir_key": "date", "type": "datetime"},
        },
    },
    {
        "fhir_path": "authenticator",
        "fhir_reference": "authenticator_reference",
        "columns": {
            "authenticator_reference": {"fhir_key": "reference", "type": "str"},
            "authenticator_type": {"fhir_key": "type", "type": "str"},
            "authenticator_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "custodian",
        "fhir_reference": "custodian_reference",
        "columns": {
            "custodian_reference": {"fhir_key": "reference", "type": "str"},
            "custodian_type": {"fhir_key": "type", "type": "str"},
            "custodian_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "description",
        "columns": {
            "description": {"fhir_key": "description", "type": "str"},
        },
    },
    {
        "fhir_path": "context",
        "columns": {
            "context_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "context_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
            "context_facility_type_text": {
                "fhir_key": "facilityType.text",
                "type": "str",
            },
            "context_practice_setting_text": {
                "fhir_key": "practiceSetting.text",
                "type": "str",
            },
            "context_source_patient_info_reference": {
                "fhir_key": "sourcePatientInfo.reference",
                "type": "str",
            },
            "context_source_patient_info_type": {
                "fhir_key": "sourcePatientInfo.type",
                "type": "str",
            },
            "context_source_patient_info_display": {
                "fhir_key": "sourcePatientInfo.display",
                "type": "str",
            },
        },
    },
]


class DocumentReferenceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DocumentReference' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", None, TRANSFORM_SCHEMA)

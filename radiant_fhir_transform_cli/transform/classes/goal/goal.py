"""
FHIR Goal transformer
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
        "fhir_path": "lifecycleStatus",
        "columns": {
            "lifecycle_status": {"fhir_key": "lifecycleStatus", "type": "str"},
        },
    },
    {
        "fhir_path": "achievementStatus",
        "columns": {
            "achievement_status_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "priority",
        "columns": {
            "priority_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "description",
        "columns": {
            "description_text": {"fhir_key": "text", "type": "str"},
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
        "fhir_path": "startDate",
        "columns": {
            "start_date": {"fhir_key": "startDate", "type": "datetime"},
        },
    },
    {
        "fhir_path": "startCodeableConcept",
        "columns": {
            "start_codeable_concept_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "statusDate",
        "columns": {
            "status_date": {"fhir_key": "statusDate", "type": "datetime"},
        },
    },
    {
        "fhir_path": "statusReason",
        "columns": {
            "status_reason": {"fhir_key": "statusReason", "type": "str"},
        },
    },
    {
        "fhir_path": "expressedBy",
        "fhir_reference": "expressed_by_reference",
        "columns": {
            "expressed_by_reference": {"fhir_key": "reference", "type": "str"},
            "expressed_by_type": {"fhir_key": "type", "type": "str"},
            "expressed_by_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "Goal",
        "columns": {
            "goal_raw_json": {
                "type": "str",
            }
        },
    },
]


class GoalTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR.

    Transform Goal JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the GoalTransformer instance with the resource
            type 'Goal' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", None, TRANSFORM_SCHEMA)

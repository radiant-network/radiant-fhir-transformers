"""
FHIR CarePlan transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": "id",
        "columns": {"id": {"type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {"resource_type": {"type": "str"}},
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"type": "str"}},
    },
    {
        "fhir_path": "intent",
        "columns": {"intent": {"type": "str"}},
    },
    {
        "fhir_path": "title",
        "columns": {"title": {"type": "str"}},
    },
    {
        "fhir_path": "description",
        "columns": {"description": {"type": "str"}},
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
            "subject_type": {"fhir_key": "type", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "encounter_display": {"fhir_key": "display", "type": "str"},
            "encounter_type": {"fhir_key": "type", "type": "str"},
        },
    },
    {
        "fhir_path": "period",
        "columns": {
            "period_start": {"fhir_key": "start", "type": "datetime"},
            "period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "created",
        "columns": {"created": {"type": "datetime"}},
    },
    {
        "fhir_path": "author",
        "fhir_reference": "author_reference",
        "columns": {
            "author_reference": {"fhir_key": "reference", "type": "str"},
            "author_type": {"fhir_key": "type", "type": "str"},
            "author_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class CarePlanTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CarePlan' resource in FHIR.

    Transform CarePlan JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the CarePlanTransformer instance with the resource
            type 'CarePlan' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", None, TRANSFORM_SCHEMA)

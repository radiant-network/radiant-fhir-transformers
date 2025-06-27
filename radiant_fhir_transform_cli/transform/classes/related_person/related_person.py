"""
FHIR RelatedPerson transformer
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
        "fhir_path": "active",
        "columns": {
            "active": {"fhir_key": "active", "type": "bool"},
        },
    },
    {
        "fhir_path": "patient",
        "fhir_reference": "patient_reference",
        "columns": {
            "patient_reference": {"fhir_key": "reference", "type": "str"},
            "patient_type": {"fhir_key": "type", "type": "str"},
            "patient_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "gender",
        "columns": {
            "gender": {"fhir_key": "gender", "type": "str"},
        },
    },
    {
        "fhir_path": "birthDate",
        "columns": {
            "birth_date": {"fhir_key": "birthDate", "type": "datetime"},
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
        "fhir_path": "RelatedPerson",
        "columns": {
            "related_person_raw_json": {
                "type": "str",
            }
        },
    },
]


class RelatedPersonTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR.

    Transform RelatedPerson JSON objects into flat dictionaries representing
    rows in an output CSV file

    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the RelatedPersonTransformer instance with the resource
            type 'RelatedPerson' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", None, TRANSFORM_SCHEMA)

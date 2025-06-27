"""
FHIR CareTeam transformer
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
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "name",
        "columns": {
            "name": {"fhir_key": "name", "type": "str"},
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
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {"fhir_key": "reference", "type": "str"},
            "encounter_type": {"fhir_key": "type", "type": "str"},
            "encounter_display": {"fhir_key": "display", "type": "str"},
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
        "fhir_path": "CareTeam",
        "columns": {
            "care_team_raw_json": {
                "type": "str",
            }
        },
    },
]


class CareTeamTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CareTeam' resource in FHIR.

    Transform CareTeam JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the CareTeamTransformer instance with the resource
            type 'CareTeam' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("CareTeam", None, TRANSFORM_SCHEMA)

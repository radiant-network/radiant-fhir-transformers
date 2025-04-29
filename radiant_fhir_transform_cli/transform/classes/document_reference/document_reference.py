"""
FHIR Document Reference transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "docStatus",
        "columns": {"doc_status": {"fhir_key": "docStatus", "type": "str"}},
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
        },
    },
    {
        "fhir_path": "date",
        "columns": {
            "date": {
                "fhir_key": "date",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "custodian.display",
        "columns": {
            "custodian_display": {
                "fhir_key": "custodian_display",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "description",
        "columns": {"description": {"fhir_key": "description", "type": "str"}},
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

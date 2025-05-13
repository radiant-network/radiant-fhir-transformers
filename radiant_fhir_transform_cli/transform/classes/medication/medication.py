"""
FHIR Medication transformer
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
            "resource_type": {
                "fhir_key": "resourceType",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "manufacturer",
        "fhir_reference": "manufacturer_reference",
        "columns": {
            "manufacturer_reference": {"fhir_key": "reference", "type": "str"},
            "manufacturer_type": {"fhir_key": "type", "type": "str"},
            "manufacturer_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "form.text",
        "columns": {
            "form_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "batch",
        "columns": {
            "batch_lot_number": {"fhir_key": "lotNumber", "type": "str"},
            "batch_expiration_date": {
                "fhir_key": "expirationDate",
                "type": "datetime",
            },
        },
    },
]


class MedicationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR.

    Transform Medication JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the MedicationTransformer instance with the resource
            type 'Medication' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Medication", None, TRANSFORM_SCHEMA)

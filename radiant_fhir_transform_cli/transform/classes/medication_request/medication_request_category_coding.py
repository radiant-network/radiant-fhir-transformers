"""
FHIR MedicationRequest transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "medication_request_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "category.coding",
        "columns": {
            "category_coding_system": {"fhir_key": "system", "type": "str"},
            "category_coding_code": {"fhir_key": "code", "type": "str"},
            "category_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationRequestCategoryCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR.

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
        super().__init__(
            "MedicationRequest", "category_coding", TRANSFORM_SCHEMA
        )

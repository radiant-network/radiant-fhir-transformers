"""
Fhir Encounter Reason Reference Transformer
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
        "is_foreign_key": True,
        "columns": {
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "reasonReference",
        "columns": {
            "reason_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "reason_reference_type": {"fhir_key": "type", "type": "str"},
            "reason_reference_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class EncounterReasonReferenceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'reasonReference' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reasonReference' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'reason_reference'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.

    Methods:
        __init__(self):
            Initializes the EncounterReasonReferenceTransformer instance with the resource type 'Encounter',
            the resource subtype 'reason_reference', and the transformation schema.
    """

    def __init__(self):
        super().__init__("Encounter", "reason_reference", TRANSFORM_SCHEMA)

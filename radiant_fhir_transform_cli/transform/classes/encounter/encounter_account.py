"""
FHIR Encounter Account Transformer
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
        "fhir_path": "account",
        "columns": {
            "account_reference": {"fhir_key": "reference", "type": "str"},
            "account_type": {"fhir_key": "type", "type": "str"},
            "account_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class EncounterAccountTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'account' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'account' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'account'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.
    """

    def __init__(self):
        super().__init__("Encounter", "account", TRANSFORM_SCHEMA)

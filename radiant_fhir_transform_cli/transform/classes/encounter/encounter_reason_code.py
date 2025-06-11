"""
FHIR Encounter Reason Code Transformer
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
        "fhir_path": "reasonCode",
        "columns": {
            "reason_code_coding": {"fhir_key": "coding", "type": "str"},
            "reason_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class EncounterReasonCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'reasonCode' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reasonCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'reason_code'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.

    Methods:
    __init__():
        Initializes the EncounterReasonCodeTransformer instance with the resource type 'Encounter',
        subtype 'reason_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", "reason_code", TRANSFORM_SCHEMA)

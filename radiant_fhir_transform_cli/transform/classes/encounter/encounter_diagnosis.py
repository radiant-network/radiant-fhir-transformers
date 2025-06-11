"""
FHIR Encounter Diagnosis Class
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
        "fhir_path": "diagnosis",
        "columns": {
            "diagnosis_condition_reference": {
                "fhir_key": "condition.reference",
                "type": "str",
            },
            "diagnosis_condition_type": {
                "fhir_key": "condition.type",
                "type": "str",
            },
            "diagnosis_condition_display": {
                "fhir_key": "condition.display",
                "type": "str",
            },
            "diagnosis_use_coding": {"fhir_key": "use.coding", "type": "str"},
            "diagnosis_use_text": {"fhir_key": "use.text", "type": "str"},
            "diagnosis_rank": {"fhir_key": "rank", "type": "int"},
        },
    },
]


class EncounterDiagnosisTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'diagnosis' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'diagnosis' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'diagnosis'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.

    Methods:
    __init__():
        Initializes the EncounterDiagnosisTransformer instance with the resource type 'Encounter',
        subtype 'diagnosis', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", "diagnosis", TRANSFORM_SCHEMA)

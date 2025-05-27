"""
FHIR Encounter Status History transformer
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
        "fhir_path": "statusHistory",
        "columns": {
            "status_history_status": {"fhir_key": "statusHistory.status", "type": "str"},
            "status_history_period_start": {"fhir_key": "statusHistory.period.start", "type": "datetime"},
            "status_history_period_end": {"fhir_key": "statusHistory.period.end", "type": "datetime"},
        }
    },
]
class EncounterStatusHistoryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'statusHistory' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'statusHistory' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('status_history').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    """

    def __init__(self):
        super().__init__("Encounter", "status_history", TRANSFORM_SCHEMA)
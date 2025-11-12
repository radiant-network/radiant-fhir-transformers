"""
FHIR MedicationDispense EventHistory transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
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
            "medication_dispense_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "eventHistory",
        "fhir_reference": "event_history_reference",
        "columns": {
            "event_history_reference": {"fhir_key": "reference", "type": "str"},
            "event_history_type": {"fhir_key": "type", "type": "str"},
            "event_history_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class MedicationDispenseEventHistoryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'eventHistory' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'eventHistory' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('event_history').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseEventHistoryTransformer instance with the resource type 'MedicationDispense',
            subtype 'event_history', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationDispense", "event_history", TRANSFORM_SCHEMA
        )

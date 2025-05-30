"""
Fhir Encounter Participant Transformer Class
"""

from radiant_fhir_transform_cli.transform.classes.base import FhirResourceTransformer

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
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "participant",
        "columns": {
            "participant_type": {"fhir_key": "type", "type": "str"},
            "participant_period": {"fhir_key": "period", "type": "str"},
            "participant_individual": {"fhir_key": "individual", "type": "str"},
            # TODO: Add support for nested fields 
        },
    },
]

class EncounterParticipantTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'participant' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'participant' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('participant').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the EncounterParticipantTransformer instance with the resource type 'Encounter',
            subtype 'participant', and the specified transformation dictionary.
    """
    
    def __init__(self):
        super().__init__("Encounter", "participant", TRANSFORM_SCHEMA)
"""
FHIR Observation Identifier transformer
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
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "identifier",
        "columns": {
            "identifier_use": {"fhir_key": "use", "type": "str"},
            "identifier_type_text": {"fhir_key": "type.text", "type": "str"},
            "identifier_system": {"fhir_key": "system", "type": "str"},
            "identifier_value": {"fhir_key": "value", "type": "str"},
            "identifier_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "identifier_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class ObservationIdentifierTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Observation' resource in FHIR, focusing on the 'identifier' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'identifier' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('identifier').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationIdentifierTransformer instance with the resource type 'Observation',
            subtype 'identifier', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "identifier", TRANSFORM_SCHEMA)

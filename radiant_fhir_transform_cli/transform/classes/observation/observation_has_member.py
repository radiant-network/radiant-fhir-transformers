"""
FHIR Observation HasMember transformer
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
        "fhir_path": "hasMember",
        "fhir_reference": "has_member_reference",
        "columns": {
            "has_member_reference": {"fhir_key": "reference", "type": "str"},
            "has_member_type": {"fhir_key": "type", "type": "str"},
            "has_member_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationHasMemberTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'hasMember' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'hasMember' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('has_member').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationHasMemberTransformer instance with the resource type 'Observation',
            subtype 'has_member', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "has_member", TRANSFORM_SCHEMA)
